// api/aave.js — el LOOP en Aave v3 (Ethereum, mercado Core) leido on-chain en vivo.
//
// Devuelve colateral, deuda, health factor, umbral de liquidacion y el PRECIO DE
// LIQUIDACION de BTC, mas el detalle por activo (saldo, APY de prestamo, LT).
// Todo sale del contrato, no de la interfaz de Aave: Pool.getUserAccountData para los
// totales (lo mismo que usa Aave para liquidar) y getReserveData + balanceOf de los
// aTokens / variableDebtTokens para el desglose.
//
// La direccion de la wallet NO esta en este repo (es publico): se lee del repo privado
// (data/wallets.json) igual que api/portfolio.js, y la respuesta no la incluye.
// Protegido con la misma contrasena que api/private.js.

const { authConfigured, requestAuthorized } = require("../lib/auth");
const fs = require("fs");
const pathLib = require("path");
const REPO = process.env.PRIVATE_REPO || "brovira/DeFi-Tracker";

// Misma lista de RPCs que api/portfolio.js (probada en el pipeline privado).
const ETH_RPCS = ["https://ethereum-rpc.publicnode.com", "https://eth.llamarpc.com", "https://eth.drpc.org",
                  "https://1rpc.io/eth", "https://eth.merkle.io", "https://cloudflare-eth.com"];
const POOL = "0x87870Bca3F3fD6335C3F4ce8392D69350B4fA4E2";   // Aave v3 Ethereum Core · Pool
// Activos que pueden formar parte del loop. btc:true = cuenta como colateral BTC para el
// precio de liquidacion (cbBTC y WBTC siguen a BTC).
const ASSETS = [
  { symbol: "cbBTC", address: "0xcbB7C0000aB88B473b1f5aFd9ef808440eed33Bf", decimals: 8, btc: true },
  { symbol: "WBTC", address: "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599", decimals: 8, btc: true },
  { symbol: "WETH", address: "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2", decimals: 18, btc: false },
  { symbol: "USDC", address: "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48", decimals: 6, btc: false, stable: true },
  { symbol: "USDT", address: "0xdAC17F958D2ee523a2206206994597C13D831ec7", decimals: 6, btc: false, stable: true },
];
// Selectores (keccak256 de la firma, primeros 4 bytes)
const SEL = {
  getUserAccountData: "0xbf92857c", getReserveData: "0x35ea6a75", ADDRESSES_PROVIDER: "0x0542975c",
  getPriceOracle: "0xfca513a8", getAssetPrice: "0xb3596f07", balanceOf: "0x70a08231", getUserEMode: "0xeddf1b79",
};
const SECONDS_PER_YEAR = 31536000;

const pad = (h) => h.replace(/^0x/, "").toLowerCase().padStart(64, "0");
const word = (hex, i) => BigInt("0x" + (hex.replace(/^0x/, "").slice(i * 64, i * 64 + 64) || "0"));
const addr = (hex, i) => "0x" + hex.replace(/^0x/, "").slice(i * 64 + 24, i * 64 + 64);
const units = (v, dec) => Number(v) / 10 ** dec;

