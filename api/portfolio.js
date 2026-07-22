// api/portfolio.js — estado ACTUAL de tus 2 wallets (Solana + EVM), con contraseña.
// Fuentes 100% GRATIS, sin API keys de pago:
//   · Solana: RPC público (o SOLANA_RPC_URL de Vercel si la pones — Helius free tier vale)
//   · EVM (Ethereum + Base): Blockscout público (trae precios USD de cada token)
//   · Precios BTC/SOL: Binance
// Las direcciones viven en el repo PRIVADO (data/wallets.json): {"solana":"...","evm":"..."}
// GET /api/portfolio  (cabecera x-dash-pw)  →  { solana:{...}, evm:{...}, prices:{...} }

const REPO = process.env.PRIVATE_REPO || "brovira/DeFi-Tracker";
const SOL_RPC = process.env.SOLANA_RPC_URL || "https://api.mainnet-beta.solana.com";
const KNOWN = { // mints de Solana que ya conocemos → se valoran con precio BTC/USDC
  "cbbtcf3aa214zXHbiAZQwf4122FBYbraNdFqgw4iMij": { sym: "cbBTC", kind: "btc" },
  "3NZ9JMVBmGAqocybic2c7LQCJScmgsAZ6vQqTDzcqmJh": { sym: "WBTC", kind: "btc" },
  "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v": { sym: "USDC", kind: "usd" },
};

function passwordOk(req, url, pass) {
  const given = req.headers["x-dash-pw"] || url.searchParams.get("pw") || "";
  return given.length === pass.length && (() => {
    let d = 0; for (let i = 0; i < pass.length; i++) d |= given.charCodeAt(i) ^ pass.charCodeAt(i); return d === 0;
  })();
}

async function ghFile(token, path) {
  const r = await fetch(`https://api.github.com/repos/${REPO}/contents/${path}`, {
    headers: { Authorization: `Bearer ${token}`, Accept: "application/vnd.github.raw+json", "User-Agent": "portfolio" },
  });
  if (!r.ok) return null;
  try { return JSON.parse(await r.text()); } catch (e) { return null; }
}

async function solRpc(method, params) {
  const r = await fetch(SOL_RPC, {
    method: "POST", headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ jsonrpc: "2.0", id: 1, method, params }),
  });
  if (!r.ok) throw new Error("sol_rpc_" + r.status);
  const j = await r.json();
  if (j.error) throw new Error("sol_rpc: " + (j.error.message || "error"));
  return j.result;
}

async function fetchSolana(addr, px) {
  const out = { address: addr, tokens: [], totalUsd: 0 };
  const bal = await solRpc("getBalance", [addr]);
  const sol = (bal && bal.value != null ? bal.value : 0) / 1e9;
  if (sol > 0) { const usd = sol * (px.SOL || 0); out.tokens.push({ sym: "SOL", amount: sol, usd }); out.totalUsd += usd; }
  for (const programId of ["TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA", "TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb"]) {
    try {
      const res = await solRpc("getTokenAccountsByOwner", [addr, { programId }, { encoding: "jsonParsed" }]);
      for (const acc of (res && res.value) || []) {
        const info = acc.account.data.parsed.info;
        const amt = info.tokenAmount.uiAmount;
        if (!amt || amt <= 0) continue;
        const mint = info.mint; const k = KNOWN[mint];
        if (k) {
          const usd = k.kind === "usd" ? amt : amt * (px.BTC || 0);
          out.tokens.push({ sym: k.sym, amount: amt, usd }); out.totalUsd += usd;
        } else if (info.tokenAmount.decimals === 0 && amt === 1) {
          out.nfts = (out.nfts || 0) + 1; // NFTs de posición (Orca) — se valoran en lp.html
        } else {
          out.tokens.push({ sym: mint.slice(0, 6) + "…", amount: amt, usd: null });
        }
      }
    } catch (e) { out.warning = String(e.message || e); }
  }
  out.tokens.sort((a, b) => (b.usd || 0) - (a.usd || 0));
  return out;
}

