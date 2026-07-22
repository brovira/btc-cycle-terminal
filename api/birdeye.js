// api/birdeye.js — precios EXACTOS de los tokens de Solana del LP (cbBTC, WBTC, SOL)
// vía Birdeye (free tier). La key vive como env var en Vercel, nunca en el frontend.
//
// CONFIGURACIÓN (una vez): Vercel → Settings → Environment Variables →
//   BIRDEYE_API_KEY = <tu key del free tier de birdeye.so>
// (los GitHub Secrets del DeFi-Tracker no se pueden leer desde aquí — hay que
//  pegar la misma key también en Vercel).
//
// GET /api/birdeye  →  { "cbBTC": 66123.4, "WBTC": 66090.1, "SOL": 171.2, "USDC": 1 }
// Sin key → 503 {error:"no_key"} y el frontend cae a la aproximación (Binance).

const MINTS = {
  cbBTC: "cbbtcf3aa214zXHbiAZQwf4122FBYbraNdFqgw4iMij",
  WBTC: "3NZ9JMVBmGAqocybic2c7LQCJScmgsAZ6vQqTDzcqmJh",
  SOL: "So11111111111111111111111111111111111111112",
};

module.exports = async (req, res) => {
  res.setHeader("Content-Type", "application/json; charset=utf-8");
  const key = process.env.BIRDEYE_API_KEY;
  if (!key) { res.statusCode = 503; return res.end(JSON.stringify({ error: "no_key", message: "Falta BIRDEYE_API_KEY en Vercel." })); }
  try {
    const list = Object.values(MINTS).join(",");
    const r = await fetch(`https://public-api.birdeye.so/defi/multi_price?list_address=${encodeURIComponent(list)}`, {
      headers: { "X-API-KEY": key, "x-chain": "solana", accept: "application/json" },
    });
    if (!r.ok) { res.statusCode = r.status; return res.end(JSON.stringify({ error: "birdeye_" + r.status })); }
    const j = await r.json();
    const data = (j && j.data) || {};
    const out = { USDC: 1 };
    for (const [sym, mint] of Object.entries(MINTS)) {
      const v = data[mint] && data[mint].value;
      if (v != null) out[sym] = +v;
    }
    res.setHeader("Cache-Control", "s-maxage=60, stale-while-revalidate=120"); // 1 min de caché
    return res.end(JSON.stringify(out));
  } catch (e) {
    res.statusCode = 502; return res.end(JSON.stringify({ error: "fetch_error", message: String((e && e.message) || e) }));
  }
};
