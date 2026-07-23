// api/altprices.js — precios EN VIVO + drawdown vs ATH de las alts (para la vista "Situación").
// Fuente: CoinGecko /coins/markets (una llamada, sin key) → precio, ATH real de TODA la historia
// (no solo la ventana de Binance) y % desde el ATH. Incluye TON, que Binance no sirve bien.
// Cache corta (60s) para que sea ~tiempo real. Fallback de precio a Binance ticker si CG falla.

const IDS = {
  bitcoin: "BTC",
  ethereum: "ETH",
  binancecoin: "BNB",
  solana: "SOL",
  hyperliquid: "HYPE",
  "the-open-network": "TON",
};

module.exports = async (req, res) => {
  res.setHeader("Content-Type", "application/json; charset=utf-8");
  res.setHeader("Cache-Control", "public, max-age=60, s-maxage=60"); // ~tiempo real
  const out = { asOf: new Date().toISOString(), prices: {}, warnings: [] };

  const ids = Object.keys(IDS).join(",");
  try {
    const r = await fetch(
      `https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=${ids}&price_change_percentage=24h`,
      { headers: { "User-Agent": "btc-terminal" } });
    if (!r.ok) throw new Error("cg_" + r.status);
    const arr = await r.json();
    for (const c of (Array.isArray(arr) ? arr : [])) {
      const key = IDS[c && c.id];
      if (!key) continue;
      out.prices[key] = {
        price: c.current_price != null ? +c.current_price : null,
        ath: c.ath != null ? +c.ath : null,
        athDate: c.ath_date ? String(c.ath_date).slice(0, 10) : null,
        athPct: c.ath_change_percentage != null ? +c.ath_change_percentage / 100 : null, // drawdown vs ATH (negativo)
        pct24h: c.price_change_percentage_24h != null ? +c.price_change_percentage_24h / 100 : null,
        atl: c.atl != null ? +c.atl : null,
      };
    }
  } catch (e) { out.warnings.push("cg_markets: " + ((e && e.message) || e)); }

  // Fallback: si CoinGecko no dio nada, al menos el precio de Binance (sin ATH/drawdown).
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
};
