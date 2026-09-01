#!/usr/bin/env python3
"""
Historico de RATIOS contra BTC (SOL/BTC, HYPE/BTC, ETH/BTC, BNB/BTC).

POR QUE EL RATIO Y NO EL PRECIO EN DOLARES
------------------------------------------
En una posicion de liquidez concentrada lo unico que decide si te sales de rango es
el RATIO del par. La correlacion en dolares NO lo predice: BTC y ETH tienen rho=0,90
a un ano y su ratio se hundio un 43% dentro de esa misma ventana.

    sigma^2(ratio) = sigma_a^2 + sigma_b^2 - 2*rho*sigma_a*sigma_b

FUENTES, Y POR QUE HAY VARIAS
-----------------------------
Dos intentos fallaron contra la realidad y por eso esto es una cadena, no una fuente:
  · CoinGecko  -> 401: days=max es de pago en el tier gratuito
  · api.binance.com -> 451 (Unavailable For Legal Reasons): geobloquea las IP de
    los runners de GitHub, que estan en EEUU. No es rate limit, es un muro.
Se prueban varias en orden y se declara cual sirvio. Si ninguna responde para un par,
ese par se OMITE diciendolo: nunca se rellena con otra cosa.

Todo se pide contra USDT y el ratio se deriva dividiendo. Un unico camino de codigo
en vez de uno directo y otro derivado, y USDT existe para los cinco activos.

SALIDA: data/ratios/<par>.json  +  data/ratios/_resumen.json
"""
import json, math, sys, time, urllib.error, urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT   = Path(__file__).resolve().parents[1]
OUTDIR = ROOT / "data" / "ratios"
ACTIVOS = ["BTC", "SOL", "HYPE", "ETH", "BNB"]
BASE_QUOTE = "BTC"

def get(url, reintentos=3, timeout=45):
    ultimo = None
    for i in range(reintentos):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 btc-cycle-terminal"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            ultimo = f"HTTP {e.code}"
            if e.code in (451, 403, 401): raise FuenteBloqueada(ultimo)   # inutil reintentar
            time.sleep(2 * (i + 1))
        except Exception as e:
            ultimo = f"{type(e).__name__}"; time.sleep(2 * (i + 1))
    raise FuenteBloqueada(ultimo or "sin respuesta")

class FuenteBloqueada(RuntimeError): pass

def _dia(ms): return datetime.fromtimestamp(ms / 1000, timezone.utc).strftime("%Y-%m-%d")

# ─── adaptadores: cada uno devuelve {fecha: cierre} contra USDT ───────────────
def src_binance_vision(sim):
    """Mirror publico de datos de Binance; no arrastra el geobloqueo de la API."""
    out, desde = {}, 0
    while True:
        lote = get(f"https://data-api.binance.vision/api/v3/klines"
                   f"?symbol={sim}USDT&interval=1d&limit=1000&startTime={desde}")
        if not lote: break
        for k in lote: out[_dia(k[0])] = float(k[4])
        if len(lote) < 1000: break
        desde = lote[-1][6] + 1; time.sleep(0.25)
    return out

def src_okx(sim):
    out, antes = {}, ""
    for _ in range(40):                      # 100 velas por pagina
        u = (f"https://www.okx.com/api/v5/market/history-candles"
             f"?instId={sim}-USDT&bar=1Dutc&limit=100" + (f"&after={antes}" if antes else ""))
        d = get(u)
        filas = d.get("data") or []
        if not filas: break
        for f in filas: out[_dia(int(f[0]))] = float(f[4])
        antes = filas[-1][0]; time.sleep(0.25)
    return out

def src_coinbase(sim):
    """Granularidad diaria, 300 velas por peticion, hacia atras por tiempo."""
    import urllib.parse
    out, fin = {}, None
    for _ in range(40):
        u = f"https://api.exchange.coinbase.com/products/{sim}-USD/candles?granularity=86400"
        if fin: u += "&end=" + urllib.parse.quote(fin)
        filas = get(u)
        if not isinstance(filas, list) or not filas: break
        for f in filas: out[_dia(f[0] * 1000)] = float(f[4])
        fin = datetime.fromtimestamp(min(f[0] for f in filas), timezone.utc).isoformat()
        if len(filas) < 300: break
        time.sleep(0.3)
    return out

FUENTES = [("binance.vision", src_binance_vision), ("okx", src_okx), ("coinbase", src_coinbase)]

def serie(sim, diario):
    for nombre, fn in FUENTES:
        try:
            d = fn(sim)
            if len(d) >= 60:
                diario.append(f"  {sim:>5}  {nombre:<16} {len(d)} dias  {min(d)} → {max(d)}")
                return d, nombre
            diario.append(f"  {sim:>5}  {nombre:<16} solo {len(d)} dias, siguiente")
        except FuenteBloqueada as e:
            diario.append(f"  {sim:>5}  {nombre:<16} {e}")
        except Exception as e:
            diario.append(f"  {sim:>5}  {nombre:<16} {type(e).__name__}")
    return None, None

