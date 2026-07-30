#!/usr/bin/env python3
"""Ingesta de métricas ON-CHAIN gratis desde bitcoin-data.com (BGeometrics).

Baja unas pocas métricas (MVRV Z-Score, realized price, SOPR) y las guarda en
data/onchain/<metrica>.json como serie [{date, value}] para que el dashboard y
los backtests las lean sin depender de la API en cada carga.

FRUGAL A PROPÓSITO: el plan gratis de BGeometrics permite ~15 peticiones/día.
Cada métrica = 1 petición (trae el histórico completo de golpe), así que el lote
normal gasta len(METRICS) peticiones. Usa --probe para gastar solo 1 mientras
verificamos el formato.

Token: variable de entorno BGAPI_TOKEN (secreto; nunca en el código ni en el repo).

Uso:
  python ingesta/fetch_onchain.py --probe            # 1 métrica, imprime crudo
  python ingesta/fetch_onchain.py                    # todas, escribe data/onchain/
"""
import argparse, json, os, sys, urllib.request, urllib.error

BASE = "https://bitcoin-data.com/v1"
OUTDIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "onchain")

# nombre_local -> slug del endpoint en bitcoin-data.com.
# TODOS verificados el 30-jul-2026 con `descubrir_metricas.py` (ver data/onchain/_disponibilidad.json):
# devuelven 1.461 puntos = ventana MÓVIL de 4 años exactos (el plan gratis no da más histórico).
#
# El orden importa: si la cuota diaria (~15 peticiones) se agota, se pierden las de abajo.
# Arriba van las que Glassnode usa HOY para decidir (medido sobre sus conclusiones 2025-26,
# ver agentes/glassnode_tactico/catalogo_indicadores.md).
METRICS = {
    # --- la escalera de cost basis: los NIVELES que anclan sus decisiones ---
    "true_market_mean":   "true-market-mean",    # línea divisoria bull/bear (50% de conclusiones en 2026)
    "sth_realized_price": "sth-realized-price",  # STH cost basis: techo en bear, suelo en bull (32%)
    "realized_price":     "realized-price",      # suelo estructural del ciclo (17%)
    # --- flujos: el driver nº1 de sus conclusiones (67% en 2026) ---
    "realized_profit":    "realized-profit",
    "realized_loss":      "realized-loss",       # su condición de suelo: enfriar bajo $25M/día
    # --- osciladores de confirmación de régimen ---
    "sth_mvrv":           "sth-mvrv",            # reclamar 1,0 = condición de transición pre-bull
    "sth_sopr":           "sth-sopr",            # <1 sostenido = bear de manual
    "lth_sopr":           "lth-sopr",
    # --- contexto (ya no deciden en su método, pero los usan otros analistas/páginas) ---
    "mvrv_zscore":        "mvrv-zscore",         # OJO: métrica de Cowen/retail, NO de Glassnode
    "sopr":               "sopr",
}

# Pendiente: el % de supply en profit (umbrales 54,2 / 60 / 75 / 90 que marcan techos de
# rally de bear y confirmación de bull). El slug `supply-in-profit` da 404 — probar variantes
# con: python ingesta/descubrir_metricas.py --slugs percent-supply-in-profit,supply-profit,...

DATE_KEYS = ("d", "date", "theday", "day", "t")
IGNORE_KEYS = ("unixts",)  # columnas auxiliares que NO son el valor de la métrica

def fetch(slug):
    """GET /v1/<slug> con el token. Devuelve (status, texto_crudo)."""
    token = os.environ.get("BGAPI_TOKEN", "").strip()
    url = f"{BASE}/{slug}"
    req = urllib.request.Request(url, headers={
        "Accept": "application/json",
        "User-Agent": "btc-cycle-terminal/onchain",
        # BGeometrics acepta el token por cabecera; mandamos las dos variantes
        # habituales para no fallar por el nombre exacto.
        "x-bgapi-token": token,
        "Authorization": f"Bearer {token}",
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace")
    except Exception as e:
        return 0, f"__EXC__ {e}"

def normalize(raw):
    """Convierte la respuesta en [{date, value}] detectando las claves solo."""
    data = json.loads(raw)
    if isinstance(data, dict) and "data" in data:  # por si viene envuelto
        data = data["data"]
    if not isinstance(data, list) or not data:
        raise ValueError("respuesta no es una lista con datos")
    sample = data[0]
    dkey = next((k for k in sample if k.lower() in DATE_KEYS), None)
    # el valor es la primera clave que no es la fecha ni una columna auxiliar (unixTs)
    vkey = next((k for k in sample if k != dkey and k.lower() not in IGNORE_KEYS
                 and k.lower() not in DATE_KEYS), None)
    if not dkey or not vkey:
        raise ValueError(f"no encuentro claves fecha/valor en {sample}")
    out = []
    for row in data:
        try:
            out.append({"date": str(row[dkey]), "value": float(row[vkey])})
        except (KeyError, ValueError, TypeError):
            continue
    return out, dkey, vkey

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--probe", action="store_true", help="solo 1 métrica, imprime respuesta cruda")
    args = ap.parse_args()

    if not os.environ.get("BGAPI_TOKEN", "").strip():
        print("AVISO: BGAPI_TOKEN vacío — la API probablemente devolverá 401.", file=sys.stderr)

    items = list(METRICS.items())[:1] if args.probe else list(METRICS.items())
    os.makedirs(OUTDIR, exist_ok=True)
    ok = 0
    for name, slug in items:
        status, raw = fetch(slug)
        print(f"[{name}] GET /v1/{slug} -> HTTP {status}")
        if args.probe or status != 200:
            print("---- respuesta cruda (primeros 800 chars) ----")
            print(raw[:800])
            print("---- fin ----")
        if status != 200:
            continue
        try:
            series, dkey, vkey = normalize(raw)
            path = os.path.join(OUTDIR, f"{name}.json")
            with open(path, "w") as f:
                json.dump({"metric": name, "source": f"{BASE}/{slug}",
                           "points": len(series), "series": series}, f, indent=2)
            print(f"  -> {len(series)} puntos (fecha='{dkey}', valor='{vkey}') escrito en data/onchain/{name}.json")
            ok += 1
        except Exception as e:
            print(f"  !! no pude normalizar: {e}")
            print("  primeros 400 chars:", raw[:400])
    print(f"OK {ok}/{len(items)}")
    sys.exit(0 if (ok or args.probe) else 1)

if __name__ == "__main__":
    main()