async function ghFile(token, path) {
  if (process.env.LOCAL_DATA_DIR) {
    try {
      const localPath = pathLib.join(process.env.LOCAL_DATA_DIR, path.replace(/^data\//, ""));
      return JSON.parse(await fs.promises.readFile(localPath, "utf8"));
    } catch (e) { return null; }
  }
  const r = await fetch(`https://api.github.com/repos/${REPO}/contents/${path}`, {
    headers: { Authorization: `Bearer ${token}`, Accept: "application/vnd.github.raw+json", "User-Agent": "aave-loop" },
  });
  if (!r.ok) return null;
  try { return JSON.parse(await r.text()); } catch (e) { return null; }
}

// eth_call con reparto de RPCs: si uno falla o devuelve vacio, prueba el siguiente.
async function ethCall(to, data) {
  let last = "sin RPC";
  for (const rpc of ETH_RPCS) {
    try {
      const r = await fetch(rpc, { method: "POST", headers: { "Content-Type": "application/json", "User-Agent": "aave-loop" },
        body: JSON.stringify({ jsonrpc: "2.0", id: 1, method: "eth_call", params: [{ to, data }, "latest"] }) });
      if (!r.ok) { last = rpc + " HTTP " + r.status; continue; }
      const j = await r.json();
      if (j.result && j.result !== "0x") return j.result;
      last = rpc + " " + ((j.error && j.error.message) || "vacio");
    } catch (e) { last = rpc + " " + String(e.message || e); }
  }
  throw new Error("eth_call " + data.slice(0, 10) + ": " + last);
}

const apy = (rayRate) => {           // tasa anual en RAY (1e27, interes simple) -> APY compuesto por segundo
  const r = Number(rayRate) / 1e27;
  return (Math.pow(1 + r / SECONDS_PER_YEAR, SECONDS_PER_YEAR) - 1) * 100;
};

async function leerLoop(wallet) {
  const w = pad(wallet);
  const [cuenta, emode, provider] = await Promise.all([
    ethCall(POOL, SEL.getUserAccountData + w),
    ethCall(POOL, SEL.getUserEMode + w).catch(() => null),
    ethCall(POOL, SEL.ADDRESSES_PROVIDER),
  ]);
  const oracle = addr(await ethCall(addr(provider, 0), SEL.getPriceOracle), 0);

  // getUserAccountData: totales en la moneda base del mercado (USD con 8 decimales)
  const account = {
    collateralUsd: units(word(cuenta, 0), 8),
    debtUsd: units(word(cuenta, 1), 8),
    availableBorrowsUsd: units(word(cuenta, 2), 8),
    liquidationThresholdPct: Number(word(cuenta, 3)) / 100,   // media ponderada, en bps
    ltvPct: Number(word(cuenta, 4)) / 100,
    healthFactor: word(cuenta, 1) === 0n ? null : units(word(cuenta, 5), 18),
  };

  const reservas = await Promise.all(ASSETS.map(async (a) => {
    const [rd, px] = await Promise.all([
      ethCall(POOL, SEL.getReserveData + pad(a.address)),
      ethCall(oracle, SEL.getAssetPrice + pad(a.address)),
    ]);
    // ReserveDataLegacy: 0 configuration · 2 liquidityRate · 4 variableBorrowRate · 8 aToken · 10 variableDebtToken
    const conf = word(rd, 0);
    const aToken = addr(rd, 8), debtToken = addr(rd, 10);
    const [sup, deb] = await Promise.all([
      ethCall(aToken, SEL.balanceOf + w),
      ethCall(debtToken, SEL.balanceOf + w),
    ]);
    const priceUsd = units(word(px, 0), 8);
    const supplied = units(word(sup, 0), a.decimals), debt = units(word(deb, 0), a.decimals);
    return {
      symbol: a.symbol, btc: a.btc, stable: !!a.stable, priceUsd,
      supplied, suppliedUsd: supplied * priceUsd, debt, debtUsd: debt * priceUsd,
      ltvPct: Number(conf & 0xffffn) / 100,
      liquidationThresholdPct: Number((conf >> 16n) & 0xffffn) / 100,
      supplyApyPct: apy(word(rd, 2)), borrowApyPct: apy(word(rd, 4)),
    };
  }));

  // Precio de liquidacion de BTC. Exacto si el colateral es solo BTC y la deuda no es BTC:
  // el HF escala lineal con el precio, asi que P_liq = P / HF. Si hay mezcla, se resuelve
  // con el LT de cada activo (y se avisa si hay e-mode, que cambia los LT).
  const btcPx = (reservas.find((r) => r.symbol === "cbBTC") || {}).priceUsd || null;
  const colBtc = reservas.filter((r) => r.btc && r.supplied > 0);
  const colOtro = reservas.filter((r) => !r.btc && r.supplied > 0);
  const debBtc = reservas.filter((r) => r.btc && r.debt > 0);
  const debOtro = reservas.filter((r) => !r.btc && r.debt > 0);
  const btcColateral = colBtc.reduce((s, r) => s + r.supplied, 0);
  const debtUsd = reservas.reduce((s, r) => s + r.debtUsd, 0);
  let liqPrice = null, liqMetodo = null;
  if (account.healthFactor && btcPx && !colOtro.length && !debBtc.length) {
    liqPrice = btcPx / account.healthFactor; liqMetodo = "P / HF (colateral solo BTC, deuda en estables)";
  } else if (btcPx && debtUsd > 0) {
    const den = colBtc.reduce((s, r) => s + r.supplied * r.liquidationThresholdPct / 100, 0) - debBtc.reduce((s, r) => s + r.debt, 0);
    const num = debOtro.reduce((s, r) => s + r.debtUsd, 0) - colOtro.reduce((s, r) => s + r.suppliedUsd * r.liquidationThresholdPct / 100, 0);
    if (den > 0) { liqPrice = Math.max(0, num / den); liqMetodo = "por activo (colateral mixto)"; }
  }
  // Los intereses hacen crecer la deuda: precio de liquidacion dentro de 12 meses a las tasas de hoy.
  const interesAnualUsd = reservas.reduce((s, r) => s + r.debtUsd * r.borrowApyPct / 100, 0);
  const borrowApyMedio = debtUsd > 0 ? interesAnualUsd / debtUsd * 100 : null;
  const liqPrice12m = liqPrice != null && debtUsd > 0 ? liqPrice * (debtUsd + interesAnualUsd) / debtUsd : null;
  const equityUsd = account.collateralUsd - account.debtUsd;

  return {
    generado: new Date().toISOString(),
    mercado: "Aave v3 · Ethereum Core", pool: POOL, oracle,
    eMode: emode ? Number(word(emode, 0)) : null,
    account, btcPriceUsd: btcPx, btcColateral,
    equityUsd, equityBtc: btcPx ? equityUsd / btcPx : null,
    leverage: equityUsd > 0 ? account.collateralUsd / equityUsd : null,
    liqPrice, liqMetodo, liqDistancePct: liqPrice && btcPx ? (1 - liqPrice / btcPx) * 100 : null,
    borrowApyMedioPct: borrowApyMedio, interesAnualUsd, liqPrice12m,
    reservas: reservas.filter((r) => r.supplied > 0 || r.debt > 0),
    tasas: reservas.map((r) => ({ symbol: r.symbol, borrowApyPct: r.borrowApyPct, supplyApyPct: r.supplyApyPct,
                                  ltvPct: r.ltvPct, liquidationThresholdPct: r.liquidationThresholdPct, priceUsd: r.priceUsd })),
  };
}

module.exports = async (req, res) => {
  res.setHeader("Content-Type", "application/json; charset=utf-8");
  const url = new URL(req.url, "http://x");
  if (!authConfigured(req)) { res.statusCode = 503; return res.end(JSON.stringify({ error: "no_password" })); }
  if (!requestAuthorized(req, url)) {
    await new Promise((r) => setTimeout(r, 600));
    res.statusCode = 401; return res.end(JSON.stringify({ error: "bad_password" }));
  }
  const token = process.env.GH_TOKEN;
  if (!token && !process.env.LOCAL_DATA_DIR) { res.statusCode = 503; return res.end(JSON.stringify({ error: "no_github_token" })); }
  try {
    const wallets = (await ghFile(token, "data/wallets.json")) || {};
    if (!wallets.evm) { res.statusCode = 404; return res.end(JSON.stringify({ error: "no_wallet", message: "Falta la wallet EVM en data/wallets.json del repo privado." })); }
    const out = await leerLoop(wallets.evm);
    res.setHeader("Cache-Control", "no-store");
    return res.end(JSON.stringify(out));
  } catch (e) {
    res.statusCode = 502;
    return res.end(JSON.stringify({ error: "rpc", message: String((e && e.message) || e) }));
  }
};
module.exports.leerLoop = leerLoop;