def percentil(v, p):
    s = sorted(v); k = (len(s) - 1) * p / 100
    lo, hi = math.floor(k), math.ceil(k)
    return s[lo] if lo == hi else s[lo] + (s[hi] - s[lo]) * (k - lo)

def estadisticas(fechas, valores):
    act = valores[-1]
    logs = [math.log(valores[i]/valores[i-1]) for i in range(1, len(valores)) if valores[i-1] > 0]
    vol = None
    if len(logs) > 30:
        mu = sum(logs)/len(logs)
        vol = math.sqrt(sum((x-mu)**2 for x in logs)/(len(logs)-1)) * math.sqrt(365) * 100
    cob = {}
    for et, (a, b) in {"80%": (10, 90), "90%": (5, 95), "98%": (1, 99)}.items():
        lo, hi = percentil(valores, a), percentil(valores, b)
        cob[et] = {"min": lo, "max": hi,
                   "desde_hoy_abajo_pct": (lo/act-1)*100, "desde_hoy_arriba_pct": (hi/act-1)*100,
                   "anchura_total_pct": (hi/lo-1)*100}
    pico, suelo = max(valores), min(valores)
    return {"dias": len(valores), "desde": fechas[0], "hasta": fechas[-1], "actual": act,
            "minimo": suelo, "maximo": pico,
            "caida_max_desde_pico_pct": (suelo/pico-1)*100, "vol_anualizada_pct": vol,
            "percentiles": {f"p{p}": percentil(valores, p) for p in (1,5,10,25,50,75,90,95,99)},
            "rango_para_cubrir": cob}

def main():
    OUTDIR.mkdir(parents=True, exist_ok=True)
    diario = []
    print("buscando fuente que responda para cada activo (contra USDT):")
    usd, origen = {}, {}
    for sim in ACTIVOS:
        d, fuente = serie(sim, diario)
        if d: usd[sim], origen[sim] = d, fuente
    print("\n".join(diario))

    if BASE_QUOTE not in usd:
        print(f"\nNinguna fuente sirve {BASE_QUOTE}. Sin el denominador no hay ratios.")
        return 1

    resumen = {"generado": datetime.now(timezone.utc).isoformat(),
               "metodo": "cada activo contra USDT; el ratio se deriva dividiendo",
               "fuentes_por_activo": origen, "pares": {}, "omitidos": [], "diario": diario}

    for sim in ACTIVOS:
        if sim == BASE_QUOTE: continue
        if sim not in usd:
            resumen["omitidos"].append({"par": f"{sim}/BTC", "motivo": "ninguna fuente respondio"})
            print(f"\n{sim}/BTC OMITIDO: ninguna fuente respondio."); continue
        fechas = sorted(set(usd[sim]) & set(usd[BASE_QUOTE]))
        if len(fechas) < 60:
            resumen["omitidos"].append({"par": f"{sim}/BTC", "motivo": f"solo {len(fechas)} dias comunes"})
            print(f"\n{sim}/BTC OMITIDO: solo {len(fechas)} dias comunes."); continue
        valores = [usd[sim][f] / usd[BASE_QUOTE][f] for f in fechas]
        est = estadisticas(fechas, valores)
        (OUTDIR / f"{sim.lower()}_btc.json").write_text(json.dumps(
            {"par": f"{sim}/BTC", "fuente": f"{origen[sim]} + {origen[BASE_QUOTE]} (via USDT)",
             "serie": [{"date": f, "value": v} for f, v in zip(fechas, valores)], **est},
            ensure_ascii=False, indent=1))
        resumen["pares"][f"{sim}/BTC"] = est
        c = est["rango_para_cubrir"]["90%"]
        print(f"\n{sim}/BTC · {est['dias']} dias ({est['desde']} → {est['hasta']}) · hoy {est['actual']:.6f}")
        print(f"   vol anualizada del ratio : {est['vol_anualizada_pct']:.1f}%")
        print(f"   caida maxima desde pico  : {est['caida_max_desde_pico_pct']:.1f}%")
        print(f"   rango que cubre el 90%   : {c['desde_hoy_abajo_pct']:+.1f}% / "
              f"{c['desde_hoy_arriba_pct']:+.1f}%  (anchura {c['anchura_total_pct']:.0f}%)")

    (OUTDIR / "_resumen.json").write_text(json.dumps(resumen, ensure_ascii=False, indent=1))
    print(f"\n→ data/ratios/  ({len(resumen['pares'])} pares, {len(resumen['omitidos'])} omitidos)")
    return 0 if resumen["pares"] else 1

if __name__ == "__main__":
    sys.exit(main())
