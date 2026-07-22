// api/portfolio.js — estado ACTUAL de tus 2 wallets (Solana + EVM), con contraseña.
// Fuentes 100% GRATIS, sin API keys de pago:
//   · Solana: RPC público (o SOLANA_RPC_URL de Vercel si la pones — Helius free tier vale)
//   · EVM (Ethereum + Base): Blockscout público (trae precios USD de cada token)
//   · Precios BTC/SOL: Binance
// Las direcciones viven en el repo PRIVADO (data/wallets.json): {"solana":"...","evm":"..."}
// GET /api/portfolio  →  { solana:{...}, evm:{...}, prices:{...} }

const { authConfigured, requestAuthorized } = require("../lib/auth");
const fs = require("fs");
const pathLib = require("path");
const REPO = process.env.PRIVATE_REPO || "brovira/DeFi-Tracker";
const SOL_RPC = process.env.SOLANA_RPC_URL || "https://api.mainnet-beta.solana.com";
const KNOWN = { // mints de Solana que ya conocemos → se valoran con precio BTC/USDC
  "cbbtcf3aa214zXHbiAZQwf4122FBYbraNdFqgw4iMij": { sym: "cbBTC", kind: "btc" },
  "3NZ9JMVBmGAqocybic2c7LQCJScmgsAZ6vQqTDzcqmJh": { sym: "WBTC", kind: "btc" },
  "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v": { sym: "USDC", kind: "usd" },
};

async function ghFile(token, path) {
  if (process.env.LOCAL_DATA_DIR) {
    try {
      const localPath = pathLib.join(process.env.LOCAL_DATA_DIR, path.replace(/^data\//, ""));
      return JSON.parse(await fs.promises.readFile(localPath, "utf8"));
    } catch (e) { return null; }
  }
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

/* Jupiter (gratis, sin key): precio y metadata de CUALQUIER token de Solana por mint.
   Sustituye la lista fija de 3 mints — así aparecen JUP, KMNO, MELANIA, etc. solos. */
async function jupiterPrices(mints) {
  if (!mints.length) return {};
  try {
    const r = await fetch(`https://api.jup.ag/price/v2?ids=${mints.map(encodeURIComponent).join(",")}`, { headers: { "User-Agent": "portfolio" } });
    if (!r.ok) return {};
    const j = await r.json(); const out = {};
    for (const m of mints) { const d = j.data && j.data[m]; if (d && d.price != null) out[m] = +d.price; }
    return out;
  } catch (e) { return {}; }
}
async function jupiterMeta(mint) {
  try {
    const r = await fetch(`https://tokens.jup.ag/token/${mint}`, { headers: { "User-Agent": "portfolio" } });
    if (r.ok) { const j = await r.json(); if (j && j.symbol) return j.symbol; }
  } catch (e) {}
  return null;
}

async function fetchSolana(addr, px) {
  const out = { address: addr, tokens: [], totalUsd: 0 };
  const bal = await solRpc("getBalance", [addr]);
  const sol = (bal && bal.value != null ? bal.value : 0) / 1e9;
  if (sol > 0) { const usd = sol * (px.SOL || 0); out.tokens.push({ sym: "SOL", amount: sol, usd }); out.totalUsd += usd; }
  const unknown = []; // {mint, amount} — tokens fuera de la lista KNOWN (cbBTC/WBTC/USDC)
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
          unknown.push({ mint, amount: amt });
        }
      }
    } catch (e) { out.warning = String(e.message || e); }
  }
  if (unknown.length) {
    const mints = [...new Set(unknown.map(u => u.mint))];
    const [prices, metaPairs] = await Promise.all([
      jupiterPrices(mints),
      Promise.all(mints.map(m => jupiterMeta(m).then(sym => [m, sym]))),
    ]);
    const metaMap = Object.fromEntries(metaPairs);
    for (const u of unknown) {
      const price = prices[u.mint];
      if (price == null) continue; // sin precio en Jupiter = sin liquidez real → probable spam/polvo, se descarta
      const usd = u.amount * price;
      out.tokens.push({ sym: metaMap[u.mint] || (u.mint.slice(0, 6) + "…"), amount: u.amount, usd });
      out.totalUsd += usd;
    }
  }
  out.tokens.sort((a, b) => (b.usd || 0) - (a.usd || 0));
  return out;
}

