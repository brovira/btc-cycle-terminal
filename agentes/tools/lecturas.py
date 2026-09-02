#!/usr/bin/env python3
"""lecturas.py — pase DIARIO que mantiene al día la lectura actual de cada analista.

QUÉ ES UNA "LECTURA"
--------------------
Lo que cada uno dice HOY, en su propio marco, reducido a lo que sirve para decidir con las
pools: tendencia, escenario, niveles, y (según quién) sus posiciones de farming (LMEC) o el
rango que espera para el precio (WoC). Vive en `data/lecturas/<agente>.json` y el panel de LPs
la enseña en la sección "Decisiones".

POR QUÉ UN PASE DIARIO Y NO UNO POR CADENCIA
--------------------------------------------
No publican con horario: Cowen casi a diario, WoC los miércoles/jueves, LMEC una vez al mes.
El pase corre cada día para los tres y SOLO llama al modelo cuando hay material nuevo
(transcript o informe con fecha posterior a la última lectura). Si no hay nada nuevo, no
gasta nada y no toca el fichero.

CÓMO SE PAGA
------------
Como sync_woc_reports.py: `claude -p` en modo headless con CLAUDE_CODE_OAUTH_TOKEN (la
suscripción), no con la API. Sin token, el pase deja constancia de que hay material nuevo
SIN LEER (`pendiente`) y conserva la última lectura buena; el panel avisa.

CADA LECTURA LLEVA FECHA Y FUENTE. El marco de cada uno cambia con el tiempo y una lectura
vieja hay que verla como vieja: el panel marca en ámbar la que supera el doble de su cadencia.

USO
  python agentes/tools/lecturas.py                # los tres
  python agentes/tools/lecturas.py --agente lmec  # uno
  python agentes/tools/lecturas.py --listar       # solo dice qué hay nuevo, sin modelo
"""
import argparse, glob, json, os, re, subprocess, sys, tempfile
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SALIDA_DIR = os.path.join(ROOT, "data", "lecturas")

AGENTES = {
    "cowen": {
        "nombre": "Benjamin Cowen",
        "carpeta": os.path.join("agentes", "cowen", "yt-transcripts"),
        "cadencia_dias": 2, "max_fuentes": 3, "chars_por_fuente": 14000,
        "marco": "ciclo de 4 anos, risk metric, 200-week SMA, bull market support band (20W SMA / 21W EMA), "
                 "50-week SMA, dominancia BTC, macro (Fed, tipos, liquidez)",
        "extra": '''  "risk_metric": numero_0_a_1_o_null,
  "niveles": {"ma200w": num_o_null, "bmsb": num_o_null, "ma50w": num_o_null, "objetivo_correccion": num_o_null, "invalidacion": num_o_null},''',
    },
    "lmec": {
        "nombre": "LMEC",
        "carpeta": os.path.join("agentes", "lmec", "yt-transcripts"),
        "cadencia_dias": 30, "max_fuentes": 2, "chars_por_fuente": 20000,
        "marco": "ciclo BTC (halving cycle profit), Bull Market Support Band, RSI/MACD semanal, MVRV Z, 200W SMA, "
                 "DCA con ordenes limite, y sus pools de liquidez / farming (pares, rangos, volumen/TVL)",
        "extra": '''  "posiciones": [{"par": "BNB/ETH", "protocolo": "Uniswap v3", "red": "Ethereum", "rango": "texto tal cual lo dice (p.ej. +/-140%)", "peso": "% de cartera o importe si lo dice, si no null", "comentario": "1 frase"}],
  "cartera": {"stables_pct": num_o_null, "btc_pct": num_o_null, "alts_pct": num_o_null, "farming_pct": num_o_null},
  "niveles": {"soporte": num_o_null, "resistencia": num_o_null, "objetivo": num_o_null, "compra_escalonada": [nums_o_vacio]},''',
    },
    "woc": {
        "nombre": "Glassnode · Week On-Chain",
        "carpeta": os.path.join("agentes", "glassnode_woc", "reports"),
        "cadencia_dias": 7, "max_fuentes": 1, "chars_por_fuente": 24000,
        "marco": "escalera de cost basis (Realized Price, True Market Mean, STH cost basis y sus bandas +/-1 sigma, "
                 "quantiles, URPD), supply in profit/loss, SOPR, funding/OI/skew, y su recomendacion de LP",
        "extra": '''  "rango_esperado": {"bajo": num_usd, "alto": num_usd, "base": "de que niveles sale (p.ej. STH cost basis -1 sigma a resistencia URPD)"},
  "regimen_leverage": "texto corto o null",
  "accion_lp": "MANTENER" | "ESTRECHAR" | "ENSANCHAR" | "REDUCIR" | "SALIR" | "FARM" | null,
  "niveles": {"sth_cost_basis": num_o_null, "true_market_mean": num_o_null, "realized_price": num_o_null, "soporte": num_o_null, "resistencia": num_o_null, "sth_menos_1s": num_o_null, "sth_mas_1s": num_o_null},''',
    },
}

