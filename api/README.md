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
