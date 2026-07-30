#!/usr/bin/env python3
"""Explora QUÉ fuentes de datos on-chain GRATIS existen, qué métricas dan y CUÁNTO HISTÓRICO.

Motivación: BGeometrics (nuestra fuente actual) solo da una **ventana móvil de 4 años**, así que el
backtest cubre ~1 ciclo. Si otra fuente gratis da histórico completo, podríamos validar reglas contra
los suelos de 2015 / 2018 / 2022 y no solo contra el actual. Este script busca eso.

NO gasta cuota de BGeometrics (se prueba aparte con descubrir_metricas.py).

Uso:
  python ingesta/descubrir_fuentes.py            # prueba todas las fuentes
  python ingesta/descubrir_fuentes.py --fuente coinmetrics

Salida: data/onchain/_fuentes.json + resumen por consola.
"""
import argparse, json, os, re, urllib.request, urllib.error

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data", "onchain", "_fuentes.json")
UA = "Mozilla/5.0 (compatible; btc-cycle-terminal/1.0)"

# Lo que buscamos, por orden de peso en las decisiones de Glassnode (ver catalogo_indicadores.md)
OBJETIVOS = [
    "realized profit/loss", "ETF flows", "true market mean", "STH cost basis",
    "realized price / realized cap", "% supply in profit", "spot CVD", "supply por cohorte",
]


def get(url, headers=None, timeout=35):
    h = {"Accept": "application/json", "User-Agent": UA}
    h.update(headers or {})
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=timeout) as r:
            return r.status, r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        try:    body = e.read().decode("utf-8", "replace")[:200]
        except Exception: body = ""
        return e.code, body
    except Exception as e:
        return 0, f"__EXC__ {e}"


def _rango_fechas(fechas):
    fechas = [f for f in fechas if f]
    return (min(fechas), max(fechas), len(fechas)) if fechas else (None, None, 0)


# ─────────────────────────── 1. Coin Metrics Community ───────────────────────────
def coinmetrics():
    """El gran candidato: sin key, y su histórico llega a 2010. Si tiene realized cap,
    podemos derivar el realized price de TODA la historia (no 4 años)."""
    r = {"fuente": "Coin Metrics Community", "url": "community-api.coinmetrics.io", "key": "no"}
    catal = None
    for u in [
        "https://community-api.coinmetrics.io/v4/catalog-v2/asset-metrics?assets=btc&page_size=10000",
        "https://community-api.coinmetrics.io/v4/catalog-all/asset-metrics?assets=btc&page_size=10000",
        "https://community-api.coinmetrics.io/v4/catalog/asset-metrics?assets=btc&page_size=10000",
        "https://community-api.coinmetrics.io/v4/reference-data/asset-metrics?page_size=10000",
    ]:
        st, raw = get(u)
        if st == 200:
            try:
                d = json.loads(raw).get("data", [])
                catal = d[0]["metrics"] if d and isinstance(d[0], dict) and "metrics" in d[0] else d
                if catal:
                    r["catalogo_endpoint"] = u.split("/v4/")[1][:30]
                    break
            except Exception:
                pass
    if catal:
        nombres = sorted({m.get("metric") for m in catal if isinstance(m, dict) and m.get("metric")})
        r["metricas_totales"] = len(nombres)
        r["relevantes"] = sorted(n for n in nombres
                                 if re.search(r"real|prof|loss|mvrv|sply|cap", n, re.I))[:60]
    # Probar de verdad las métricas clave y ver desde cuándo hay datos
    clave = "CapRealUSD,SplyCur,CapMrktCurUSD,PriceUSD"
    st, raw = get("https://community-api.coinmetrics.io/v4/timeseries/asset-metrics"
                  f"?assets=btc&metrics={clave}&frequency=1d&page_size=10&start_time=2010-01-01")
    r["prueba_http"] = st
    if st == 200:
        try:
            d = json.loads(raw)["data"]
            r["primer_dato"] = d[0].get("time", "")[:10] if d else None
            r["campos_devueltos"] = [k for k in (d[0] if d else {}) if k not in ("asset", "time")]
        except Exception as e:
            r["error"] = str(e)
    else:
        r["respuesta"] = raw[:200]
    # ¿hasta hoy?
    st2, raw2 = get("https://community-api.coinmetrics.io/v4/timeseries/asset-metrics"
                    f"?assets=btc&metrics={clave}&frequency=1d&page_size=3&start_time=2026-01-01")
    if st2 == 200:
        try:
            d2 = json.loads(raw2)["data"]
            r["ultimo_dato_2026"] = d2[-1].get("time", "")[:10] if d2 else None
        except Exception:
            pass
    return r