async function fetchEvmChain(base, chain, addr) {
  const out = { chain, tokens: [], totalUsd: 0, hidden: 0 };
  try {
    const a = await fetch(`${base}/api/v2/addresses/${addr}`, { headers: { "User-Agent": "portfolio" } });
    if (a.ok) {
      const j = await a.json();
      const wei = +(j.coin_balance || 0); const eth = wei / 1e18;
      const rate = +(j.exchange_rate || 0);
      const nativeSym = chain === "hyperevm" ? "HYPE" : chain === "polygon" ? "POL" : "ETH";
      if (eth > 0) { const usd = eth * rate; out.tokens.push({ sym: nativeSym, amount: eth, usd: usd || null }); if (usd) out.totalUsd += usd; }
    } else if (a.status !== 404) { out.warning = "blockscout_" + a.status; }
    const t = await fetch(`${base}/api/v2/addresses/${addr}/token-balances`, { headers: { "User-Agent": "portfolio" } });
    if (t.ok) {
      for (const row of await t.json()) {
        const tok = row.token || {}; const dec = +(tok.decimals || 18);
        const amt = +(row.value || 0) / Math.pow(10, dec);
        if (!amt || amt <= 0 || tok.type !== "ERC-20") continue;
        // ANTI-SPAM: token "legítimo" si tiene market cap real EN Blockscout, o si no lo
        // tiene pero el precio existe y la cantidad es razonable (spam suele mandar
        // cantidades absurdas, billones/trillones de unidades, para inflar un precio falso).
        const hasMcap = tok.circulating_market_cap != null && +tok.circulating_market_cap > 0;
        const rate = tok.exchange_rate != null ? +tok.exchange_rate : null;
        const plausible = rate != null && (hasMcap || amt < 1e9);
        const usd = plausible ? amt * rate : null;
        if (usd == null) { out.hidden++; continue; } // sin precio fiable → fuera (spam/ilíquido)
        out.tokens.push({ sym: tok.symbol || "?", amount: amt, usd });
        out.totalUsd += usd;
      }
    }
  } catch (e) { out.warning = String(e.message || e); }
  out.tokens.sort((a, b) => (b.usd || 0) - (a.usd || 0));
  return out;
}

/* ---- Posiciones V3 (Uniswap en ETH, ProjectX en HyperEVM, cualquier fork estilo V3) ----
   Para protocolos conocidos se enumeran sus NFTs directamente en el position manager.
   Para forks desconocidos se usa la lista paginada de ERC-721 de Blockscout y se prueba
   positions(tokenId). El pool sale de factory()+getPool() y el precio actual de slot0(). */
const ETH_RPCS = ["https://eth.blockscout.com/api/eth-rpc", "https://eth.llamarpc.com", "https://cloudflare-eth.com", "https://rpc.ankr.com/eth"];
const HYPE_RPCS = ["https://rpc.hyperliquid.xyz/evm"];
const UNISWAP_V3_POSITION_MANAGER = "0xC36442b4a4522E871399CD717aBDD847Ab11FE88";
const PROJECTX_POSITION_MANAGER = "0xeaD19AE861c29bBb2101E834922B2FEee69B9091";
const TOPIC_INCREASE = "0x3067048beee31b25b2f1681f88dac838c8bba36af25bfb2b7cf7473a5847e35f";
const TOPIC_DECREASE = "0x26f6a048ee9138f2c0ce266f322cb99228e8d619ae2bff30c67f8dcf9d2377b4";
const TOPIC_COLLECT = "0x40d0efd1a53d60ecbf40971b9daf7dc90178c3aadc7aab1765632738fa8b8f01";
const MAX_UINT128 = "f".repeat(32);
const HISTORICAL_PRICE_CACHE = new Map();
const POSITION_HISTORY_CACHE = new Map();
const pad = (h) => h.replace(/^0x/, "").padStart(64, "0");
const word = (hex, i) => BigInt("0x" + (hex.replace(/^0x/, "").slice(i * 64, i * 64 + 64) || "0"));
const toInt = (v) => (v > (1n << 255n) ? v - (1n << 256n) : v);
async function rpcRequest(rpcs, method, params) {
  for (const rpc of rpcs) {
    try {
      const r = await fetch(rpc, { method: "POST", headers: { "Content-Type": "application/json", "User-Agent": "portfolio" },
        body: JSON.stringify({ jsonrpc: "2.0", id: 1, method, params }) });
      if (!r.ok) continue;
      const j = await r.json();
      if (j.result != null) return j.result;
    } catch (e) {}
  }
  return null;
}
function rpcCaller(rpcs) {
  return async (to, data, from) => {
    const tx = { to, data };
    if (from) tx.from = from;
    const result = await rpcRequest(rpcs, "eth_call", [tx, "latest"]);
    return result && result !== "0x" ? result : null;
  };
}
function decodeRpcString(hex) {
  const raw = (hex || "").replace(/^0x/, "");
  if (!raw) return "?";
  try {
    const offset = Number(BigInt("0x" + raw.slice(0, 64)));
    if (offset === 32) {
      const length = Number(BigInt("0x" + raw.slice(64, 128)));
      return Buffer.from(raw.slice(128, 128 + length * 2), "hex").toString("utf8") || "?";
    }
    return Buffer.from(raw.slice(0, 64).replace(/00+$/, ""), "hex").toString("utf8") || "?";
  } catch (e) { return "?"; }
}

