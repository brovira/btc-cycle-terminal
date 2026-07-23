// api/altcycles.js — "Reloj de alts": suelos de ciclo (CURADOS) de cada alt vs el ciclo de BTC.
// Datos PÚBLICOS de mercado (velas semanales de Binance, sin API key, sin auth) → sin secretos.
// Corre SERVER-SIDE (Vercel tiene red), así que funciona aunque no se pueda probar desde el sandbox.
//
// POR QUÉ CURADO (no auto-detección): detectar suelos por "−60% + mínimo local" fragmentaba el
// mismo bear en varios "suelos" y partía el múltiplo en trozos pequeños (ETH salía ×2/×2.6/×3 en
// vez del ×5 real 2022→2025). Ahora usamos las fechas conocidas de capitulación de cada alt (un
// suelo por ciclo) y calculamos el múltiplo REAL desde ese suelo hasta el SIGUIENTE ATH, con datos
// vivos. HYPE y TON no tienen ciclo previo en Binance → shortHistory (no se inventan suelos).

const WEEK_MS = 7 * 24 * 3600 * 1000;

// Techos de BTC ANCLADOS (coherentes con el resto del terminal). Se usan para "semanas desde el
// techo de BTC" en cada suelo de alt. El VALOR del drawdown de BTC sí sale de la serie viva.
const BTC_TOPS = ["2017-12-17", "2021-11-08", "2025-10-06"].map((d) => Date.parse(d));

// Suelos de ciclo CURADOS por alt (capitulaciones conocidas; fecha aprox., se refina al mínimo real
// de cierre semanal en ±8 semanas). Un suelo por ciclo → múltiplo real al siguiente ATH.
const CURATED_BOTTOMS = {
  ETH: ["2018-12-16", "2022-06-19"],  // fin bear 2018 (~$85) · bear 2022 (~$900)
  BNB: ["2018-12-16", "2022-06-19"],  // ~$5 · ~$180
  SOL: ["2022-12-26"],                // colapso FTX (~$10). SOL se listó 2020 (medio ciclo) → solo un ciclo previo.
  HYPE: [],                           // listado nov-2024 → sin ciclo previo
  TON: [],                            // histórico corto en Binance → sin ciclo previo fiable
};

const ASSETS = [
  { key: "BTC", symbol: "BTCUSDT", name: "Bitcoin", isRef: true },
  { key: "ETH", symbol: "ETHUSDT", name: "Ethereum", catalyst: "Sigue el macro de BTC (aquí aplica el gate de Cowen)." },
  { key: "BNB", symbol: "BNBUSDT", name: "BNB", catalyst: "Timing propio: ligado a Binance/BSC más que a BTC." },
  { key: "SOL", symbol: "SOLUSDT", name: "Solana", catalyst: "Timing propio: colapso de FTX (nov-2022) fue su suelo; corrió su ciclo casi solo." },
  { key: "HYPE", symbol: "HYPEUSDT", name: "Hyperliquid", catalyst: "Fuera del marco de Cowen. Listado nov-2024 → sin ciclo previo." },
  { key: "TON", symbol: "TONUSDT", name: "Toncoin", catalyst: "Fuera del marco de Cowen. Techó jun-2024 (ATH ~$8,2) por Telegram/ecosistema — ciclo PROPIO, desacoplado de BTC (techó 16 meses antes); en bear desde entonces." },
];

async function fetchKlines(symbol, warnings) {
  const hosts = ["api.binance.com", "api.binance.us"];
  let lastErr = null;
  for (const h of hosts) {
    try {
      const r = await fetch(`https://${h}/api/v3/klines?symbol=${symbol}&interval=1w&limit=1000`, {
        headers: { "User-Agent": "btc-terminal" },
      });
      if (!r.ok) { lastErr = `${h}:${r.status}`; continue; }
      const k = await r.json();
      if (Array.isArray(k) && k.length) return k;
      lastErr = `${h}:empty`;
    } catch (e) { lastErr = `${h}:${(e && e.message) || e}`; }
  }
  warnings.push(`${symbol}: sin velas (${lastErr})`);
  return null;
}

// serie base: tiempos (openTime), cierres, ATH acumulado y drawdown desde ese ATH.
function buildSeries(rows) {
  const t = rows.map((r) => +r[0]);
  const c = rows.map((r) => +r[4]);
  const n = c.length;
  const dd = new Array(n);
  let peak = -Infinity;
  for (let i = 0; i < n; i++) {
    if (c[i] > peak) peak = c[i];
    dd[i] = peak > 0 ? c[i] / peak - 1 : 0;
  }
  let athIdx = 0;
  for (let i = 1; i < n; i++) if (c[i] > c[athIdx]) athIdx = i;
  return { t, c, dd, n, athIdx };
}

// BTC drawdown vivo en un instante t0: última vela BTC con tiempo <= t0
function btcDrawdownAt(btc, t0) {
  if (!btc) return null;
  let idx = -1;
  for (let i = 0; i < btc.n; i++) { if (btc.t[i] <= t0) idx = i; else break; }
  if (idx < 0) return null;
  return { drawdown: btc.dd[idx] };
}

