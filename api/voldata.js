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

  // ── Derivatives (Binance futures; algunos endpoints pueden bloquearse por región) ──
  { const p = await j(`https://fapi.binance.com/fapi/v1/premiumIndex?symbol=BTCUSDT`, "funding", W); out.funding = p && p.lastFundingRate != null ? round(+p.lastFundingRate, 6) : null; }
  { const oih = await j(`https://fapi.binance.com/futures/data/openInterestHist?symbol=BTCUSDT&period=1d&limit=8`, "oihist", W); if (Array.isArray(oih) && oih.length >= 2) { const a = +oih[0].sumOpenInterest, b = +oih[oih.length - 1].sumOpenInterest; out.oiChg7d = a > 0 ? round(b / a - 1, 3) : null; } }
  { const ls = await j(`https://fapi.binance.com/futures/data/globalLongShortAccountRatio?symbol=BTCUSDT&period=1d&limit=1`, "ls", W); if (Array.isArray(ls) && ls.length) out.longShort = round(+ls[0].longShortRatio, 2); }
  { const tk = await j(`https://fapi.binance.com/futures/data/takerlongshortRatio?symbol=BTCUSDT&period=1d&limit=1`, "taker", W); if (Array.isArray(tk) && tk.length) out.takerRatio = round(+tk[0].buySellRatio, 2); }

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

  return res.end(JSON.stringify(out));
};
