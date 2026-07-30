# Especificación de backtest — de las reglas de Glassnode a código

**Para qué:** los frameworks dicen *qué* miran y con *qué* umbrales. Esto traduce cada regla a algo
**implementable y falsable**: qué serie exacta hace falta, de qué archivo, qué decisión de diseño queda
abierta, y si la regla es testeable o no. Sin este paso, cualquier backtest acaba siendo una elección
arbitraria disfrazada de resultado.

**Fuentes:** `framework_direccion.md` (on-chain) · `../derivados_glassnode/framework.md` y
`estrategia_leverage.md` (posicionamiento) · `catalogo_indicadores.md` (peso real de cada indicador) ·
`extraccion_woc/informe_g*.md` (las ~100 reglas literales con cita).

---

## 0) Datos disponibles (tras la extracción de Checkonchain, 30-jul-2026)

| Serie que necesitamos | Archivo · nombre de la serie | Cobertura |
|---|---|---|
| STH Cost Basis | `pricing__pricing_costbasisoriginals` · `STH Cost Basis` | 2009→hoy |
| True Mean Price | idem · `True Mean Price` | 2009→hoy |
| Realised Price | idem · `Realised Price` | 2009→hoy |
| LTH Cost Basis · Cointime · Vaulted · 128/200DMA | idem | 2009→hoy |
| % supply en profit (total) | `supply__breakdown_pnl` · `Percent Supply in Profit/Loss` | 2009→hoy |
| Supply STH/LTH en profit y loss | `supply__breakdown_lthsth_pnl_0` · `STH in Profit`/`STH in Loss` | 2009→hoy |
| Realised P/L Ratio (all/STH/LTH) | `realised__realisedpnl_ratio_{all,sth,lth}` | 2009→hoy |
| Sell-Side Risk Ratio | `realised__sellsideriskratio_all` · `ALL Sell-side Risk Ratio` | 2009→hoy |
| MVRV Z-Score | `unrealised__mvrv_all_zscore` · `MVRV Z-Score` | 2009→hoy |
| AVIV Z-Score | `unrealised__mvrv_aviv_zscore` · `AVIV Z-Score` | 2009→hoy |
| Liveliness / A2VR | `cointime__liveliness` | 2009→hoy |
| Funding rate | `derivatives__derivatives_futures_fundingrate` | **2020-03→hoy** |
| Open Interest por exchange | `derivatives__derivatives_futures_oi_byexchange_0` | **2020-02→hoy** |
| Spot CVD | `derivatives__derivatives_spotvolume_cvd_0` | 2014→hoy |
| ETF flows por emisor | `etfs__etf_flows_1` (+ cumflows, balance) | **2024-01→hoy** |
| URPD (estantes / air gaps) | `urpd__urpd`, `urpd__urpd_cohort` | **distribución, snapshot** |
| Precio diario | Binance + Coin Metrics (ya en el terminal) | 2010→hoy |
| DVOL / VRP | `api/voldata` (Deribit) | **2021-03→hoy** |
| 25d Skew (1W/1M/3M/6M) | `derivatives__options_25deltaskew` | **~2021→hoy** ✅ |
| ATM Implied Vol por tenor | `derivatives__options_atmimpliedvolatility` | ~2021→hoy ✅ |
| Realized Volatility | `technical__technical_realizedvolatility` | 2009→hoy ✅ |

**Ventanas efectivas (manda la serie más corta de cada regla):** on-chain puro **2009→ (4 ciclos)** ·
cruce con derivados/vol **2021→ (ventana fijada, ver §5)** · con ETF **2024→**.

---

## 1) Reglas de NIVEL (la escalera)

