const { authConfigured, requestAuthorized } = require("../lib/auth");

const SOL_RPC = process.env.SOLANA_RPC_URL || "https://api.mainnet-beta.solana.com";
const MAX_POSITIONS = 20;
const CACHE_MS = 30_000;
const cache = new Map();

let sdkPromise;
function loadSdk() {
  if (!sdkPromise) {
    sdkPromise = Promise.all([
      import("@solana/kit"),
      import("@orca-so/whirlpools-client"),
      import("@orca-so/whirlpools-core"),
    ]);
  }
  return sdkPromise;
}

async function quotePosition(rpc, mint) {
  const cached = cache.get(mint);
  if (cached && Date.now() - cached.createdAt < CACHE_MS) return cached.value;

  const [{ address }, client, core] = await loadSdk();
  const deployment = client.DEFAULT_WHIRLPOOL_DEPLOYMENT;
  const [positionAddress] = await client.getPositionAddress(address(mint), deployment.programId);
  const position = await client.fetchPosition(rpc, positionAddress);
  const whirlpool = await client.fetchWhirlpool(rpc, position.data.whirlpool);
  const lowerStart = core.getTickArrayStartTickIndex(position.data.tickLowerIndex, whirlpool.data.tickSpacing);
  const upperStart = core.getTickArrayStartTickIndex(position.data.tickUpperIndex, whirlpool.data.tickSpacing);
  const [lowerAddress] = await client.getTickArrayAddress(whirlpool.address, lowerStart, deployment.programId);
  const [upperAddress] = await client.getTickArrayAddress(whirlpool.address, upperStart, deployment.programId);
  const [lowerArray, upperArray] = await client.fetchAllTickArray(rpc, [lowerAddress, upperAddress]);
  const lowerTick = lowerArray.data.ticks[
    core.getTickIndexInArray(position.data.tickLowerIndex, lowerStart, whirlpool.data.tickSpacing)
  ];
  const upperTick = upperArray.data.ticks[
    core.getTickIndexInArray(position.data.tickUpperIndex, upperStart, whirlpool.data.tickSpacing)
  ];
  const quote = core.collectFeesQuote(whirlpool.data, position.data, lowerTick, upperTick);
  const value = {
    tokenA: String(whirlpool.data.tokenMintA),
    tokenB: String(whirlpool.data.tokenMintB),
    feeOwedA: quote.feeOwedA.toString(),
    feeOwedB: quote.feeOwedB.toString(),
  };
  cache.set(mint, { createdAt: Date.now(), value });
  return value;
}

module.exports = async (req, res) => {
  res.setHeader("Content-Type", "application/json; charset=utf-8");
  const url = new URL(req.url, "http://x");
  if (!authConfigured(req)) {
    res.statusCode = 503;
    return res.end(JSON.stringify({ error: "no_password" }));
  }
  if (!requestAuthorized(req, url)) {
    res.statusCode = 401;
    return res.end(JSON.stringify({ error: "bad_password" }));
  }

  const mints = [...new Set((url.searchParams.get("mints") || "").split(",").filter(Boolean))];
  if (!mints.length || mints.length > MAX_POSITIONS || mints.some(m => !/^[1-9A-HJ-NP-Za-km-z]{32,44}$/.test(m))) {
    res.statusCode = 400;
    return res.end(JSON.stringify({ error: "bad_mints" }));
  }

  try {
    const [{ createSolanaRpc }] = await loadSdk();
    const rpc = createSolanaRpc(SOL_RPC);
    const entries = await Promise.all(mints.map(async mint => {
      try { return [mint, await quotePosition(rpc, mint)]; }
      catch (e) { return [mint, { error: String((e && e.message) || e) }]; }
    }));
    res.setHeader("Cache-Control", "private, max-age=30");
    return res.end(JSON.stringify({ positions: Object.fromEntries(entries) }));
  } catch (e) {
    res.statusCode = 502;
    return res.end(JSON.stringify({ error: "orca_fees", message: String((e && e.message) || e) }));
  }
};
