const crypto = require("crypto");

function safeEqual(a, b) {
  const left = Buffer.from(String(a || ""));
  const right = Buffer.from(String(b || ""));
  return left.length === right.length && crypto.timingSafeEqual(left, right);
}

function cookie(req, name) {
  const raw = (req.headers && req.headers.cookie) || "";
  for (const part of raw.split(/;\s*/)) {
    const at = part.indexOf("=");
    if (at > 0 && part.slice(0, at) === name) return part.slice(at + 1);
  }
  return "";
}

function siteToken(pass) {
  return crypto.createHash("sha256").update("btc-terminal::" + pass).digest("hex");
}

function localRequest(req) {
  const host = String((req.headers && req.headers.host) || "").split(":")[0].replace(/^\[|\]$/g, "");
  return Boolean(process.env.LOCAL_DATA_DIR) && (host === "localhost" || host === "127.0.0.1" || host === "::1");
}

function authConfigured(req) {
  return localRequest(req) || Boolean(process.env.SITE_PASSWORD || process.env.DASH_PASSWORD);
}

function requestAuthorized(req, url) {
  if (localRequest(req)) return true;
  const dashboardPass = process.env.DASH_PASSWORD || process.env.SITE_PASSWORD || "";
  const given = req.headers["x-dash-pw"] || url.searchParams.get("pw") || "";
  if (dashboardPass && safeEqual(given, dashboardPass)) return true;

  const sitePass = process.env.SITE_PASSWORD || process.env.DASH_PASSWORD || "";
  return Boolean(sitePass) && safeEqual(cookie(req, "site_auth"), siteToken(sitePass));
}

module.exports = { authConfigured, requestAuthorized };
