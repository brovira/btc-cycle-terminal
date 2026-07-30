#!/usr/bin/env python3
"""Realized price y MVRV con HISTÓRICO LARGO (2010→hoy) desde Coin Metrics Community. GRATIS, sin key.

POR QUÉ EXISTE: BGeometrics (nuestra fuente principal) solo da una **ventana móvil de 4 años**, así que
un backtest ahí cubre ~1 ciclo. Coin Metrics Community sí tiene histórico completo, pero su métrica
`CapRealUSD` (realized cap) está detrás del muro de pago (403).

EL TRUCO: MVRV = market cap / realized cap  →  realized cap = market cap / MVRV
Y las tres piezas que hacen falta SÍ son gratis: `CapMVRVCur`, `CapMrktCurUSD`, `SplyCur`.

    realized_cap   = CapMrktCurUSD / CapMVRVCur
    realized_price = realized_cap  / SplyCur

VALIDADO (30-jul-2026): el realized price derivado coincide **al 0,0%** con el de BGeometrics en el
solape (2025-01-01: $41.014 en ambos). No hay costura entre fuentes para esta métrica.

GOTCHA de su API: pedir solo `start_time` con `page_size` devuelve datos RECIENTES, no el principio de
la serie. Hay que iterar con rangos CERRADOS (start_time + end_time) o seguir `next_page_token`.
Aquí se hace por tramos anuales, que además hace el progreso visible y reanudable.

Uso:
  python ingesta/fetch_onchain_largo.py                 # 2010 → hoy
  python ingesta/fetch_onchain_largo.py --desde 2015    # solo desde 2015
"""
import argparse, json, os, sys, urllib.request, urllib.error
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTDIR = os.path.join(ROOT, "data", "onchain")
BASE = "https://community-api.coinmetrics.io/v4/timeseries/asset-metrics"
METRICAS = "CapMVRVCur,CapMrktCurUSD,SplyCur"
UA = "Mozilla/5.0 (compatible; btc-cycle-terminal/1.0)"


def get_json(url):
    req = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=45) as r:
            return json.loads(r.read().decode("utf-8", "replace"))
    except urllib.error.HTTPError as e:
        print(f"  [HTTP {e.code}] {e.read().decode('utf-8','replace')[:140]}", file=sys.stderr)
    except Exception as e:
        print(f"  [err] {e}", file=sys.stderr)
    return None


def tramo(anio):
    """Un año completo, siguiendo next_page_token si hace falta."""
    filas, url = [], (f"{BASE}?assets=btc&metrics={METRICAS}&frequency=1d"
                      f"&start_time={anio}-01-01&end_time={anio}-12-31&page_size=1000")
    while url:
        j = get_json(url)
        if not j:
            break
        filas.extend(j.get("data", []))
        nxt = j.get("next_page_url") or None
        url = nxt if nxt else None
    return filas


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--desde", type=int, default=2010)
    a = ap.parse_args()

    hoy = date.today()
    rp, mvrv, saltados = [], [], []
    for anio in range(a.desde, hoy.year + 1):
        filas = tramo(anio)
        if not filas:
            saltados.append(anio)
            print(f"{anio}: sin datos")
            continue
        n_ok = 0
        for x in filas:
            f = str(x.get("time", ""))[:10]
            mv, mc, sp = x.get("CapMVRVCur"), x.get("CapMrktCurUSD"), x.get("SplyCur")
            if not (f and mv and mc and sp):
                continue
            try:
                mv, mc, sp = float(mv), float(mc), float(sp)
                if mv <= 0 or sp <= 0:
                    continue
                rp.append({"date": f, "value": round(mc / mv / sp, 4)})
                mvrv.append({"date": f, "value": round(mv, 6)})
                n_ok += 1
            except (TypeError, ValueError):
                continue
        print(f"{anio}: {n_ok} días")

    if not rp:
        print("No se obtuvo ningún dato — abortando sin escribir.", file=sys.stderr)
        sys.exit(1)

    rp.sort(key=lambda x: x["date"]); mvrv.sort(key=lambda x: x["date"])
    os.makedirs(OUTDIR, exist_ok=True)
    for nombre, serie, desc in [
        ("realized_price_largo", rp, "realized price DERIVADO: (CapMrktCurUSD/CapMVRVCur)/SplyCur"),
        ("mvrv_largo", mvrv, "MVRV ratio (CapMVRVCur) directo de Coin Metrics"),
    ]:
        with open(os.path.join(OUTDIR, f"{nombre}.json"), "w") as fh:
            json.dump({
                "metric": nombre,
                "source": "coinmetrics-community (derivado)" if "realized" in nombre else "coinmetrics-community",
                "formula": desc,
                "validado_vs_bgeometrics": "2025-01-01: 41.014 vs 41.014 (desvío 0,0%)" if "realized" in nombre else None,
                "points": len(serie),
                "series": serie,
            }, fh, indent=2)
        print(f"→ data/onchain/{nombre}.json  {len(serie)} pts  {serie[0]['date']} → {serie[-1]['date']}")
    if saltados:
        print("Años sin datos:", saltados)


if __name__ == "__main__":
    main()
