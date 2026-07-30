# Framework TÁCTICO de Glassnode — DIRECCIÓN y NIVELES (reverse-engineering)

**Qué es:** reconstrucción del método con el que Glassnode decide **dirección** (¿alcista o bajista?) y
**niveles/rangos** (¿dónde frena el precio?) a horizonte de **semanas–meses**. Es el **gemelo on-chain** de
`../derivados_glassnode/framework.md` (que cubre posicionamiento/vol). Juntos dan el paquete completo:
**on-chain = el DÓNDE y la DIRECCIÓN · derivados = el COMBUSTIBLE y el MOMENTO**.

**Fuente:** barrido de los **328 Week On-Chain** archivados (2019→jul-2026) en el KB privado
(`research/glassnode-kb/articulos/` del repo DeFi-Tracker), leídos íntegros por 12 extractores en paralelo.
**NO es texto oficial de Glassnode** — es el marco destilado de lo que ellos escriben, con sus umbrales
literales y sus propias advertencias.

> ### ⚠️ Cobertura honesta del corpus
> **272 de 328 artículos están completos. 56 son stubs** (solo intro, el cuerpo no se archivó):
> **78% de 2022** (39/50) y **26% de 2021** (14/52). **2023→2026 está completo al 100%.**
> **Mitigado (30-jul-2026):** se bajaron 214 transcripts del canal de YouTube y **67 son de 2022**,
> las mismas ediciones del WoC en vídeo. Cubren el hueco, pero como auto-subs: valen para el
> razonamiento, no para citar cifras exactas. Ver `README.md`.
>
> Consecuencia: el método aquí descrito es **sólido para 2023-2026** (que es además el método que usan HOY,
> mucho más formalizado) y **flojo en el bear de 2022** — justo el análogo del régimen actual. Para cerrar
> ese hueco **se intentó re-ingestar y no se pudo** (0 de 56 recuperados: están cerradas a
> miembros). La cobertura de 2022 son los vídeos. Ver `README.md`.

---

## A) LA IDEA CENTRAL: el mercado es una escalera de *cost basis*

Todo su análisis de nivel se apoya en una sola pregunta: **¿a qué precio compró cada grupo de holders?**
Ese precio medio (*cost basis*) es un imán de comportamiento: cuando el precio vuelve a él, la gente que
estaba atrapada **vende para salir en tablas**, y la que estaba en ganancia **defiende su posición**.

De ahí sale una **escalera de modelos de precio**, del suelo al techo. La posición del *spot* dentro de la
escalera **es** el régimen de mercado. No hay más magia que eso.

## B) LA ESCALERA (de abajo arriba) — los modelos de nivel

| Modelo | Qué mide | Cómo lo usan |
|---|---|---|
| **Realized Price** | Coste medio de **todo** el supply circulante | **Suelo estructural del ciclo.** Perderlo requiere "una dislocación sistémica tipo LUNA o FTX" [wk06-2026]. En 2026 ≈ $54-55k |
| **True Market Mean (TMM)** / *Active Investor Price* | Coste medio del supply **activo** (excluye monedas perdidas/dormidas y mineros) | **La línea divisoria bull/bear.** "Historically marking the dividing line between bear and bull market regimes" [wk21-2026]. ~50% de días históricos a cada lado [WoC09-2025] |
| **STH Cost Basis** | Coste medio de los holders **<155 días** (los más sensibles al precio) | **La frontera táctica.** Soporte en tendencia alcista, **resistencia en bajista** (ver §D) |
| **Bandas ±σ del STH CB** | Desviación estándar sobre el STH CB | **El rango operativo local.** −1σ = zona de sobreventa · +1σ/+2σ = techo local. Solo ~17,5% de la historia cotiza sobre +1σ [WoC21-2025] |
| **Supply Quantiles 0,75 / 0,85 / 0,95** | Niveles donde el 25% / 15% / 5% del supply queda en pérdida | Bandas de régimen: euforia sobre q0,95; bull lateral entre 0,85–0,95; **bajo q0,75 = risk-off** [WoC22-2025] |
| **URPD / Cost Basis Distribution** | Cuánto supply cambió de manos a cada precio | **Estantes** (cluster denso) = soporte/resistencia real · **air gaps** (zona vacía) = el precio la cruza rápido |
| **Cost basis por cohorte de edad** (1s, 1s-1m, 1m-3m, 3-6m) | La misma idea, por antigüedad de compra | "Cinta" rápida-a-lenta = indicador de momentum. Ej.: soporte $70,2k (1s-1m) vs resistencia $82,2k (1m-3m) [wk12-2026] |