ESQUEMA = '''{{
  "agente": "{clave}",
  "nombre": "{nombre}",
  "fuente_fecha": "{fecha}",
  "fuentes": {fuentes},
  "titulo": "titulo del video/informe mas reciente",
  "tendencia": "alcista" | "bajista" | "neutral" | "lateral",
  "horizonte": "dias" | "semanas" | "meses",
  "escenario": "2-3 frases con SU escenario base, en sus terminos, con cifras si las da",
{extra}
  "accion": "su postura en 1 frase (que hace o recomienda hacer EL)",
  "para_mis_lps": "1-2 frases: que implica su lectura para rangos de liquidez concentrada BTC/USDC o pares volatiles (sin inventar: si no aplica, dilo)",
  "citas": ["cita corta textual 1", "cita corta textual 2"],
  "confianza": "alta" | "media" | "baja",
  "cambios_vs_anterior": "1 frase: que cambia respecto a la lectura anterior que te paso (o 'primera lectura')"
}}'''

PROMPT = """Lee estos ficheros con la herramienta Read (son transcripts/informes de {nombre}, marco: {marco}):
{lista}

{anterior}
Escribe con la herramienta Write UN UNICO fichero JSON en {salida} con exactamente esta forma (JSON valido, sin markdown, sin comentarios):
{esquema}

Reglas:
- Extrae SU lectura, no la tuya. No inventes cifras: si no la dice, null. Si algo no aplica, dilo en el campo.
- Los transcripts son speech-to-text con erratas (p.ej. "200 semanas" puede salir raro): usa el contexto.
- Manda lo mas RECIENTE si varios ficheros se contradicen; anota el cambio en cambios_vs_anterior.
- Las citas, cortas y textuales (max 25 palabras cada una), en el idioma original.
- No escribas ningun otro fichero ni modifiques nada mas."""


def hoy():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def fuentes_de(clave):
    cfg = AGENTES[clave]
    out = []
    for fp in glob.glob(os.path.join(ROOT, cfg["carpeta"], "*.md")):
        m = re.match(r"(\d{8})-", os.path.basename(fp))
        if not m:
            continue
        d = m.group(1)
        out.append({"fecha": f"{d[:4]}-{d[4:6]}-{d[6:]}", "fichero": os.path.basename(fp), "ruta": fp})
    out.sort(key=lambda x: (x["fecha"], x["fichero"]))
    return out


def cargar(clave):
    p = os.path.join(SALIDA_DIR, f"{clave}.json")
    if os.path.exists(p):
        try:
            return json.load(open(p, encoding="utf-8"))
        except json.JSONDecodeError:
            pass
    return None


def guardar(clave, doc):
    os.makedirs(SALIDA_DIR, exist_ok=True)
    with open(os.path.join(SALIDA_DIR, f"{clave}.json"), "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
        f.write("\n")


def llamar_modelo(clave, nuevas, anterior):
    """Devuelve (dict, None) o (None, motivo). Verifica el RESULTADO, no el exit code."""
    if not os.environ.get("CLAUDE_CODE_OAUTH_TOKEN", "").strip():
        return None, "falta CLAUDE_CODE_OAUTH_TOKEN (secret del repo; se genera con `claude setup-token`)"
    cfg = AGENTES[clave]
    # Se recortan por el final: lo ultimo del video suele ser despedida/publicidad, y el
    # inicio lleva la tesis. Para no pasar ficheros gigantes, se copian recortados a /tmp.
    tmpdir = tempfile.mkdtemp(prefix=f"lectura-{clave}-")
    rutas = []
    for fu in nuevas[-cfg["max_fuentes"]:]:
        txt = open(fu["ruta"], encoding="utf-8", errors="replace").read()[: cfg["chars_por_fuente"]]
        dst = os.path.join(tmpdir, fu["fichero"])
        open(dst, "w", encoding="utf-8").write(txt)
        rutas.append((fu, dst))
    salida = os.path.join(tmpdir, "lectura.json")
    lista = "\n".join(f"- {dst}  (fecha {fu['fecha']}, fichero original {fu['fichero']})" for fu, dst in rutas)
    ant = ""
    if anterior and not anterior.get("pendiente_inicial"):
        resumen_ant = {k: anterior.get(k) for k in ("fuente_fecha", "tendencia", "escenario", "accion", "niveles", "posiciones", "rango_esperado") if anterior.get(k) is not None}
        ant = "LECTURA ANTERIOR (para el campo cambios_vs_anterior):\n" + json.dumps(resumen_ant, ensure_ascii=False) + "\n"
    esquema = ESQUEMA.format(clave=clave, nombre=cfg["nombre"], fecha=nuevas[-1]["fecha"],
                             fuentes=json.dumps([fu["fichero"] for fu, _ in rutas], ensure_ascii=False),
                             extra=cfg["extra"])
    prompt = PROMPT.format(nombre=cfg["nombre"], marco=cfg["marco"], lista=lista, anterior=ant,
                           salida=salida, esquema=esquema)
    cmd = ["claude", "-p", prompt, "--allowedTools", "Read,Write", "--permission-mode", "acceptEdits"]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=900)
    except FileNotFoundError:
        return None, "no esta el CLI `claude` en el PATH"
    except subprocess.TimeoutExpired:
        return None, "el modelo no termino en 15 minutos"
    if not os.path.exists(salida):
        return None, "el modelo no escribio el JSON: " + (r.stderr or r.stdout or "")[-300:].replace("\n", " ")
    try:
        doc = json.load(open(salida, encoding="utf-8"))
    except json.JSONDecodeError as e:
        return None, f"JSON invalido: {e}"
    for k in ("tendencia", "escenario", "accion", "fuente_fecha"):
        if not doc.get(k):
            return None, f"falta el campo {k}"
    if doc["tendencia"] not in ("alcista", "bajista", "neutral", "lateral"):
        return None, f"tendencia fuera de vocabulario: {doc['tendencia']}"
    return doc, None