| ID | Regla (suya, literal o parafraseada con cita) | Umbral | Datos | Testeable |
|---|---|---|---|---|
| **N1** | *"Approached from below in a downtrend, the break-even of recent buyers acts as a rejection zone"* [wk29-2026] → en bear el STH CB es **techo**; en bull, **suelo** | cruce | STH CB + precio | ✅ |
| **N2** | TMM = *"the dividing line between bear and bull market regimes"* [wk21-2026] | cruce | True Mean Price | ✅ |
| **N3** | Realised Price = suelo estructural; perderlo requiere *"a systemic dislocation similar to LUNA or FTX"* [wk06-2026] | cruce | Realised Price | ✅ |
| **N4** | 4 regímenes: Deep bear `<RP` · Recovery `RP→TMM` · Enthusiastic `TMM→ATH` · Euphoric `>ATH` | bandas | los 3 + ATH | ✅ |
| **N5** | Bandas ±1σ/±2σ del STH CB como rango local; −1σ = sobreventa, +1σ techo local (*solo 17,5% de la historia cotiza sobre +1σ* [WoC21-2025]) | ±σ | calculadas: **1 año móvil** (D1, su ventana) | ✅ |
| **N6** | *"Pre-bull market phases require **weeks to months** of sustained consolidation around this model"* [wk20-2026] — reclamar ≠ tocar | **cierre semanal ≥2 sem** (D2, su unidad) | precio + TMM | ✅ |
| **N7** | Air gaps: zonas de baja densidad de cost basis donde el precio corre rápido → **no poner rango de LP estrecho ahí** | densidad | URPD (snapshot) | 🟡 ver D3 |

## 2) Reglas de OSCILADOR (confirmación de régimen)

| ID | Regla | Umbral literal | Datos | Testeable |
|---|---|---|---|---|
| **O1** | STH-MVRV reclama 1,0 = condición explícita de transición pre-bull [wk24-2026] | `= 1,0` | **derivable**: precio / STH CB | ✅ |
| **O2** | % STH supply in profit: techo de rally de bear al acercarse a su media | **54,2%** [wk15/16/29-2026] | `STH in Profit/(Profit+Loss)` | ✅ |
| **O3** | idem: `−1σ ≈ 60%` inicio de bear profundo · `>75%` confirma bull · `>90% (+1σ)` euforia | 60/75/90% | idem | ✅ |
| **O4** | Realised P/L Ratio: `<1` pérdida en exceso · **`>2` sostenido = flujo de capital de bull genuino** · `2–5` bull temprano · `>9` agotamiento de demanda | 1 / 2 / 5 / 9 | `realisedpnl_ratio_all` | ✅ |
| **O5** | SOPR / STH-SOPR: en bull los *undercuts breves* de 1,0 = compra del dip; `<1` sostenido = bear (*"textbook bear market"* con 0,985 [wk10-2026]) | `1,0` | BGeometrics `sopr`, `sth-sopr` (4 años) | 🟡 ventana corta |
| **O6** | AVIV z-score `< −1` = descuento extremo (jun-2026 tocó −1,09) | `−1` | `AVIV Z-Score` | ✅ |
| **O7** | STH-SOPR z-score `−2` = capitulación severa (jun-2026: −1,86) | `−2` | `sth-sopr` + z móvil 4a | 🟡 ventana corta |
| **O8** | Sell-Side Risk Ratio: **ambos extremos preceden volatilidad** (alto = debe reencontrar equilibrio; bajo = agotamiento) | percentiles | `ALL Sell-side Risk Ratio` | ✅ |
| **O9** | Enfriamiento de Realized Loss como condición de suelo: `<$25M/día` [wk13-2026] o `<1k BTC/día` [wk14-2026] | absoluto | BGeometrics `realized-loss` | 🟡 ver D4 |
| **O10** | MVRV Z: techo `+2σ` / suelo `−1,5σ` sobre media móvil **de 1 año** (ellos calibran a 1a, no a toda la historia) [WoC06/07-2025] | ±σ 1a | `MVRV Z-Score` | ✅ |

## 3) Reglas de POSICIONAMIENTO (derivados) — de `estrategia_leverage.md §C`

