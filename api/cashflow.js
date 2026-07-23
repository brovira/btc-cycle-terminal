// api/cashflow.js — "disponible para invertir" de BELROGAM, leído del endpoint que ya lo
// calcula (NO se recalcula aquí). Ver sops/gestion_caja_inversion.md para el porqué.
//
// El dashboard de BELROGAM expone GET /api/cash (bearer token propio, fuera de su login de
// cookie) devolviendo: saldo, los dos escenarios (confirmado/esperado) con su "suelo" y el
// disponible a 0/1/2/3 meses de margen, las capas de seguridad, el objetivo de acumulación
// (retirado/desplegado/munición), el flujo semanal y avisos. Este endpoint es solo un proxy
// con la contraseña del terminal por delante — una sola fuente de verdad, un solo cálculo.
//
// CONFIGURACIÓN (Vercel → Environment Variables):
//   BELROGAM_DASHBOARD_URL = https://<tu-dashboard-belrogam>.vercel.app   (sin /api/cash)
//   CASH_API_TOKEN         = el MISMO valor que CASH_API_TOKEN en el proyecto Vercel del
//                            dashboard de BELROGAM (es el que autoriza /api/cash allí)
//   SITE_PASSWORD          = (la contraseña única de la web; DASH_PASSWORD sigue compatible)

const { authConfigured, requestAuthorized } = require("../lib/auth");
const fs = require("fs");

const clean = (v) => {
  let s = v == null ? "" : String(v).trim();
  if ((s.startsWith('"') && s.endsWith('"')) || (s.startsWith("'") && s.endsWith("'"))) s = s.slice(1, -1).trim();
  return s;
};

module.exports = async (req, res) => {
  res.setHeader("Content-Type", "application/json; charset=utf-8");
  const url = new URL(req.url, "http://x");

  if (!authConfigured(req)) { res.statusCode = 503; return res.end(JSON.stringify({ error: "no_password" })); }
  if (!requestAuthorized(req, url)) { await new Promise(r => setTimeout(r, 600)); res.statusCode = 401; return res.end(JSON.stringify({ error: "bad_password" })); }

  // atajo para desarrollo local: sirve una respuesta con la MISMA forma que /api/cash
  if (process.env.LOCAL_CASHFLOW_FILE) {
    try {
      const cached = await fs.promises.readFile(process.env.LOCAL_CASHFLOW_FILE, "utf8");
      res.setHeader("Cache-Control", "no-store");
      return res.end(cached);
    } catch (e) {
      res.statusCode = e && e.code === "ENOENT" ? 404 : 500;
      return res.end(JSON.stringify({ error: "local_cashflow", message: String((e && e.message) || e) }));
    }
  }

  let BASE = clean(process.env.BELROGAM_DASHBOARD_URL);
  let TOKEN = clean(process.env.CASH_API_TOKEN).replace(/^Bearer\s+/i, "").trim();
  if (!BASE || !TOKEN) {
    for (const k of Object.keys(process.env)) {
      if (!BASE && /BELROGAM/i.test(k) && /(URL|HOST|DOMAIN)/i.test(k)) BASE = clean(process.env[k]);
      if (!TOKEN && /CASH/i.test(k) && /(TOKEN|KEY|SECRET)/i.test(k)) TOKEN = clean(process.env[k]).replace(/^Bearer\s+/i, "").trim();
    }
  }
  if (!BASE || !TOKEN) {
    const diag = Object.keys(process.env).filter(k => /BELROGAM|CASH_API/i.test(k)).map(k => {
      const raw = process.env[k] || ""; const len = raw.length, trimmed = raw.trim().length;
      return `${k} (${len === 0 ? "vacía" : trimmed === 0 ? "solo espacios/saltos de línea" : `${len} caracteres, OK`})`;
    });
    res.statusCode = 503;
    return res.end(JSON.stringify({
      error: "no_config",
      message: "Faltan BELROGAM_DASHBOARD_URL y/o CASH_API_TOKEN en Vercel. " +
        "Lo que veo con esos nombres: " + (diag.length ? diag.join(" · ") : "ninguna variable") +
        ". BELROGAM_DASHBOARD_URL = la URL de tu dashboard de BELROGAM en Vercel (sin /api/cash al final). " +
        "CASH_API_TOKEN = el MISMO valor que tengas puesto como CASH_API_TOKEN en el proyecto Vercel de ese dashboard " +
        "(si no existe ahí todavía, genera un token y ponlo en los dos proyectos). Tras corregir, Redeploy.",
    }));
  }

  try {
    const r = await fetch(`${BASE.replace(/\/+$/, "")}/api/cash`, {
      headers: { Authorization: `Bearer ${TOKEN}` },
      cache: "no-store",
    });
    const text = await r.text();
    if (!r.ok) {
      res.statusCode = r.status === 401 ? 502 : r.status;
      let msg = text.slice(0, 300);
      try { msg = JSON.parse(text).error || msg; } catch (e) {}
      return res.end(JSON.stringify({ error: "belrogam_" + r.status, message: r.status === 401
        ? "El dashboard de BELROGAM rechazó el token (401). Comprueba que CASH_API_TOKEN es idéntico en los dos proyectos de Vercel."
        : msg }));
    }
    res.setHeader("Cache-Control", "private, max-age=120"); // 2 min — el dashboard ya calcula en vivo
    return res.end(text);
  } catch (e) {
    res.statusCode = 502;
    return res.end(JSON.stringify({ error: "fetch_error", message: String((e && e.message) || e) }));
  }
};