def procesar(clave, solo_listar=False):
    cfg = AGENTES[clave]
    fuentes = fuentes_de(clave)
    if not fuentes:
        print(f"{clave}: sin fuentes en {cfg['carpeta']}")
        return "sin fuentes"
    anterior = cargar(clave)
    ultima_leida = (anterior or {}).get("fuente_fecha") or "0000-00-00"
    nuevas = [f for f in fuentes if f["fecha"] > ultima_leida]
    if not nuevas:
        print(f"{clave}: sin novedad (ultima fuente {fuentes[-1]['fecha']}, ya leida)")
        return "sin novedad"
    print(f"{clave}: {len(nuevas)} fuente(s) nueva(s) desde {ultima_leida}: " + ", ".join(f["fichero"] for f in nuevas[-3:]))
    if solo_listar:
        return "hay novedad"

    doc, error = llamar_modelo(clave, nuevas, anterior)
    ahora = datetime.now(timezone.utc).isoformat(timespec="seconds")
    if error:
        print(f"  ! {error}")
        base = anterior or {"agente": clave, "nombre": cfg["nombre"], "pendiente_inicial": True}
        base["pendiente"] = {"desde": nuevas[-1]["fecha"], "fuentes": [f["fichero"] for f in nuevas[-3:]],
                             "motivo": error, "detectado": ahora}
        base.setdefault("cadencia_dias", cfg["cadencia_dias"])
        guardar(clave, base)
        return "pendiente"

    historial = (anterior or {}).get("historial") or []
    if anterior and anterior.get("fuente_fecha") and not anterior.get("pendiente_inicial"):
        previa = {k: v for k, v in anterior.items() if k not in ("historial", "pendiente")}
        historial = ([previa] + historial)[:12]
    doc.update({"agente": clave, "nombre": cfg["nombre"], "cadencia_dias": cfg["cadencia_dias"],
                "actualizado": ahora, "historial": historial})
    doc.pop("pendiente", None)
    guardar(clave, doc)
    print(f"  ✓ lectura {doc['fuente_fecha']}: {doc['tendencia']} — {doc['escenario'][:90]}…")
    return "actualizada"


def escribir_indice(resultados):
    idx = {"actualizado": datetime.now(timezone.utc).isoformat(timespec="seconds"), "agentes": {}}
    for clave, cfg in AGENTES.items():
        d = cargar(clave) or {}
        idx["agentes"][clave] = {
            "nombre": cfg["nombre"], "cadencia_dias": cfg["cadencia_dias"],
            "fuente_fecha": d.get("fuente_fecha"), "actualizado": d.get("actualizado"),
            "tendencia": d.get("tendencia"), "pendiente": d.get("pendiente"),
            "resultado_pase": resultados.get(clave),
        }
    os.makedirs(SALIDA_DIR, exist_ok=True)
    with open(os.path.join(SALIDA_DIR, "_indice.json"), "w", encoding="utf-8") as f:
        json.dump(idx, f, ensure_ascii=False, indent=1)
        f.write("\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--agente", choices=list(AGENTES))
    ap.add_argument("--listar", action="store_true")
    a = ap.parse_args()
    resultados = {}
    for clave in ([a.agente] if a.agente else list(AGENTES)):
        resultados[clave] = procesar(clave, solo_listar=a.listar)
    if not a.listar:
        escribir_indice(resultados)
    resumen = " · ".join(f"{k}: {v}" for k, v in resultados.items())
    print("\n==== LECTURAS ====\n" + resumen)
    gp = os.environ.get("GITHUB_STEP_SUMMARY")
    if gp:
        open(gp, "a").write("### Lecturas diarias\n\n" + resumen + "\n")
    # Codigo 2 = hay material nuevo que no se pudo leer (sin token o fallo del modelo):
    # el workflow lo convierte en aviso, no en fallo, pero queda a la vista.
    return 2 if "pendiente" in resultados.values() else 0


if __name__ == "__main__":
    sys.exit(main())