async function tokenInfo(baseUrl, address, call) {
  try { const r = await fetch(`${baseUrl}/api/v2/tokens/${address}`, { headers: { "User-Agent": "portfolio" } });
    if (r.ok) { const j = await r.json(); return { sym: j.symbol || "?", dec: +(j.decimals || 18), px: j.exchange_rate != null ? +j.exchange_rate : null }; } } catch (e) {}
  if (call) {
    try {
      const [symbol, decimals] = await Promise.all([call(address, "0x95d89b41"), call(address, "0x313ce567")]);
      return { sym: decodeRpcString(symbol), dec: decimals ? Number(word(decimals, 0)) : 18, px: null };
    } catch (e) {}
  }
  return { sym: "?", dec: 18, px: null };
}

function isUsdStable(symbol) {
  return (symbol || "").toUpperCase().replace(/[^A-Z0-9]/g, "").startsWith("USD");
}

function marketPair(symbol) {
  const sym = (symbol || "").toUpperCase().replace(/[^A-Z0-9]/g, "");
  if (isUsdStable(sym)) return "USD";
  if (["BTC", "WBTC", "CBBTC", "UBTC"].includes(sym)) return "BTCUSDT";
  if (["ETH", "WETH"].includes(sym)) return "ETHUSDT";
  if (sym === "BNB") return "BNBUSDT";
  return null;
}

async function historicalUsdPrice(symbol, timestamp) {
  const pair = marketPair(symbol);
  if (pair === "USD") return 1;
  const minute = Math.floor(timestamp / 60000) * 60000;
  const key = `${pair || symbol}:${minute}`;
  if (!HISTORICAL_PRICE_CACHE.has(key)) {
    HISTORICAL_PRICE_CACHE.set(key, (async () => {
      if (pair) {
        for (const host of ["api.binance.com", "api.binance.us"]) {
          try {
            const r = await fetch(`https://${host}/api/v3/klines?symbol=${pair}&interval=1m&startTime=${minute}&limit=1`, { headers: { "User-Agent": "portfolio" } });
            if (!r.ok) continue;
            const rows = await r.json();
            if (Array.isArray(rows) && rows[0] && +rows[0][4] > 0) return +rows[0][4];
          } catch (e) {}
        }
      }
      if ((symbol || "").toUpperCase() === "HYPE") {
        try {
          const from = Math.floor(timestamp / 1000) - 3600;
          const to = Math.floor(timestamp / 1000) + 3600;
          const r = await fetch(`https://api.coingecko.com/api/v3/coins/hyperliquid/market_chart/range?vs_currency=usd&from=${from}&to=${to}`, { headers: { "User-Agent": "portfolio" } });
          if (r.ok) {
            const prices = (await r.json()).prices || [];
            prices.sort((a, b) => Math.abs(a[0] - timestamp) - Math.abs(b[0] - timestamp));
            if (prices[0] && +prices[0][1] > 0) return +prices[0][1];
          }
        } catch (e) {}
      }
      return null;
    })());
  }
  return HISTORICAL_PRICE_CACHE.get(key);
}

async function discoverPositionMint(baseUrl, manager, tokenId, network) {
  if (network === "HyperEVM") {
    const r = await fetch(`https://hyperevmscan.io/nft/${manager}/${tokenId}`, { headers: { "User-Agent": "portfolio" } });
    if (!r.ok) return null;
    const html = await r.text();
    const match = html.match(/var\s+dt_Data\s*=\s*(\[[\s\S]*?\]);/);
    if (!match) return null;
    const row = JSON.parse(match[1]).find(x => String(x.action) === "0" || String(x._from || "").toLowerCase() === "0x0000000000000000000000000000000000000000");
    if (!row) return null;
    return { hash: row.txhash, block: +row.blockNumber, timestamp: Date.parse(String(row.dt).replace(" ", "T") + "Z") };
  }
  const r = await fetch(`${baseUrl}/api/v2/tokens/${manager}/instances/${tokenId}/transfers`, { headers: { "User-Agent": "portfolio" } });
  if (!r.ok) return null;
  const body = await r.json();
  const row = (body.items || []).find(x => x.type === "token_minting" || String(x.from && x.from.hash).toLowerCase() === "0x0000000000000000000000000000000000000000");
  return row ? { hash: row.transaction_hash, block: +row.block_number, timestamp: Date.parse(row.timestamp) } : null;
}

