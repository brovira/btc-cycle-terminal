#!/usr/bin/env python3
"""sync_woc_reports.py — destila los Week On-Chain que le faltan al agente `glassnode_woc`.

EL AGUJERO QUE TAPA
-------------------
`sync_woc.py` traía la recomendación semanal a `data/woc_semana.json` (la tarjeta del
dashboard). Pero la carpeta que el AGENTE lee de verdad para citar —
`agentes/glassnode_woc/reports/`— no la escribía nadie: un grep por "glassnode_woc" en
todos los .py y .yml del repo no devolvía nada. Resultado: el 17-ago-2026 el agente
respondía citando el informe del 22-jul mientras el KB privado ya tenía tres artículos
posteriores. El dato nunca se perdió; faltaba el puente.

POR QUÉ HACE FALTA UN MODELO Y NO UN `cp`
-----------------------------------------
Este repo es PÚBLICO. La convención (ver sops/ y agentes/glassnode_strategy/) es guardar
RESÚMENES PROPIOS, no el texto de terceros. El informe del 22-jul es una reescritura
—7.886 bytes frente a 9.609 del original— con estructura propia y niveles extraídos. Así
que el puente necesita destilar, y destilar necesita un modelo.

CÓMO SE PAGA
------------
Con la suscripción, no con la API: `claude` en modo headless leyendo CLAUDE_CODE_OAUTH_TOKEN
(generado con `claude setup-token`). Un artículo por semana es carga trivial.

USO
  python ingesta/sync_woc_reports.py              # destila lo que falte (máx 4)
  python ingesta/sync_woc_reports.py --max 1      # limita cuántos
  python ingesta/sync_woc_reports.py --listar     # solo dice qué falta, no llama al modelo
"""
import argparse, base64, glob, json, os, re, subprocess, sys, tempfile, urllib.request, urllib.error

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DESTINO = os.path.join(ROOT, "agentes", "glassnode_woc", "reports")
MODELO_REF = os.path.join(DESTINO, "20260722-optimism-meets-overhead.md")
REPO_KB = "brovira/defi-tracker"
RUTA_KB = "research/glassnode-kb/articulos"
# Solo Week On-Chain. El KB también guarda Strategy Watch y piezas sueltas, que son otro
# producto y tienen su propio agente (glassnode_strategy).
PATRON_WOC = re.compile(r"^(\d{4})-(\d{2})-(\d{2})-the-week-on-?chain.*\.md$", re.I)


