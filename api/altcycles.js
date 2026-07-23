// api/altcycles.js — "Reloj de alts": ciclos de cada alt vs el ciclo de BTC.
// Datos PÚBLICOS de mercado (velas semanales de Binance, sin API key, sin auth) → sin secretos.
// Corre SERVER-SIDE (Vercel tiene red), así que funciona aunque no se pueda probar desde el sandbox.
//
// Qué calcula, por activo (BTC + ETH BNB SOL HYPE TON):
//  - precio actual, ATH (máx de cierres) y drawdown actual (precio/ATH − 1)
//  - serie SEMANAL de drawdown desde el ATH acumulado (peak running)
//  - suelos de ciclo = mínimos MAYORES de esa serie (dd < −60% y mínimo local separado ≥26 sem)
//  - por cada suelo: el techo (ATH) previo a ese desplome = "mejor salida", y el siguiente máximo
//    tras el suelo = "mejor entrada → múltiplo"
//  - REFERENCIA BTC: en la fecha del suelo de cada alt, drawdown de BTC desde SU ATH y semanas desde
//    el último techo de BTC (posición de BTC en su propio ciclo), + offset vs el suelo de BTC más cercano
// HYPE y TON tienen histórico corto en Binance (listados 2024) → shortHistory:true y NO se inventan
// suelos de ciclo (no hay bear previo que muestrear).

const WEEK_MS = 7 * 24 * 3600 * 1000;

// Techos/suelos de BTC ANCLADOS (coherentes con el resto del terminal). Se usan para "semanas desde
// el techo de BTC" y para el offset del suelo. El VALOR del drawdown de BTC sí sale de la serie viva.
const BTC_TOPS = ["2017-12-17", "2021-11-08", "2025-10-06"].map((d) => Date.parse(d));
const BTC_BOTTOMS = ["2018-12-16", "2022-11-21"].map((d) => Date.parse(d));

const ASSETS = [
  { key: "BTC", symbol: "BTCUSDT", name: "Bitcoin", isRef: true },
  { key: "ETH", symbol: "ETHUSDT", name: "Ethereum", catalyst: "Sigue el macro de BTC (aquí aplica el gate de Cowen)." },
  { key: "BNB", symbol: "BNBUSDT", name: "BNB", catalyst: "Timing propio: ligado a Binance/BSC más que a BTC." },
  { key: "SOL", symbol: "SOLUSDT", name: "Solana", catalyst: "Timing propio: colapso de FTX (nov-2022) fue su suelo; corrió su ciclo casi solo." },
  { key: "HYPE", symbol: "HYPEUSDT", name: "Hyperliquid", catalyst: "Fuera del marco de Cowen. Listado nov-2024 → sin ciclo previo." },
  { key: "TON", symbol: "TONUSDT", name: "Toncoin", catalyst: "Fuera del marco de Cowen. Catalizador propio (Telegram); histórico Binance corto." },
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
  // ATH global (máx de cierres) + su índice
  let athIdx = 0;
  for (let i = 1; i < n; i++) if (c[i] > c[athIdx]) athIdx = i;
  return { t, c, dd, n, athIdx };
}

// suelos de ciclo = mínimos locales de la serie de drawdown que caen por debajo de un umbral,
// deduplicados dentro de una ventana de separación (se queda con el más profundo).
function findBottoms(s, { threshold = -0.6, sep = 26 } = {}) {
  const { dd, n } = s;
  const cands = [];
  for (let i = 0; i < n; i++) {
    if (dd[i] >= threshold) continue;
    let isMin = true;
    const lo = Math.max(0, i - sep), hi = Math.min(n - 1, i + sep);
    for (let j = lo; j <= hi; j++) { if (dd[j] < dd[i]) { isMin = false; break; } }
    if (isMin) cands.push(i);
  }
  cands.sort((a, b) => a - b);
  const out = [];
  for (const i of cands) {
    const last = out[out.length - 1];
    if (last != null && i - last < sep) { if (dd[i] < dd[last]) out[out.length - 1] = i; }
    else out.push(i);
  }
  return out; // índices
}

// BTC drawdown vivo en un instante t0: última vela BTC con tiempo <= t0
function btcDrawdownAt(btc, t0) {
  if (!btc) return null;
  let idx = -1;
  for (let i = 0; i < btc.n; i++) { if (btc.t[i] <= t0) idx = i; else break; }
  if (idx < 0) return null;
  return { drawdown: btc.dd[idx], date: new Date(btc.t[idx]).toISOString().slice(0, 10) };
}

