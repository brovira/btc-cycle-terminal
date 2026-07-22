const fs = require("fs");
const http = require("http");
const path = require("path");

const ROOT = __dirname;
const PORT = Number(process.env.PORT || process.argv[2] || 8000);
const LOCAL_DATA = process.env.LOCAL_DATA_DIR || path.resolve(ROOT, "../DeFi-Tracker-main/data");
const LOCAL_CASHFLOW = process.env.LOCAL_CASHFLOW_FILE || path.join(ROOT, ".local/cashflow.json");

if (fs.existsSync(LOCAL_DATA)) process.env.LOCAL_DATA_DIR = LOCAL_DATA;
if (fs.existsSync(LOCAL_CASHFLOW)) process.env.LOCAL_CASHFLOW_FILE = LOCAL_CASHFLOW;

const API = new Set(["baseline", "birdeye", "cashflow", "coinglass", "coinmetrics", "journal", "portfolio", "private"]);
const MIME = {
  ".css": "text/css; charset=utf-8",
  ".csv": "text/csv; charset=utf-8",
  ".html": "text/html; charset=utf-8",
  ".ico": "image/x-icon",
  ".js": "text/javascript; charset=utf-8",
  ".json": "application/json; charset=utf-8",
  ".md": "text/markdown; charset=utf-8",
  ".png": "image/png",
  ".svg": "image/svg+xml",
};

function send(res, status, body, type = "text/plain; charset=utf-8") {
  res.statusCode = status;
  res.setHeader("Content-Type", type);
  res.setHeader("Cache-Control", "no-store");
  res.end(body);
}

async function serveApi(req, res, name) {
  if (!API.has(name)) return send(res, 404, JSON.stringify({ error: "api_not_found" }), MIME[".json"]);
  try {
    const handler = require(path.join(ROOT, "api", name + ".js"));
    await handler(req, res);
  } catch (e) {
    if (!res.headersSent) res.setHeader("Content-Type", MIME[".json"]);
    res.statusCode = 500;
    res.end(JSON.stringify({ error: "local_api", message: String((e && e.message) || e) }));
  }
}

async function serveStatic(req, res, pathname) {
  let decoded;
  try { decoded = decodeURIComponent(pathname); }
  catch (e) { return send(res, 400, "Bad request"); }
  if (decoded === "/") decoded = "/index.html";
  const file = path.resolve(ROOT, "." + decoded);
  if (!file.startsWith(ROOT + path.sep)) return send(res, 403, "Forbidden");
  try {
    const stat = await fs.promises.stat(file);
    if (!stat.isFile()) return send(res, 404, "Not found");
    res.statusCode = 200;
    res.setHeader("Content-Type", MIME[path.extname(file).toLowerCase()] || "application/octet-stream");
    res.setHeader("Cache-Control", "no-store");
    if (req.method === "HEAD") return res.end();
    fs.createReadStream(file).pipe(res);
  } catch (e) {
    return send(res, e && e.code === "ENOENT" ? 404 : 500, e && e.code === "ENOENT" ? "Not found" : "Server error");
  }
}

const server = http.createServer(async (req, res) => {
  const url = new URL(req.url, `http://${req.headers.host || "localhost"}`);
  const match = url.pathname.match(/^\/api\/([a-z0-9_-]+)\/?$/i);
  if (match) return serveApi(req, res, match[1].toLowerCase());
  if (req.method !== "GET" && req.method !== "HEAD") return send(res, 405, "Method not allowed");
  return serveStatic(req, res, url.pathname);
});

server.on("error", (e) => {
  if (e && e.code === "EADDRINUSE") {
    console.error(`El puerto ${PORT} ya está ocupado. Cierra el servidor anterior o usa: npm run dev -- 8001`);
  } else console.error(e);
  process.exitCode = 1;
});

server.listen(PORT, "127.0.0.1", () => {
  console.log(`BTC Terminal local: http://localhost:${PORT}`);
  console.log(`APIs locales: activas · contraseña: desactivada en localhost`);
  console.log(`Datos privados: ${process.env.LOCAL_DATA_DIR || "no encontrados"}`);
  console.log(`Cashflow local: ${process.env.LOCAL_CASHFLOW_FILE || "no encontrado"}`);
});
