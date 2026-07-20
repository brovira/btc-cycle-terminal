#!/usr/bin/env python3
"""
BTC signal alerts (LMEC / Regime framework).

Runs on a schedule (GitHub Actions). Fetches weekly BTC price + on-chain (MVRV),
computes the same indicators as the dashboard, and sends a Telegram message when
a signal *newly* fires (transition-based dedup via alerts/state.json).

Stdlib only. Env: TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID.
"""
import os, json, math, statistics, urllib.request, urllib.parse, ssl
from datetime import datetime, timezone

STATE_PATH = os.path.join(os.path.dirname(__file__), "state.json")
UA = {"User-Agent": "btc-cycle-terminal-alerts/1.0"}
CTX = ssl.create_default_context()


def http_json(url, timeout=30):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
        return json.loads(r.read().decode())


# ---------------- data ----------------
def fetch_binance(host):
    j = http_json("https://%s/api/v3/klines?symbol=BTCUSDT&interval=1w&limit=1000" % host)
    return {
        "t": [k[0] for k in j],
        "c": [float(k[4]) for k in j],
        "h": [float(k[2]) for k in j],
        "l": [float(k[3]) for k in j],
    }


def fetch_coingecko():
    j = http_json("https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
                  "?vs_currency=usd&days=max&interval=daily")
    px = j.get("prices", [])
    WK = 7 * 864e5
    t, c, h, l = [], [], [], []
    bs = None
    for ms, p in px:
        if bs is None:
            bs = ms; bh = bl = bc = p; bt = ms; continue
        if ms - bs >= WK:
            t.append(bt); c.append(bc); h.append(bh); l.append(bl)
            bs = ms; bh = bl = bc = p; bt = ms
        else:
            bh = max(bh, p); bl = min(bl, p); bc = p; bt = ms
    if bs is not None:
        t.append(bt); c.append(bc); h.append(bh); l.append(bl)
    return {"t": t, "c": c, "h": h, "l": l}


def load_price():
    for fn in (lambda: fetch_binance("api.binance.com"),
               lambda: fetch_binance("api.binance.us"),
               fetch_coingecko):
        try:
            d = fn()
            if d and len(d["c"]) > 60:
                return d
        except Exception:
            continue
    raise RuntimeError("no price source")


def load_mvrv(weekly_t):
    """Return MVRV Z-score aligned to weekly timestamps (list, may contain None)."""
    try:
        url = ("https://community-api.coinmetrics.io/v4/timeseries/asset-metrics"
               "?assets=btc&metrics=CapMrktCurUSD,CapRealUSD&frequency=1d"
               "&page_size=10000&start_time=2011-01-01")
        rows = http_json(url).get("data", [])
        dt, mkt, real = [], [], []
        for x in rows:
            try:
                ms = datetime.strptime(x["time"][:10], "%Y-%m-%d").replace(tzinfo=timezone.utc).timestamp() * 1000
            except Exception:
                continue
            dt.append(ms)
            mkt.append(float(x["CapMrktCurUSD"]) if x.get("CapMrktCurUSD") else None)
            real.append(float(x["CapRealUSD"]) if x.get("CapRealUSD") else None)
        vals = [v for v in mkt if v is not None]
        mean = sum(vals) / len(vals)
        sd = math.sqrt(sum((v - mean) ** 2 for v in vals) / len(vals))
        z = [None] * len(weekly_t)
        j = 0
        for i, wt in enumerate(weekly_t):
            while j + 1 < len(dt) and dt[j + 1] <= wt:
                j += 1
            if dt and dt[j] <= wt + 7 * 864e5 and mkt[j] is not None and real[j] is not None and sd > 0:
                z[i] = (mkt[j] - real[j]) / sd
        return z
    except Exception:
        return [None] * len(weekly_t)


# ---------------- indicators ----------------
def sma(a, n):
    o = [None] * len(a); s = 0.0
    for i, v in enumerate(a):
        s += v
        if i >= n: s -= a[i - n]
        if i >= n - 1: o[i] = s / n
    return o


def ema(a, n):
    o = [None] * len(a); k = 2 / (n + 1); prev = None; ss = 0.0; seeded = False
    for i, v in enumerate(a):
        if not seeded:
            ss += v
            if i >= n - 1:
                prev = ss / n; o[i] = prev; seeded = True
            continue
        prev = v * k + prev * (1 - k); o[i] = prev
    return o


