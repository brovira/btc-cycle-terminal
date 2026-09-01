#!/usr/bin/env python3
"""
Historico de RATIOS contra BTC (SOL/BTC, HYPE/BTC, ETH/BTC, BNB/BTC).

POR QUE EL RATIO Y NO EL PRECIO EN DOLARES
------------------------------------------
Para una posicion de liquidez concentrada lo unico que decide si te sales de rango
es el RATIO del par, no lo que hagan los dos activos contra el dolar. Y la
correlacion en dolares no lo predice: BTC y ETH tienen rho=0,90 a un ano y su ratio
igualmente se hundio un 43% dentro de esa misma ventana.

    sigma^2(ratio) = sigma_a^2 + sigma_b^2 - 2*rho*sigma_a*sigma_b

Con sigma_BTC~50%, sigma_ETH~70% y rho=0,90 la volatilidad del ratio sigue siendo
~33% anual. Por eso el rango se calibra sobre la serie del ratio y no sobre una
matriz de correlaciones.

SALIDA: data/ratios/<par>.json  +  data/ratios/_resumen.json

Solo stdlib. Uso:  python3 ingesta/fetch_ratios.py
"""
import json, math, sys, time, urllib.error, urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT   = Path(__file__).resolve().parents[1]
OUTDIR = ROOT / "data" / "ratios"
BASE   = "https://api.coingecko.com/api/v3"

# id de coingecko -> simbolo
ACTIVOS = {"bitcoin": "BTC", "solana": "SOL", "hyperliquid": "HYPE",
           "ethereum": "ETH", "binancecoin": "BNB"}
CONTRA  = "bitcoin"

def get(url, reintentos=5):
    for i in range(reintentos):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "btc-cycle-terminal/1.0",
                                                       "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            if e.code == 429:                      # rate limit: esperar de verdad
                time.sleep(15 * (i + 1)); continue
            if i == reintentos - 1: raise
            time.sleep(3 * (i + 1))
        except Exception:
            if i == reintentos - 1: raise
            time.sleep(3 * (i + 1))
    raise SystemExit(f"sin respuesta de {url}")

def serie_usd(cg_id):
    """days=max da granularidad diaria automatica; 'interval' exige clave de pago."""
    d = get(f"{BASE}/coins/{cg_id}/market_chart?vs_currency=usd&days=max")
    puntos = d.get("prices") or []
    if not puntos:
        raise SystemExit(f"{cg_id}: coingecko no devuelve precios")
    # un timestamp por dia, nos quedamos con el ultimo de cada dia
    por_dia = {}
    for ts, precio in puntos:
        if precio:
            por_dia[datetime.fromtimestamp(ts / 1000, timezone.utc).strftime("%Y-%m-%d")] = precio
    return por_dia

def percentil(v, p):
    if not v: return None
    s = sorted(v); k = (len(s) - 1) * p / 100
    lo, hi = math.floor(k), math.ceil(k)
    return s[lo] if lo == hi else s[lo] + (s[hi] - s[lo]) * (k - lo)

def estadisticas(fechas, valores):
    act = valores[-1]
    logs = [math.log(valores[i] / valores[i - 1])
            for i in range(1, len(valores)) if valores[i - 1] > 0]
    n = len(logs)
    vol = None
    if n > 30:
        mu = sum(logs) / n
        vol = math.sqrt(sum((x - mu) ** 2 for x in logs) / (n - 1)) * math.sqrt(365) * 100
    pcts = {f"p{p}": percentil(valores, p) for p in (1, 5, 10, 25, 50, 75, 90, 95, 99)}

    # Anchura de rango que HABRIA contenido el ratio el X% de los dias, centrada
    # en el valor de hoy. Es la traduccion directa a un rango de Uniswap v3.
    cobertura = {}
    for etiqueta, (lo_p, hi_p) in {"80%": (10, 90), "90%": (5, 95), "98%": (1, 99)}.items():
        lo, hi = percentil(valores, lo_p), percentil(valores, hi_p)
        cobertura[etiqueta] = {
            "min": lo, "max": hi,
            "desde_hoy_abajo_pct": (lo / act - 1) * 100,
            "desde_hoy_arriba_pct": (hi / act - 1) * 100,
            "anchura_total_pct": (hi / lo - 1) * 100,
        }
    pico = max(valores); suelo = min(valores)
    return {
        "dias": len(valores), "desde": fechas[0], "hasta": fechas[-1],
        "actual": act, "minimo": suelo, "maximo": pico,
        "caida_max_desde_pico_pct": (suelo / pico - 1) * 100,
        "vol_anualizada_pct": vol,
        "percentiles": pcts, "rango_para_cubrir": cobertura,
    }

def main():
    OUTDIR.mkdir(parents=True, exist_ok=True)
    print("descargando series USD de coingecko…")
    usd = {}
    for cg_id, sim in ACTIVOS.items():
        usd[cg_id] = serie_usd(cg_id)
        print(f"  {sim:>5}  {len(usd[cg_id])} dias  "
              f"{min(usd[cg_id])} → {max(usd[cg_id])}")
        time.sleep(8)          # el tier gratuito es estrecho: mejor ir sobrado

    resumen = {"generado": datetime.now(timezone.utc).isoformat(),
               "fuente": "coingecko market_chart days=max", "pares": {}}

    for cg_id, sim in ACTIVOS.items():
        if cg_id == CONTRA: continue
        comunes = sorted(set(usd[cg_id]) & set(usd[CONTRA]))
        if len(comunes) < 60:
            print(f"  {sim}/BTC: solo {len(comunes)} dias comunes, se omite"); continue
        valores = [usd[cg_id][f] / usd[CONTRA][f] for f in comunes]
        est = estadisticas(comunes, valores)
        par = f"{sim.lower()}_btc"
        (OUTDIR / f"{par}.json").write_text(json.dumps(
            {"par": f"{sim}/BTC", "fuente": "coingecko",
             "serie": [{"date": f, "value": v} for f, v in zip(comunes, valores)],
             **est}, ensure_ascii=False, indent=1))
        resumen["pares"][f"{sim}/BTC"] = est

        c = est["rango_para_cubrir"]["90%"]
        print(f"\n{sim}/BTC · {est['dias']} días · hoy {est['actual']:.6f}")
        print(f"   vol anualizada del ratio: {est['vol_anualizada_pct']:.1f}%")
        print(f"   caída máxima desde pico:  {est['caida_max_desde_pico_pct']:.1f}%")
        print(f"   rango que cubre el 90%:   {c['desde_hoy_abajo_pct']:+.1f}% / "
              f"{c['desde_hoy_arriba_pct']:+.1f}%  (anchura {c['anchura_total_pct']:.0f}%)")

    (OUTDIR / "_resumen.json").write_text(json.dumps(resumen, ensure_ascii=False, indent=1))
    print(f"\n→ data/ratios/  ({len(resumen['pares'])} pares)")
    return 0 if resumen["pares"] else 1

if __name__ == "__main__":
    sys.exit(main())
