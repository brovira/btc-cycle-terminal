// api/bitacora.js — LEE y GUARDA la bitácora del operador en el repo PRIVADO
// (brovira/DeFi-Tracker → data/bitacora.json). Nunca vive en el repo público.
//
//   GET  /api/bitacora           → devuelve el JSON de la bitácora (o [] si no existe aún)
//   POST /api/bitacora  (body=JSON array de entradas) → lo guarda en el repo privado
//
// Ambas rutas están detrás de la MISMA contraseña que /api/private.js.
//
// CONFIGURACIÓN — OPCIÓN SIMPLE (reutilizar el token que ya tienes):
//   Basta con SUBIR el permiso del GH_TOKEN existente a escritura:
//   GitHub → Settings → Developer settings → Fine-grained tokens → (tu token) →
//   Permissions → Repository permissions → Contents: cambia "Read-only" a
//   "Read and write" → Save. No hay que crear ninguna variable nueva en Vercel.
//
// CONFIGURACIÓN — OPCIÓN LIMPIA (token de escritura aparte, opcional):
//   Crea GH_TOKEN_WRITE en Vercel con un token nuevo (Contents: Read and write).
//   Si existe, tiene prioridad sobre GH_TOKEN. Si no, se usa GH_TOKEN.
//   (DASH_PASSWORD ya existe si usas /api/private.js.)

const { authConfigured, requestAuthorized } = require("../lib/auth");
const REPO = process.env.PRIVATE_REPO || "brovira/DeFi-Tracker";
const FILE = "data/bitacora.json";
const API = `https://api.github.com/repos/${REPO}/contents/${FILE}`;
const UA = "lp-dashboard";

function readBody(req) {
  return new Promise((resolve, reject) => {
    let data = "";
    req.on("data", (c) => { data += c; if (data.length > 5_000_000) reject(new Error("body_too_large")); });
    req.on("end", () => resolve(data));
    req.on("error", reject);
  });
}

module.exports = async (req, res) => {
  res.setHeader("Content-Type", "application/json; charset=utf-8");
  const url = new URL(req.url, "http://x");

  if (!authConfigured(req)) { res.statusCode = 503; return res.end(JSON.stringify({ error: "no_password", message: "Falta SITE_PASSWORD o DASH_PASSWORD en Vercel." })); }
  if (!requestAuthorized(req, url)) {
    await new Promise((r) => setTimeout(r, 600));
    res.statusCode = 401; return res.end(JSON.stringify({ error: "bad_password" }));
  }

  const roToken = process.env.GH_TOKEN_WRITE || process.env.GH_TOKEN;
  // Reutilizamos el GH_TOKEN existente para escribir (solo hay que subirlo a
  // "Contents: Read and write" en GitHub). GH_TOKEN_WRITE sigue teniendo prioridad
  // por si algún día quieres separar el token de lectura del de escritura.
  const rwToken = process.env.GH_TOKEN_WRITE || process.env.GH_TOKEN || null;

  // ── GET: devolver la bitácora actual ────────────────────────────────
  if (req.method === "GET") {
    if (!roToken) { res.statusCode = 503; return res.end(JSON.stringify({ error: "no_github_token", message: "Falta GH_TOKEN_WRITE (o GH_TOKEN) en Vercel." })); }
    try {
      const r = await fetch(API, { headers: { Authorization: `Bearer ${roToken}`, Accept: "application/vnd.github.raw+json", "User-Agent": UA } });
      if (r.status === 404) { res.setHeader("Cache-Control", "no-store"); return res.end("[]"); } // aún no existe
      if (!r.ok) { res.statusCode = r.status; return res.end(JSON.stringify({ error: "github_" + r.status })); }
      const text = await r.text();
      res.setHeader("Cache-Control", "no-store");
      return res.end(text);
    } catch (e) {
      res.statusCode = 502; return res.end(JSON.stringify({ error: "fetch_error", message: String((e && e.message) || e) }));
    }
  }

  // ── POST: guardar la bitácora ───────────────────────────────────────
  if (req.method === "POST") {
    if (!rwToken) { res.statusCode = 503; return res.end(JSON.stringify({ error: "no_write_token", message: "Falta un token con permiso de escritura: sube el GH_TOKEN a 'Contents: Read and write' en GitHub (o crea GH_TOKEN_WRITE)." })); }
    let entries;
    try {
      const body = await readBody(req);
      entries = JSON.parse(body);
      if (!Array.isArray(entries)) throw new Error("no_array");
    } catch (e) {
      res.statusCode = 400; return res.end(JSON.stringify({ error: "bad_body", message: "El cuerpo debe ser un array JSON de entradas." }));
    }
    try {
      // 1) obtener el SHA actual (necesario para actualizar; ausente si es el 1er guardado)
      let sha = null;
      const cur = await fetch(API, { headers: { Authorization: `Bearer ${rwToken}`, Accept: "application/vnd.github+json", "User-Agent": UA } });
      if (cur.ok) { sha = (await cur.json()).sha; }
      else if (cur.status !== 404) { res.statusCode = cur.status; return res.end(JSON.stringify({ error: "github_get_" + cur.status, message: "El token de escritura no tiene acceso o expiró." })); }

      // 2) PUT con el contenido nuevo
      const content = Buffer.from(JSON.stringify(entries, null, 2), "utf8").toString("base64");
      const put = await fetch(API, {
        method: "PUT",
        headers: { Authorization: `Bearer ${rwToken}`, Accept: "application/vnd.github+json", "User-Agent": UA },
        body: JSON.stringify({ message: `bitacora: ${entries.length} entradas`, content, sha: sha || undefined }),
      });
      if (!put.ok) { const t = await put.text(); res.statusCode = put.status; return res.end(JSON.stringify({ error: "github_put_" + put.status, message: t.slice(0, 300) })); }
      res.setHeader("Cache-Control", "no-store");
      return res.end(JSON.stringify({ ok: true, count: entries.length }));
    } catch (e) {
      res.statusCode = 502; return res.end(JSON.stringify({ error: "write_error", message: String((e && e.message) || e) }));
    }
  }

  res.statusCode = 405; return res.end(JSON.stringify({ error: "method_not_allowed" }));
};
