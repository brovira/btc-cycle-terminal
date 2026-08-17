#!/usr/bin/env python3
"""frescura.py — ¿está caducado el material del que viven los agentes?

POR QUÉ EXISTE
--------------
El 16-ago-2026 los cinco agentes respondieron con material de entre 4 y 7 semanas
mientras TODOS los workflows salían en verde. Cada pipeline informaba de su propia
ejecución ("he corrido, no he petado") y ninguno informaba de lo único que importa:
si el dato que hay en disco sigue sirviendo.

Este script no mira pipelines. Mira FECHAS DE DATOS. Da igual por qué se quedó atrás
—bug, token que falta, cron inexistente, la fuente caída, YouTube bloqueando— si el
dato está viejo, esto se pone rojo.

Es deliberadamente tonto: no arregla nada, solo se niega a decir que todo va bien.

USO
  python ingesta/frescura.py            # informe + sale 1 si algo está caducado
  python ingesta/frescura.py --aviso    # solo avisa, siempre sale 0
"""
import json, os, re, sys, glob
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOY = datetime.now(timezone.utc).date()

# (etiqueta, cómo se obtiene la fecha, límite en días, por qué ese límite)
# Los límites son ~2x la cadencia real: un margen implica un fallo, no un fin de semana.
FUENTES = []


def _fecha_max_por_nombre(patron):
    """Transcripts: el nombre del archivo es YYYYMMDD-slug.md."""
    mejor = None
    for p in glob.glob(os.path.join(ROOT, patron)):
        m = re.match(r"(\d{8})-", os.path.basename(p))
        if not m:
            continue
        try:
            d = datetime.strptime(m.group(1), "%Y%m%d").date()
        except ValueError:
            continue
        if mejor is None or d > mejor:
            mejor = d
    return mejor


def _fecha_json_series(ruta):
    """data/onchain/*.json → {"series":[{"date": "YYYY-MM-DD", ...}]}"""
    try:
        s = json.load(open(os.path.join(ROOT, ruta)))["series"]
        return datetime.strptime(s[-1]["date"], "%Y-%m-%d").date()
    except Exception:
        return None


def _fecha_json_fechas(ruta):
    """data/checkonchain/*.json → {"fechas": ["YYYY-MM-DD", ...]}"""
    try:
        f = json.load(open(os.path.join(ROOT, ruta)))["fechas"]
        return datetime.strptime(f[-1], "%Y-%m-%d").date()
    except Exception:
        return None


def _fecha_woc():
    try:
        d = json.load(open(os.path.join(ROOT, "data/woc_semana.json")))
        return datetime.strptime(d["woc_fecha"], "%Y-%m-%d").date()
    except Exception:
        return None


COMPROBACIONES = [
    ("Transcripts · Cowen", lambda: _fecha_max_por_nombre("agentes/cowen/yt-transcripts/*.md"),
     7, "publica casi a diario"),
    ("Transcripts · LMEC", lambda: _fecha_max_por_nombre("agentes/lmec/yt-transcripts/*.md"),
     14, "publica cada pocos días"),
    ("WoC · informes del agente", lambda: _fecha_max_por_nombre("agentes/glassnode_woc/reports/*.md"),
     14, "semanal; hoy es MANUAL, nada lo escribe"),
    ("WoC · resumen del dashboard", _fecha_woc,
     14, "semanal, jueves (sync-woc.yml)"),
    ("On-chain · BGeometrics", lambda: _fecha_json_series("data/onchain/mvrv_zscore.json"),
     4, "diario (onchain.yml)"),
    ("On-chain · realized price", lambda: _fecha_json_series("data/onchain/realized_price.json"),
     4, "diario (onchain.yml)"),
    ("Checkonchain · cost basis", lambda: _fecha_json_fechas("data/checkonchain/pricing__pricing_costbasisoriginals.json"),
     5, "diario (checkonchain.yml)"),
    ("Checkonchain · derivados", lambda: _fecha_json_fechas("data/checkonchain/derivatives__options_atmimpliedvolatility.json"),
     5, "diario; alimenta el semáforo de LP"),
    # urpd__urpd.json NO se comprueba: es un snapshot sin eje temporal ("distribuciones",
    # no "fechas"), así que no puede declarar su propia edad. Se refresca en el mismo lote
    # que el resto de checkonchain, de modo que la fila de "cost basis" ya lo cubre.
]


def main():
    solo_aviso = "--aviso" in sys.argv
    caducados, ausentes, filas = [], [], []

    for etiqueta, fn, limite, nota in COMPROBACIONES:
        fecha = fn()
        if fecha is None:
            ausentes.append(etiqueta)
            filas.append(("SIN DATO", etiqueta, "—", "", nota))
            continue
        dias = (HOY - fecha).days
        mal = dias > limite
        if mal:
            caducados.append((etiqueta, fecha, dias, limite))
        filas.append(("  RANCIO" if mal else "      ok", etiqueta,
                      fecha.isoformat(), f"{dias}d / máx {limite}d", nota))

    ancho = max(len(f[1]) for f in filas)
    print(f"\nFrescura del material · {HOY.isoformat()}\n")
    for estado, etiqueta, fecha, edad, nota in filas:
        print(f"{estado} │ {etiqueta.ljust(ancho)} │ {fecha:<12} {edad:<16} {nota}")

    print()
    if not caducados and not ausentes:
        print("Todo al día.")
        return 0

    for etiqueta, fecha, dias, limite in caducados:
        print(f"CADUCADO: {etiqueta} — última fecha {fecha}, {dias} días (máx {limite}).")
    for etiqueta in ausentes:
        print(f"SIN DATO: {etiqueta} — el archivo no existe o no se pudo leer.")

    print("\nUn dato caducado se siente igual de convincente que uno fresco.")
    print("No decidas capital con esto hasta arreglarlo.")
    return 0 if solo_aviso else 1


if __name__ == "__main__":
    sys.exit(main())
