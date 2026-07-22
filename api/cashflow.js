// api/cashflow.js — cashflow de BELROGAM para el "plan de guerra" BTC (con contraseña).
// SOLO LECTURA sobre Supabase (misma BD que el dashboard de belrogam):
//   · saldos_cuentas            → cash disponible hoy
//   · transacciones_clean       → neto mensual real (últimos meses)
//   · v_proyeccion_reservas     → ingresos futuros ya CONFIRMADOS por mes
//
// CONFIGURACIÓN (Vercel → Environment Variables — copia los valores del proyecto belrogam):
//   SUPABASE_URL         = https://<proyecto>.supabase.co
//   SUPABASE_SERVICE_KEY = <service role key>   (queda solo en el backend)
//   SITE_PASSWORD        = (la contraseña única de la web; DASH_PASSWORD sigue compatible)

const { authConfigured, requestAuthorized } = require("../lib/auth");

module.exports = async (req, res) => {
  res.setHeader("Content-Type", "application/json; charset=utf-8");
  const url = new URL(req.url, "http://x");
  // tolerante a variantes/typos del nombre (SUPABASE_URL, SUPBASE_URL, SUPABASE-URL…) y a
  // espacios/saltos de línea accidentales al pegar el valor en Vercel (trim()).
  const clean = (v) => {
    let s = v == null ? "" : String(v).trim();
    if ((s.startsWith('"') && s.endsWith('"')) || (s.startsWith("'") && s.endsWith("'"))) s = s.slice(1, -1).trim();
    return s;
  };
  const cleanKey = (v) => clean(v).replace(/^Bearer\s+/i, "").trim();
  let SB = clean(process.env.SUPABASE_URL), KEY = clean(process.env.SUPABASE_SERVICE_KEY);
  if (!SB || !KEY) {
    for (const k of Object.keys(process.env)) {
      if (!SB && /SUPABASE/i.test(k) && /URL/i.test(k)) SB = clean(process.env[k]);
      if (!KEY && /SUPABASE/i.test(k) && /(SERVICE|ROLE|KEY|TOKEN|SECRET)/i.test(k)) KEY = cleanKey(process.env[k]);
    }
  }
  KEY = cleanKey(KEY);
  if (!authConfigured()) { res.statusCode = 503; return res.end(JSON.stringify({ error: "no_password" })); }
  if (!requestAuthorized(req, url)) { await new Promise(r => setTimeout(r, 600)); res.statusCode = 401; return res.end(JSON.stringify({ error: "bad_password" })); }
  if (!SB || !KEY) {
    // diagnóstico: nombres + LONGITUD de lo que hay (nunca el valor) — así se ve si está
    // vacía, si tiene solo espacios, o si directamente no existe la variable.
    const diag = Object.keys(process.env).filter(k => /SUP/i.test(k)).map(k => {
      const raw = process.env[k] || ""; const len = raw.length, trimmed = raw.trim().length;
      return `${k} (${len === 0 ? "vacía" : trimmed === 0 ? "solo espacios/saltos de línea" : `${len} caracteres, OK`})`;
    });
    res.statusCode = 503;
    return res.end(JSON.stringify({ error: "no_supabase", message: "No encuentro SUPABASE_URL / SUPABASE_SERVICE_KEY con valor. Lo que veo con ese nombre: " + (diag.length ? diag.join(" · ") : "ninguna variable con 'SUP' en el nombre") + ". Si pone 'vacía', bórrala y vuelve a pegar el valor en Vercel (a veces el campo Value se queda en blanco). Tras corregir, Redeploy." }));
  }

  if (!/^https:\/\/[^/]+\.supabase\.co\/?$/i.test(SB)) {
    res.statusCode = 503;
    return res.end(JSON.stringify({ error: "bad_supabase_url", message: "SUPABASE_URL debe ser algo como https://xxxxx.supabase.co (sin /rest/v1 al final)." }));
  }

  const H = { apikey: KEY, Authorization: `Bearer ${KEY}` };
  const get = async (path) => {
    const r = await fetch(`${SB.replace(/\/+$/, "")}/rest/v1/${path}`, { headers: H });
    if (!r.ok) {
      const txt = await r.text().catch(() => "");
      throw new Error("supabase_" + r.status + " en " + path.split("?")[0] + (txt ? ": " + txt.slice(0, 220) : ""));
    }
    return r.json();
  };

  try {
    const today = new Date();
    const iso = (d) => d.toISOString().slice(0, 10);
    const monthsAgo = new Date(today); monthsAgo.setMonth(monthsAgo.getMonth() - 5); monthsAgo.setDate(1);

    const [saldos, txns, futuras] = await Promise.all([
      get("saldos_cuentas?select=cuenta,saldo,moneda,synced_at"),
      get(`transacciones_clean?select=fecha,importe&fecha=gte.${iso(monthsAgo)}`),
      get(`v_proyeccion_reservas?select=check_in,revenue_caja&cobrado=eq.false&check_in=gte.${iso(today)}`),
    ]);

    const saldoTotal = saldos.reduce((s, r) => s + (+r.saldo || 0), 0);

    const byMonth = {};
    for (const t of txns) {
      const m = String(t.fecha).slice(0, 7);
      const v = +t.importe || 0;
      const o = byMonth[m] || (byMonth[m] = { mes: m, ingresos: 0, gastos: 0, neto: 0 });
      if (v > 0) o.ingresos += v; else o.gastos += v;
      o.neto += v;
    }
    const curMonth = iso(today).slice(0, 7);
    const monthly = Object.values(byMonth).sort((a, b) => a.mes.localeCompare(b.mes))
      .map(o => ({ ...o, ingresos: Math.round(o.ingresos), gastos: Math.round(o.gastos), neto: Math.round(o.neto), completo: o.mes < curMonth }));

    const futMonth = {};
    for (const f of futuras) {
      const m = String(f.check_in).slice(0, 7);
      futMonth[m] = (futMonth[m] || 0) + (+f.revenue_caja || 0);
    }
    const future = Object.entries(futMonth).sort((a, b) => a[0].localeCompare(b[0]))
      .map(([mes, eur]) => ({ mes, eur: Math.round(eur) }));

    res.setHeader("Cache-Control", "private, max-age=600"); // 10 min
    return res.end(JSON.stringify({ saldoTotal: Math.round(saldoTotal), saldos, monthly, future, curMonth }));
  } catch (e) {
    res.statusCode = 502; return res.end(JSON.stringify({ error: "fetch_error", message: String((e && e.message) || e) }));
  }
};
