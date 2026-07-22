# Memoria de proyecto — BTC Cycle Terminal (para retomar en otra sesión/LLM)

**Propósito:** terminal personal de inversión en BTC. Sigue 3 analistas (LMEC, Cowen,
OnChainMind) con citas verbatim de sus transcripts, agrega señales, y gestiona el
capital real (personal + BELROGAM SL) para decidir cuánto/cuándo comprar.

## Repos (3, en Claude Code Remote — todos ya en la sesión vía add_repo)
- **`brovira/btc-cycle-terminal`** (PÚBLICO) — la web (Vercel: btc-cycle-terminal.vercel.app).
  Todo el código, agentes/transcripts, KB de señales. Nunca commitear datos personales aquí.
- **`brovira/DeFi-Tracker`** (PRIVADO) — pipeline Python que decodifica tu wallet Solana
  (Orca LP) desde on-chain, y guarda tus datos personales (journal, wallets, baseline).
- **`belrogam`** (repo de trabajo separado, negocio de alquileres — NO tocar salvo que
  se pida explícitamente; solo se leyó su Supabase de solo-lectura para el cashflow).

## Arquitectura de contraseñas / secrets (Vercel del proyecto btc-cycle-terminal)
- `SITE_PASSWORD` → gate de TODA la web (middleware.js, Edge Middleware).
- `DASH_PASSWORD` → ver datos personales (LP, cartera, diario, plan de guerra).
- `GH_TOKEN` → fine-grained token sobre DeFi-Tracker (Contents: Read+Write) para que
  el backend lea/escriba data/*.json del repo privado.
- `SOLANA_RPC_URL` → RPC de Helius (mejor que el público) para el portfolio.
- `SUPABASE_URL` + `SUPABASE_SERVICE_KEY` → copia de las credenciales del proyecto
  belrogam, SOLO LECTURA (el código solo hace SELECT), para el "plan de guerra".
  **BUG ABIERTO:** el usuario las puso pero `/api/cashflow` seguía sin encontrarlas
  ("no_supabase"). Se mejoró el diagnóstico (api/cashflow.js) para reportar LONGITUD
  de cada var (vacía / solo espacios / N caracteres) — pendiente que el usuario relea
  el mensaje de error tras el último redeploy y lo resuelva (probable: campo Value
  vacío en Vercel, o falta Redeploy tras guardar).
- `BIRDEYE_API_KEY` → NO se llegó a configurar (el usuario no tenía key); se sustituyó
  por Jupiter API (gratis, sin key) para precios de Solana.

## Páginas principales (todas en btc-cycle-terminal, raíz del repo)
- **`index.html`** — hub, reordenado por capas: 1) Portfolio (Mi portfolio + BELROGAM
  plan de guerra) 2) decision.html 3) DeFi (LPs + loop futuro) 4) Trading 5) Herramientas.
- **`decision.html`** — "¿Qué hago hoy?": semáforo de señales agregadas, relojes de
  ciclo (halving/midterm), **Plan de guerra** (cashflow BELROGAM → cash invertible
  sep-nov, con contraseña), tarjetas **LMEC · Cowen** (ya NO OnChainMind, ver abajo)
  con: fase del ciclo según él + checklist de señales EN VIVO (🟢/⚪, motor de reglas
  contra el KB) + qué hace/por qué/próximo movimiento/pólvora + aviso de sesgo auditado
  + link a su framework completo + gráfica de fases (sombras por semana del halving).
  Se auto-refresca cada 30 min.
- **`lmec.html` / `cowen.html` / `onchainmind.html`** — panel de cada agente (framework,
  indicadores, verdict box "¿comprar o esperar?").
- **`portfolio.html`** — cartera Nansen-style (Token/Protocol/Chain/Address, filas
  expandibles, toggle "ocultar <$5"). Backend `api/portfolio.js`.
- **`lp.html`** — DeFi-Tracker: LPs de Orca, PnL, fresh start (línea base "farming
  desde cero"), diario de operativa (journal.json en repo privado).
- **`backtest.html`** — backtester con presets de los 3 agentes (citas reales),
  indicador risk-metric aprox de Cowen, modo DCA, builder libre ("＋ Crear nueva").
- **`montecarlo.html`, `derivados.html`** — sin cambios recientes.

## APIs backend (Vercel serverless, en `/api`)
- `private.js` — sirve archivos whitelisted del repo privado (orca_pnl, journal,
  manual_assets, wallets…) con contraseña.
- `journal.js` — lee/escribe el diario de operativa.
- `baseline.js` — fresh start del farming (línea base fecha/valor).
- `portfolio.js` — agrega TODO el patrimonio: Solana (RPC + Jupiter para precios
  genéricos de cualquier SPL token, ya no solo 3 mints hardcodeados), EVM (Blockscout:
  Ethereum, Base, HyperEVM, Polygon, Arbitrum, Optimism — BNB Chain NO hace falta, el
  BNB de Nansen es de la LP Uniswap, no una wallet BNB Chain nativa), Hyperliquid L1
  (spot + staking, API pública), Kamino Lend (api.kamino.finance, sin verificar en vivo
  — sandbox bloquea red), posiciones V3 auto-detectadas (Uniswap ETH + ProjectX
  HyperEVM, vía positions()/factory()/getPool()/slot0() genérico).
- `cashflow.js` — cashflow BELROGAM (Supabase solo-lectura) para el plan de guerra.
- `coinmetrics.js`, `coinglass.js`, `birdeye.js` (sin usar, sustituido por Jupiter).

## KB de señales (agentes/<agente>/senales.json) — LO MÁS VALIOSO DEL PROYECTO
Construido por 3 agentes en paralelo, cada señal con **cita verbatim + archivo fuente**.
Regla de oro: nunca añadir señal sin cita real. 78 señales totales:
- `agentes/lmec/senales.json` — 26 señales, 4 fases, 5 cambios de opinión.
- `agentes/cowen/senales.json` — 25 señales, 6 fases, 5 cambios.
- `agentes/onchainmind/senales.json` — 27 señales, 5 fases, 4 cambios.

## Auditorías de track-record (agentes/<agente>/track_record.md + audits)
- `lmec/track_record.md` (7/10 general 2022-26) + `lmec/audit_2022_bottom_2025_top.md`
  (**4/10 específico ciclo 2022-25**): NO hay evidencia verificable de que comprara el
  suelo real de nov-2022 en tiempo real (corpus con hueco jul-22→ene-23; las citas de
  "compré a 15.750" son AUTOCITAS RETROSPECTIVAS de 2023+). Su venta real más completa
  llegó tarde (23-may-2025, ~$110-112k, solo ~5 meses antes del techo real oct-2025).
  **Importante: nunca vende BTC en sí** — solo rota altcoins→stablecoin.
- `cowen/track_record.md` (6/10 general 2021-26) + `cowen/audit_eth_dominance_rallies.md`
  (**5/10 específico ciclo 2022-25**): fuerte en MACRO (BTC dominance con niveles
  acertados; rallies de contratendencia 2026 avisados con precisión casi exacta — banda
  $78-79k anunciada 8-abr, tocada 20-abr). Débil en calls operativos tempranos (no vendió
  en ningún techo en tiempo real: 2021 "see you at 100k"; 2025 risk "moderate" días antes
  del top). El "ETH go home antes del ATH" que el usuario recordaba **no se sostiene
  tal cual** en los transcripts revisados — pero el usuario, que sigue a Cowen desde
  2021, afirma que SÍ predijo que ETH no rompería su ATH anterior hasta volver a la
  banda de regresión, y que fue exactamente lo que pasó este ciclo. **Pendiente**:
  re-verificar específicamente esa tesis (ETH banda de regresión → ATH) con más
  transcripts de 2024, no solo ago-2025.
- `onchainmind/track_record.md`: **la hipótesis del usuario se confirmó** — OCM NUNCA
  dio señal de venta en tiempo real desde sep-2025 (solo retrospectiva en mar-2026).
  Nota timing VENTA 1/10, COMPRA 4/10. **OnChainMind se retiró de las tarjetas de
  decision.html** (solo sirve para timing de compra, no de decisión completa). Su panel
  (onchainmind.html) sigue disponible, solo se quitó de la comparativa de 2 agentes.

## Pendiente de verificar (el usuario lo pidió, AÚN NO investigado — próxima sesión)
1. **LMEC 2022 "mentalidad + acumular BTC"**: el usuario (le sigue desde 2021) dice que
   LMEC SÍ empezó a hablar de mentalidad de holder y acumular BTC durante el bear 2022
   (no solo yield farming), con vídeos de "plan de inversión del año que viene" que va
   actualizando en tiempo real según la fase del ciclo. El audit anterior solo encontró
   3 vídeos de 2022 (todos DeFi/yield) — puede que falten transcripts en el corpus de
   esas fechas, o que el agente no los localizara bien. **Acción sugerida**: buscar en
   `agentes/lmec/yt-transcripts/` vídeos de 2022 con keywords "mentalidad", "hodl",
   "acumular", "plan del año que viene", "rotar cartera" — puede que falte ingerir esos
   vídeos del canal (usar `agentes/tools/fetch_captions.py --persona lmec --since 20220101`).
2. **Cowen ETH "banda de regresión → ATH"**: re-verificar con transcripts de 2023-2024
   (no solo ago-2025) si predijo que ETH no rompería su ATH de 2021 hasta volver primero
   a su banda de regresión logarítmica — el usuario confirma que esto SÍ pasó este ciclo.

## Pendiente técnico (sin resolver, próxima sesión)
1. **Portfolio: $54k (nuestro) vs $62k (Nansen)** — brecha de ~$8k. Candidatos del hueco
   (comparar con captura de Nansen "Holdings" por protocolo: Wallet $34.78k, Orca $19.22k,
   Uniswap V3 $4.60k, ProjectX $1.51k, Hyperliquid $1.45k, Kamino $457, Jupiter DAO $69):
   - Verificar que `fetchV3Positions` (Uniswap) esté devolviendo el valor completo de la
     pool BNB/WETH (~$4.6k en Nansen) — puede que la detección automática V3 no la esté
     cazando bien (o el sandbox nunca pudo probarlo en vivo, red bloqueada aquí).
   - `data/manual_assets.json` (repo privado DeFi-Tracker) tiene JUP con `amount: 0`
     (placeholder) — el usuario nunca dio la cantidad real de JUP stakeado en Jupiter DAO
     (~$69 según Nansen, vote.jup.ag). Hay que rellenarlo o pedírselo de nuevo.
   - Verificar Kamino (`fetchKamino` en api/portfolio.js) — nunca se pudo probar en vivo
     (sandbox sin red); Nansen marca $457 en Kamino, comprobar que el parsing coincida
     con la respuesta real de `api.kamino.finance`.
   - Ya generalizado (debería estar resuelto tras el redeploy): tokens Solana sueltos
     vía Jupiter (JUP, KMNO, MELANIA, POL, AVAX, ETH-wrapped) — antes solo veíamos 3
     mints hardcodeados. Confirmar con el usuario que ya aparecen tras el último push.
2. **Rediseño visual "más profesional, menos hecho por IA"** — el usuario pidió que
   `portfolio.html` (y quizá el resto) se parezca más a Nansen: tabs superiores
   (Overview/Holdings/Transactions/PnL), tarjetas de protocolo clicables arriba tipo
   "chips" (Wallet $34.78k · Orca $19.22k · ...), iconos de token/protocolo, sparklines
   de gainers&losers, un "Risk Profile" bar (large-cap/stables/mid/micro/small-cap).
   **No se ha empezado este rediseño** — es la tarea más grande pendiente. Sugerencia:
   crear un sistema de diseño consistente (tipografía, espaciado, iconos SVG en vez de
   emoji, tarjetas con sombra sutil) y aplicarlo a portfolio.html primero, luego decision.html.

## Automatizaciones activas
- `.github/workflows/ingest-transcripts.yml` — diaria 06:30 UTC, baja subtítulos nuevos
  (yt-dlp, máx 5 vídeos, últimos 10 días) de los 3 canales, commit automático.
- `.github/workflows/decision-snapshot.yml` — lunes 09:00 UTC, snapshot de la decisión
  del día a `data/decision_history.json` (histórico + scorecard de acierto en decision.html).
- `.github/workflows/alerts.yml` — diario, alertas de señales (Telegram, heredado).
- **Routine "actualizar-kb-senales-agentes"** (Claude Code Remote, viernes 10:00 UTC,
  sesión nueva cada vez, notificación push): lee transcripts nuevos de la semana,
  actualiza senales.json de cada agente (nunca borra, siempre con cita), actualiza
  regimen_actual y cambios_opinion, y las tarjetas de decision.html si la postura cambió.

## Canales YouTube (para fetch_captions.py)
- LMEC: `https://www.youtube.com/@LaMejorEstrategiaCriptomonedas/videos` (español)
- Cowen: `https://www.youtube.com/@IntoTheCryptoverse/videos` (inglés)
- OnChainMind: `https://www.youtube.com/@OnChainMind/videos` (inglés)

## Wallets del usuario (repo privado DeFi-Tracker, data/wallets.json)
- Solana: `DGL6MYPYaCPQQK5CxYpWLkSgMrSDQsh2eex9WLG8AgNr`
- EVM (una sola, multi-chain): `0xe555D4983536a513A6C26843cae16612c8C3104F`

## Contexto de negocio (para el plan de guerra BTC)
- BELROGAM SL: colchón operativo intocable ~€60k, neto medio mensual ~€12-15k (variable),
  reservas confirmadas con ~3 meses de visibilidad (v_proyeccion_reservas de Supabase).
- Plan de entrada BTC (registrado en el diario, DeFi-Tracker/data/journal.json):
  Fase 0 (hasta 31-ago): sin compras salvo BTC<$60k. Fase 1 (sep, si hay debilidad):
  DCA semanal. Fase 2 (Q4, suelo esperado oct-nov): desplegar pólvora. Fase 3 (~mar-2027,
  3ª ruptura BMSB de LMEC): compra fuerte. BELROGAM compra spot, hold 3 años — libro en
  `DeFi-Tracker/data/belrogam_portfolio.json` (vacío, a la espera de la 1ª compra real).
- Estrategia declarada: seguir el marco de Cowen (DCA por risk metric + estacionalidad
  midterm), con niveles de LMEC (200W, realized, BMSB) como refuerzo.

## Estilo de trabajo esperado (instrucciones del usuario, repetidas)
- SIEMPRE citas verbatim reales de los transcripts — nunca inventar señales/umbrales.
- Sintaxis-check todo (`node -e 'new Function(js)'`) antes de commit.
- Commits con mensaje descriptivo + co-authored-by Claude (formato ya usado en el repo).
- No preguntar por confirmación para tareas ya en marcha — actuar y avisar.
- El usuario se queda sin tokens fácilmente en sesiones largas — ser eficiente, no
  releer archivos innecesariamente, usar Agent en paralelo para investigaciones grandes.