async function recentManagerTransactions(baseUrl, owner, manager, network) {
  if (network === "HyperEVM") {
    const r = await fetch(`https://hyperevmscan.io/txs?a=${owner}&ps=100&p=1`, { headers: { "User-Agent": "portfolio" } });
    if (!r.ok) return { rows: [], oldestBlock: null };
    const html = await r.text();
    const rows = [];
    const blocks = [];
    for (const match of html.matchAll(/<tr\b[\s\S]*?<\/tr>/gi)) {
      const row = match[0];
      const block = +(row.match(/href=["']\/block\/(\d+)["']/i) || [])[1];
      if (block > 0) blocks.push(block);
      if (!row.toLowerCase().includes(manager.toLowerCase())) continue;
      const hash = (row.match(/href=["']\/tx\/(0x[0-9a-f]{64})["']/i) || [])[1];
      const timestamp = +((row.match(/showLocalDate[\s\S]*?>(\d{10})<\/span>/i) || [])[1]) * 1000;
      if (hash && block) rows.push({ hash, block, timestamp: timestamp || null });
    }
    return { rows, oldestBlock: blocks.length ? Math.min(...blocks) : null };
  }
  const r = await fetch(`${baseUrl}/api/v2/addresses/${owner}/transactions`, { headers: { "User-Agent": "portfolio" } });
  if (!r.ok) return { rows: [], oldestBlock: null };
  const body = await r.json();
  const all = body.items || [];
  const rows = all.filter(x => String(x.to && x.to.hash).toLowerCase() === manager.toLowerCase())
    .map(x => ({ hash: x.hash, block: +x.block_number, timestamp: Date.parse(x.timestamp) }));
  const blocks = all.map(x => +x.block_number).filter(Boolean);
  return { rows, oldestBlock: blocks.length ? Math.min(...blocks) : null };
}

function decodeLiquidityEvent(log, tokenId, dec0, dec1) {
  if (!log || !log.topics || log.topics.length < 2) return null;
  try { if (word(log.topics[1], 0).toString() !== String(tokenId)) return null; } catch (e) { return null; }
  const topic = String(log.topics[0]).toLowerCase();
  if (![TOPIC_INCREASE, TOPIC_DECREASE, TOPIC_COLLECT].includes(topic)) return null;
  return {
    type: topic === TOPIC_INCREASE ? "increase" : topic === TOPIC_DECREASE ? "decrease" : "collect",
    amount0: Number(word(log.data, 1)) / Math.pow(10, dec0),
    amount1: Number(word(log.data, 2)) / Math.pow(10, dec1),
  };
}

async function pendingPositionCollect(call, manager, tokenId, owner, token0, token1, px0, px1) {
  const data = "0xfc6f7865" + pad(BigInt(tokenId).toString(16)) + pad(owner) + pad(MAX_UINT128) + pad(MAX_UINT128);
  const result = await call(manager, data, owner);
  if (!result) return null;
  const amount0 = Number(word(result, 0)) / Math.pow(10, token0.dec);
  const amount1 = Number(word(result, 1)) / Math.pow(10, token1.dec);
  return { amount0, amount1, usd: (px0 != null ? amount0 * px0 : 0) + (px1 != null ? amount1 * px1 : 0) };
}

async function fetchPositionHistory({ baseUrl, rpcs, call, owner, manager, tokenId, network, token0, token1, currentUsd, px0, px1 }) {
  const [mint, recent, pending] = await Promise.all([
    discoverPositionMint(baseUrl, manager, tokenId, network),
    recentManagerTransactions(baseUrl, owner, manager, network),
    pendingPositionCollect(call, manager, tokenId, owner, token0, token1, px0, px1),
  ]);
  if (!mint) return null;
  const txRows = recent.rows.filter(x => x.block >= mint.block);
  if (!txRows.some(x => x.hash.toLowerCase() === mint.hash.toLowerCase())) txRows.push(mint);
  const receipts = await Promise.all(txRows.map(async row => ({
    ...row,
    receipt: await rpcRequest(rpcs, "eth_getTransactionReceipt", [row.hash]),
  })));
  receipts.sort((a, b) => a.block - b.block);

  let deposited0 = 0, deposited1 = 0, investedUsd = 0, withdrawnUsd = 0;
  let claimedFeesUsd = 0, gasUsd = 0, gasComplete = true, owed0 = 0, owed1 = 0;
  let entryCost0 = 0, entryCost1 = 0, openedAt = mint.timestamp;
  const nativeSymbol = network === "Ethereum" ? "ETH" : network === "HyperEVM" ? "HYPE" : null;
  const events = [];
  for (const tx of receipts) {
    if (!tx.receipt) continue;
    let timestamp = tx.timestamp || null;
    if (!timestamp) {
      const block = await rpcRequest(rpcs, "eth_getBlockByNumber", [tx.receipt.blockNumber, false]);
      if (block && block.timestamp) timestamp = Number(BigInt(block.timestamp)) * 1000;
    }
    const decoded = (tx.receipt.logs || [])
      .filter(log => String(log.address).toLowerCase() === manager.toLowerCase())
      .map(log => decodeLiquidityEvent(log, tokenId, token0.dec, token1.dec)).filter(Boolean);
    if (!decoded.length) continue;
    const [eventPx0, eventPx1, nativePx] = await Promise.all([
      historicalUsdPrice(token0.sym, timestamp), historicalUsdPrice(token1.sym, timestamp),
      nativeSymbol ? historicalUsdPrice(nativeSymbol, timestamp) : null,
    ]);
    for (const event of decoded) {
      events.push({ type: event.type, timestamp, amount0: event.amount0, amount1: event.amount1 });
      if (event.type === "increase") {
        deposited0 += event.amount0; deposited1 += event.amount1;
        if (eventPx0 == null || eventPx1 == null) return null;
        const cost0 = event.amount0 * eventPx0, cost1 = event.amount1 * eventPx1;
        investedUsd += cost0 + cost1; entryCost0 += cost0; entryCost1 += cost1;
        if (!openedAt || timestamp < openedAt) openedAt = timestamp;
      } else if (event.type === "decrease") {
        owed0 += event.amount0; owed1 += event.amount1;
      } else {
        if (eventPx0 == null || eventPx1 == null) return null;
        withdrawnUsd += event.amount0 * eventPx0 + event.amount1 * eventPx1;
        const principal0 = Math.min(owed0, event.amount0), principal1 = Math.min(owed1, event.amount1);
        claimedFeesUsd += (event.amount0 - principal0) * eventPx0 + (event.amount1 - principal1) * eventPx1;
        owed0 -= principal0; owed1 -= principal1;
      }
    }
    const gasNative = Number(BigInt(tx.receipt.gasUsed || "0x0") * BigInt(tx.receipt.effectiveGasPrice || "0x0")) / 1e18;
    if (gasNative > 0) {
      if (nativePx != null) gasUsd += gasNative * nativePx;
      else gasComplete = false;
    }
  }
  if (!(investedUsd > 0) || !openedAt) return null;
  const pendingAmount0 = pending ? Math.max(0, pending.amount0 - owed0) : 0;
  const pendingAmount1 = pending ? Math.max(0, pending.amount1 - owed1) : 0;
  const pendingFeesUsd = (px0 != null ? pendingAmount0 * px0 : 0) + (px1 != null ? pendingAmount1 * px1 : 0);
  const pendingCollectUsd = pending ? pending.usd : 0;
  const feesUsd = claimedFeesUsd + pendingFeesUsd;
  const pnlUsd = (currentUsd || 0) + withdrawnUsd + pendingCollectUsd - investedUsd - gasUsd;
  const durationDays = Math.max((Date.now() - openedAt) / 86400000, 1 / 24);
  const entryPrices = [];
  if (!isUsdStable(token0.sym) && deposited0 > 0) entryPrices.push({ symbol: token0.sym === "WETH" ? "ETH" : token0.sym, priceUsd: entryCost0 / deposited0 });
  if (!isUsdStable(token1.sym) && deposited1 > 0) entryPrices.push({ symbol: token1.sym === "WETH" ? "ETH" : token1.sym, priceUsd: entryCost1 / deposited1 });
  return {
    openedAt, durationDays, deposited0, deposited1, investedUsd, withdrawnUsd,
    claimedFeesUsd, pendingFeesUsd, feesUsd, gasUsd: gasComplete ? gasUsd : null,
    pnlUsd, pnlPct: pnlUsd / investedUsd * 100,
    annualizedYieldPct: feesUsd / investedUsd * 365 / durationDays * 100,
    entryPrices, events,
    complete: recent.oldestBlock != null && recent.oldestBlock <= mint.block,
  };
}

async function cachedPositionHistory(args) {
  const key = `${args.network}:${String(args.manager).toLowerCase()}:${args.tokenId}`;
  const cached = POSITION_HISTORY_CACHE.get(key);
  if (cached && Date.now() - cached.createdAt < 120000) return cached.promise;
  const promise = fetchPositionHistory(args).catch(error => {
    POSITION_HISTORY_CACHE.delete(key);
    throw error;
  });
  POSITION_HISTORY_CACHE.set(key, { createdAt: Date.now(), promise });
  return promise;
}

function nftContract(item) {
  return (((item.token && (item.token.address_hash || item.token.address)) || "") + "").toLowerCase();
}

async function ownedPositionNfts(call, addr, managers) {
  const items = [];
  let checked = false;
  for (const manager of managers) {
    const balance = await call(manager, "0x70a08231" + pad(addr)); // balanceOf(address)
    if (!balance) continue;
    checked = true;
    const count = Number(word(balance, 0));
    for (let i = 0; i < Math.min(count, 100); i++) {
      const tokenId = await call(manager, "0x2f745c59" + pad(addr) + pad(BigInt(i).toString(16))); // tokenOfOwnerByIndex
      if (tokenId) items.push({ id: word(tokenId, 0).toString(), token: { address_hash: manager } });
    }
  }
  return { items, checked };
}

async function blockscoutNfts(baseUrl, addr, wantedContracts = []) {
  const endpoint = `${baseUrl}/api/v2/addresses/${addr}/nft`;
  const wanted = new Set(wantedContracts.map(x => x.toLowerCase()));
  const items = [];
  let params = { type: "ERC-721" };
  for (let page = 0; page < 10; page++) {
    const url = new URL(endpoint);
    for (const [key, value] of Object.entries(params)) {
      if (value != null) url.searchParams.set(key, String(value));
    }
    const r = await fetch(url, { headers: { "User-Agent": "portfolio" } });
    if (!r.ok) break;
    const body = await r.json();
    const pageItems = (body.items || []).filter(it => it.id != null);
    const matches = wanted.size ? pageItems.filter(it => wanted.has(nftContract(it))) : pageItems;
    items.push(...matches);
    if (!body.next_page_params || !Object.keys(body.next_page_params).length) break;
    params = { type: "ERC-721", ...body.next_page_params };
  }
  return items;
}

function displayPriceRange(sp, spa, spb, token0, token1) {
  const scale = Math.pow(10, token0.dec - token1.dec);
  let currentPrice = sp * sp * scale;
  let priceLow = spa * spa * scale;
  let priceHigh = spb * spb * scale;
  let base = token0.sym;
  let quote = token1.sym;
  if (currentPrice < 1) {
    currentPrice = 1 / currentPrice;
    const inverseLow = 1 / priceHigh;
    priceHigh = 1 / priceLow;
    priceLow = inverseLow;
    base = token1.sym;
    quote = token0.sym;
  }
  return { priceLow, priceHigh, currentPrice, base, quote };
}

async function fetchV3Positions(baseUrl, rpcs, addr, protoLabel, knownManagers = [], network = "EVM") {
  const out = { positions: [], totalUsd: 0, protocol: protoLabel };
  const call = rpcCaller(rpcs);
  try {
    const direct = knownManagers.length ? await ownedPositionNfts(call, addr, knownManagers) : { items: [], checked: false };
    const items = direct.checked
      ? direct.items
      : await blockscoutNfts(baseUrl, addr, knownManagers);
    for (const it of items.slice(0, knownManagers.length ? 100 : 15)) {
      const npm = nftContract(it);
      if (!npm) continue;
      const pos = await call(npm, "0x99fbab88" + pad(BigInt(it.id).toString(16)));
      if (!pos || pos.replace(/^0x/, "").length < 64 * 12) continue; // no es un position manager V3
      const token0 = "0x" + pos.replace(/^0x/, "").slice(2 * 64 + 24, 3 * 64);
      const token1 = "0x" + pos.replace(/^0x/, "").slice(3 * 64 + 24, 4 * 64);
      const fee = Number(word(pos, 4));
      const tl = Number(toInt(word(pos, 5))), tu = Number(toInt(word(pos, 6)));
      const L = Number(word(pos, 7));
      if (!(L > 0) || !(tl < tu)) continue; // vacía/cerrada o layout raro
      const factoryRes = await call(npm, "0xc45a0155"); // factory()
      if (!factoryRes) continue;
      const factory = "0x" + factoryRes.replace(/^0x/, "").slice(-40);
      const pool = await call(factory, "0x1698ee82" + pad(token0) + pad(token1) + pad(fee.toString(16)));
      if (!pool) continue;
      const slot0 = await call("0x" + pool.replace(/^0x/, "").slice(-40), "0x3850c7bd");
      if (!slot0) continue;
      const sp = Number(word(slot0, 0)) / Math.pow(2, 96); // sqrt(price) actual
      if (!(sp > 0)) continue;
      const spa = Math.pow(1.0001, tl / 2), spb = Math.pow(1.0001, tu / 2);
      const spc = Math.min(Math.max(sp, spa), spb);
      const a0 = L * (spb - spc) / (spc * spb), a1 = L * (spc - spa);
      const [t0, t1] = await Promise.all([tokenInfo(baseUrl, token0, call), tokenInfo(baseUrl, token1, call)]);
      const amt0 = a0 / Math.pow(10, t0.dec), amt1 = a1 / Math.pow(10, t1.dec);
      const currentRaw = sp * sp * Math.pow(10, t0.dec - t1.dec);
      let px0 = isUsdStable(t0.sym) ? 1 : t0.px;
      let px1 = isUsdStable(t1.sym) ? 1 : t1.px;
      if (px0 == null && px1 != null) px0 = currentRaw * px1;
      if (px1 == null && px0 != null) px1 = px0 / currentRaw;
      const usd = (px0 != null ? amt0 * px0 : 0) + (px1 != null ? amt1 * px1 : 0);
      const priced = px0 != null && px1 != null;
      const range = displayPriceRange(sp, spa, spb, t0, t1);
      const position = { id: String(it.id), pair: `${t0.sym}/${t1.sym}`, fee: fee / 10000 + "%",
        amt0, amt1, sym0: t0.sym, sym1: t1.sym, usd: priced ? usd : (usd || null),
        price0: px0, price1: px1, inRange: sp >= spa && sp <= spb, range, protocol: protoLabel, network };
      position.history = await cachedPositionHistory({ baseUrl, rpcs, call, owner: addr, manager: npm,
        tokenId: it.id, network, token0: t0, token1: t1, currentUsd: position.usd, px0, px1 }).catch(() => null);
      out.positions.push(position);
      if (usd) out.totalUsd += usd;
    }
  } catch (e) { out.warning = String(e.message || e); }
  return out;
}

/* ---- Kamino Lend (Solana): depósitos-préstamos del usuario vía su API pública ---- */
const KAMINO_MARKETS = ["7u3HeHxYDLhnCoErrtycNokbQYbWGzLs6JSDqGAv5PfF"]; // main market
async function fetchKamino(addr) {
  const out = { usd: 0, detail: [], ok: false };
  try {
    for (const mkt of KAMINO_MARKETS) {
      const r = await fetch(`https://api.kamino.finance/kamino-market/${mkt}/users/${addr}/obligations`, { headers: { "User-Agent": "portfolio" } });
      if (!r.ok) { out.warning = "kamino_" + r.status; continue; }
      const arr = await r.json();
      for (const ob of Array.isArray(arr) ? arr : []) {
        // parsing defensivo: buscamos los totales en refreshedStats (nombres estables del SDK)
        const st = ob.refreshedStats || ob.stats || {};
        const dep = +(st.userTotalDeposit ?? st.totalDeposit ?? 0);
        const bor = +(st.userTotalBorrow ?? st.totalBorrow ?? 0);
        const net = dep - bor;
        if (net > 1) { out.usd += net; out.detail.push({ deposit: dep, borrow: bor }); out.ok = true; }
      }
    }
  } catch (e) { out.warning = String(e.message || e); }
  return out;
}

/* ---- Hyperliquid L1: spot + HYPE en staking (API pública gratis) ---- */
async function fetchHyperliquid(addr) {
  const out = { tokens: [], staked: null, totalUsd: 0 };
  const call = async (body) => {
    const r = await fetch("https://api.hyperliquid.xyz/info", {
      method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) });
    if (!r.ok) throw new Error("hl_" + r.status);
    return r.json();
  };
  try {
    const [spot, stake, mids] = await Promise.all([
      call({ type: "spotClearinghouseState", user: addr }).catch(() => null),
      call({ type: "delegatorSummary", user: addr }).catch(() => null),
      call({ type: "allMids" }).catch(() => null),
    ]);
    const px = (sym) => sym === "USDC" ? 1 : (mids && mids[sym] != null ? +mids[sym] : null);
    if (spot && Array.isArray(spot.balances)) {
      for (const b of spot.balances) {
        const amt = +(b.total || 0); if (!(amt > 0)) continue;
        const p = px(b.coin); const usd = p != null ? amt * p : null;
        if (usd != null && usd < 20) continue;
        out.tokens.push({ sym: b.coin, amount: amt, usd });
        if (usd) out.totalUsd += usd;
      }
    }
    if (stake) {
      const st = +(stake.delegated || 0) + +(stake.undelegated || 0) + +(stake.totalPendingWithdrawal || 0);
      if (st > 0) { const p = px("HYPE"); const usd = p != null ? st * p : null;
        out.staked = { sym: "HYPE (staked)", amount: st, usd }; if (usd) out.totalUsd += usd; }
    }
  } catch (e) { out.warning = String(e.message || e); }
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
  const token = process.env.GH_TOKEN;
  if (!authConfigured(req)) { res.statusCode = 503; return res.end(JSON.stringify({ error: "no_password" })); }
  if (!requestAuthorized(req, url)) { await new Promise(r => setTimeout(r, 600)); res.statusCode = 401; return res.end(JSON.stringify({ error: "bad_password" })); }
  if (!token && !process.env.LOCAL_DATA_DIR) { res.statusCode = 503; return res.end(JSON.stringify({ error: "no_github_token" })); }

  try {
    const wallets = (await ghFile(token, "data/wallets.json")) || {};
    if (!wallets.solana && !wallets.evm) {
      return res.end(JSON.stringify({ error: "no_wallets", message: "Rellena data/wallets.json en el repo privado: {\"solana\":\"...\",\"evm\":\"...\"}" }));
    }
    const px = await fetchPrices();
    const [sol, eth, base, hyperevm, polygon, arbitrum, optimism, hl, uni, prjx, kamino] = await Promise.all([
      wallets.solana ? fetchSolana(wallets.solana, px).catch(e => ({ error: String(e.message || e) })) : null,
      wallets.evm ? fetchEvmChain("https://eth.blockscout.com", "ethereum", wallets.evm).catch(e => ({ error: String(e.message || e) })) : null,
      wallets.evm ? fetchEvmChain("https://base.blockscout.com", "base", wallets.evm).catch(e => ({ error: String(e.message || e) })) : null,
      wallets.evm ? fetchEvmChain("https://hyperliquid.cloud.blockscout.com", "hyperevm", wallets.evm).catch(e => ({ error: String(e.message || e) })) : null,
      wallets.evm ? fetchEvmChain("https://polygon.blockscout.com", "polygon", wallets.evm).catch(e => ({ error: String(e.message || e) })) : null,
      wallets.evm ? fetchEvmChain("https://arbitrum.blockscout.com", "arbitrum", wallets.evm).catch(e => ({ error: String(e.message || e) })) : null,
      wallets.evm ? fetchEvmChain("https://optimism.blockscout.com", "optimism", wallets.evm).catch(e => ({ error: String(e.message || e) })) : null,
      wallets.evm ? fetchHyperliquid(wallets.evm).catch(e => ({ tokens: [], totalUsd: 0, warning: String(e.message || e) })) : null,
      wallets.evm ? fetchV3Positions("https://eth.blockscout.com", ETH_RPCS, wallets.evm, "Uniswap V3", [UNISWAP_V3_POSITION_MANAGER], "Ethereum").catch(e => ({ positions: [], totalUsd: 0, warning: String(e.message || e) })) : null,
      wallets.evm ? fetchV3Positions("https://hyperliquid.cloud.blockscout.com", HYPE_RPCS, wallets.evm, "ProjectX", [PROJECTX_POSITION_MANAGER], "HyperEVM").catch(e => ({ positions: [], totalUsd: 0, warning: String(e.message || e) })) : null,
      wallets.solana ? fetchKamino(wallets.solana).catch(e => ({ usd: 0, ok: false, warning: String(e.message || e) })) : null,
    ]);
    res.setHeader("Cache-Control", "private, max-age=120");
    return res.end(JSON.stringify({ prices: px, solana: sol, evm: { ethereum: eth, base, hyperevm, polygon, arbitrum, optimism }, hyperliquid: hl, uniswap: uni, projectx: prjx, kamino }));
  } catch (e) {
    res.statusCode = 502; return res.end(JSON.stringify({ error: "fetch_error", message: String((e && e.message) || e) }));
  }
};