async function fetchEvmChain(base, chain, addr) {
  const out = { chain, tokens: [], totalUsd: 0 };
  try {
    const a = await fetch(`${base}/api/v2/addresses/${addr}`, { headers: { "User-Agent": "portfolio" } });
    if (a.ok) {
      const j = await a.json();
      const wei = +(j.coin_balance || 0); const eth = wei / 1e18;
      const rate = +(j.exchange_rate || 0);
      if (eth > 0) { const usd = eth * rate; out.tokens.push({ sym: chain === "base" ? "ETH (Base)" : "ETH", amount: eth, usd }); out.totalUsd += usd; }
    } else if (a.status !== 404) { out.warning = "blockscout_" + a.status; }
    const t = await fetch(`${base}/api/v2/addresses/${addr}/token-balances`, { headers: { "User-Agent": "portfolio" } });
    if (t.ok) {
      for (const row of await t.json()) {
        const tok = row.token || {}; const dec = +(tok.decimals || 18);
        const amt = +(row.value || 0) / Math.pow(10, dec);
        if (!amt || amt <= 0 || tok.type !== "ERC-20") continue;
        const rate = tok.exchange_rate != null ? +tok.exchange_rate : null;
        const usd = rate != null ? amt * rate : null;
        // sin precio conocido y polvo → fuera (los airdrops-spam de EVM son infinitos)
        if (usd == null && amt < 1e12) continue;
        out.tokens.push({ sym: tok.symbol || "?", amount: amt, usd });
        if (usd) out.totalUsd += usd;
      }
    }
  } catch (e) { out.warning = String(e.message || e); }
  out.tokens.sort((a, b) => (b.usd || 0) - (a.usd || 0));
  return out;
}

async function fetchPrices() {
  const px = { USDC: 1 };
  for (const [sym, pair] of [["BTC", "BTCUSDT"], ["SOL", "SOLUSDT"]]) {
    for (const h of ["api.binance.com", "api.binance.us"]) {
      try { const r = await fetch(`https://${h}/api/v3/ticker/price?symbol=${pair}`); if (r.ok) { px[sym] = +(await r.json()).price; break; } } catch (e) {}
    }
  }
  return px;
}

module.exports = async (req, res) => {
  res.setHeader("Content-Type", "application/json; charset=utf-8");
  const url = new URL(req.url, "http://x");
  const pass = process.env.DASH_PASSWORD; const token = process.env.GH_TOKEN;
  if (!pass) { res.statusCode = 503; return res.end(JSON.stringify({ error: "no_password" })); }
  if (!passwordOk(req, url, pass)) { await new Promise(r => setTimeout(r, 600)); res.statusCode = 401; return res.end(JSON.stringify({ error: "bad_password" })); }
  if (!token) { res.statusCode = 503; return res.end(JSON.stringify({ error: "no_github_token" })); }

  try {
    const wallets = (await ghFile(token, "data/wallets.json")) || {};
    if (!wallets.solana && !wallets.evm) {
      return res.end(JSON.stringify({ error: "no_wallets", message: "Rellena data/wallets.json en el repo privado: {\"solana\":\"...\",\"evm\":\"...\"}" }));
    }
    const px = await fetchPrices();
    const [sol, eth, base] = await Promise.all([
      wallets.solana ? fetchSolana(wallets.solana, px).catch(e => ({ error: String(e.message || e) })) : null,
      wallets.evm ? fetchEvmChain("https://eth.blockscout.com", "ethereum", wallets.evm).catch(e => ({ error: String(e.message || e) })) : null,
      wallets.evm ? fetchEvmChain("https://base.blockscout.com", "base", wallets.evm).catch(e => ({ error: String(e.message || e) })) : null,
    ]);
    res.setHeader("Cache-Control", "private, max-age=120");
    return res.end(JSON.stringify({ prices: px, solana: sol, evm: { ethereum: eth, base } }));
  } catch (e) {
    res.statusCode = 502; return res.end(JSON.stringify({ error: "fetch_error", message: String((e && e.message) || e) }));
  }
};
