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
| 25d Skew histórico | ❌ **no disponible** | — |

**Ventanas efectivas (manda la serie más corta de cada regla):** on-chain puro **4 ciclos** ·
con funding/OI **2020→** (1,5 ciclos) · con VRP **2021→** · con ETF **2024→**.

---

## 1) Reglas de NIVEL (la escalera)

| ID | Regla (suya, literal o parafraseada con cita) | Umbral | Datos | Testeable |
|---|---|---|---|---|
| **N1** | *"Approached from below in a downtrend, the break-even of recent buyers acts as a rejection zone"* [wk29-2026] → en bear el STH CB es **techo**; en bull, **suelo** | cruce | STH CB + precio | ✅ |
| **N2** | TMM = *"the dividing line between bear and bull market regimes"* [wk21-2026] | cruce | True Mean Price | ✅ |
| **N3** | Realised Price = suelo estructural; perderlo requiere *"a systemic dislocation similar to LUNA or FTX"* [wk06-2026] | cruce | Realised Price | ✅ |
| **N4** | 4 regímenes: Deep bear `<RP` · Recovery `RP→TMM` · Enthusiastic `TMM→ATH` · Euphoric `>ATH` | bandas | los 3 + ATH | ✅ |
| **N5** | Bandas ±1σ/±2σ del STH CB como rango local; −1σ = sobreventa, +1σ techo local (*solo 17,5% de la historia cotiza sobre +1σ* [WoC21-2025]) | ±σ | **hay que calcularlas** ⚠️ | 🟡 ver D1 |
| **N6** | *"Pre-bull market phases require **weeks to months** of sustained consolidation around this model"* [wk20-2026] — reclamar ≠ tocar | duración | precio + TMM | 🟡 ver D2 |
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
| **P1** | `EXIT_CROWDED_LONG` = funding ann MM3d **≥ +8%** Y z **≥ +1,5σ** Y OI **≥ p90/180d** (+ rotación de skew, no automatizable) | los 3 | funding + OI (2020→) | 🟡 sin la pata de skew |
| **P2** | `EXIT_VOL_REALIZING` = VRP `<0` ≥2 días **O** skew `>+15` con P/C volumen `>1` | VRP<0 | DVOL (2021→) | 🟡 solo la pata VRP |
| **P3** | `SQUEEZE` (la única señal direccional, **3/3** en el track record) = funding `<0` sostenido 3d + OI subiendo `+10%` en 2-4 sem + reclaim de soporte on-chain | los 3 | funding + OI + STH CB | ✅ |
| **P4** | `REENTRY_CLEAN` = flush (OI −15% en ≤3d) + OI `≤p40` + funding `≤+11%` + VRP `≥+5` + skew 0–12 | los 5 | funding + OI + DVOL | 🟡 sin skew |

## 4) Reglas de CRUCE — **la tesis de verdad**

| ID | Regla | Por qué importa |
|---|---|---|
| **X1** | Régimen on-chain (N1/N2) **×** semáforo de posicionamiento (P1-P4) → LP dentro/fuera **y** sesgo del trade | *"derivados = POSICIONAMIENTO; cost basis = el DÓNDE. La lectura completa es la intersección"* [framework.md §C5]. **Nadie la ha medido junta** |
| **X2** | Confluencia obligatoria: *"To maximise the value of on-chain insights, it is important to seek **confluence** between multiple metrics"* [WoC10-2021] → ¿mejora una regla al exigir 2-3 confirmaciones, o solo reduce el nº de señales? | Es la pregunta central de todo el método |
| **X3** | Veto macro: *"a durable recovery will require either the DXY to break below 99 or the 10-Year to compress toward 4,2%"* [wk23-2026] | ⚠️ requiere DXY y 10Y — **no los tenemos ingeridos** |
| **X4** | ETF flows como confirmación del spot bid (2º driver de sus conclusiones en 2026) | `etf_flows_1`, solo 2024→ |

---

## 5) ⚠️ DECISIONES DE DISEÑO ABIERTAS (hay que fijarlas ANTES de correr nada)

Cada una es un grado de libertad. Si se eligen *después* de ver resultados, el backtest está contaminado.
**Propuesta: fijar el valor de la columna "por defecto" y no tocarlo; si se prueba otro, reportar los dos.**

| ID | Decisión | Por defecto propuesto | Por qué |
|---|---|---|---|
| **D1** | Ventana de σ para las bandas del STH CB | **1 año móvil** | Es la que ellos usan para calibrar el MVRV Z [WoC06-2025]; coherente por analogía |
| **D2** | ¿Qué es "reclaim sostenido"? | **cierre semanal por encima 2 semanas seguidas** | Ellos dicen "semanas a meses"; 2 semanas es el mínimo compatible y evita el ruido diario |
| **D3** | ¿Qué es un "air gap"? | **percentil <20 de densidad de supply** en el bucket URPD | Arbitrario pero declarado; el URPD solo es snapshot, así que no es backtesteable en el tiempo |
| **D4** | Umbrales absolutos ($25M/día) | **convertir a percentil de su propia historia** | Un umbral en dólares de 2026 no es comparable con 2015. Reportar ambos |
| **D5** | "Sostenido" en funding negativo | **3 días consecutivos** | Es lo que dice `estrategia_leverage.md §C` |
| **D6** | Horizontes de evaluación | **+2, +4, +8 semanas** | El método declara horizonte de semanas-meses |
| **D7** | ¿Qué cuenta como acierto? | **Para nivel: dirección correcta a +4 sem. Para LP: PnL (fees−IL) vs estar siempre dentro** | Son objetivos distintos y no se deben mezclar |

## 6) Lo que NO se puede testear (y hay que decirlo)

- **25d Skew histórico** → sin fuente gratis. Tumba la pata de rotación de skew de P1/P4 (el sello del techo del 10-oct-25).
- **Rotación put→call** → requiere el skew. Queda como criterio del agente.
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
