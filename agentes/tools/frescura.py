#!/usr/bin/env python3
"""Frescura de los transcripts de cada agente → `data/agentes_frescura.json`.

POR QUÉ EXISTE
--------------
El workflow `ingest-transcripts.yml` estuvo **26 días dando verde sin ingerir un solo vídeo**
(23-jul → 17-ago-2026): YouTube bloquea las IPs de los runners de CI, yt-dlp devolvía la lista
vacía, y tanto el script como el workflow lo trataban como éxito. Nadie se enteró porque no
había ningún sitio donde se viera que el archivo se estaba pudriendo.

Esto es el equivalente de `v_etl_freshness` de BELROGAM, pero para los agentes: mide la
antigüedad del transcript MÁS NUEVO de cada persona y la publica para que el dashboard la
pinte. Si el pipeline se vuelve a romper, se ve.

Uso:
  python3 agentes/tools/frescura.py            # escribe data/agentes_frescura.json
  python3 agentes/tools/frescura.py --check    # además sale con código 1 si algo está rancio
"""
import argparse, json, os, re, sys
from datetime import date, datetime, timezone

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# Umbral por persona: cuántos días sin publicar son NORMALES para ese canal.
# Cowen publica casi a diario; LMEC cada 2-3 semanas. Un umbral único daría falsos positivos
# en LMEC o se tragaría un fallo de una semana en Cowen.
UMBRAL_DIAS = {
    "cowen": 10,
    "lmec": 30,
    "glassnode_tactico": 45,
}
UMBRAL_POR_DEFECTO = 30


def ultimo_transcript(carpeta):
    """(fecha_iso, nombre) del transcript más reciente, por la fecha del NOMBRE (AAAAMMDD-)."""
    mejor = None
    if not os.path.isdir(carpeta):
        return None, None
    for nombre in os.listdir(carpeta):
        m = re.match(r"(\d{8})-.+\.md$", nombre)
        if not m or m.group(1) == "00000000":
            continue
        try:
            f = datetime.strptime(m.group(1), "%Y%m%d").date()
        except ValueError:
            continue
        if mejor is None or f > mejor[0]:
            mejor = (f, nombre)
    return (mejor[0].isoformat(), mejor[1]) if mejor else (None, None)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="salir con código 1 si alguna persona está rancia (para CI)")
    a = ap.parse_args()

    base = os.path.join(REPO, "agentes")
    hoy = date.today()
    personas = []
    for persona in sorted(os.listdir(base)):
        carpeta = os.path.join(base, persona, "yt-transcripts")
        if not os.path.isdir(carpeta):
            continue
        iso, nombre = ultimo_transcript(carpeta)
        umbral = UMBRAL_DIAS.get(persona, UMBRAL_POR_DEFECTO)
        n = len([x for x in os.listdir(carpeta) if x.endswith(".md")])
        sin_fecha = len([x for x in os.listdir(carpeta) if x.startswith("0000-")])
        dias = (hoy - date.fromisoformat(iso)).days if iso else None
        estado = "sin_datos" if dias is None else ("rancio" if dias > umbral else "ok")
        personas.append({
            "persona": persona, "ultimo": iso, "ultimo_archivo": nombre,
            "dias": dias, "umbral_dias": umbral, "estado": estado,
            "n_transcripts": n, "sin_fecha": sin_fecha,
        })

    salida = {
        "_que_es": "Frescura del archivo de transcripts por agente. Lo genera "
                   "agentes/tools/frescura.py; el workflow ingest-transcripts.yml lo regenera "
                   "tras cada ingesta. Si 'estado' es 'rancio', la ingesta lleva rota "
                   "más días de los normales para ese canal.",
        "generado": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "personas": personas,
    }
    destino = os.path.join(REPO, "data", "agentes_frescura.json")
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    with open(destino, "w", encoding="utf-8") as f:
        json.dump(salida, f, ensure_ascii=False, indent=1)
        f.write("\n")

    for p in personas:
        marca = {"ok": "✓", "rancio": "✗", "sin_datos": "?"}[p["estado"]]
        extra = f" · {p['sin_fecha']} sin fecha" if p["sin_fecha"] else ""
        print(f"  {marca} {p['persona']:<20} último {p['ultimo'] or '—'} "
              f"({p['dias'] if p['dias'] is not None else '—'} días, umbral {p['umbral_dias']}) "
              f"· {p['n_transcripts']} transcripts{extra}")
    print(f"\nEscrito {os.path.relpath(destino, REPO)}")

    rancios = [p for p in personas if p["estado"] != "ok"]
    if a.check and rancios:
        print("\nERROR: archivo rancio en " + ", ".join(p["persona"] for p in rancios),
              file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
