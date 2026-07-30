# Repertorio de estrategias de Glassnode → qué se puede BACKTESTEAR (y con qué datos)

**Para qué:** el framework (`framework_direccion.md` + `../derivados_glassnode/framework.md`) lista ~25
herramientas. No todas son backtesteables con datos gratis. Esta es la **lista priorizada** para decidir
qué probar primero en la operativa real: **LP concentrado + algún trade direccional a semanas/meses**.

## 0) La restricción que manda: profundidad de datos

| Fuente | Métricas | Histórico REAL disponible |
|---|---|---|
| **BGeometrics** (bitcoin-data.com, gratis) | realized price, MVRV Z, SOPR | **4 años exactos, ventana móvil** (hoy: jul-2022 → jul-2026) — 1.461 puntos |
| **Binance + Coin Metrics** (gratis) | precio OHLC, 200W MA, BMSB, RV, Choppiness | Histórico completo (2010→) |
| **Deribit** (gratis) | DVOL, skew, put/call, max pain | DVOL desde ~mar-2021 |
| **Bybit / OKX** (gratis) | funding, OI | Funding largo; **OI solo ~180-400d** |
| **Glassnode de pago** | TMM, URPD, ATS, Sell-Side Risk, cohortes | ❌ No disponible |

> **Consecuencia clave:** el backtest on-chain cubre **~1 ciclo** (suelo 2022 → bull 2024-25 → techo oct-2025 →
> bear 2026). Suficiente para validar la *mecánica* de una regla; **insuficiente** para afirmar que funciona
> "en todos los ciclos". Cualquier resultado se reporta con esa etiqueta.

---

> **Actualizado 30-jul-2026** tras verificar la disponibilidad real (`data/onchain/_disponibilidad.json`).
> **La escalera de cost basis completa está disponible gratis** — el plan cambia: ya no hay que usar proxies
> para lo importante.

## Tier 1 — BACKTESTEABLE YA (datos ✅ confirmados + alto peso en sus decisiones)

| # | Estrategia | Regla mecánica | Datos | Por qué |
|---|---|---|---|---|
| **1** | **Régimen STH Cost Basis** ⭐ | Alcista si `spot > STH CB` sostenido; defensivo si `<`. En bear el nivel es **techo**; en bull, **suelo** (§D del framework) | ✅ `sth-realized-price` | El nivel táctico que más usan (32% de conclusiones en 2026) |
| **2** | **Régimen True Market Mean** ⭐ | Bull/bear según `spot ≷ TMM`. Reclamarlo exige **semanas de consolidación**, no un toque | ✅ `true-market-mean` | **50% de sus conclusiones en 2026** — su línea divisoria |
| **3** | **Escalera completa (4 regímenes)** | Deep bear `<RP` · Recovery `RP→TMM` · Enthusiastic `TMM→ATH` · Euphoric `>ATH` | ✅ los 3 niveles | Es su brújula macro entera, ahora reproducible |
| **4** | **Enfriamiento de Realized Loss** | Suelo cuando la pérdida realizada cae bajo su umbral (ellos: <$25M/día o <1k BTC/día) | ✅ `realized-loss` | Su **condición explícita de formación de suelo** |
| **5** | **Realized P/L Ratio** | `<1` pérdida en exceso · `>2` sostenido = flujo de capital de bull genuino | ✅ derivable de profit/loss | Umbral literal suyo, muy citable |
| **6** | **STH-MVRV reclama 1,0** | Condición explícita de transición pre-bull | ✅ `sth-mvrv` | Confirma (o desmiente) el cambio de régimen |
| **7** | **Confluencia dirección × vol** ⭐⭐ | Régimen on-chain (#1/#2) **×** semáforo de derivados (funding z + OI pct + VRP) → LP dentro/fuera **y** sesgo del trade | ✅ todo | **LA tesis del método**: on-chain el nivel, derivados el momento. Nadie la ha medido junta |

## Tier 2 — PENDIENTE DE UN DATO (no de un proxy)

| # | Estrategia | Qué falta |
|---|---|---|
| **8** | **% Supply in Profit** (umbrales 54,2 / 60 / 75 / 90) | Slug correcto — `supply-in-profit` da 404. Es de las reglas más citables del corpus |
| **9** | **ETF flows como confirmación** | Ingestor nuevo desde Farside. 2º driver de 2026 (67%) |
| **10** | **Air gaps / estantes URPD** | No hay dato gratis. Proxy posible: perfil de volumen por precio de Binance — **pero mide volumen transado, no cost basis**; ellos avisan de la diferencia |

## Tier 1-bis — LEGÍTIMO, PERO NO ES "EL MÉTODO DE GLASSNODE"

| Estrategia | Nota honesta |
|---|---|
| **MVRV Z bandas** · **SOPR = 1,0** | Datos ✅ y son indicadores válidos — pero **Glassnode ya no decide con ellos** (MVRV Z: 5 artículos de 328; SOPR: 5% de conclusiones recientes). Backtestearlos es útil para el terminal (Cowen sí usa MVRV Z), pero **no** se puede vender como "validación del framework de Glassnode" |

## Tier 3 — NO BACKTESTEABLE con datos gratis (documentar y dejar al agente)

Accumulation Trend Score · Sell-Side Risk Ratio · Cost Basis Distribution heatmaps por cohorte ·
Realized Supply Density · Supply Quantiles (0,75/0,85/0,95) · Entity-adjusted Realized Loss ·
ETF cost basis · Dealer gamma / GEX.

→ Estas se quedan como **lectura cualitativa del agente** al leer el WoC semanal, no como señal mecánica.
No pasa nada: son el "criterio", igual que la rotación de skew en derivados.

---

## Orden de ataque recomendado

0. **Ingestar las 10 métricas** (ya en `fetch_onchain.py`) → una corrida del workflow y tenemos las series.
1. **Caracterizar antes de optimizar.** Sobre 2022-2026, medir **el comportamiento de los niveles**:
   cuántas veces el precio tocó el STH CB / TMM, cuántas lo reclamó y aguantó, cuántas rebotó, y qué pasó
   a +2/+4/+8 semanas en cada caso. **Esto no es un backtest de estrategia, es la validación de la premisa** —
   y si la premisa falla (los niveles no hacen nada), no hay estrategia que construir.
2. **Backtest #1 + #2** por separado (STH CB y TMM como régimen direccional).
3. **Backtest #7** — la confluencia con el semáforo de vol. Es la hipótesis que de verdad importa para tu
   operativa (LP + trade táctico).
4. **#4, #5, #6** como confirmadores: ¿mejoran el timing de entrada/salida de #1-#2 o solo añaden ruido?

## Cómo se reporta (regla de honestidad)

Cada backtest debe decir: ventana real de datos · nº de señales (si son <10, decirlo) · si el umbral es
**de ellos** o **optimizado por nosotros** (¡lo segundo es sospechoso de overfit!) · y qué pata quedó fuera
por falta de datos. Sin eso, un backtest bonito es una trampa.

## Cómo se reporta (regla de honestidad)

Cada backtest debe decir: ventana real de datos · nº de señales (si son <10, decirlo) · si el umbral es
**de ellos** o **optimizado por nosotros** (¡lo segundo es sospechoso de overfit!) · y qué pata quedó fuera
por falta de datos. Sin eso, un backtest bonito es una trampa.
