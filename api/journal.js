// api/journal.js — diario de operativa (trade journal) PERSONAL.
// GET  /api/journal            → lee las entradas del repo privado (data/journal.json)
// POST /api/journal            → añade una entrada nueva (y la commitea al repo privado)
// Ambas requieren la sesión global de la web. Los datos NUNCA están en el
// repo público: se leen/escriben en el momento contra brovira/DeFi-Tracker con GH_TOKEN.
//
// CONFIGURACIÓN (Vercel → Settings → Environment Variables):
//   DASH_PASSWORD = <la misma contraseña del dashboard>
//   GH_TOKEN      = token de GitHub fine-grained sobre DeFi-Tracker con
//                   Repository permissions → Contents: Read AND Write
//                   (para poder AÑADIR entradas; si solo es Read-only, el GET funciona
//                    pero el POST devolverá 403).

const REPO = process.env.PRIVATE_REPO || "brovira/DeFi-Tracker";
const PATH = "data/journal.json";
const { authConfigured, requestAuthorized } = require("../lib/auth");

async function readBody(req) {
  if (req.body) return typeof req.body === "string" ? JSON.parse(req.body) : req.body;
  const chunks = []; for await (const c of req) chunks.push(c);
  const raw = Buffer.concat(chunks).toString("utf8");
  return raw ? JSON.parse(raw) : {};
}

function slug(s) {
  return String(s || "").toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "")
    .replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "").slice(0, 48);
}

module.exports = async (req, res) => {
  res.setHeader("Content-Type", "application/json; charset=utf-8");
  const url = new URL(req.url, "http://x");
  const token = process.env.GH_TOKEN;

  if (!authConfigured()) { res.statusCode = 503; return res.end(JSON.stringify({ error: "no_password", message: "Falta SITE_PASSWORD o DASH_PASSWORD en Vercel." })); }
  if (!requestAuthorized(req, url)) { await new Promise(r => setTimeout(r, 600)); res.statusCode = 401; return res.end(JSON.stringify({ error: "bad_password" })); }
  if (!token) { res.statusCode = 503; return res.end(JSON.stringify({ error: "no_github_token", message: "Falta GH_TOKEN en Vercel." })); }

  const gh = (extra) => ({ Authorization: `Bearer ${token}`, "User-Agent": "lp-journal", Accept: "application/vnd.github+json", ...extra });
  const contentsUrl = `https://api.github.com/repos/${REPO}/contents/${PATH}`;

  // --- leer estado actual (sha + entradas) ---
  async function loadCurrent() {
    const r = await fetch(contentsUrl, { headers: gh() });
    if (r.status === 404) return { sha: null, doc: { entries: [] } };
    if (!r.ok) throw new Error("github_" + r.status);
    const j = await r.json();
    const text = Buffer.from(j.content || "", "base64").toString("utf8");
    let doc; try { doc = JSON.parse(text); } catch (_) { doc = { entries: [] }; }
    if (!Array.isArray(doc.entries)) doc.entries = [];
    return { sha: j.sha, doc };
  }

  try {
    if (req.method === "POST") {
      const body = await readBody(req);
      const date = (body.date || new Date().toISOString().slice(0, 10)).slice(0, 10);
      const entry = {
        id: `${date}-${slug(body.action || body.type || "entry")}-${Math.random().toString(36).slice(2, 6)}`,
        date,
        type: body.type || "Nota",
        action: body.action || "",
        venue: body.venue || "",
        asset: body.asset || "",
        position: body.position || "",
        result: body.result || "",
        rationale: body.rationale || "",
        plan: body.plan || "",
        agents: Array.isArray(body.agents) ? body.agents : [],
        levels: body.levels && typeof body.levels === "object" ? body.levels : {},
        tags: Array.isArray(body.tags) ? body.tags : [],
      };
      if (!entry.rationale && !entry.action) { res.statusCode = 400; return res.end(JSON.stringify({ error: "empty", message: "Escribe al menos acción o razonamiento." })); }

      const { sha, doc } = await loadCurrent();
      doc.entries.unshift(entry); // más reciente primero
      const content = Buffer.from(JSON.stringify(doc, null, 2) + "\n", "utf8").toString("base64");
      const put = await fetch(contentsUrl, {
        method: "PUT",
        headers: gh({ "Content-Type": "application/json" }),
        body: JSON.stringify({ message: `journal: ${date} ${entry.action || entry.type}`.slice(0, 72), content, sha: sha || undefined }),
      });
      if (!put.ok) {
        const t = await put.text().catch(() => "");
        res.statusCode = put.status;
        return res.end(JSON.stringify({ error: "github_" + put.status, message: put.status === 403 ? "El token no tiene permiso de escritura (Contents: Read AND Write)." : t.slice(0, 200) }));
      }
      return res.end(JSON.stringify({ ok: true, entry, count: doc.entries.length }));
    }

    // --- GET (por defecto): devolver entradas ---
    const { doc } = await loadCurrent();
    res.setHeader("Cache-Control", "private, max-age=30");
    return res.end(JSON.stringify(doc));
  } catch (e) {
    res.statusCode = 502; return res.end(JSON.stringify({ error: "fetch_error", message: String((e && e.message) || e) }));
  }
};
