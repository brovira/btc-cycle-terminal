// api/voldata.js — Cockpit de Volatilidad & Régimen. Datos GRATIS server-side (Deribit + Binance),
// sin API key. No se puede probar desde el sandbox (red bloqueada) pero funciona en Vercel.
//
// Gauges: DVOL (vol implícita, Deribit) + percentil · RV (realizada, Binance) · VRP = DVOL−RV ·
// Choppiness Index + BB width (rango vs tendencia → señal LP) · funding + OI + long/short + taker
// (flujo/apalancamiento) · distancia a la 200W MA (zona de re-entrada). Clasifica el régimen y da
// lecturas accionables (muelle cargado, LP ON/OFF, vol cara/barata).

async function j(url, tag, warnings) {
  try {
    const r = await fetch(url, { headers: { "User-Agent": "btc-terminal" } });
    if (!r.ok) { warnings.push(`${tag}_${r.status}`); return null; }
    return await r.json();
  } catch (e) { warnings.push(`${tag}: ${(e && e.message) || e}`); return null; }
}

function pctile(arr, v) {
  if (!arr || !arr.length || v == null) return null;
  const s = arr.filter(x => x != null && !isNaN(x)).slice().sort((a, b) => a - b);
  if (!s.length) return null;
  let c = 0; for (const x of s) if (x <= v) c++;
  return c / s.length;
}
function round(v, d) { if (v == null || isNaN(v)) return null; const m = Math.pow(10, d == null ? 2 : d); return Math.round(v * m) / m; }
function stdev(a) { if (a.length < 2) return null; const m = a.reduce((x, y) => x + y, 0) / a.length; const v = a.reduce((s, y) => s + (y - m) * (y - m), 0) / (a.length - 1); return Math.sqrt(v); }

async function klines(interval, limit, tag, W) {
  for (const host of ["api.binance.com", "api.binance.us"]) {
    const k = await j(`https://${host}/api/v3/klines?symbol=BTCUSDT&interval=${interval}&limit=${limit}`, tag, W);
    if (Array.isArray(k) && k.length) return k;
  }
  return null;
}

// Choppiness(n) en el índice i sobre arrays closes/highs/lows
function chopIdx(closes, highs, lows, i, n) {
  if (i < n) return null;
  let tr = 0, hi = -Infinity, lo = Infinity;
  for (let jj = i - n + 1; jj <= i; jj++) { const t = Math.max(highs[jj] - lows[jj], Math.abs(highs[jj] - closes[jj - 1]), Math.abs(lows[jj] - closes[jj - 1])); tr += t; if (highs[jj] > hi) hi = highs[jj]; if (lows[jj] < lo) lo = lows[jj]; }
  const rng = hi - lo; if (rng <= 0) return null;
  return 100 * Math.log10(tr / rng) / Math.log10(n);
}