// último techo BTC (anclado) antes de t0 → semanas desde ese techo
function weeksSinceBtcTop(t0) {
  let top = null;
  for (const tp of BTC_TOPS) { if (tp <= t0) top = tp; }
  if (top == null) return null;
  return { topDate: new Date(top).toISOString().slice(0, 10), weeks: Math.round((t0 - top) / WEEK_MS) };
}

function iso(ms) { return new Date(ms).toISOString().slice(0, 10); }
function round(v, d) { const m = Math.pow(10, d == null ? 2 : d); return v == null ? null : Math.round(v * m) / m; }

// procesa un activo: drawdown actual + suelos CURADOS con múltiplo real al siguiente ATH + contexto BTC
function processAsset(meta, rows, btc, warnings) {
  const s = buildSeries(rows);
  const price = s.c[s.n - 1];
  const athPrice = s.c[s.athIdx];
  const out = {
    key: meta.key, name: meta.name, symbol: meta.symbol, isRef: !!meta.isRef, catalyst: meta.catalyst || null,
    weeks: s.n, firstDate: iso(s.t[0]), lastDate: iso(s.t[s.n - 1]),
    price: round(price, price < 10 ? 4 : 2),
    ath: round(athPrice, athPrice < 10 ? 4 : 2), athDate: iso(s.t[s.athIdx]),
    drawdownNow: round(s.dd[s.n - 1], 4),
    shortHistory: false, bottoms: [],
    ddSeries: s.t.map((tt, i) => [iso(tt), round(s.dd[i], 4)]),
  };
  if (meta.isRef) return out; // BTC = referencia del gráfico; sin suelos propios

  const curated = CURATED_BOTTOMS[meta.key] || [];
  if (s.n < 104 || !curated.length) {
    out.shortHistory = true;
    warnings.push(`${meta.key}: sin ciclo previo (histórico ${s.n} sem / sin suelos curados)`);
    return out;
  }

  // refinar cada suelo curado al mínimo de cierre semanal real en ±8 semanas
  const idxs = [];
  for (const bd of curated) {
    const bms = Date.parse(bd);
    if (isNaN(bms) || bms < s.t[0] || bms > s.t[s.n - 1]) continue;
    const lo = bms - 8 * WEEK_MS, hi = bms + 8 * WEEK_MS;
    let bi = -1;
    for (let i = 0; i < s.n; i++) { if (s.t[i] >= lo && s.t[i] <= hi) { if (bi < 0 || s.c[i] < s.c[bi]) bi = i; } }
    if (bi >= 0) idxs.push(bi);
  }
  idxs.sort((a, b) => a - b);

  for (let k = 0; k < idxs.length; k++) {
    const i = idxs[k];
    const bound = k + 1 < idxs.length ? idxs[k + 1] : s.n - 1; // siguiente suelo, o el final
    let maxI = i;
    for (let j = i; j <= bound; j++) if (s.c[j] > s.c[maxI]) maxI = j;
    const mult = s.c[i] > 0 ? s.c[maxI] / s.c[i] : null;
    const bt = btcDrawdownAt(btc, s.t[i]);
    const wt = weeksSinceBtcTop(s.t[i]);
    out.bottoms.push({
      date: iso(s.t[i]),
      price: round(s.c[i], s.c[i] < 10 ? 4 : 2),
      drawdown: round(s.dd[i], 4),
      nextMax: { date: iso(s.t[maxI]), price: round(s.c[maxI], s.c[maxI] < 10 ? 4 : 2), multiple: round(mult, 1) },
      btc: bt ? { drawdown: round(bt.drawdown, 4), weeksSinceTop: wt ? wt.weeks : null, topDate: wt ? wt.topDate : null } : null,
    });
  }
  if (!out.bottoms.length) { out.shortHistory = true; warnings.push(`${meta.key}: suelos curados fuera del rango de datos`); }
  return out;
}

module.exports = async (req, res) => {
  res.setHeader("Content-Type", "application/json; charset=utf-8");
  res.setHeader("Cache-Control", "public, max-age=3600, s-maxage=3600, stale-while-revalidate=7200"); // 1h
  const out = { asOf: new Date().toISOString(), warnings: [], btcTops: BTC_TOPS.map(iso), assets: [] };

  try {
    // 1) BTC primero (referencia de ciclo para las alts)
    const btcRows = await fetchKlines("BTCUSDT", out.warnings);
    const btc = btcRows ? buildSeries(btcRows) : null;
    if (btcRows) out.assets.push(processAsset(ASSETS[0], btcRows, null, out.warnings));

    // 2) el resto (secuencial: evita rate-limit de Binance)
    for (let a = 1; a < ASSETS.length; a++) {
      const meta = ASSETS[a];
      try {
        const rows = await fetchKlines(meta.symbol, out.warnings);
        if (rows) out.assets.push(processAsset(meta, rows, btc, out.warnings));
        else out.assets.push({ key: meta.key, name: meta.name, symbol: meta.symbol, catalyst: meta.catalyst || null, unavailable: true, shortHistory: true, bottoms: [] });
      } catch (e) {
        out.warnings.push(`${meta.key}: ${(e && e.message) || e}`);
        out.assets.push({ key: meta.key, name: meta.name, symbol: meta.symbol, unavailable: true, shortHistory: true, bottoms: [] });
      }
    }
  } catch (e) {
    out.warnings.push("fatal: " + ((e && e.message) || e));
  }

  return res.end(JSON.stringify(out));
};