def rsi(c, n=14):
    o = [None] * len(c); g = 0.0; l = 0.0
    for i in range(1, len(c)):
        ch = c[i] - c[i - 1]; gg = max(0, ch); ll = max(0, -ch)
        if i <= n:
            g += gg; l += ll
            if i == n:
                g /= n; l /= n; o[i] = 100 - 100 / (1 + (1e9 if l == 0 else g / l))
        else:
            g = (g * (n - 1) + gg) / n; l = (l * (n - 1) + ll) / n
            o[i] = 100 - 100 / (1 + (1e9 if l == 0 else g / l))
    return o


def macd(c):
    f = ema(c, 12); s = ema(c, 26)
    m = [(f[i] - s[i]) if (f[i] is not None and s[i] is not None) else None for i in range(len(c))]
    sig = ema([0 if x is None else x for x in m], 9)
    sig = [None if m[i] is None else sig[i] for i in range(len(c))]
    hh = [(m[i] - sig[i]) if (m[i] is not None and sig[i] is not None) else None for i in range(len(c))]
    return m, sig, hh


def bmsb_breaks(c, s20, e21):
    """Return (first_idx[], second_idx[], cur_in_bear, cur_ups)."""
    n = len(c)
    hi = lambda i: max(s20[i], e21[i]) if (s20[i] is not None and e21[i] is not None) else None
    lb = lambda i: min(s20[i], e21[i]) if (s20[i] is not None and e21[i] is not None) else None
    ev = []; state = None
    for i in range(1, n):
        H = hi(i); L = lb(i)
        if H is None: continue
        aC = c[i] > H and hi(i - 1) is not None and c[i - 1] > hi(i - 1)
        bC = c[i] < L and lb(i - 1) is not None and c[i - 1] < lb(i - 1)
        if aC and state != "up":
            if state: ev.append((i, "up"))
            state = "up"
        elif bC and state != "down":
            if state: ev.append((i, "down"))
            state = "down"
        elif state is None:
            state = "up" if c[i] > H else ("down" if c[i] < L else None)
    first = []; second = []; in_bear = False; ups = 0; last_up = None
    for (i, t) in ev:
        if t == "up":
            last_up = i
            if in_bear:
                ups += 1
                if ups == 1: first.append(i)
                elif ups == 2: second.append(i); in_bear = False
        else:
            bl = (i - last_up) if last_up is not None else 999
            if bl >= 40: in_bear = True; ups = 0
    return first, second, in_bear, ups


# ---------------- evaluate ----------------
def evaluate(d, z):
    c = d["c"]; n = len(c)
    s20 = sma(c, 20); e21 = ema(c, 21); s200 = sma(c, 200); rs = rsi(c); m, sig, hh = macd(c)
    i = n - 1
    price = c[i]
    band_hi = max(s20[i], e21[i]); band_lo = min(s20[i], e21[i])
    above_band = price > band_hi; below_band = price < band_lo
    above200 = s200[i] is not None and price > s200[i]
    rsiV = rs[i]; hist = hh[i]
    macd_cross = (m[i] is not None and sig[i] is not None and m[i - 1] is not None and sig[i - 1] is not None
                  and m[i] > sig[i] and m[i - 1] <= sig[i - 1] and m[i] < 0)
    rsi34_now = rsiV is not None and rsiV > 34
    rsi34_prev = rs[i - 1] is not None and rs[i - 1] > 34
    zi = z[i]
    # BMSB breaks
    first, second, in_bear, ups = bmsb_breaks(c, s20, e21)
    second_recent = bool(second) and (n - 1 - second[-1]) <= 8
    macd_green = hist is not None and hist > 0 and m[i] is not None and m[i - 1] is not None and m[i] > m[i - 1]
    rsi4050 = rsiV is not None and 40 <= rsiV <= 50
    strong_buy = second_recent and macd_green and rsi4050

    # phase
    if below_band:
        phase = "Suelo/Acumulacion" if (rsiV is not None and rsiV < 30 and (zi is None or zi < 0)) else "Bajista"
    elif above_band:
        if (zi is not None and False) or (rsiV is not None and rsiV > 78):
            phase = "Euforia/Techo"
        else:
            phase = "Alcista"
    else:
        phase = "Transicion"

    return {
        "date": datetime.utcfromtimestamp(d["t"][i] / 1000).strftime("%Y-%m-%d"),
        "price": price, "phase": phase,
        "rsi": rsiV, "macd_hist": hist, "mvrv_z": zi,
        "above_band": above_band, "above200": above200,
        "signals": {
            "strong_buy": strong_buy,
            "macd_bull_cross_neg": bool(macd_cross),
            "rsi_reclaim_34": bool(rsi34_now and not rsi34_prev),
            "mvrv_z_out_of_green": bool(zi is not None and zi >= 0 and z[i - 1] is not None and z[i - 1] < 0),
            "reclaim_bmsb": bool(above_band),
        },
        "bmsb_stage": ("bear_wait1" if (in_bear and ups == 0) else
                       "bear_wait2" if (in_bear and ups >= 1) else
                       "post_second" if second_recent else "outside"),
    }