// ── mode=backtest ── ¿el Choppiness predice volatilidad? ¿mejora el PnL del LP salir con CHOP>60?
async function backtest(res) {
  res.setHeader("Cache-Control", "public, max-age=3600, s-maxage=3600"); // 1h
  const W = [], out = { mode: "backtest", asOf: new Date().toISOString(), warnings: W, fwdDays: 14, chopExit: 60, feeApr: 0.30 };
  let closes = [], highs = [], lows = [], times = [];
  { const k = await klines("1d", 1000, "bt_klines", W); if (Array.isArray(k)) { closes = k.map(x => +x[4]); highs = k.map(x => +x[2]); lows = k.map(x => +x[3]); times = k.map(x => +x[0]); } }
  const n = closes.length;
  if (n < 200) { W.push("backtest: histórico insuficiente"); return res.end(JSON.stringify(out)); }
  out.from = new Date(times[0]).toISOString().slice(0, 10); out.to = new Date(times[n - 1]).toISOString().slice(0, 10); out.days = n;

  const ret = new Array(n).fill(0); for (let i = 1; i < n; i++) ret[i] = Math.log(closes[i] / closes[i - 1]);
  const FWD = 14;
  const rows = []; // {chop, fwdVol, fwdDD}
  for (let i = 20; i < n - FWD; i++) {
    const ch = chopIdx(closes, highs, lows, i, 14); if (ch == null) continue;
    let s = 0, s2 = 0, c = 0; for (let jj = i + 1; jj <= i + FWD; jj++) { s += ret[jj]; s2 += ret[jj] * ret[jj]; c++; }
    const varr = c > 1 ? (s2 - s * s / c) / (c - 1) : 0;
    const fwdVol = Math.sqrt(Math.max(0, varr)) * Math.sqrt(365) * 100;
    let mn = closes[i]; for (let jj = i; jj <= i + FWD; jj++) if (closes[jj] < mn) mn = closes[jj];
    rows.push({ chop: ch, fwdVol, fwdDD: mn / closes[i] - 1 });
  }
  out.samples = rows.length;
  const buck = (lbl, f) => { const g = rows.filter(f), nn = g.length; if (!nn) return { label: lbl, n: 0 }; return { label: lbl, n: nn, fwdVol: round(g.reduce((a, r) => a + r.fwdVol, 0) / nn, 1), fwdDD: round(g.reduce((a, r) => a + r.fwdDD, 0) / nn, 4), bigMovePct: round(g.filter(r => Math.abs(r.fwdDD) > 0.1).length / nn, 3) }; };
  out.buckets = [buck("CHOP < 40 (tendencia)", r => r.chop < 40), buck("CHOP 40–60", r => r.chop >= 40 && r.chop <= 60), buck("CHOP > 60 (tanque lleno)", r => r.chop > 60)];
  const baseVol = rows.reduce((a, r) => a + r.fwdVol, 0) / rows.length; out.baseVol = round(baseVol, 1);
  const hiCh = rows.filter(r => r.chop > 60); out.signalLift = hiCh.length ? round((hiCh.reduce((a, r) => a + r.fwdVol, 0) / hiCh.length) / baseVol - 1, 3) : null;

  // LP sim (modelo v2: valor LP = capital·√(P/entry); fees ~ feeApr sobre el valor mientras dentro).
  // Regla: FUERA del LP cuando CHOP>60 (viene vol); DENTRO en caso contrario. vs "siempre dentro".
  const feeApr = 0.30;
  function sim(useRule) {
    let inLP = true, entry = closes[20], cap = 1, fees = 0;
    for (let i = 21; i < n; i++) {
      const ch = chopIdx(closes, highs, lows, i, 14);
      const wantIn = useRule ? (ch == null ? inLP : ch <= 60) : true;
      if (inLP && !wantIn) { cap *= Math.sqrt(closes[i] / entry); inLP = false; }
      else if (!inLP && wantIn) { entry = closes[i]; inLP = true; }
      if (inLP) fees += cap * Math.sqrt(closes[i] / entry) * (feeApr / 365);
    }
    if (inLP) cap *= Math.sqrt(closes[n - 1] / entry);
    return cap + fees - 1; // retorno neto (fracción)
  }
  out.lpSim = { feeApr, alwaysIn: round(sim(false), 3), chopRule: round(sim(true), 3) };

  // ── Test C · STRADDLE largo cuando la vol está BARATA (¿cómo de barata?) ──
  // Compra un straddle ATM a H días: gana si el movimiento REALIZADO supera al IMPLÍCITO por opciones.
  // Barremos umbrales de percentil de DVOL para ver a partir de qué "baratura" hay edge.
  let dvolByDate = {};
  { const now = Date.now(), start = now - 5 * 365 * 864e5;
    const d = await j(`https://www.deribit.com/api/v2/public/get_volatility_index_data?currency=BTC&start_timestamp=${start}&end_timestamp=${now}&resolution=1D`, "bt_dvol", W);
    const data = d && d.result && d.result.data;
    if (Array.isArray(data)) for (const x of data) { const dt = new Date(+x[0]).toISOString().slice(0, 10); const v = +x[4]; if (v > 0) dvolByDate[dt] = v; } }
  const dvolVals = Object.values(dvolByDate).sort((a, b) => a - b);
  const dvolPctOf = v => { if (!dvolVals.length || v == null) return null; let c = 0; for (const x of dvolVals) if (x <= v) c++; return c / dvolVals.length; };
  if (dvolVals.length > 60) {
    const H = 14, strRows = [];
    for (let i = 20; i < n - H; i++) {
      const dt = new Date(times[i]).toISOString().slice(0, 10), dv = dvolByDate[dt];
      if (dv == null) continue;
      const impMove = dv / 100 * Math.sqrt(H / 365);          // movimiento implícito (fracción)
      const realMove = Math.abs(closes[i + H] / closes[i] - 1); // movimiento realizado
      strRows.push({ pct: dvolPctOf(dv), pnl: realMove - 0.8 * impMove }); // 0.8·implícito ≈ coste straddle ATM
    }
    const sweep = [0.1, 0.2, 0.3, 0.5, 1.0].map(th => {
      const g = strRows.filter(r => r.pct != null && r.pct <= th), nn = g.length;
      if (!nn) return { th, n: 0 };
      return { th, n: nn, avgPnl: round(g.reduce((a, r) => a + r.pnl, 0) / nn, 4), winRate: round(g.filter(r => r.pnl > 0).length / nn, 3) };
    });
    out.straddle = { horizon: H, samples: strRows.length, dvolNowPct: null, sweep, note: "PnL = fracción de notional: |mov. realizado| − 0.8·(vol implícita·√T). >0 = el straddle largo gana. 'th' = percentil de DVOL máximo para entrar." };
  } else { W.push("straddle: sin histórico de DVOL suficiente"); }

  return res.end(JSON.stringify(out));
}

