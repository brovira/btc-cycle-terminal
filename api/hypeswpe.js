// api/hypeswpe.js — SWPE (Supply-Weighted P/E) de Hyperliquid (HYPE).
// Réplica del indicador de skewga.com/@skewga_hyper. Datos PÚBLICOS de mercado, sin API key,
// sin auth → sin secretos. Corre SERVER-SIDE (Vercel tiene red), así que funciona aunque no se
// pueda probar desde el sandbox (allí las APIs dan 403 por el proxy).
//
// Definición (la que replicamos):
//   SWPE = market cap del FLOAT ÷ ingresos ANUALIZADOS
//        = "cuántos AÑOS de ingresos harían falta para recomprar todo el float a precio actual".
//   Hyperliquid destina ~97% de los ingresos del protocolo a recomprar HYPE (Assistance Fund).
//   SWPE bajo = demanda del AF fuerte vs float (barato); alto = especulación por delante de ingresos.
//
// Fórmula implementada:
//   floatMcap = circulating_supply × precio
//   revAnual  = (revenue_30d_total / 30) × 365   (revenue diario medio de 30d, anualizado)
//   SWPE      = floatMcap / revAnual
//
// LIMITACIÓN (declarada también en el front): nuestro "float" = circulating_supply de CoinGecko,
// un PROXY del RFS (Ready-for-Sale) exacto de skewga (que excluye locked/foundation/team/emisiones
// futuras). Por eso nuestro SWPE puede diferir algo del suyo.

async function getJSON(url, warnings, tag) {
  const r = await fetch(url, { headers: { "User-Agent": "btc-terminal" } });
  if (!r.ok) throw new Error(`${tag}_${r.status}`);
  return r.json();
}

function round(v, d) {
  if (v == null || isNaN(v)) return null;
  const m = Math.pow(10, d == null ? 2 : d);
  return Math.round(v * m) / m;
}

// Suma los últimos N puntos [tsSeg, valorUSD] de totalDataChart → total del periodo.
function sumLastPoints(chart, n) {
  if (!Array.isArray(chart) || !chart.length) return null;
  const pts = chart.filter(p => Array.isArray(p) && p.length >= 2 && p[1] != null && !isNaN(+p[1]));
  if (!pts.length) return null;
  const slice = pts.slice(-n);
  return slice.reduce((a, p) => a + (+p[1]), 0);
}

// Construye la serie diaria [isoDate, usd] de los últimos `days` puntos, para el mini-gráfico.
function chartToSeries(chart, days) {
  if (!Array.isArray(chart) || !chart.length) return [];
  const pts = chart
    .filter(p => Array.isArray(p) && p.length >= 2 && p[1] != null && !isNaN(+p[1]))
    .slice(-days);
  return pts.map(p => [new Date((+p[0]) * 1000).toISOString().slice(0, 10), round(+p[1], 0)]);
}