## C) LOS 4 REGÍMENES DE CICLO (su brújula macro)

Definidos por dónde cotiza el spot en la escalera [WoC27-2024, WoC36-2024, WoC43-2024]:

| Régimen | Condición | Sesgo |
|---|---|---|
| **Deep Bear** | precio **< Realized Price** | Bajista profundo, zona de capitulación |
| **Early Bull / Recovery** | entre **Realized Price y TMM** | Recuperación, aún frágil |
| **Enthusiastic Bull** | entre **TMM y el ATH previo** | Alcista sano |
| **Euphoric Bull** | **> ATH previo** | Alcista eufórico → vigilar distribución |

**Variante por LTH** (mismo esquema con el múltiplo de ganancia de los holders largos) [WoC47-2023, WoC26-2024]:
`LTH-MVRV <1` capitulación · `1,0–1,5` transición · `1,5–3,5` equilibrio · `>3,5` **euforia** (LTH con +250% de
ganancia → venta acelerada).

## D) 🔑 LA ASIMETRÍA (lo más accionable del framework)

**El mismo nivel es soporte o resistencia según de qué lado vengas.** Lo dicen explícitamente:

> *"Approached from below in a downtrend, the break-even of recent buyers acts as a **rejection zone**
> (holders about to be made whole sell). Above it, the profile thins into an air pocket."* [wk29-2026]

> *"Should the key on-chain support level between $45k and $47k fall, many of our observations may swap
> from **strong support to heavy resistance**."* [WoC10-2021]

**Traducción operativa:**
- **En bear (precio bajo el STH CB):** el STH CB es **TECHO**. Cada rally que llega ahí encuentra vendedores
  (los atrapados salen en tablas). Los rallies "typically required **multiple attempts** before resolution"
  [wk16-2026], retrocediendo a la banda −1σ entre intentos.
- **En bull (precio sobre el STH CB):** el STH CB es **SUELO**. Los retests son la compra del dip.
- **El evento que cambia el régimen** es reclamarlo **y sostenerlo**, no tocarlo: *"pre-bull market phases
  require **weeks to months** of sustained consolidation around this model"* [wk20-2026].

## E) OSCILADORES DE CONFIRMACIÓN (¿el régimen está cambiando?)

Los niveles dicen *dónde*; estos dicen *si va en serio*. **Umbrales literales del corpus:**

| Oscilador | Umbrales que ellos citan |
|---|---|
| **STH-MVRV** | `1,0` = breakeven de compradores recientes. Reclamarlo es **condición explícita** de transición pre-bull [wk24-2026] |
| **% STH Supply in Profit** | **~54,2%** = techo típico de rally de bear ("peak distribution pressure") [wk15/16/29-2026] · **60% (−1σ)** = inicio de bear profundo · **>75%** = confirma bull · **>90% (+1σ)** = euforia |
| **Realized P/L Ratio** | `<1` régimen de pérdida en exceso · `1–2` transición · **`>2` sostenido = "genuine bull capital flow"** [wk20/07-2026] · `2–5` bull temprano · `>9` agotamiento de demanda |
| **SOPR / STH-SOPR** | `1,0` es el eje. En bull, los **undercuts breves de 1,0 = compra del dip**; bajo 1,0 sostenido = bear ("textbook bear market" con STH-SOPR 0,985 [wk10-2026]) |
| **NUPL** | `<0,12` capitulación · `0,12–0,35` bajo · `0,35–0,59` alto · `>0,59` muy alto/euforia · `0,75` frontera creencia→euforia |
| **Sell-Side Risk Ratio** | **Ambos extremos preceden volatilidad**: alto = el mercado debe reencontrar equilibrio; bajo = agotamiento, "todos los que querían vender ya vendieron" |
| **Accumulation Trend Score** | `<0,1` distribución fuerte · `~0,5` equilibrio frágil · `→1` acumulación de convicción |
| **AVIV z-score** (spot vs TMM, normalizado 4 años) | `< −1` = descuento extremo (jun-2026 tocó −1,09) |
| **STH-SOPR z-score** | `−2` = **capitulación severa** (jun-2026 llegó a −1,86, a 0,14σ) |
| **Realized Loss (enfriamiento)** | Condición de suelo: LTH realized loss **<$25M/día** [wk13-2026] o **<1k BTC/día** [wk14-2026] |