module.exports = async (req, res) => {
  res.setHeader("Content-Type", "application/json; charset=utf-8");
  const _url = new URL(req.url, "http://x");
  if ((_url.searchParams.get("mode") || "") === "backtest") return backtest(res);
  res.setHeader("Cache-Control", "public, max-age=300, s-maxage=300"); // 5 min
  const out = { asOf: new Date().toISOString(), warnings: [] };
  const W = out.warnings;

  // ── DVOL (Deribit, vol implícita) — ~1 año, diario ──
  let dvolSeries = [];
  {
    const now = Date.now(), start = now - 370 * 864e5;
    const d = await j(`https://www.deribit.com/api/v2/public/get_volatility_index_data?currency=BTC&start_timestamp=${start}&end_timestamp=${now}&resolution=43200`, "dvol", W);
    const data = d && d.result && d.result.data;
    if (Array.isArray(data)) dvolSeries = data.map(x => [+x[0], +x[4]]).filter(p => p[1] > 0);
    else W.push("dvol: sin datos");
  }
  const dvolNow = dvolSeries.length ? dvolSeries[dvolSeries.length - 1][1] : null;
  out.dvol = round(dvolNow, 1);
  out.dvolPct = dvolNow != null ? round(pctile(dvolSeries.map(p => p[1]), dvolNow), 2) : null;
  // serie adelgazada (1 punto/día) para el gráfico
  const seen = {};
  out.dvolSeries = dvolSeries.map(p => [new Date(p[0]).toISOString().slice(0, 10), round(p[1], 1)])
    .filter(p => { if (seen[p[0]]) return false; seen[p[0]] = 1; return true; });

  // ── Binance diario (RV, CHOP, BB width) ──
  let closes = [], highs = [], lows = [];
  {
    const k = await klines("1d", 400, "klines", W);
    if (Array.isArray(k)) { closes = k.map(x => +x[4]); highs = k.map(x => +x[2]); lows = k.map(x => +x[3]); }
  }
  const price = closes.length ? closes[closes.length - 1] : null;
  out.price = round(price, 0);

  // RV 30d anualizada (%)
  if (closes.length > 31) {
    const rets = []; for (let i = closes.length - 30; i < closes.length; i++) rets.push(Math.log(closes[i] / closes[i - 1]));
    const sd = stdev(rets);
    out.rv = sd != null ? round(sd * Math.sqrt(365) * 100, 1) : null;
  } else out.rv = null;
  out.vrp = (out.dvol != null && out.rv != null) ? round(out.dvol - out.rv, 1) : null;

  // Choppiness Index (14): 100·log10(ΣTR / (maxH−minL)) / log10(n)
  function chop(n) {
    if (closes.length < n + 1) return null;
    const N = closes.length; let trSum = 0, hi = -Infinity, lo = Infinity;
    for (let i = N - n; i < N; i++) {
      const tr = Math.max(highs[i] - lows[i], Math.abs(highs[i] - closes[i - 1]), Math.abs(lows[i] - closes[i - 1]));
      trSum += tr; if (highs[i] > hi) hi = highs[i]; if (lows[i] < lo) lo = lows[i];
    }
    const rng = hi - lo; if (rng <= 0) return null;
    return 100 * Math.log10(trSum / rng) / Math.log10(n);
  }
  out.chop = round(chop(14), 1);

  // BB width (20) = 4σ/media, + su percentil ~1 año
  function bbw(endIdx) {
    if (endIdx < 19) return null;
    const seg = closes.slice(endIdx - 19, endIdx + 1);
    const m = seg.reduce((a, b) => a + b, 0) / 20, sd = stdev(seg);
    if (sd == null || m <= 0) return null;
    return (4 * sd) / m;
  }
  out.bbw = round(bbw(closes.length - 1), 4);
  { const arr = []; for (let i = Math.max(19, closes.length - 365); i < closes.length; i++) { const w = bbw(i); if (w != null) arr.push(w); } out.bbwPct = out.bbw != null ? round(pctile(arr, out.bbw), 2) : null; }

  // ── 200W MA (semanal) ──
  {
    const k = await klines("1w", 300, "weekly", W);
    if (Array.isArray(k) && k.length >= 200) {
      const wc = k.map(x => +x[4]).slice(-200);
      const ma = wc.reduce((a, b) => a + b, 0) / 200;
      out.ma200w = round(ma, 0);
      out.distTo200w = price != null ? round(price / ma - 1, 4) : null;
    } else W.push("200w: histórico insuficiente");
  }

  // ── Derivatives: funding + OI + long/short (Bybit primario; Binance fapi suele geobloquearse) ──
  { const t = await j(`https://api.bybit.com/v5/market/tickers?category=linear&symbol=BTCUSDT`, "bybit_tick", W);
    const r0 = t && t.result && t.result.list && t.result.list[0];
    if (r0) { if (r0.fundingRate != null) out.funding = round(+r0.fundingRate, 6); if (r0.openInterest != null) out.oi = round(+r0.openInterest, 0); } }
  if (out.funding == null) { const o = await j(`https://www.okx.com/api/v5/public/funding-rate?instId=BTC-USDT-SWAP`, "okx_fund", W); const d0 = o && o.data && o.data[0]; if (d0 && d0.fundingRate != null) out.funding = round(+d0.fundingRate, 6); }
  { const oih = await j(`https://api.bybit.com/v5/market/open-interest?category=linear&symbol=BTCUSDT&intervalTime=1d&limit=8`, "bybit_oi", W);
    const lst = oih && oih.result && oih.result.list; // Bybit devuelve del más nuevo al más viejo
    if (Array.isArray(lst) && lst.length >= 2) { const newest = +lst[0].openInterest, oldest = +lst[lst.length - 1].openInterest; out.oiChg7d = oldest > 0 ? round(newest / oldest - 1, 3) : null; } }
  { const ls = await j(`https://api.bybit.com/v5/market/account-ratio?category=linear&symbol=BTCUSDT&period=1d&limit=1`, "bybit_ls", W);
    const l0 = ls && ls.result && ls.result.list && ls.result.list[0];
    if (l0 && l0.buyRatio != null && l0.sellRatio != null && +l0.sellRatio > 0) out.longShort = round(+l0.buyRatio / +l0.sellRatio, 2); }

  // ── OPCIONES (Deribit) — put/call OI, OI total, skew 25d aprox, expiry cercana ──
  // Métricas que Glassnode usa en su Week On-Chain para leer posicionamiento y miedo direccional.
  { const bs = await j(`https://www.deribit.com/api/v2/public/get_book_summary_by_currency?currency=BTC&kind=option`, "opt", W);
    const list = bs && bs.result;
    if (Array.isArray(list) && list.length) {
      let callOi = 0, putOi = 0, spot = null;
      const byExp = {};
      const monN = { JAN: 1, FEB: 2, MAR: 3, APR: 4, MAY: 5, JUN: 6, JUL: 7, AUG: 8, SEP: 9, OCT: 10, NOV: 11, DEC: 12 };
      const expMs = s => { const m = String(s).match(/(\d+)([A-Z]{3})(\d{2})/); if (!m || !monN[m[2]]) return Infinity; return Date.parse(`20${m[3]}-${String(monN[m[2]]).padStart(2, "0")}-${String(+m[1]).padStart(2, "0")}`); };
      for (const o of list) {
        const parts = String(o.instrument_name || "").split("-"); // BTC-27DEC24-100000-C
        if (parts.length < 4) continue;
        const type = parts[3], strike = +parts[2], iv = o.mark_iv != null ? +o.mark_iv : null, oi = o.open_interest != null ? +o.open_interest : 0;
        if (o.underlying_price) spot = +o.underlying_price;
        if (type === "C") callOi += oi; else if (type === "P") putOi += oi;
        (byExp[parts[1]] = byExp[parts[1]] || []).push({ strike, iv, type });
      }
      out.optPutCall = callOi > 0 ? round(putOi / callOi, 2) : null;
      out.optOi = round(callOi + putOi, 0);
      if (spot == null) spot = price;
      if (spot) {
        const now = Date.now();
        const near = Object.keys(byExp).sort((a, b) => expMs(a) - expMs(b)).find(e => expMs(e) > now + 3 * 864e5);
        if (near) {
          const arr = byExp[near], putT = spot * 0.9, callT = spot * 1.1;
          let bp = null, bc = null;
          for (const o of arr) { if (o.iv == null) continue; if (o.type === "P") { if (bp == null || Math.abs(o.strike - putT) < Math.abs(bp.strike - putT)) bp = o; } else if (o.type === "C") { if (bc == null || Math.abs(o.strike - callT) < Math.abs(bc.strike - callT)) bc = o; } }
          if (bp && bc) out.optSkew = round(bp.iv - bc.iv, 1); // >0 = puts más caras = miedo abajo
          out.optNearExp = near;
        }
      }
    }
  }

  // ── Régimen + lecturas ──
  const dv = out.dvolPct, bw = out.bbwPct, ch = out.chop;
  let regime = "neutral", regimeTxt = "Neutral — sin señal de compresión ni tendencia clara.";
  if (ch != null && ch < 38.2) { regime = "trending"; regimeTxt = "📈 Tendencia — el precio se mueve con dirección (malo para LP; favorece momentum)."; }
  else if (dv != null && dv > 0.75) { regime = "stress"; regimeTxt = "⚡ Estrés / vol alta — DVOL en percentil alto; el movimiento ya está en marcha."; }
  else if ((dv != null && dv < 0.30) && (bw != null && bw < 0.30) && (ch != null && ch > 55)) { regime = "compression"; regimeTxt = "🪤 Muelle cargado — vol implícita y rango comprimidos. Viene un movimiento grande (la dirección NO la dice esto)."; }
  out.regime = regime; out.regimeTxt = regimeTxt;

  let lp = "neutral", lpTxt = "Neutral — vigila el Choppiness.";
  if (ch != null) { if (ch > 61.8) { lp = "on"; lpTxt = "🧵 LP ON — mercado en rango (cobras fees, poco IL)."; } else if (ch < 38.2) { lp = "off"; lpTxt = "🚫 LP OFF — tendencia en marcha (riesgo de IL)."; } }
  out.lp = lp; out.lpTxt = lpTxt;

  if (out.vrp != null) out.vrpTxt = out.vrp < 0 ? "Vol BARATA (IV<RV) → favorece COMPRAR vol (straddle / long gamma)." : out.vrp > 6 ? "Vol CARA (VRP ancho) → favorece VENDER premium." : "VRP normal — sin edge claro solo por vol.";
  if (out.optSkew != null) out.optSkewTxt = out.optSkew > 3 ? "Miedo a la BAJADA (puts caras) — cobertura/pesimismo." : out.optSkew < -3 ? "Codicia al ALZA (calls caras) — chase alcista." : "Skew equilibrado — sin sesgo direccional fuerte en opciones.";
  if (out.optPutCall != null) out.optPutCallTxt = out.optPutCall > 1 ? "Más OI en puts que en calls — posicionamiento defensivo/bajista." : "Más OI en calls que en puts — posicionamiento alcista.";

  return res.end(JSON.stringify(out));
};