module.exports = async (req, res) => {
  res.setHeader("Content-Type", "application/json; charset=utf-8");
  res.setHeader("Cache-Control", "public, max-age=3600, s-maxage=3600, stale-while-revalidate=7200"); // 1h

  const out = {
    asOf: new Date().toISOString(),
    price: null,
    circulatingSupply: null,
    totalSupply: null,
    floatMcapUsd: null,
    fdvUsd: null,
    revenue: { d24h: null, d7d: null, d30d: null, annualized: null },
    fees: { d30d: null },
    swpe: null,
    swpeFdv: null,
    revChart: [],
    warnings: [],
  };

  // ── 1) CoinGecko — precio, circulating/total supply, FDV ──────────────────────────
  try {
    const cg = await getJSON(
      "https://api.coingecko.com/api/v3/coins/hyperliquid?localization=false&tickers=false&market_data=true&community_data=false&developer_data=false&sparkline=false",
      out.warnings, "cg");
    const md = cg && cg.market_data;
    if (md) {
      out.price = (md.current_price && md.current_price.usd != null) ? +md.current_price.usd : null;
      out.circulatingSupply = md.circulating_supply != null ? +md.circulating_supply : null;
      out.totalSupply = md.total_supply != null ? +md.total_supply : null;
      out.fdvUsd = (md.fully_diluted_valuation && md.fully_diluted_valuation.usd != null)
        ? +md.fully_diluted_valuation.usd : null;
    } else {
      out.warnings.push("coingecko: sin market_data");
    }
  } catch (e) {
    out.warnings.push("coingecko: " + ((e && e.message) || e));
  }

  // ── Fallback de precio (Binance) si CoinGecko no dio precio ────────────────────────
  // circulating_supply SOLO la da CoinGecko → si CG falla del todo, el SWPE quedará null.
  if (out.price == null) {
    for (const host of ["api.binance.com", "api.binance.us"]) {
      try {
        const r = await fetch(`https://${host}/api/v3/klines?symbol=HYPEUSDT&interval=1d&limit=1`,
          { headers: { "User-Agent": "btc-terminal" } });
        if (!r.ok) continue;
        const k = await r.json();
        if (Array.isArray(k) && k.length && k[0] && k[0][4] != null) {
          out.price = +k[0][4]; // cierre de la última vela diaria
          out.warnings.push("precio: fallback Binance (" + host + ")");
          break;
        }
      } catch (e) { /* siguiente host */ }
    }
    if (out.price == null) out.warnings.push("precio: sin fuente (CoinGecko y Binance fallaron)");
  }

  // ── 2) DefiLlama — revenue diario del protocolo ────────────────────────────────────
  let revChart = null;
  try {
    const rev = await getJSON(
      "https://api.llama.fi/summary/fees/Hyperliquid?dataType=dailyRevenue",
      out.warnings, "llama_rev");
    out.revenue.d24h = rev && rev.total24h != null ? +rev.total24h : null;
    out.revenue.d7d = rev && rev.total7d != null ? +rev.total7d : null;
    out.revenue.d30d = rev && rev.total30d != null ? +rev.total30d : null;
    revChart = (rev && rev.totalDataChart) || null;
    // Si total30d no viene, sumarlo de los últimos 30 puntos de totalDataChart.
    if (out.revenue.d30d == null && revChart) {
      out.revenue.d30d = sumLastPoints(revChart, 30);
      if (out.revenue.d30d != null) out.warnings.push("revenue.d30d: sumado de totalDataChart");
    }
    if (revChart) out.revChart = chartToSeries(revChart, 90);
  } catch (e) {
    out.warnings.push("llama_revenue: " + ((e && e.message) || e) +
      " (¿'Hyperliquid' no es el slug correcto en DefiLlama?)");
  }

  // ── 2b) DefiLlama — fees brutos (contexto) ─────────────────────────────────────────
  try {
    const fees = await getJSON(
      "https://api.llama.fi/summary/fees/Hyperliquid?dataType=dailyFees",
      out.warnings, "llama_fees");
    out.fees.d30d = fees && fees.total30d != null ? +fees.total30d : null;
    if (out.fees.d30d == null && fees && fees.totalDataChart) {
      out.fees.d30d = sumLastPoints(fees.totalDataChart, 30);
    }
  } catch (e) {
    out.warnings.push("llama_fees: " + ((e && e.message) || e));
  }

  // ── 3) Cálculos ────────────────────────────────────────────────────────────────────
  if (out.price != null && out.circulatingSupply != null) {
    out.floatMcapUsd = out.price * out.circulatingSupply;
  }
  // FDV: usa el de CoinGecko; si no vino pero hay total_supply, derívalo.
  if (out.fdvUsd == null && out.price != null && out.totalSupply != null) {
    out.fdvUsd = out.price * out.totalSupply;
  }

  // revenue anualizado = media diaria de 30d × 365
  if (out.revenue.d30d != null && out.revenue.d30d > 0) {
    out.revenue.annualized = (out.revenue.d30d / 30) * 365;
  }

  // SWPE = float mcap / revenue anualizado
  if (out.floatMcapUsd != null && out.revenue.annualized != null && out.revenue.annualized > 0) {
    out.swpe = round(out.floatMcapUsd / out.revenue.annualized, 2);
  } else {
    out.warnings.push("swpe: null (falta float mcap o revenue anualizado)");
  }

  // SWPE sobre FDV (contexto; siempre mayor que el de float)
  if (out.fdvUsd != null && out.revenue.annualized != null && out.revenue.annualized > 0) {
    out.swpeFdv = round(out.fdvUsd / out.revenue.annualized, 2);
  }

  // Redondeos de presentación
  out.price = round(out.price, out.price != null && out.price < 10 ? 4 : 2);
  out.circulatingSupply = round(out.circulatingSupply, 0);
  out.totalSupply = round(out.totalSupply, 0);
  out.floatMcapUsd = round(out.floatMcapUsd, 0);
  out.fdvUsd = round(out.fdvUsd, 0);
  out.revenue.d24h = round(out.revenue.d24h, 0);
  out.revenue.d7d = round(out.revenue.d7d, 0);
  out.revenue.d30d = round(out.revenue.d30d, 0);
  out.revenue.annualized = round(out.revenue.annualized, 0);
  out.fees.d30d = round(out.fees.d30d, 0);

  return res.end(JSON.stringify(out));
};
