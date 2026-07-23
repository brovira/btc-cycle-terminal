# Memoria de proyecto — BTC Cycle Terminal (para retomar en otra sesión/LLM)

**Propósito:** terminal personal de inversión en BTC. Sigue el método de analistas (LMEC,
Cowen) + investigación propia (Patrón temporal) con citas verbatim de sus transcripts,
agrega señales, y gestiona el capital real (personal + BELROGAM SL) para decidir
cuánto/cuándo comprar.

> ## Estado a 23-jul-2026 (última sesión) — léelo primero
> - **Trabajamos en paralelo con "codex"** (otra IA). Codex hizo el sistema de diseño
>   `dashboard.css` (scoped bajo `.dashboard-page` + `.page-<name>`). Su rama
>   `codex/fix-cashflow-supabase` está **mergeada en main** (cero commits sin integrar).
> - **Las 3 señales que seguimos** (idénticas en decision.html e index.html):
>   1. **Cowen · DCA** = risk metric < 0,3 (regresión log-log; implementación en `risk.js`).
>   2. **LMEC · suelo** = **53 semanas desde el TECHO** (2025-10-06) → **oct/nov 2026**.
>      ⚠️ CORREGIDO esta sesión: antes usaba un eje inventado "semanas del halving (125)".
>      LMEC NUNCA razona en semanas del halving — siempre desde el techo (su vídeo más
>      reciente: `lmec/04-plan-completo-2027`). Reframeado en decision.html, index.html,
>      lmec.html y los presets del backtest (topw/botw en vez de halvw).
>   3. **Patrón · ventana de suelo** = 52-58 semanas tras el techo → oct-nov 2026
>      (cálculo propio, n=3, no es cita de nadie).
> - **Cashflow BELROGAM RESUELTO**: `/api/cashflow` ahora es un **PROXY** al endpoint
>   `/api/cash` del dashboard de BELROGAM (NO recalcula nada, NO lee Supabase directo).
>   El "disponible para invertir" lo calcula el dashboard (suelo − impuestos − margen);
>   aquí solo se lee. Página dedicada: **`belrogam.html`**. Método en `sops/gestion_caja_inversion.md`.
> - **Auditoría exhaustiva hecha** (5 dimensiones, agentes en paralelo): sin bugs críticos.
>   Arreglos aplicados abajo. Único pendiente serio era privacidad (ver §Privacidad).

## Repos (en Claude Code Remote — ya en la sesión vía add_repo)
- **`brovira/btc-cycle-terminal`** (PÚBLICO) — la web (Vercel: btc-cycle-terminal.vercel.app).
  Todo el código, agentes/transcripts, KB de señales. **NUNCA commitear datos personales
  ni cifras reales del negocio aquí** (es público en GitHub aunque la web esté con contraseña).
- **`brovira/DeFi-Tracker`** (PRIVADO) — pipeline Python que decodifica la wallet Solana
  (Orca LP) desde on-chain, y guarda los datos personales (journal, wallets, baseline,
  btc_compras). Los NÚMEROS del plan personal viven aquí, no en el repo público.
- **`belrogam`** (repo del negocio de alquileres — NO tocar salvo petición explícita; se
  lee su dashboard `/api/cash` de solo-lectura para el cashflow).

