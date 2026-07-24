// api/altsdata.js — DOS endpoints en uno (el plan Hobby limita a 12 funciones serverless).
//   ?mode=rotation → gates de rotación de Cowen (CoinGecko global/price + FRED + ETHBTC 20M MA)
//   ?mode=prices   → precios EN VIVO + drawdown vs ATH (CoinGecko markets, incl. TON) [+fallback Binance]
// Todo son datos PÚBLICOS sin API key. Cada modo pone su propio Cache-Control.

async function cg(path) {
  const r = await fetch(`https://api.coingecko.com/api/v3/${path}`, { headers: { "User-Agent": "btc-terminal" } });
  if (!r.ok) throw new Error("cg_" + r.status);
  return r.json();
}

// FRED CSV público (sin API key): última observación numérica de una serie
async function fredLast(id) {
  const r = await fetch(`https://fred.stlouisfed.org/graph/fredgraph.csv?id=${id}`, { headers: { "User-Agent": "btc-terminal" } });
  if (!r.ok) throw new Error("fred_" + r.status);
  const lines = (await r.text()).trim().split(/\r?\n/);
  for (let i = lines.length - 1; i >= 1; i--) {
    const parts = lines[i].split(",");
    const v = parseFloat(parts[1]);
    if (!isNaN(v)) return { date: parts[0], value: v };
  }
  return null;
}

// ── mode=rotation ──────────────────────────────────────────────────────────────────
async function rotation(res) {
  res.setHeader("Cache-Control", "public, max-age=1800"); // 30 min
  const out = { asOf: null, warnings: [] };

  try {
    const g = (await cg("global")).data || {};
    const pct = g.market_cap_percentage || {};
    const btc = pct.btc != null ? +pct.btc : null;
    const eth = pct.eth != null ? +pct.eth : null;
    const usdt = pct.usdt != null ? +pct.usdt : null;
    const stables = (pct.usdt || 0) + (pct.usdc || 0) + (pct.dai || 0);
    out.totalMcapUsd = (g.total_market_cap && g.total_market_cap.usd) || null;
    out.btcDominance = btc;
    out.btcDominanceExStables = (btc != null) ? (btc / (100 - stables)) * 100 : null;
    out.allBtcPairs = (btc != null && eth != null && usdt != null) ? (100 - btc - eth - usdt) / btc : null;
  } catch (e) { out.warnings.push("global: " + (e.message || e)); }

  try {
    const p = await cg("simple/price?ids=bitcoin,ethereum&vs_currencies=usd");
    const b = p.bitcoin && +p.bitcoin.usd, e = p.ethereum && +p.ethereum.usd;
    out.btcPrice = b || null; out.ethPrice = e || null;
    out.ethBtc = (b && e) ? e / b : null;
  } catch (e) { out.warnings.push("price: " + (e.message || e)); }

  try { const ff = await fredLast("DFF"); out.fedFunds = ff ? ff.value : null; out.asOf = ff ? ff.date : out.asOf; }
  catch (e) { out.warnings.push("fedfunds: " + (e.message || e)); }
  try { const y2 = await fredLast("DGS2"); out.twoYear = y2 ? y2.value : null; }
  catch (e) { out.warnings.push("2y: " + (e.message || e)); }

  for (const host of ["api.binance.com", "api.binance.us"]) {
    try {
      const r = await fetch(`https://${host}/api/v3/klines?symbol=ETHBTC&interval=1M&limit=24`, { headers: { "User-Agent": "btc-terminal" } });
      if (!r.ok) continue;
      const k = await r.json();
      const closes = (Array.isArray(k) ? k : []).map(x => +x[4]).filter(v => v > 0);
      if (closes.length >= 20) {
        out.ethBtc20mMa = closes.slice(-20).reduce((a, b) => a + b, 0) / 20;
        out.ethBtcMonthly = closes[closes.length - 1];
        break;
      }
    } catch (e) {}
  }
  if (out.ethBtc20mMa == null) out.warnings.push("ethbtc_ma: sin datos Binance");

  const ethNow = out.ethBtc != null ? out.ethBtc : out.ethBtcMonthly;
  out.gates = {
    rates: (out.fedFunds != null && out.twoYear != null) ? (out.fedFunds < out.twoYear) : null,
    ethBtc20m: (out.ethBtc20mMa != null && ethNow != null) ? (ethNow > out.ethBtc20mMa) : null,
    allBtcPairs: (out.allBtcPairs != null) ? (out.allBtcPairs >= 0.25) : null,
  };
  return res.end(JSON.stringify(out));
}

// ── mode=prices ────────────────────────────────────────────────────────────────────
const PRICE_IDS = {
  bitcoin: "BTC", ethereum: "ETH", binancecoin: "BNB",
  solana: "SOL", hyperliquid: "HYPE", "the-open-network": "TON",
};
async function prices(res) {
  res.setHeader("Cache-Control", "public, max-age=60, s-maxage=60"); // ~tiempo real
  const out = { asOf: new Date().toISOString(), prices: {}, warnings: [] };
  const ids = Object.keys(PRICE_IDS).join(",");
  try {
    const arr = await cg(`coins/markets?vs_currency=usd&ids=${ids}&price_change_percentage=24h`);
    for (const c of (Array.isArray(arr) ? arr : [])) {
      const key = PRICE_IDS[c && c.id];
      if (!key) continue;
      out.prices[key] = {
        price: c.current_price != null ? +c.current_price : null,
        ath: c.ath != null ? +c.ath : null,
        athDate: c.ath_date ? String(c.ath_date).slice(0, 10) : null,
        athPct: c.ath_change_percentage != null ? +c.ath_change_percentage / 100 : null,
        pct24h: c.price_change_percentage_24h != null ? +c.price_change_percentage_24h / 100 : null,
        atl: c.atl != null ? +c.atl : null,
      };
    }
  } catch (e) { out.warnings.push("cg_markets: " + ((e && e.message) || e)); }

  if (!Object.keys(out.prices).length) {
    const SYM = { BTC: "BTCUSDT", ETH: "ETHUSDT", BNB: "BNBUSDT", SOL: "SOLUSDT", HYPE: "HYPEUSDT", TON: "TONUSDT" };
    for (const host of ["api.binance.com", "api.binance.us"]) {
      try {
        const r = await fetch(`https://${host}/api/v3/ticker/price`, { headers: { "User-Agent": "btc-terminal" } });
        if (!r.ok) continue;
        const arr = await r.json();
        const bySym = {};
        for (const t of (Array.isArray(arr) ? arr : [])) bySym[t.symbol] = +t.price;
        for (const k in SYM) { if (bySym[SYM[k]] != null) out.prices[k] = { price: bySym[SYM[k]], ath: null, athPct: null, pct24h: null }; }
        if (Object.keys(out.prices).length) { out.warnings.push("precios: fallback Binance (sin ATH)"); break; }
      } catch (e) { /* siguiente host */ }
    }
  }
  return res.end(JSON.stringify(out));
}

module.exports = async (req, res) => {
  res.setHeader("Content-Type", "application/json; charset=utf-8");
  const url = new URL(req.url, "http://x");
  const mode = (url.searchParams.get("mode") || "rotation").toLowerCase();
  if (mode === "prices") return prices(res);
  return rotation(res);
};
