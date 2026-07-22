# Backend serverless (`/api`)

Funciones serverless que corren en Vercel (no en el frontend público). Sirven para
usar APIs que necesitan **API key** sin exponer la key en el HTML.

## `coinglass.js` — proxy de Coinglass (liquidaciones, OI y funding agregados)

El frontend (`derivados.html`) llama a `/api/coinglass?metric=<...>` y el backend
añade la key y reenvía la petición a Coinglass.

### Configuración (una vez)
1. Crea cuenta en https://www.coinglass.com/ → **Account → API** y copia tu API key.
2. En **Vercel → proyecto `btc-cycle-terminal` → Settings → Environment Variables**:
   - `COINGLASS_API_KEY = <tu key>` (marca Production y Preview)
3. **Redeploy** (o haz un push). Ya está: el panel de Derivados mostrará las
   liquidaciones agregadas en cuanto detecte la key.

Mientras no haya key, el backend responde `503 {error:"no_key"}` y el frontend
muestra un aviso de "configura tu key" — nada se rompe.

### Métricas permitidas (lista blanca en `coinglass.js`)
`liquidation_history` · `liquidation_coin` · `open_interest` · `funding` ·
`long_short` · `heatmap`

> Los *paths* exactos de Coinglass dependen de tu **plan** y de la **versión** de su
> API (v4 por defecto aquí, header `CG-API-KEY`). Si un endpoint devuelve error,
> ajusta `PATHS` (y si tu plan usa v3, cambia `COINGLASS_KEY_HEADER=coinglassSecret`
> como env var). Todo está comentado en `coinglass.js`.

### Seguridad
- La key vive **solo** como env var en Vercel, nunca en el repo.
- El proxy solo acepta métricas de la lista blanca (no es un proxy abierto).
- Respuestas cacheadas 5 min en el edge para no quemar el rate limit.

---

## `../middleware.js` — contraseña para ENTRAR en toda la web

Gate de **servidor** (Vercel Edge Middleware, en la raíz del repo): antes de servir
cualquier página, pide una contraseña. No es un JS del frontend que se salte "viendo
código" — sin la cookie correcta, Vercel no entrega el HTML.

- **Configurar:** Vercel → `btc-cycle-terminal` → Settings → Environment Variables →
  `SITE_PASSWORD = <la contraseña para entrar>` (Production + Preview) → Redeploy.
- Mientras `SITE_PASSWORD` **no** esté puesta, **no bloquea nada** (así no te dejas fuera).
- Al entrar bien, deja una cookie `site_auth` (HttpOnly, 90 días); no vuelve a pedirla.
- Es distinta de `DASH_PASSWORD`: `SITE_PASSWORD` = entrar en la web; `DASH_PASSWORD` =
  ver tus datos personales del DeFi-Tracker. Puedes poner la misma o distintas.
- El repo es público, así que el **código** sigue en GitHub; esto protege el **sitio**.

---

## `private.js` + `journal.js` — datos PERSONALES con contraseña

Tus posiciones/PnL (DeFi-Tracker) y tu **diario de operativa** son **datos personales**.
Este repo es **público**, así que esos datos **nunca** viven aquí: se guardan en tu repo
**privado** `brovira/DeFi-Tracker` y el backend los trae **al momento**, solo durante una
sesión autorizada por la entrada global de la web.

- `private.js` → `GET /api/private?file=orca_pnl` — sirve `data/normalized/orca_pnl.json`
  (también `orca_positions` / `orca_events`). Solo lectura.
- `journal.js` → `GET/POST /api/journal` — lee y **añade** entradas a `data/journal.json`
  (tu diario de trades + razonamiento). El POST **escribe** en el repo privado.

La herramienta pide la contraseña una sola vez al entrar. La cookie segura `site_auth`
autoriza también `portfolio.html`, `lp.html` y sus APIs, que **auto-cargan** los datos sin
volver a mostrar formularios. La cookie es `HttpOnly`; la contraseña no se guarda en el
navegador y los datos personales se vuelven a pedir al backend en cada carga.

### Configuración (una vez, en Vercel → `btc-cycle-terminal` → Settings → Environment Variables)
1. `SITE_PASSWORD = <la contraseña que elijas>` (Production + Preview). `DASH_PASSWORD`
   sigue aceptándose por compatibilidad, pero ya no es necesario usar dos claves.
2. `GH_TOKEN = <token fine-grained de GitHub sobre DeFi-Tracker>`:
   - GitHub → **Settings → Developer settings → Fine-grained tokens → Generate new token**.
   - **Resource owner:** tú · **Repository access:** *Only select repositories* → **DeFi-Tracker**.
   - **Repository permissions → Contents:**
     - **Read-only** → basta para ver posiciones/PnL y **leer** el diario.
     - **Read and write** → necesario para **añadir** entradas al diario desde el dashboard.
   - Generate token y pega el valor en `GH_TOKEN`.
3. *(Opcional)* `PRIVATE_REPO = brovira/DeFi-Tracker` (es el valor por defecto).
4. **Redeploy** (o push). Introduce la contraseña al entrar en la web; las zonas privadas
   cargarán después con esa misma sesión.

### Comportamiento sin configurar (nada se rompe)
- Sin `SITE_PASSWORD` ni `DASH_PASSWORD` → `503 {error:"no_password"}` y el frontend avisa.
- Sesión inválida → `401` con un pequeño retardo anti-fuerza-bruta.
- Sin `GH_TOKEN` → `503`; con token sin escritura, el diario **se lee** pero el POST da `403`.
- El `file-upload` manual (arrastrar el JSON/CSV) sigue disponible como alternativa.

### Seguridad
- La contraseña y el token viven **solo** como env vars en Vercel, nunca en el repo.
- `private.js` solo sirve una **lista blanca** de archivos; no es un proxy abierto al repo.
- Comparación de contraseña en tiempo (casi) constante + retardo en fallo.
- Los datos personales **no se persisten** en `localStorage` (solo la contraseña, si marcas
  «recordar»); se vuelven a pedir al backend en cada carga.
