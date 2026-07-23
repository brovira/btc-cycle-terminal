// api/private.js — sirve tus datos PERSONALES (posiciones/PnL del DeFi-Tracker)
// solo si se envía la contraseña correcta. Los datos NUNCA están en el repo
// público: se leen en el momento del repo privado brovira/DeFi-Tracker con un
// token de GitHub (secret), y solo se devuelven si la contraseña coincide.
//
// CONFIGURACIÓN (una vez, en Vercel → proyecto → Settings → Environment Variables):
//   DASH_PASSWORD = <la contraseña que elijas>
//   GH_TOKEN      = <token de GitHub con permiso de LECTURA sobre DeFi-Tracker>
// Cómo sacar el GH_TOKEN: GitHub → Settings → Developer settings →
//   Fine-grained tokens → Generate new token → Resource owner: tú →
//   Repository access: Only select repositories → DeFi-Tracker →
//   Permissions → Repository permissions → Contents: Read-only → Generate.
//
// La cookie del acceso global autoriza estas peticiones. La cabecera 'x-dash-pw'
// se mantiene como compatibilidad para desarrollo y clientes antiguos.

const { authConfigured, requestAuthorized } = require("../lib/auth");
const fs = require("fs");
const pathLib = require("path");
const REPO = process.env.PRIVATE_REPO || "brovira/DeFi-Tracker";
const FILES = {                       // lista blanca de archivos que se pueden pedir
  orca_pnl: "data/normalized/orca_pnl.json",
  orca_positions: "data/normalized/orca_positions.json",
  orca_events: "data/normalized/orca_events.json",
  manual_assets: "data/manual_assets.json", // activos sin API pública (Jupiter DAO, CEX…)
  btc_compras: "data/btc_compras.json",     // compras BTC del ciclo (Revolut round-up + órdenes BELROGAM)
  mc_plan: "data/mc_plan.json",             // ajustes por defecto del Monte Carlo del plan (presupuesto, DCA, órdenes…)
};

module.exports = async (req, res) => {
  res.setHeader("Content-Type", "application/json; charset=utf-8");
  const url = new URL(req.url, "http://x");
  const token = process.env.GH_TOKEN;

  if (!authConfigured(req)) { res.statusCode = 503; return res.end(JSON.stringify({ error: "no_password", message: "Falta SITE_PASSWORD o DASH_PASSWORD en Vercel." })); }
  if (!requestAuthorized(req, url)) {
    await new Promise(r => setTimeout(r, 600)); // pequeño freno anti fuerza bruta
    res.statusCode = 401; return res.end(JSON.stringify({ error: "bad_password" }));
  }
  const key = (url.searchParams.get("file") || "orca_pnl").toLowerCase();
  const path = FILES[key];
  if (!path) { res.statusCode = 400; return res.end(JSON.stringify({ error: "bad_file", files: Object.keys(FILES) })); }
  if (process.env.LOCAL_DATA_DIR) {
    try {
      const localPath = pathLib.join(process.env.LOCAL_DATA_DIR, path.replace(/^data\//, ""));
      const text = await fs.promises.readFile(localPath, "utf8");
      res.setHeader("Cache-Control", "no-store");
      return res.end(text);
    } catch (e) {
      res.statusCode = e && e.code === "ENOENT" ? 404 : 500;
      return res.end(JSON.stringify({ error: "local_file", message: String((e && e.message) || e) }));
    }
  }
  if (!token) { res.statusCode = 503; return res.end(JSON.stringify({ error: "no_github_token", message: "Falta GH_TOKEN en Vercel." })); }

  try {
    const r = await fetch(`https://api.github.com/repos/${REPO}/contents/${path}`, {
      headers: { Authorization: `Bearer ${token}`, Accept: "application/vnd.github.raw+json", "User-Agent": "lp-dashboard" },
    });
    if (!r.ok) { res.statusCode = r.status; return res.end(JSON.stringify({ error: "github_" + r.status, message: r.status === 404 ? "Archivo no encontrado (¿ya corrió la Action?)" : "El token no tiene acceso o expiró." })); }
    const text = await r.text();
    res.setHeader("Cache-Control", "private, max-age=120");
    return res.end(text);
  } catch (e) {
    res.statusCode = 502; return res.end(JSON.stringify({ error: "fetch_error", message: String((e && e.message) || e) }));
  }
};