# ---------------- telegram ----------------
def send_telegram(text):
    tok = os.environ.get("TELEGRAM_BOT_TOKEN"); chat = os.environ.get("TELEGRAM_CHAT_ID")
    if not tok or not chat:
        print("[warn] no telegram creds; message would be:\n" + text)
        return
    data = urllib.parse.urlencode({"chat_id": chat, "text": text,
                                   "parse_mode": "HTML", "disable_web_page_preview": "true"}).encode()
    req = urllib.request.Request("https://api.telegram.org/bot%s/sendMessage" % tok, data=data, headers=UA)
    with urllib.request.urlopen(req, timeout=30, context=CTX) as r:
        r.read()


def fmt_usd(v):
    return "$%s" % ("{:,.0f}".format(v) if v and v >= 10 else "{:,.2f}".format(v or 0))


SIGNAL_LABELS = {
    "strong_buy": "🟢 <b>COMPRA FUERTE (LMEC)</b> — 2ª ruptura BMSB + MACD verde + RSI 40-50",
    "macd_bull_cross_neg": "📈 <b>MACD</b> cruce alcista en negativo (buen punto de compra histórico)",
    "rsi_reclaim_34": "📊 <b>RSI</b> semanal recupera &gt;34 (confirmación de giro)",
    "mvrv_z_out_of_green": "🟩 <b>MVRV Z</b> sale de zona de infravaloración (&gt;0) — confirmación de suelo",
    "reclaim_bmsb": "⚑ <b>Precio</b> recupera la Bull Market Support Band",
}


def main():
    d = load_price()
    z = load_mvrv(d["t"])
    cur = evaluate(d, z)

    prev = {}
    if os.path.exists(STATE_PATH):
        try:
            prev = json.load(open(STATE_PATH))
        except Exception:
            prev = {}
    prev_sig = prev.get("signals", {})
    prev_phase = prev.get("phase")
    prev_date = prev.get("date")

    msgs = []
    # only evaluate transitions on a new weekly candle OR first run
    new_week = prev_date != cur["date"]

    # 1) signal transitions (false -> true)
    for key, active in cur["signals"].items():
        if active and not prev_sig.get(key, False):
            msgs.append(SIGNAL_LABELS.get(key, key))

    # 2) regime / strategy change
    if prev_phase and prev_phase != cur["phase"]:
        msgs.append("🔄 <b>Cambio de régimen:</b> %s → <b>%s</b> (revisa estrategia)" % (prev_phase, cur["phase"]))

    if msgs:
        head = ("<b>BTC %s</b> · %s · fase <b>%s</b>\nRSI %s · MACD %s · MVRV-Z %s\n" % (
            fmt_usd(cur["price"]), cur["date"], cur["phase"],
            ("%.0f" % cur["rsi"]) if cur["rsi"] is not None else "—",
            ("%.0f" % cur["macd_hist"]) if cur["macd_hist"] is not None else "—",
            ("%.2f" % cur["mvrv_z"]) if cur["mvrv_z"] is not None else "—",
        ))
        body = "\n".join("• " + mstr for mstr in msgs)
        tail = "\n\nhttps://btc-cycle-terminal.vercel.app"
        send_telegram(head + "\n" + body + tail)
        print("sent %d alert(s)" % len(msgs))
    else:
        print("no new signals (%s, fase %s)" % (cur["date"], cur["phase"]))

    # persist state
    json.dump({"date": cur["date"], "phase": cur["phase"], "signals": cur["signals"],
               "price": cur["price"], "checked_at": datetime.utcnow().isoformat() + "Z"},
              open(STATE_PATH, "w"), indent=2)


if __name__ == "__main__":
    main()