## F) EL ÁRBOL DE DECISIÓN SEMANAL (cómo lo encadenan)

1. **¿Qué régimen?** Sitúa el spot en la escalera (Realized Price → TMM → STH CB). Eso da el **sesgo**.
2. **¿Dónde están las paredes?** URPD: estante denso abajo = soporte; cluster arriba = oferta pendiente;
   air gap = por donde el precio corre rápido (**y donde NO conviene poner un rango de LP estrecho**).
3. **¿El sesgo está cambiando?** Osciladores (§E): ¿STH-MVRV reclama 1,0? ¿RPL Ratio sobre 2? ¿% supply
   in profit rompe su umbral?
4. **¿Hay combustible y cuándo?** Aquí entra el **framework de derivados**: funding/OI/skew/VRP.
5. **Macro como veto:** *"a durable recovery will require either the DXY to break below 99 with conviction
   or the 10-Year to compress toward 4,2%"* [wk23-2026]. Si el techo macro sigue, los rallies son de alivio.

**Regla maestra de composición:** un nivel **solo** no decide; un oscilador **solo** tampoco.
*"To maximise the value of on-chain insights, it is important to seek **confluence** between multiple
metrics"* [WoC10-2021].

## G) GUARDARRAÍLES (lo que ellos mismos declaran)

- **Necesario ≠ suficiente:** *"Reclaiming this level is a **necessary but not sufficient** condition for a
  structural transition"* [wk20-2026].
- **Un giro no prueba agotamiento:** *"One turn does not prove exhaustion, and a fresh shock could restart it"* [wk28-2026].
- **El consenso puede ser contrarian:** sobre el Accumulation Trend Score — *"overwhelming consensus behavior
  is not always a reliable indicator of future direction (**and can in fact be a contrarian one**)"*, ilustrado
  con el ATH de nov-2021, donde la acumulación fuerte precedió al techo [WoC21-2025].
- **Vol baja ≠ dirección:** en bear, la compresión de volatilidad "ha roto en **ambas direcciones**, con poco
  sesgo direccional evidente" [WoC42-2022].
- **Squeeze ≠ tendencia:** *"it flips constructive with breadth and follow-through, **not with one squeeze**"* [wk29-2026].
- **Las comparaciones de ciclo son analogías, no pronóstico:** *"This comparison is not a forecast... but rather
  a framework for calibrating the potential depth and duration"* [wk14-2026].
- **Datos sucios:** métricas crudas (CDD, Liveliness, SOPR, Realized Cap) se distorsionan con movimientos
  internos de exchanges o wallets grandes (Mt.Gox, Bitfinex) → usar siempre la variante **entity-adjusted**.
- **Balances de exchange:** disclaimer permanente — pueden no capturar todas las reservas.

## H) CÓMO EVOLUCIONÓ EL MÉTODO (por qué solo vale lo reciente)

| Etapa | Método dominante | ¿Sirve hoy? |
|---|---|---|
| **2019–2020** | GNI / "Market Compass" (índice propietario de 4 regímenes) + métricas sueltas (Reserve Risk, NUPL) | ❌ Descontinuado |
| **2021–2022** | Cohortes LTH/STH, SOPR, URPD, Mayer Multiple, Thermocap | 🟡 Parcial (y mal archivado) |
| **2023–2026** | **La escalera de cost basis** (Realized Price / TMM / STH CB / quantiles) + osciladores normalizados (z-scores, bandas σ) | ✅ **Es el método actual** |

**Implicación:** para backtestear, **la ventana correcta es 2023→hoy**, no el corpus entero. Ellos mismos
cambiaron de herramientas; mezclar épocas mezcla métodos distintos.
