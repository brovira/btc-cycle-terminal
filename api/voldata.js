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

module.exports = async (req, res) => {
  res.setHeader("Content-Type", "application/json; charset=utf-8");
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
