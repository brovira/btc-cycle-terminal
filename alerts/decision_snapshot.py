#!/usr/bin/env python3
"""
Snapshot semanal de la decisión "¿Qué hago hoy?".

Corre en GitHub Actions (lunes, tras el cierre de la vela semanal). Calcula las
MISMAS 6 señales que decision.html y AÑADE el resultado a data/decision_history.json,
para que el panel muestre cómo evolucionó la recomendación y puntúe su acierto
(retorno posterior). Solo stdlib. Reutiliza los fetchers/indicadores de check_signals.py.

IMPORTANTE: la lógica de señales y decisión debe ir SINCRONIZADA con decision.html
(y con el resumen del hub en index.html). Si cambias umbrales en un sitio, cámbialos aquí.
"""
import os, json, math
from datetime import datetime, timezone
import check_signals as cs

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HIST_PATH = os.path.join(ROOT, "data", "decision_history.json")

HALVINGS = [datetime.strptime(d, "%Y-%m-%d").replace(tzinfo=timezone.utc).timestamp() * 1000
            for d in ["2012-11-28", "2016-07-09", "2020-05-11", "2024-04-19", "2028-04-20"]]


def halv_weeks(ms):
    H = HALVINGS[0]
    for h in HALVINGS:
        if h <= ms:
            H = h
    return (ms - H) / (7 * 864e5)


def fetch_fng():
    try:
        j = cs.http_json("https://api.alternative.me/fng/?limit=1&format=json")
        d = j.get("data") or []
        if d:
            return int(d[0]["value"])
    except Exception:
        pass
    return None


def decide(d, z, fng):
    c = d["c"]; n = len(c); price = c[-1]
    s20 = cs.sma(c, 20); e21 = cs.ema(c, 21); s200 = cs.sma(c, 200); rs = cs.rsi(c, 14)
    i = n - 1
    bh = max(s20[i], e21[i]) if (s20[i] is not None and e21[i] is not None) else None
    ma200 = s200[i]; rsiV = rs[i]; zi = z[i] if z else None
    now = d["t"][i]; dt = datetime.utcfromtimestamp(now / 1000)
    hw = halv_weeks(now); ym = dt.year % 4; mo = dt.month
    accum = 120 <= hw <= 180
    cowen = (ym == 2 and mo >= 7)
    dist = 70 <= hw <= 110
    cycle_buy = accum or cowen
    below = (price < bh) if bh is not None else None

    sig = {
        "below_bmsb":   below,
        "near_200w":    (price <= ma200 * 1.05) if ma200 is not None else None,
        "mvrv_low":     (zi < 0.5) if zi is not None else None,
        "rsi_weak":     (rsiV < 45) if rsiV is not None else None,
        "fear":         (fng < 30) if fng is not None else None,
        "cycle_window": cycle_buy,
    }
    with_data = [v for v in sig.values() if v is not None]
    lit = sum(1 for v in with_data if v); tot = len(with_data)
    expensive = (below is False)

    if dist and (expensive or (zi is not None and zi > 2)):
        action = "Tomar beneficio"
    elif tot and lit >= math.ceil(tot * 0.66) and below:
        action = "Comprar por niveles"
    elif cycle_buy and expensive:
        action = "Esperar dip a nivel"
    elif cowen and lit >= 2:
        action = "Esperar seasonality"
    elif lit >= 2:
        action = "DCA base"
    else:
        action = "Esperar dip"

    return {
        "date": dt.strftime("%Y-%m-%d"),
        "price": round(price, 2),
        "lit": lit, "tot": tot, "action": action,
        "signals": sig,
        "metrics": {
            "bmsb": round(bh, 2) if bh is not None else None,
            "ma200": round(ma200, 2) if ma200 is not None else None,
            "mvrv_z": round(zi, 3) if zi is not None else None,
            "rsi": round(rsiV, 1) if rsiV is not None else None,
            "fng": fng,
            "halv_week": round(hw, 1),
        },
    }


def main():
    d = cs.load_price()
    z = cs.load_mvrv(d["t"])
    fng = fetch_fng()
    snap = decide(d, z, fng)

    os.makedirs(os.path.dirname(HIST_PATH), exist_ok=True)
    hist = {"snapshots": []}
    if os.path.exists(HIST_PATH):
        try:
            hist = json.load(open(HIST_PATH))
        except Exception:
            hist = {"snapshots": []}
    if not isinstance(hist.get("snapshots"), list):
        hist["snapshots"] = []

    # dedup/overwrite por fecha de vela semanal (una entrada por semana)
    snaps = [s for s in hist["snapshots"] if s.get("date") != snap["date"]]
    snaps.append(snap)
    snaps.sort(key=lambda s: s.get("date", ""))
    hist["snapshots"] = snaps
    hist["updated_at"] = datetime.utcnow().isoformat() + "Z"

    json.dump(hist, open(HIST_PATH, "w"), indent=2, ensure_ascii=False)
    print("snapshot %s -> %s (%d/%d) [%d en total]" % (
        snap["date"], snap["action"], snap["lit"], snap["tot"], len(snaps)))


if __name__ == "__main__":
    main()
