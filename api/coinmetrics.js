// api/coinmetrics.js — proxy serverless para la Community API de Coin Metrics.
//
// POR QUÉ: el navegador recibe a veces HTTP 403 al llamar directamente a
// community-api.coinmetrics.io (bloqueo tipo Cloudflare al origen del browser).
// Llamando desde el servidor (server-to-server) ese bloqueo desaparece y el
// on-chain (MVRV Z, realized...) carga de forma fiable. Gratis, sin key.
//
// El frontend llama a /api/coinmetrics?<mismos params que la API> y esto lo
// reenvía a .../v4/timeseries/asset-metrics. Si algún día pagas Glassnode,
// añadimos aquí un /api/glassnode con la key como secret (mismo patrón).

module.exports = async (req, res) => {
  res.setHeader("Content-Type", "application/json; charset=utf-8");
  res.setHeader("Access-Control-Allow-Origin", "*");
  const url = new URL(req.url, "http://x");
  const upstream = "https://community-api.coinmetrics.io/v4/timeseries/asset-metrics" + (url.search || "");
  try {
    // User-Agent de navegador: Coin Metrics/Cloudflare devuelve 403 a peticiones sin UA
    // (era la causa probable del on-chain "n/d"). Con UA de servidor-a-servidor pasa.
    const r = await fetch(upstream, { headers: { accept: "application/json", "User-Agent": "Mozilla/5.0 (compatible; btc-cycle-terminal/1.0; +https://btc-cycle-terminal.vercel.app)" } });
    const text = await r.text();
    res.setHeader("Cache-Control", "s-maxage=1800, stale-while-revalidate=3600"); // cache 30 min
    res.statusCode = r.status;
    return res.end(text);
  } catch (e) {
    res.statusCode = 502;
    return res.end(JSON.stringify({ error: "upstream_error", message: String((e && e.message) || e) }));
  }
};
