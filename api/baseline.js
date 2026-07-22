// api/baseline.js — línea base del "farming desde cero" (fresh start).
// GET  /api/baseline  → lee data/baseline.json del repo privado (DeFi-Tracker)
// POST /api/baseline  → fija la línea base de HOY (valor actual de las posiciones
//                       estables) y la commitea al repo privado.
// Requiere la sesión global de la web, igual que journal.js.
//
// La línea base marca el "día cero" del farming: a partir de ahí el dashboard
// calcula el PnL solo con los flujos posteriores (capital fresco = depósito
// posterior → se resta solo, no infla el PnL).

const REPO = process.env.PRIVATE_REPO || "brovira/DeFi-Tracker";
const PATH = "data/baseline.json";
const { authConfigured, requestAuthorized } = require("../lib/auth");

async function readBody(req) {
  if (req.body) return typeof req.body === "string" ? JSON.parse(req.body) : req.body;
  const chunks = []; for await (const c of req) chunks.push(c);
  const raw = Buffer.concat(chunks).toString("utf8");
  return raw ? JSON.parse(raw) : {};
}

module.exports = async (req, res) => {
  res.setHeader("Content-Type", "application/json; charset=utf-8");
  const url = new URL(req.url, "http://x");
  const token = process.env.GH_TOKEN;

  if (!authConfigured()) { res.statusCode = 503; return res.end(JSON.stringify({ error: "no_password" })); }
  if (!requestAuthorized(req, url)) { await new Promise(r => setTimeout(r, 600)); res.statusCode = 401; return res.end(JSON.stringify({ error: "bad_password" })); }
  if (!token) { res.statusCode = 503; return res.end(JSON.stringify({ error: "no_github_token" })); }

  const gh = (extra) => ({ Authorization: `Bearer ${token}`, "User-Agent": "lp-baseline", Accept: "application/vnd.github+json", ...extra });
  const contentsUrl = `https://api.github.com/repos/${REPO}/contents/${PATH}`;

  async function loadCurrent() {
    const r = await fetch(contentsUrl, { headers: gh() });
    if (r.status === 404) return { sha: null, doc: null };
    if (!r.ok) throw new Error("github_" + r.status);
    const j = await r.json();
    let doc; try { doc = JSON.parse(Buffer.from(j.content || "", "base64").toString("utf8")); } catch (_) { doc = null; }
    return { sha: j.sha, doc };
  }

  try {
    if (req.method === "POST") {
      const b = await readBody(req);
      if (!(b && b.usd > 0 && b.ts > 0)) { res.statusCode = 400; return res.end(JSON.stringify({ error: "bad_baseline", message: "Faltan usd/ts." })); }
      const doc = {
        ts: Math.round(b.ts),                       // ms epoch del momento de la foto
        date: b.date || new Date(b.ts).toISOString().slice(0, 10),
        usd: Math.round(b.usd * 100) / 100,         // valor de las posiciones estables en ese momento
        btc: b.btc != null ? b.btc : null,          // lo mismo en BTC
        btcPrice: b.btcPrice != null ? b.btcPrice : null,
        scope: Array.isArray(b.scope) && b.scope.length ? b.scope : ["cbBTC / USDC"],
        note: String(b.note || "Fresh start del farming (solo pares con estable)").slice(0, 200),
      };
      const { sha } = await loadCurrent();
      const content = Buffer.from(JSON.stringify(doc, null, 2) + "\n", "utf8").toString("base64");
      const put = await fetch(contentsUrl, {
        method: "PUT",
        headers: gh({ "Content-Type": "application/json" }),
        body: JSON.stringify({ message: `baseline: fresh start ${doc.date} ($${doc.usd})`, content, sha: sha || undefined }),
      });
      if (!put.ok) { const t = await put.text().catch(() => ""); res.statusCode = put.status; return res.end(JSON.stringify({ error: "github_" + put.status, message: t.slice(0, 200) })); }
      return res.end(JSON.stringify({ ok: true, baseline: doc }));
    }

    const { doc } = await loadCurrent();
    res.setHeader("Cache-Control", "private, max-age=30");
    return res.end(JSON.stringify({ baseline: doc }));
  } catch (e) {
    res.statusCode = 502; return res.end(JSON.stringify({ error: "fetch_error", message: String((e && e.message) || e) }));
  }
};