| ID | Regla | Umbral | Datos | Testeable |
|---|---|---|---|---|
| **P1** | `EXIT_CROWDED_LONG` = funding ann MM3d **≥ +8%** Y z **≥ +1,5σ** Y OI **≥ p90/180d** Y **rotación de skew** put-rich→call-heavy (1W de ≥+10 a ≤+5 en ≤7d) | los 4 | funding + OI + **skew** | ✅ **completo** |
| **P2** | `EXIT_VOL_REALIZING` = VRP `<0` ≥2 días **O** skew `>+15` con P/C volumen `>1` | VRP<0 · skew>15 | IV + RV (**VRP derivable**) + skew | ✅ **completo** |
| **P3** | `SQUEEZE` (la única señal direccional, **3/3** en el track record) = funding `<0` sostenido 3d + OI subiendo `+10%` en 2-4 sem + reclaim de soporte on-chain | los 3 | funding + OI + STH CB | ✅ |
| **P4** | `REENTRY_CLEAN` = flush (OI −15% en ≤3d) + OI `≤p40` + funding `≤+11%` + VRP `≥+5` + skew 0–12 | los 5 | funding + OI + IV/RV + skew | ✅ **completo** |

## 4) Reglas de CRUCE — **la tesis de verdad**

| ID | Regla | Por qué importa |
|---|---|---|
| **X1** | Régimen on-chain (N1/N2) **×** semáforo de posicionamiento (P1-P4) → LP dentro/fuera **y** sesgo del trade | *"derivados = POSICIONAMIENTO; cost basis = el DÓNDE. La lectura completa es la intersección"* [framework.md §C5]. **Nadie la ha medido junta** |
| **X2** | Confluencia obligatoria: *"To maximise the value of on-chain insights, it is important to seek **confluence** between multiple metrics"* [WoC10-2021] → ¿mejora una regla al exigir 2-3 confirmaciones, o solo reduce el nº de señales? | Es la pregunta central de todo el método |
| **X3** | Veto macro: *"a durable recovery will require either the DXY to break below 99 or the 10-Year to compress toward 4,2%"* [wk23-2026] | ⚠️ requiere DXY y 10Y — **no los tenemos ingeridos** |
| **X4** | ETF flows como confirmación del spot bid (2º driver de sus conclusiones en 2026) | `etf_flows_1`, solo 2024→ |

---

## 5) ⚠️ DECISIONES DE DISEÑO — FIJADAS (30-jul-2026)

**Principio acordado con el usuario:** esta sección usa **solo el conocimiento de Glassnode**. Todo
parámetro debe venir de **sus artículos, con cita**. Lo que sea criterio operativo propio va aparte,
etiquetado como tal — nunca disfrazado de método suyo.

Por eso se releyó el corpus buscando sus definiciones operativas. **5 de 7 decisiones ya no son mías:**

| ID | Decisión | Valor FIJADO | Origen |
|---|---|---|---|
| **D1** | Ventana de σ / z-score | **Depende de la métrica, y ellos lo dicen:** MVRV Z → **1 año móvil** · AVIV z y STH-SOPR z → **4 años** | 📗 *"we have applied a **1-year rolling window** to the Z-Score calculation, resulting in a more refined and promising [transition]"* · *"Bull markets are characterized by prices trading between the **1-year mean**, and peaking around **2σ** above it"* · *"This chart uses a **[4-year Z-Score]** `sma(m1,1460)`"* · *"AVIV Ratio… its **4-year** z-score"* |
| **D2** | ¿Qué es "reclaim sostenido"? | **Cierre de vela SEMANAL por encima, ≥2 semanas** | 📗 *"Over the past **two weeks**, Bitcoin has struggled to **close a weekly candle above** this key level"* · *"**weekly close** above $70k, establishing this region as a meaningful near-term resistance"* · *"sustained **over multiple weeks**, would constitute a more meaningful signal"* |
| **D3** | ¿Qué es un "air gap"? | **percentil <20 de densidad en el bucket URPD** | ⚙️ **criterio propio** — ellos lo describen en cualitativo ("thinly populated"). Y el URPD es snapshot, así que **no es backtesteable en el tiempo**: queda como criterio del agente |
| **D4** | Umbrales absolutos ($25M/día) | **percentil de su propia historia** (reportando también el absoluto) | ⚙️ criterio propio, confirmado por el usuario. Un umbral en dólares de 2026 no es comparable con 2015 |
| **D5** | "Sostenido" en funding negativo | **3 días consecutivos** | 📗 `estrategia_leverage.md §C`, destilado de su corpus |
| **D6** | Horizontes de evaluación | **+2, +4, +8 semanas** | 📗 Su horizonte declarado es semanas-meses; sus llamadas se cumplen en 0-3 semanas (`track_record.md`) |
| **D7** | ¿Qué cuenta como acierto? | **Nivel:** dirección correcta a +4 sem · **LP:** PnL (fees−IL) vs estar siempre dentro | ⚙️ criterio propio: son objetivos distintos y no se mezclan |

