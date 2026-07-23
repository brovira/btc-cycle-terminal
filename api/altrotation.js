// api/altrotation.js — datos para el panel "Rotación de alts" (gates del marco de Cowen).
// Todo son datos PÚBLICOS sin API key (CoinGecko global/price + FRED CSV) → sin secretos, sin auth.
// Corre server-side (Vercel tiene red), así que funciona aunque no se pueda probar en el sandbox.
//
// Gates (marco de Cowen, ver PROJECT_MEMORY §Plan de ALTS):
//  1. rates       Fed funds < 2-year yield (tipo neutral) — el gate MACRO decisivo
//  2. allBtcPairs (TOTAL3−USDT)/BTC ≥ ~0.25 sostenido
//  3. btcDomExStab BTC dominance EXCLUYENDO stables (contexto; "romper a la baja" necesita histórico)
//  4. ethBtc      ETH/BTC (contexto; el gate real es reclaim de la 20-month MA → juicio)
// M2 NO se usa (Cowen lo rechaza). Social/retail no tiene fuente pública fiable → se omite.

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

module.exports = async (req, res) => {
  res.setHeader("Content-Type", "application/json; charset=utf-8");
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
    // BTC.D excluyendo stables ≈ btc% / (100 − stables%)  (los % están sobre el total con stables)
    out.btcDominanceExStables = (btc != null) ? (btc / (100 - stables)) * 100 : null;
    // "all Bitcoin pairs" = (TOTAL3 − USDT) / BTC.  TOTAL3 = total·(1−btc−eth); todo en %, el total cancela:
    //   = (100 − btc − eth − usdt) / btc
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

  // ETH/BTC vs su MEDIA MÓVIL DE 20 MESES — el gatillo real de rotación de Cowen ("reclaim
  // duradero de la 20-month MA"). Se calcula con velas MENSUALES de ETHBTC (Binance, sin key).
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

  // Gates. rates y ethBtc20m son AUTOMÁTICOS y fiables; allBtcPairs es un proxy sin calibrar
  // (se expone como contexto en el front); dominancia-rompiendo y social quedan a juicio.
  const ethNow = out.ethBtc != null ? out.ethBtc : out.ethBtcMonthly;
  out.gates = {
    rates: (out.fedFunds != null && out.twoYear != null) ? (out.fedFunds < out.twoYear) : null,
    ethBtc20m: (out.ethBtc20mMa != null && ethNow != null) ? (ethNow > out.ethBtc20mMa) : null,
    allBtcPairs: (out.allBtcPairs != null) ? (out.allBtcPairs >= 0.25) : null,
  };
  return res.end(JSON.stringify(out));
};