# ─────────────────────────── 2. Blockchain.com Charts ───────────────────────────
def blockchain_com():
    r = {"fuente": "Blockchain.com Charts", "url": "api.blockchain.info", "key": "no"}
    charts = ["market-price", "market-cap", "estimated-transaction-volume-usd", "mvrv", "nvt", "hash-rate"]
    r["graficos"] = {}
    for c in charts:
        st, raw = get(f"https://api.blockchain.info/charts/{c}?timespan=all&format=json&sampled=true")
        info = {"http": st}
        if st == 200:
            try:
                v = json.loads(raw).get("values", [])
                info["puntos"] = len(v)
                if v:
                    import datetime as dt
                    info["desde"] = dt.datetime.utcfromtimestamp(v[0]["x"]).strftime("%Y-%m-%d")
            except Exception as e:
                info["error"] = str(e)
        r["graficos"][c] = info
    return r


# ─────────────────────────── 3. Glassnode tier gratuito ───────────────────────────
def glassnode_free():
    """Glassnode tiene endpoints públicos con métricas T1 (resolución 24h). Sin key suele dar 401,
    pero conviene confirmarlo: si algún día tienes una key gratuita, esto es el camino directo."""
    r = {"fuente": "Glassnode API (tier free)", "url": "api.glassnode.com", "key": "requiere (gratis limitada)"}
    st, raw = get("https://api.glassnode.com/v1/metrics/market/price_usd_close?a=BTC&i=24h")
    r["sin_key_http"] = st
    r["respuesta"] = raw[:160]
    r["nota"] = ("401/403 = necesita API key. El tier gratis de Glassnode da métricas T1 con retardo; "
                 "si te registras, la key va en un secret y se añade un /api/glassnode como proxy.")
    return r


# ─────────────────────────── 4. Farside — flujos de ETF ───────────────────────────
def farside_etf():
    """2º driver de las conclusiones de Glassnode en 2026 (67%) y hoy no lo cubrimos."""
    r = {"fuente": "Farside Investors (ETF flows)", "url": "farside.co.uk", "key": "no", "formato": "HTML"}
    st, raw = get("https://farside.co.uk/bitcoin-etf-flow-all-data/", {"Accept": "text/html"})
    r["http"] = st
    if st == 200:
        r["bytes"] = len(raw)
        r["tiene_tabla"] = "<table" in raw.lower()
        fechas = re.findall(r"\d{2}\s+\w{3}\s+20\d{2}", raw)
        r["muestra_fechas"] = fechas[:3] + (["…"] + fechas[-3:] if len(fechas) > 6 else [])
        r["nota"] = "Scrapeable con pandas.read_html. Requiere ingestor propio (no hay API JSON)."
    else:
        r["respuesta"] = raw[:160]
    return r


# ─────────────────────────── 5. Otras fuentes candidatas ───────────────────────────
def otras():
    pruebas = {
        "mempool.space (fees/bloques)": "https://mempool.space/api/v1/mining/hashrate/1y",
        "CoinGecko (precio/mcap)":      "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=max&interval=daily",
        "Blockchair (stats)":           "https://api.blockchair.com/bitcoin/stats",
        "bitcoin-data.com (raíz API)":  "https://bitcoin-data.com/v1",
        "Checkonchain (charts JSON)":   "https://charts.checkonchain.com/",
    }
    out = {}
    for nombre, u in pruebas.items():
        st, raw = get(u, {"Accept": "*/*"}, timeout=25)
        out[nombre] = {"http": st, "bytes": len(raw) if st == 200 else 0,
                       "muestra": raw[:120] if st == 200 else raw[:120]}
    return out


FUENTES = {
    "coinmetrics": coinmetrics,
    "blockchain": blockchain_com,
    "glassnode": glassnode_free,
    "farside": farside_etf,
    "otras": otras,
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fuente", default="", help="probar solo una: " + ", ".join(FUENTES))
    a = ap.parse_args()
    sel = [a.fuente] if a.fuente else list(FUENTES)

    informe = {"objetivos": OBJETIVOS}
    for nombre in sel:
        fn = FUENTES.get(nombre)
        if not fn:
            print(f"fuente desconocida: {nombre}"); continue
        print(f"\n{'='*70}\n{nombre.upper()}\n{'='*70}")
        try:
            res = fn()
        except Exception as e:
            res = {"error": f"{type(e).__name__}: {e}"}
        informe[nombre] = res
        print(json.dumps(res, indent=1, ensure_ascii=False)[:2200])

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(informe, f, indent=2, ensure_ascii=False)
    print(f"\nInforme escrito en data/onchain/_fuentes.json")


if __name__ == "__main__":
    main()