// último techo BTC (anclado) antes de t0 → semanas desde ese techo
function weeksSinceBtcTop(t0) {
  let top = null;
  for (const tp of BTC_TOPS) { if (tp <= t0) top = tp; }
  if (top == null) return null;
  return { topDate: new Date(top).toISOString().slice(0, 10), weeks: Math.round((t0 - top) / WEEK_MS) };
}

// suelo BTC (anclado) más cercano a t0 → offset en semanas (negativo = la alt tocó fondo ANTES que BTC)
function offsetVsBtcBottom(t0) {
  let best = null, bestD = Infinity;
  for (const b of BTC_BOTTOMS) { const d = Math.abs(b - t0); if (d < bestD) { bestD = d; best = b; } }
  if (best == null) return null;
  return { btcBottomDate: new Date(best).toISOString().slice(0, 10), offsetWeeks: Math.round((t0 - best) / WEEK_MS) };
}

function iso(ms) { return new Date(ms).toISOString().slice(0, 10); }
function round(v, d) { const m = Math.pow(10, d == null ? 2 : d); return v == null ? null : Math.round(v * m) / m; }

// procesa un activo: drawdown actual, suelos y, por cada suelo, techo previo + siguiente máximo + contexto BTC
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
    // serie de drawdown adelgazada para el gráfico (fecha + dd)
    ddSeries: s.t.map((tt, i) => [iso(tt), round(s.dd[i], 4)]),
  };

  // Histórico corto (listados 2024): < 104 semanas ⇒ no muestrear ciclos, no inventar suelos.
  if (s.n < 104) {
    out.shortHistory = true;
    warnings.push(`${meta.key}: histórico corto (${s.n} sem) → sin suelos de ciclo`);
    return out;
  }

  const bottomIdx = findBottoms(s);
  for (let bi = 0; bi < bottomIdx.length; bi++) {
    const i = bottomIdx[bi];
    const prevB = bi > 0 ? bottomIdx[bi - 1] : 0;
    // TECHO previo al desplome = ATH entre el suelo anterior y este suelo ("mejor salida")
    let topI = prevB;
    for (let j = prevB; j <= i; j++) if (s.c[j] > s.c[topI]) topI = j;
    // SIGUIENTE MÁXIMO tras el suelo (hasta el próximo suelo o el final) → múltiplo
    const nextB = bi + 1 < bottomIdx.length ? bottomIdx[bi + 1] : s.n - 1;
    let maxI = i;
    for (let j = i; j <= nextB; j++) if (s.c[j] > s.c[maxI]) maxI = j;
    const mult = s.c[i] > 0 ? s.c[maxI] / s.c[i] : null;

    const bt = meta.isRef ? null : btcDrawdownAt(btc, s.t[i]);
    const wt = meta.isRef ? null : weeksSinceBtcTop(s.t[i]);
    const off = meta.isRef ? null : offsetVsBtcBottom(s.t[i]);

    out.bottoms.push({
      date: iso(s.t[i]),
      price: round(s.c[i], s.c[i] < 10 ? 4 : 2),
      drawdown: round(s.dd[i], 4),
      bestExit: { date: iso(s.t[topI]), price: round(s.c[topI], s.c[topI] < 10 ? 4 : 2) }, // ATH previo
      nextMax: { date: iso(s.t[maxI]), price: round(s.c[maxI], s.c[maxI] < 10 ? 4 : 2), multiple: round(mult, 1) },
      btc: bt ? { drawdown: round(bt.drawdown, 4), asOf: bt.date, weeksSinceTop: wt ? wt.weeks : null, topDate: wt ? wt.topDate : null } : null,
      offset: off ? { weeks: off.offsetWeeks, btcBottomDate: off.btcBottomDate } : null,
    });
  }
  if (!out.bottoms.length) warnings.push(`${meta.key}: sin suelo < −60% en la serie`);
  return out;
}

module.exports = async (req, res) => {
  res.setHeader("Content-Type", "application/json; charset=utf-8");
  res.setHeader("Cache-Control", "public, max-age=3600, s-maxage=3600, stale-while-revalidate=7200"); // 1h
  const out = { asOf: new Date().toISOString(), warnings: [], btcTops: BTC_TOPS.map(iso), btcBottoms: BTC_BOTTOMS.map(iso), assets: [] };

  try {
    // 1) BTC primero (referencia de ciclo para las alts)
    const btcRows = await fetchKlines("BTCUSDT", out.warnings);
    const btc = btcRows ? buildSeries(btcRows) : null;
    if (btcRows) out.assets.push(processAsset(ASSETS[0], btcRows, null, out.warnings));

    // 2) el resto (secuencial: son 5 peticiones, evita rate-limit de Binance)
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
