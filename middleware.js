// middleware.js — puerta de contraseña para TODA la web (Vercel Edge Middleware).
//
// Pide una contraseña antes de servir cualquier página. Es un gate de SERVIDOR
// (no un JS del frontend que se salte viendo el código): sin la cookie correcta,
// Vercel ni siquiera entrega el HTML.
//
// CONFIGURACIÓN (una vez): Vercel → proyecto btc-cycle-terminal → Settings →
//   Environment Variables → SITE_PASSWORD = <la contraseña para entrar>
// Mientras SITE_PASSWORD no esté puesta, NO bloquea nada (así no te dejas fuera).
//
// Nota: el repo es público, así que el CÓDIGO sigue visible en GitHub; esto
// protege el SITIO desplegado (la URL), que es lo que pediste.

export const config = {
  // aplica a todo menos al propio favicon/robots (para no romper esas peticiones)
  matcher: "/((?!favicon.ico|robots.txt).*)",
};

async function token(pass) {
  const buf = await crypto.subtle.digest("SHA-256", new TextEncoder().encode("btc-terminal::" + pass));
  return Array.from(new Uint8Array(buf)).map((b) => b.toString(16).padStart(2, "0")).join("");
}

function loginPage(err) {
  return `<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>Acceso · BTC Terminal</title>
<style>
  :root{color-scheme:dark}
  *{box-sizing:border-box}
  body{margin:0;min-height:100vh;display:flex;align-items:center;justify-content:center;
    background:radial-gradient(1000px 500px at 70% -10%,rgba(232,161,58,.10),transparent 60%),linear-gradient(#0d1420,#101a28);
    color:#e8eef7;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
  .card{width:340px;max-width:92vw;background:#152131;border:1px solid #25384f;border-radius:16px;
    padding:26px 24px;box-shadow:0 20px 50px -24px rgba(0,0,0,.75)}
  h1{font-size:19px;margin:0 0 4px} p{margin:0 0 16px;color:#aebccf;font-size:13px}
  input{width:100%;padding:11px 13px;border-radius:10px;border:1px solid #25384f;background:#0d1420;color:#e8eef7;font-size:15px}
  button{width:100%;margin-top:12px;padding:11px;border:0;border-radius:10px;cursor:pointer;
    background:#e8a13a;color:#1a1205;font-weight:800;font-size:14px}
  .err{color:#f2606d;font-size:12.5px;margin-top:10px;min-height:16px}
</style></head><body>
<form class="card" method="POST" autocomplete="off">
  <h1>🔒 BTC Terminal</h1>
  <p>Introduce la contraseña para entrar.</p>
  <input type="password" name="pw" placeholder="Contraseña" autofocus required>
  <button type="submit">Entrar</button>
  <div class="err">${err ? "Contraseña incorrecta." : ""}</div>
</form></body></html>`;
}

export default async function middleware(req) {
  const pass = process.env.SITE_PASSWORD;
  if (!pass) return; // sin configurar → no bloquea (evita dejarte fuera)

  const url = new URL(req.url);
  const good = await token(pass);
  const cookie = req.headers.get("cookie") || "";
  if (cookie.split(/;\s*/).includes("site_auth=" + good)) return; // ya autenticado

  let given = null;
  if (req.method === "POST") {
    try { given = new URLSearchParams(await req.text()).get("pw"); } catch (e) {}
  } else {
    given = url.searchParams.get("pw");
  }

  if (given === pass) {
    return new Response(null, {
      status: 303,
      headers: {
        Location: url.pathname,
        "Set-Cookie": `site_auth=${good}; Path=/; HttpOnly; Secure; SameSite=Lax; Max-Age=${60 * 60 * 24 * 90}`,
      },
    });
  }

  return new Response(loginPage(given != null), {
    status: 401,
    headers: { "content-type": "text/html; charset=utf-8", "Cache-Control": "no-store" },
  });
}
