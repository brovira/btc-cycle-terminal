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

FUENTE: Binance klines. Sin clave y con historia completa. (CoinGecko se descarto:
su tier gratuito devuelve 401 a days=max, el historico largo es de pago.)

No se asume que un simbolo exista: se consulta exchangeInfo y se elige la ruta.
Para los pares sin mercado directo contra BTC se deriva via USDT.

SALIDA: data/ratios/<par>.json  +  data/ratios/_resumen.json
"""
import json, math, sys, time, urllib.error, urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT   = Path(__file__).resolve().parents[1]
OUTDIR = ROOT / "data" / "ratios"
BASE   = "https://api.binance.com/api/v3"
QUIERO = ["SOL", "HYPE", "ETH", "BNB"]

def get(url, reintentos=5):
    for i in range(reintentos):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "btc-cycle-terminal/1.0"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            if e.code in (418, 429):
                time.sleep(10 * (i + 1)); continue
            if i == reintentos - 1: raise
            time.sleep(3 * (i + 1))
        except Exception:
            if i == reintentos - 1: raise
            time.sleep(3 * (i + 1))
    raise SystemExit(f"sin respuesta de {url}")

def simbolos_vivos():
    info = get(f"{BASE}/exchangeInfo")
    return {s["symbol"] for s in info.get("symbols", []) if s.get("status") == "TRADING"}

def klines(simbolo):
    """Diarias desde el principio. 1000 por peticion, paginando por startTime."""
    salida, desde = {}, 0
    while True:
        lote = get(f"{BASE}/klines?symbol={simbolo}&interval=1d&limit=1000&startTime={desde}")
        if not lote: break
        for k in lote:
            f = datetime.fromtimestamp(k[0] / 1000, timezone.utc).strftime("%Y-%m-%d")
            salida[f] = float(k[4])                      # cierre
        if len(lote) < 1000: break
        desde = lote[-1][6] + 1
        time.sleep(0.3)
    return salida

def percentil(v, p):
    if not v: return None
    s = sorted(v); k = (len(s) - 1) * p / 100
    lo, hi = math.floor(k), math.ceil(k)
    return s[lo] if lo == hi else s[lo] + (s[hi] - s[lo]) * (k - lo)

def estadisticas(fechas, valores):
    act = valores[-1]
    logs = [math.log(valores[i] / valores[i-1]) for i in range(1, len(valores)) if valores[i-1] > 0]
    vol = None
    if len(logs) > 30:
        mu = sum(logs) / len(logs)
        vol = math.sqrt(sum((x-mu)**2 for x in logs) / (len(logs)-1)) * math.sqrt(365) * 100
    cobertura = {}
    for etiqueta, (a, b) in {"80%": (10, 90), "90%": (5, 95), "98%": (1, 99)}.items():
        lo, hi = percentil(valores, a), percentil(valores, b)
        cobertura[etiqueta] = {"min": lo, "max": hi,
                               "desde_hoy_abajo_pct": (lo/act - 1) * 100,
                               "desde_hoy_arriba_pct": (hi/act - 1) * 100,
                               "anchura_total_pct": (hi/lo - 1) * 100}
    pico, suelo = max(valores), min(valores)
    return {"dias": len(valores), "desde": fechas[0], "hasta": fechas[-1],
            "actual": act, "minimo": suelo, "maximo": pico,
            "caida_max_desde_pico_pct": (suelo/pico - 1) * 100,
            "vol_anualizada_pct": vol,
            "percentiles": {f"p{p}": percentil(valores, p) for p in (1,5,10,25,50,75,90,95,99)},
            "rango_para_cubrir": cobertura}

def main():
    OUTDIR.mkdir(parents=True, exist_ok=True)
    vivos = simbolos_vivos()
    print(f"{len(vivos)} simbolos en Binance\n")

    plan = {}
    for sim in QUIERO:
        if f"{sim}BTC" in vivos:
            plan[sim] = ("directo", f"{sim}BTC")
        elif f"{sim}USDT" in vivos and "BTCUSDT" in vivos:
            plan[sim] = ("via_usdt", f"{sim}USDT")
        else:
            plan[sim] = ("no_disponible", None)
        print(f"  {sim:>5}/BTC  {plan[sim][0]:<14} {plan[sim][1] or ''}")

    necesita_btc = any(r == "via_usdt" for r, _ in plan.values())
    btcusdt = klines("BTCUSDT") if necesita_btc else {}

    resumen = {"generado": datetime.now(timezone.utc).isoformat(),
               "fuente": "binance klines 1d", "pares": {}, "omitidos": []}

    for sim, (ruta, simbolo) in plan.items():
        if ruta == "no_disponible":
            resumen["omitidos"].append({"par": f"{sim}/BTC", "motivo": "sin mercado en Binance"})
            print(f"\n{sim}/BTC OMITIDO: no hay mercado. No se inventa la serie."); continue

        serie = klines(simbolo)
        if ruta == "directo":
            fechas = sorted(serie); valores = [serie[f] for f in fechas]
        else:
            fechas = sorted(set(serie) & set(btcusdt))
            valores = [serie[f] / btcusdt[f] for f in fechas]
        if len(fechas) < 60:
            resumen["omitidos"].append({"par": f"{sim}/BTC", "motivo": f"solo {len(fechas)} dias"})
            print(f"\n{sim}/BTC OMITIDO: solo {len(fechas)} dias."); continue

        est = estadisticas(fechas, valores)
        (OUTDIR / f"{sim.lower()}_btc.json").write_text(json.dumps(
            {"par": f"{sim}/BTC", "fuente": f"binance {simbolo} ({ruta})",
             "serie": [{"date": f, "value": v} for f, v in zip(fechas, valores)],
             **est}, ensure_ascii=False, indent=1))
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