**Umbral de % Supply in Profit, confirmado literal:** *"broken below its **−1 standard deviation
threshold near 60%**, and currently sits at approximately 57%"* → el 60% de O3 es suyo, no interpolado.

### Ventana temporal del backtest — FIJADA

**5 años (2021→2026)** para las reglas que cruzan familias (on-chain × derivados × vol), decisión del
usuario: maximiza el solape real. Las reglas **solo on-chain** se corren además sobre los **17 años**
completos (4 ciclos) porque los datos lo permiten. Los ETF entran en 2024 y se aceptan como serie corta.

| Alcance | Ventana | Ciclos |
|---|---|---|
| Solo on-chain (N1-N4, O1-O4, O6, O8, O10) | 2009→2026 | 4 |
| Cruce con derivados (P1-P4, X1, X2) | **2021→2026** | ~1,5 |
| Con ETF (X4) | 2024→2026 | — |

## 6) Lo que NO se puede testear (y hay que decirlo)

- ~~25d Skew histórico~~ → **RESUELTO (30-jul-2026)**: Checkonchain lo publica (`options_25deltaskew`,
  tenores 1W/1M/3M/6M, ~2021→hoy) — lo detectó el usuario; no salía en el índice porque su portada no
  enlaza todos los charts, hay que ir por el **sitemap.xml**. Con esto **P1 y P4 quedan completos** y la
  **rotación put→call sí es testeable** (el sello del techo del 10-oct-25: 1W de +18 a +3 vol pts en <1 sem).
- **URPD en el tiempo** → solo tenemos snapshots, no la serie histórica de la distribución.
- **DXY / 10Y** → el veto macro X3 necesita ingerirlos (fuente gratis: FRED). Pendiente.
- **Dealer gamma / GEX** → no hay fuente gratis; y es el 42% de sus conclusiones de 2026.

## 7) Orden de ejecución propuesto

1. **Caracterizar, no optimizar** (N1, N2): sobre 2009-2026, cada toque del STH CB y del TMM →
   ¿lo reclamó y aguantó, o rebotó? ¿qué hizo el precio a +2/+4/+8 semanas en cada caso?
   **Si los niveles no discriminan nada, no hay estrategia que construir encima.** Esto valida la premisa.
2. **Osciladores solos** (O2, O4, O6, O10) con **sus** umbrales literales, no optimizados.
3. **La confluencia X1/X2** — la hipótesis que de verdad importa para LP + trade táctico.
4. Solo entonces, si algo tiene edge: ajuste fino, y siempre reportando nº de señales y ventana real.

## 8) Regla de honestidad del informe

Todo resultado debe llevar: ventana real de datos · **nº de señales** (si <10, decirlo en grande) ·
si el umbral es **de ellos** o **nuestro** · qué patas quedaron fuera por falta de datos · y el
resultado del **caso base** (hold / estar siempre en el LP) para comparar.