## Secrets (Vercel del proyecto btc-cycle-terminal)
- `SITE_PASSWORD` → gate de TODA la web (middleware.js, Edge). Reusa `DASH_PASSWORD` si falta.
- `DASH_PASSWORD` → ver datos personales (LP, cartera, diario, plan del ciclo). Gate en `lib/auth.js`.
- `GH_TOKEN` → fine-grained token sobre DeFi-Tracker (Contents R/W) para leer/escribir data/*.json.
- `SOLANA_RPC_URL` → RPC de Helius para el portfolio.
- **`BELROGAM_DASHBOARD_URL`** → URL del dashboard de BELROGAM en Vercel (sin `/api/cash`).
- **`CASH_API_TOKEN`** → MISMO valor que el `CASH_API_TOKEN` del proyecto Vercel del dashboard
  de BELROGAM (bearer que autoriza su `/api/cash`, fuera de su login de cookie). Generado esta
  sesión; vive SOLO en Vercel (no en el repo). Si `/api/cashflow` da 401 → el token no coincide
  entre los dos proyectos.
- `BIRDEYE_API_KEY` → no usado (precios Solana vía Jupiter, gratis, sin key).

## Páginas (raíz del repo). Body `class="dashboard-page page-<name>"`, estilo en `dashboard.css`.
- **`index.html`** — hub, reordenado esta sesión: 1) **Estrategias·Señales** (LMEC · Cowen ·
  BELROGAM plan del ciclo) 2) **Portfolio** (Mi portfolio · LPs · loop futuro) 3) **Herramientas**
  (backtest · montecarlo) 4) **Trading** (derivados, al fondo, "pendiente de investigar"). El
  hero "¿Qué hago hoy?" usa las MISMAS 3 señales que decision.html.
- **`decision.html`** — "¿Qué hago hoy?": veredicto + **3 señales que seguimos** (chips) +
  **barra del plan del ciclo** (DCA on → suelo proyectado → fin compra) + tarjetas **LMEC ·
  Cowen** (fase del ciclo, checklist EN VIVO contra el KB, qué hace/por qué, pólvora, aviso de
  auditoría, link a su framework, **botón "Ver en el backtest"** con su estrategia precargada)
  + tarjeta **Patrón** + **gráfica de fases** (modos LMEC/Cowen/Patrón/Todos, bandas
  compra/venta). "Mi plan del ciclo" (3 libros: persona física/BELROGAM/loop). Auto-refresco 30 min.
  - Gráfica de fases esta sesión: eje X arranca en la **1ª compra (2012)**; **eje Y se
    reajusta a lo visible al hacer zoom** (handler plotly_relayout, doble clic resetea);
    banda de compra del patrón añadida para el mini-ciclo 2011; ventas añadidas para los
    techos 2011 y 2013 (antes sin banda). Confluencia "Todos" = solo ciclos con halving
    (la compra 2012 solo sale en modo Patrón, no en Todos — decisión del usuario, no inventar).
- **`belrogam.html`** (NUEVO esta sesión) — plan del ciclo de BELROGAM: objetivo de
  acumulación, excedente de caja invertible (lee `/api/cashflow` → escenarios confirmado/
  esperado, margen 0-3m, desglose saldo→suelo→impuestos→margen→disponible), órdenes
  escalonadas, flujo semanal (Plotly). NO hardcodea cifras (todo del endpoint en vivo).
- **`lmec.html` / `cowen.html` / `onchainmind.html`** — panel de cada agente (framework,
  indicadores, verdict box). lmec.html reframeado al eje del techo esta sesión.
- **`portfolio.html`** — cartera Nansen-style (Overview + Holdings, agrupa por activo
  subyacente, filtros wallet/chain, "ocultar <$5" por defecto). Valor de LPs = valor ACTUAL
  retirable (`performance.currentValueUsd`), no lo aportado. Backend `api/portfolio.js`.
- **`lp.html`** — DeFi-Tracker: LPs de Orca, PnL, "farming desde cero" (línea base), diario.
- **`backtest.html`** — backtester con presets de los 3 (citas reales), risk-metric (variante
  walk-forward propia, NO usa risk.js), modo DCA, builder libre. Deep-link `?strat=<clave>`
  precarga una estrategia (usado por los botones de las fichas). Presets LMEC en eje del techo.
- **`montecarlo.html`, `derivados.html`** — sin cambios recientes.

## risk.js (NUEVO esta sesión) — fuente única de la métrica de riesgo
`risk.js` (script en raíz, `window.BTCRisk.riskNow(D)`): la métrica de Cowen (desviación de
log(precio) sobre regresión log-log, normalizada 0-1 con min/max de toda la serie) vivía
copiada a mano en decision.html e index.html; ahora vive una sola vez y ambos la cargan
(`<script src="risk.js">`) y delegan. backtest.html usa a propósito una variante distinta
(walk-forward/expanding window, sin lookahead) que NO depende de risk.js.

## APIs backend (Vercel serverless, `/api`)
- `cashflow.js` — **PROXY** a `${BELROGAM_DASHBOARD_URL}/api/cash` con bearer `CASH_API_TOKEN`.
  Devuelve el body tal cual. NO calcula caja. Diagnóstico si faltan envs; 401 upstream → 502.
- `private.js` — sirve archivos whitelisted del repo privado (orca_pnl, journal, wallets,
  btc_compras…) con contraseña (allowlist, sin path traversal).
- `journal.js`, `baseline.js` — diario y línea base del farming.
- `portfolio.js` — agrega el patrimonio: Solana (RPC + Jupiter), EVM (Blockscout multi-chain),
  Hyperliquid, Kamino, posiciones V3 auto-detectadas (Uniswap ETH + ProjectX HyperEVM).
- `coinmetrics.js`, `coinglass.js`, `birdeye.js` (proxies de datos públicos de mercado).

## Privacidad (IMPORTANTE)
- **SOP `sops/gestion_caja_inversion.md`**: se copió del repo belrogam pero traía cifras
  reales del negocio (saldos, revenue, márgenes). Esta sesión se **quitaron todas las cifras**
  (solo queda el método: fórmula, reglas, calendario). El número real se lee de `/api/cash`.
- **`decision.html` PLAN_CICLO**: dejó de hardcodear cifras personales (objetivo 55k/1 BTC,
  órdenes 60/55/50/45k, escalera, sueldo). Ahora solo estructura + texto genérico; los NÚMEROS
  vienen del JSON privado (`/api/private?file=btc_compras`: objetivo_eur, objetivo_btc, ordenes…).
  Hub también genericizado.
- **Purga del historial de git PENDIENTE (opcional)**: las cifras del SOP ya estuvieron en
  commits públicos (7f8439c → 64954f0). Se decidió NO reescribir historial ahora (fuerza
  push, y los datos ya estuvieron públicos → darlos por expuestos). La rama de codex está
  mergeada, así que si algún día se purga, se puede hacer completo. Por ahora, sin tocar.

## KB de señales (agentes/<agente>/senales.json) — LO MÁS VALIOSO
Cada señal con **cita verbatim + archivo fuente**. Regla de oro: nunca añadir señal sin cita.
- `agentes/lmec/senales.json` — ~26 señales. Clave temporal: **techo→suelo 53 sem → oct/nov
  2026** (04-plan-completo-2027, más reciente); 54 sem/"mediados nov" (02) queda descartado.
  2ª→3ª ruptura BMSB ~280 días → bull ~mar-2027. DCA por niveles de precio, no por calendario.
- `agentes/cowen/senales.json` — ~25 señales. DCA < 0,3 risk (verbatim), venta > 0,6, estacional
  midterm (2ª mitad tras el mínimo de junio).
- `agentes/onchainmind/senales.json` — ~27 señales. Retirado de las tarjetas de decisión (ver abajo).

## Auditorías de track-record (agentes/<agente>/track_record.md + audits)
- LMEC (7/10 general; 4/10 ciclo 2022-25): no verificable que comprara el suelo real nov-2022
  en tiempo real (hueco de corpus jul-22→ene-23; "compré a 15,7k" = autocita retrospectiva).
  Venta 2025 tardía. **Nunca vende BTC en sí** (rota altcoins→stable).
- Cowen (6/10 general; 5/10 ciclo 2022-25): fuerte en MACRO (dominance, rallies contratendencia
  2026 con nivel casi exacto); sin venta en ningún techo en tiempo real. **Nunca vende BTC**.
- OnChainMind: NUNCA dio señal de venta en tiempo real (solo retrospectiva). **Retirado de las
  tarjetas de decision.html** (sirve solo para timing de compra). Su panel `onchainmind.html`
  sigue disponible; en decision.html quedan restos muertos (`ocmClock()`, fetch de su KB sin usar)
  — inofensivos, se pueden limpiar cuando toque.

## Pendiente de verificar (el usuario lo pidió, AÚN sin cerrar)
1. **LMEC 2022 "mentalidad + acumular BTC"**: el usuario dice que LMEC ya hablaba de holder
   mindset/acumular en el bear 2022, no solo yield. El audit solo halló 3 vídeos 2022 (DeFi).
   Buscar/ingerir vídeos 2022 (`fetch_captions.py --persona lmec --since 20220101`).
2. **Cowen ETH "banda de regresión → ATH"**: re-verificar con transcripts 2023-24 si predijo
   que ETH no rompería su ATH de 2021 hasta volver a su banda de regresión (el usuario confirma
   que pasó).

## Pendiente técnico
1. **Portfolio: brecha ~$8k vs Nansen** (nuestro ~$54k vs $62k). Revisar fetchV3Positions
   (pool BNB/WETH ~$4.6k), `manual_assets.json` JUP con amount 0, Kamino (~$457) — nunca
   probado en vivo (sandbox sin red). Confirmar tras redeploy que los tokens Solana sueltos
   (Jupiter) ya aparecen.
2. **Rediseño visual**: codex ya hizo `dashboard.css` (sistema de diseño). Revisar que todas
   las páginas lo usen de forma consistente.
3. **loop.html**: panel dedicado del loop de Aave — se construye cuando el usuario abra la posición.
4. **data/btc_compras.json** (DeFi-Tracker): crear cuando haya compras reales; ahí van los
   números del plan (objetivo_eur, objetivo_btc, ordenes, escalera) que se genericizaron del repo público.

## Contenido / Twitter (regla del usuario)
- **Cada vez que se enciende una señal nueva, el usuario debe publicar un tweet** sobre esa
  señal y las decisiones que toma al respecto (usa una cuenta para crecer followers). Al
  detectar una señal nueva (o un cambio de postura en decision.html / en la Routine semanal
  de KB), **recordárselo y ofrecerle el borrador del tweet + la imagen** (mismo estilo que
  `scratchpad/plan_en.html`: dark, curva del ciclo, chips; render a PNG 1600×900 con Chromium
  headless). Sin revelar el "secret sauce" (nombres de analistas, umbrales exactos, reglas de
  las señales) — solo la tesis pública y las decisiones.

## Plan de ALTS (jul-2026, en construcción)
El usuario quiere un plan de alts **basado en datos y decidido de antemano** (como el de BTC),
para no improvisar. Analista de referencia: **Cowen** (experto en rotación). Investigación de su
KB hecha (agente); claves:
- **Cowen es escéptico/bajista con alts este ciclo.** NO espera altseason en 2026 (quizá 2027-2029
  con política laxa). Tesis: "todo sangra hacia BTC"; alts = "penny stocks de esta generación".
- **Su señal de rotación es MACRO, no precio.** GATES para pesar alts (ninguno encendido hoy):
  1. **Fed funds < 2-year yield** duradero (tipo neutral). Hoy ~3,75 vs 3,77 → igualados.
  2. **(TOTAL3−USDT)/BTC ("all Bitcoin pairs") ≥ ~0,25** sostenido. Oct-2025 = 0,29.
  3. **BTC.D EXCLUYENDO stables** rompe a la baja (desde ~67-68%; techo previo ~70% jun-2025).
  4. **Social/retail** haciendo higher highs (hoy ~0,25 = nivel 2018).
  5. **ETH/BTC** reclaim duradero de la **20-month MA** (rechazado en BMSB y 20M MA).
  - Orden de rotación cuando enciendan: BTC → **ETH** (su referencia) → resto.
  - **M2 lo RECHAZA** explícitamente (no ingerir). **TON y HYPE: fuera de su marco** (0 menciones).
- **Backtest:** los gates de PRECIO (dominance, 0,25, ETH/BTC vs 20M) son backtesteables; el gate
  MACRO (tipos/social) no lo es con solo precio → documentar como contexto.
- **DOS CUBOS** (decisión del usuario): **spot** (núcleo BTC + satélite alt *gated*, holdear) vs
  **LP/yield aparte** (liquidez distinta del spot).
- **Emparejamiento de LP por CORRELACIÓN** (matriz que dio el usuario, jul-2026): emparejar
  volátiles MUY correlacionadas minimiza el IL. **Spot** (baja corr): HYPE (0,48-0,59), GRAM/TON
  (0,36-0,56). **LP** (alta corr 0,77-0,89): ETH-SOL 0,89, BTC-ETH 0,88, BTC-SOL 0,84, BNB-ETH/SOL
  ~0,78, BTC-BNB 0,77. JLP (cesta SOL-heavy + fees) = candidato del cubo LP/yield.
- **Filosofía de LP del usuario:** "set it wide and let it ride" (rangos anchos, pasivo), pero
  vigilar el precio y **tomar algo de profit si se desvía mucho de su media móvil** — asume
  **regression to the mean**, con "compass" = **200W MA** (largo plazo/ciclos) o **STH-SOPR** (más
  tendencia actual).
- **Hecho:** objetivo de asignación editable en `portfolio.html` (renderNetWorth): % target por
  categoría (BTC/Estables/Blue chips/Otros) + desviación en $ ("faltan/sobran"), persistido en
  localStorage (`btc-term-alloc-target-v1`), con nota de estrategia (núcleo BTC, alts gated, HYPE/
  TON spot, LP entre correlacionadas, cubo LP aparte).
- **Pendiente (autorizado por el usuario):** ingerir **BTC.D (+ex-stables), (TOTAL3−USDT)/BTC,
  ETH/BTC, Fed funds vs 2y (FRED)** como API(s) nuevas (corren server-side, hay red) + construir un
  **panel "Rotación de alts"** con los 5 gates en semáforo (como el cockpit de BTC) + backtest de
  los gates de precio + correlación móvil JLP↔BTC/SOL.

## Automatizaciones
- `.github/workflows/ingest-transcripts.yml` — diaria, baja subtítulos nuevos de los 3 canales.
- `.github/workflows/decision-snapshot.yml` — snapshot de la decisión del día (histórico + scorecard).
- `.github/workflows/alerts.yml` — alertas de señales (Telegram, heredado).
- **Routine "actualizar-kb-senales-agentes"** (Claude Code Remote, viernes 10:00 UTC): actualiza
  senales.json de cada agente con transcripts nuevos (nunca borra, siempre con cita).

## Canales YouTube (fetch_captions.py)
- LMEC: `@LaMejorEstrategiaCriptomonedas` (español) · Cowen: `@IntoTheCryptoverse` (inglés)
- OnChainMind: `@OnChainMind` (inglés)

## Wallets (repo privado DeFi-Tracker, data/wallets.json)
- Solana: `DGL6MYPYaCPQQK5CxYpWLkSgMrSDQsh2eex9WLG8AgNr`
- EVM (una, multi-chain): `0xe555D4983536a513A6C26843cae16612c8C3104F`

## Contexto de negocio (para el plan BTC)
- BELROGAM SL: el "disponible para invertir" NO es el saldo — es el **suelo** proyectado
  (mínimo día a día) menos impuestos y margen. Lo calcula el dashboard de BELROGAM y se lee
  por `/api/cash`. Nunca recalcularlo aquí. Método en `sops/gestion_caja_inversion.md`.
- Plan de entrada: DCA ya en marcha (BTC rompió $60K, entrando en la 2ª mitad del año);
  órdenes escalonadas hacia el suelo; artillería gorda + loop para la ventana de suelo
  (oct-nov 2026); tras el suelo seguir DCA un tiempo más; luego hold ~3 años. BELROGAM compra
  spot, hold 3 años.

## Estilo de trabajo esperado (instrucciones del usuario, repetidas)
- SIEMPRE citas verbatim reales de los transcripts — **nunca inventar señales/umbrales**
  (regla reforzada esta sesión: no inventar confluencia donde LMEC/Cowen no llegan).
- Sintaxis-check todo (`node -e 'new Function(js)'`) + check de ids del DOM antes de commit.
- Commits descriptivos + co-authored-by Claude. Push a `main` (repo del terminal).
- No preguntar por confirmación para tareas ya en marcha — actuar y avisar. SÍ confirmar
  acciones irreversibles (force-push, borrar ramas) y decisiones sobre datos personales.
- El usuario se queda sin tokens en sesiones largas — ser eficiente, no releer de más,
  usar Agent en paralelo para investigaciones/auditorías grandes.
- Respuestas cortas, al grano, en español (bullets/negritas/tablas).
