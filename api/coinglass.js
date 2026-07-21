// api/coinglass.js — proxy serverless para la API de Coinglass.
//
// POR QUÉ: la API key de Coinglass NO puede ir en el frontend (repo público).
// Este backend la guarda como variable de entorno (secret en Vercel) y hace la
// llamada del lado del servidor, devolviendo solo el JSON al navegador.
//
// CONFIGURACIÓN (una vez):
//   1. Crea cuenta en https://www.coinglass.com/ y saca tu API key (Account → API).
//   2. En Vercel → tu proyecto → Settings → Environment Variables:
//        COINGLASS_API_KEY = <tu key>   (Production + Preview)
//   3. Redeploy. Listo: el frontend llama a /api/coinglass?metric=...
//
// SEGURIDAD: solo se permiten métricas de una lista blanca (no es un proxy abierto).
// Si algún endpoint no existe en tu plan de Coinglass, ajústalo en PATHS abajo.

const BASE = process.env.COINGLASS_BASE || "https://open-api-v4.coinglass.com";
const KEY_HEADER = process.env.COINGLASS_KEY_HEADER || "CG-API-KEY"; // v3 usaba "coinglassSecret"

// Lista blanca: metric -> { path, defaults }. Los params extra de la query se
// mezclan encima de defaults. Ajusta los paths a tu plan si hace falta.
const PATHS = {
  liquidation_history: { path: "/api/futures/liquidation/aggregated-history", defaults: { symbol: "BTC", interval: "1d" } },
  liquidation_coin:    { path: "/api/futures/liquidation/coin-list",           defaults: {} },
  open_interest:       { path: "/api/futures/open-interest/aggregated-history", defaults: { symbol: "BTC", interval: "1d" } },
  funding:             { path: "/api/futures/funding-rate/oi-weight-history",   defaults: { symbol: "BTC", interval: "1d" } },
  long_short:          { path: "/api/futures/global-long-short-account-ratio/history", defaults: { symbol: "BTC", interval: "1d" } },
  heatmap:             { path: "/api/futures/liquidation/heatmap",              defaults: { symbol: "BTC", interval: "3d" } },
};

module.exports = async (req, res) => {
  res.setHeader("Content-Type", "application/json; charset=utf-8");
  if (req.method !== "GET") { res.statusCode = 405; return res.end(JSON.stringify({ error: "method_not_allowed" })); }

  const key = process.env.COINGLASS_API_KEY;
  if (!key) {
    res.statusCode = 503;
    return res.end(JSON.stringify({
      error: "no_key",
      message: "Falta COINGLASS_API_KEY. Configúrala en Vercel → Settings → Environment Variables y haz redeploy.",
      metrics: Object.keys(PATHS),
    }));
  }

  const url = new URL(req.url, "http://x");
  const metric = url.searchParams.get("metric") || "";
  const cfg = PATHS[metric];
  if (!cfg) {
    res.statusCode = 400;
    return res.end(JSON.stringify({ error: "bad_metric", message: "Métrica no permitida.", metrics: Object.keys(PATHS) }));
  }

  // construye la query upstream: defaults + los params de la petición (menos 'metric')
  const params = new URLSearchParams(cfg.defaults);
  for (const [k, v] of url.searchParams) if (k !== "metric") params.set(k, v);
  const upstream = `${BASE}${cfg.path}?${params.toString()}`;

  try {
    const r = await fetch(upstream, { headers: { [KEY_HEADER]: key, "accept": "application/json" } });
    const text = await r.text();
    // cachea en el edge para no quemar el rate limit (5 min)
    res.setHeader("Cache-Control", "s-maxage=300, stale-while-revalidate=600");
    res.statusCode = r.ok ? 200 : r.status;
    // devuelve el JSON de Coinglass tal cual (o el texto de error)
    return res.end(text);
  } catch (e) {
    res.statusCode = 502;
    return res.end(JSON.stringify({ error: "upstream_error", message: String((e && e.message) || e), upstream }));
  }
};
