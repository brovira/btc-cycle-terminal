#!/usr/bin/env python3
"""Descubre QUÉ métricas on-chain están disponibles GRATIS (y con cuánto histórico).

Por qué existe: el sandbox de Claude Code no tiene salida a los hosts de datos, así que
la disponibilidad real solo se puede comprobar desde un sitio con red (tu máquina o una
GitHub Action). Este script prueba las dos fuentes gratis y escribe un informe.

Fuentes que prueba:
  1. BGeometrics (bitcoin-data.com/v1/<slug>) — necesita BGAPI_TOKEN. Plan gratis ~15 req/día,
     así que por defecto prueba solo los slugs de PRIORIDAD (los que Glassnode usa hoy).
  2. Coin Metrics Community (community-api.coinmetrics.io) — sin key, sin límite práctico.
     Se consulta su CATÁLOGO entero de una vez (1 petición) → lista completa de lo disponible.

Uso:
  python ingesta/descubrir_metricas.py              # prioritarios (gasta ~8 req de BGeometrics)
  python ingesta/descubrir_metricas.py --todos      # todos los candidatos (gasta más cuota)
  python ingesta/descubrir_metricas.py --solo-cm    # solo Coin Metrics (0 cuota BGeometrics)

Salida: data/onchain/_disponibilidad.json + resumen por consola.
"""
import argparse, json, os, sys, urllib.request, urllib.error

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data", "onchain", "_disponibilidad.json")
UA = "btc-cycle-terminal/descubrimiento"

# Slugs candidatos en BGeometrics. PRIORIDAD = lo que Glassnode usa para DECIDIR hoy
# (medido sobre resúmenes ejecutivos y conclusiones de 2025-26).
PRIORITARIOS = [
    "sth-realized-price",       # STH cost basis — la frontera táctica
    "sth-sopr",                 # confirmación de régimen STH
    "sth-mvrv",
    "true-market-mean",         # la línea bull/bear
    "realized-profit",          # flujo de beneficio realizado
    "realized-loss",            # flujo de pérdida realizada (condición de suelo)
    "supply-in-profit",         # % supply en profit (umbrales 54/60/75/90)
    "lth-sopr",
]
EXTRA = [
    "lth-realized-price", "active-realized-price", "aviv", "nupl", "sth-nupl", "lth-nupl",
    "realized-cap", "cdd", "liveliness", "reserve-risk", "puell-multiple",
    "sopr-adjusted", "hodl-waves", "sell-side-risk-ratio",
]

# Métricas de Coin Metrics que interesan (se comprueban contra su catálogo)
CM_INTERES = {
    "CapRealUSD": "Realized Cap → realized price = CapRealUSD / SplyCur",
    "SplyCur": "Supply circulante (denominador del realized price)",
    "CapMrktCurUSD": "Market cap (numerador de MVRV)",
    "SplyActPct1yr": "% supply activa en 1 año (proxy de dormancia/HODL)",
    "PriceUSD": "Precio (ya lo usamos)",
    "FeeTotUSD": "Fees (contexto de red)",
    "SplyAdrBalUSD1M": "Supply en direcciones con >$1M (proxy de cohortes grandes)",
}


def get(url, headers=None, timeout=30):
    req = urllib.request.Request(url, headers=headers or {"Accept": "application/json", "User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace")[:300]
    except Exception as e:
        return 0, f"__EXC__ {e}"


def probar_bgeometrics(slugs):
    token = os.environ.get("BGAPI_TOKEN", "").strip()
    if not token:
        print("AVISO: BGAPI_TOKEN vacío → BGeometrics devolverá 401. Exporta el token o usa --solo-cm.\n")
    res = {}
    for s in slugs:
        status, raw = get(f"https://bitcoin-data.com/v1/{s}",
                          {"Accept": "application/json", "User-Agent": UA,
                           "x-bgapi-token": token, "Authorization": f"Bearer {token}"})
        info = {"http": status}
        if status == 200:
            try:
                d = json.loads(raw)
                d = d.get("data", d) if isinstance(d, dict) else d
                info["puntos"] = len(d)
                if d:
                    keys = list(d[0].keys())
                    fecha = next((k for k in keys if k.lower() in ("d", "date", "theday", "day", "t")), None)
                    info["campos"] = keys
                    if fecha:
                        info["desde"], info["hasta"] = str(d[0][fecha]), str(d[-1][fecha])
            except Exception as e:
                info["error_parse"] = str(e)
        else:
            info["respuesta"] = raw[:160]
        res[s] = info
        marca = "OK " if status == 200 else "-- "
        print(f"  {marca}{s:26s} HTTP {status}"
              + (f"  {info.get('puntos','?')} pts  {info.get('desde','?')} → {info.get('hasta','?')}" if status == 200 else ""))
    return res


def probar_coinmetrics():
    print("\nCoin Metrics Community (catálogo completo, 1 petición):")
    status, raw = get("https://community-api.coinmetrics.io/v4/catalog/asset-metrics?assets=btc",
                      {"Accept": "application/json", "User-Agent": "Mozilla/5.0 (compatible; btc-cycle-terminal)"})
    if status != 200:
        print(f"  -- catálogo HTTP {status}: {raw[:160]}")
        return {"http": status}
    try:
        data = json.loads(raw)["data"][0]["metrics"]
    except Exception as e:
        print("  -- no pude parsear el catálogo:", e)
        return {"http": status, "error": str(e)}
    disponibles = {m["metric"] for m in data}
    print(f"  total métricas de BTC en el tier gratis: {len(disponibles)}")
    res = {"total": len(disponibles), "interes": {}}
    for m, para_que in CM_INTERES.items():
        hay = m in disponibles
        res["interes"][m] = hay
        print(f"  {'OK ' if hay else '-- '}{m:22s} {para_que}")
    # además, listar cualquier métrica cuyo nombre suene a lo que buscamos
    import re
    sugerencias = sorted(x for x in disponibles if re.search(r"real|prof|loss|mvrv|sply.*act", x, re.I))
    res["sugerencias"] = sugerencias
    if sugerencias:
        print(f"\n  Otras métricas del catálogo que suenan relevantes ({len(sugerencias)}):")
        print("   ", ", ".join(sugerencias[:40]))
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--todos", action="store_true", help="probar también los slugs EXTRA (más cuota)")
    ap.add_argument("--solo-cm", action="store_true", help="saltar BGeometrics (0 cuota)")
    a = ap.parse_args()

    informe = {}
    if not a.solo_cm:
        slugs = PRIORITARIOS + (EXTRA if a.todos else [])
        print(f"BGeometrics — probando {len(slugs)} slugs (cuota gratis ~15/día):")
        informe["bgeometrics"] = probar_bgeometrics(slugs)
    informe["coinmetrics"] = probar_coinmetrics()

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(informe, f, indent=2)
    print(f"\nInforme escrito en data/onchain/_disponibilidad.json")
    print("Súbelo (o pásamelo) y con eso cerramos qué se puede backtestear de verdad.")


if __name__ == "__main__":
    main()