def gh(ruta):
    token = os.environ.get("GH_TOKEN", "").strip()
    if not token:
        sys.exit("ERROR: falta GH_TOKEN (lectura de Contents sobre el KB privado).")
    req = urllib.request.Request(
        f"https://api.github.com/repos/{REPO_KB}/contents/{ruta}",
        headers={"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json",
                 "User-Agent": "btc-cycle-terminal/sync-woc-reports",
                 "X-GitHub-Api-Version": "2022-11-28"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        sys.exit(f"ERROR HTTP {e.code} leyendo {ruta}: {e.read().decode('utf-8','replace')[:200]}")


def fechas_ya_publicadas():
    fechas = set()
    for p in glob.glob(os.path.join(DESTINO, "*.md")):
        m = re.match(r"(\d{8})-", os.path.basename(p))
        if m:
            f = m.group(1)
            fechas.add(f"{f[:4]}-{f[4:6]}-{f[6:]}")
    return fechas


def pendientes():
    """Artículos del KB posteriores al informe más reciente que ya tenemos.

    Se limita a lo POSTERIOR a propósito: el KB guarda desde 2019 y reprocesar 300 artículos
    no es el trabajo de un cron semanal. El histórico, si algún día hace falta, es una pasada
    manual con --max alto.
    """
    ya = fechas_ya_publicadas()
    if not ya:
        sys.exit("ERROR: no hay ni un informe en reports/. Debe existir al menos el de "
                 "referencia (20260722) para que el modelo sepa el formato.")
    corte = max(ya)
    out = []
    for entrada in gh(RUTA_KB):
        m = PATRON_WOC.match(entrada["name"])
        if not m:
            continue
        fecha = "-".join(m.groups())
        if fecha > corte and fecha not in ya:
            out.append((fecha, entrada["name"]))
    return sorted(out)


def descargar(nombre):
    d = gh(f"{RUTA_KB}/{nombre}")
    return base64.b64decode(d["content"]).decode("utf-8", "replace")


PROMPT = """Lee el artículo en {articulo} y el informe de referencia en {referencia}.

Escribe un informe destilado del artículo en la ruta exacta {salida}.

Reglas:
- El repo destino es PÚBLICO: escribe un RESUMEN ESTRUCTURADO PROPIO, con tus palabras. NO copies
  ni parafrasees frase a frase el artículo. Citas textuales solo si son cortas y entre comillas.
- Reproduce la estructura de cabecera del informe de referencia (título, Fuente, Autor, Fecha,
  Tipo, la línea "Cita como", el separador), adaptando fecha y título a este artículo.
- Mantén las secciones que use el artículo con sus encabezados.
- CONSERVA TODOS LOS NIVELES NUMÉRICOS con precisión: precios, porcentajes, umbrales, ratios.
  Son lo que el agente citará. En negrita, como en la referencia.
- Recoge explícitamente escenarios y condiciones de invalidación si el artículo los declara.
- Mismo idioma que la referencia (inglés).

No escribas ningún otro archivo ni modifiques nada más."""


def destilar(fecha, nombre, texto):
    if not os.environ.get("CLAUDE_CODE_OAUTH_TOKEN", "").strip():
        sys.exit("ERROR: falta CLAUDE_CODE_OAUTH_TOKEN. Genéralo con `claude setup-token` "
                 "y guárdalo como secret del repo.")
    slug = re.sub(r"[^a-z0-9]+", "-",
                  re.sub(r"^\d{4}-\d{2}-\d{2}-", "", nombre[:-3]).lower()).strip("-")[:60]
    salida = os.path.join(DESTINO, f"{fecha.replace('-','')}-{slug}.md")

    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as fh:
        fh.write(texto)
        tmp = fh.name
    try:
        cmd = ["claude", "-p", PROMPT.format(articulo=tmp, referencia=MODELO_REF, salida=salida),
               "--allowedTools", "Read,Write", "--permission-mode", "acceptEdits"]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=900)
    finally:
        os.unlink(tmp)

    # Verificar el RESULTADO, no que el comando saliera con 0. Es la lección de agosto:
    # un proceso que termina bien no significa que haya producido nada útil.
    if not os.path.exists(salida):
        print((r.stderr or r.stdout or "")[-800:], file=sys.stderr)
        return None, f"el modelo no creó {os.path.basename(salida)}"
    contenido = open(salida, encoding="utf-8").read()
    if len(contenido) < 1500:
        return None, f"{os.path.basename(salida)} sale demasiado corto ({len(contenido)} bytes)"
    if "Cita como" not in contenido:
        return None, f"{os.path.basename(salida)} no lleva la cabecera de la casa"
    return salida, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max", type=int, default=4, help="máximo de informes por ejecución")
    ap.add_argument("--listar", action="store_true", help="solo listar lo que falta")
    a = ap.parse_args()

    faltan = pendientes()
    if not faltan:
        print("Sin novedad: el agente ya tiene todos los Week On-Chain del KB.")
        return 0
    print(f"Faltan {len(faltan)} informe(s): " + ", ".join(f for f, _ in faltan))
    if a.listar:
        return 0

    hechos, fallos = [], []
    for fecha, nombre in faltan[:a.max]:
        print(f"  · destilando {fecha} …", flush=True)
        salida, error = destilar(fecha, nombre, descargar(nombre))
        if error:
            fallos.append((fecha, error))
            print(f"    ! {error}")
        else:
            hechos.append(salida)
            print(f"    ✓ {os.path.basename(salida)} ({os.path.getsize(salida)} bytes)")

    if len(faltan) > a.max:
        print(f"Quedan {len(faltan)-a.max} para la próxima (límite --max {a.max}).")
    print(f"\n{len(hechos)} informe(s) nuevos en agentes/glassnode_woc/reports/")
    if fallos:
        sys.exit("ERROR: " + " · ".join(f"{f}: {e}" for f, e in fallos))
    return 0


if __name__ == "__main__":
    sys.exit(main())
