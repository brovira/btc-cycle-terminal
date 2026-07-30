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

## Tier 1 — BACKTESTEABLE YA (datos confirmados, alto uso en el corpus)

| # | Estrategia | Regla mecánica | Datos | Por qué primero |
|---|---|---|---|---|
| **1** | **Régimen STH Cost Basis** ⭐ | Largo/LP-alcista si `spot > STH CB` sostenido N días; defensivo si `spot < STH CB`. Bandas ±1σ como rango | `sth-realized-price` ⚠️ slug sin verificar | **El más usado del corpus** (15/17 artículos en 2026). Es la pata de dirección que falta |
| **2** | **Régimen Realized Price** | Deep bear si `spot < realized price`; recuperación por encima | ✅ confirmado | Proxy grosero del régimen; sirve de suelo estructural |
| **3** | **MVRV Z bandas** | Techo `+2σ` / suelo `−1,5σ` sobre media móvil **de 1 año** (ellos calibran a 1a, no a toda la historia) | ✅ confirmado | Ya está en el terminal; falta backtestear los umbrales *de ellos* |
| **4** | **SOPR = 1,0 como eje** | En bull: undercut breve de 1,0 → compra. Sostenido <1,0 → bear | ✅ confirmado | Regla de 2019 que sigue viva en 2026 — la más longeva |
| **5** | **Confluencia dirección × vol** ⭐⭐ | Régimen on-chain (1 o 2) **×** semáforo de derivados (funding z + OI pct + VRP) → decide LP dentro/fuera **y** sesgo del trade | ✅ (ya construido en `/api/voldata`) | **Es LA tesis del método**: on-chain da el nivel, derivados el momento. Nadie la ha medido junta |

## Tier 2 — BACKTESTEABLE CON PROXY (hay que construir la métrica)

| # | Estrategia | Proxy posible | Riesgo del proxy |
|---|---|---|---|
| **6** | **True Market Mean** | Aproximar con realized price ajustado por Liveliness, o usar el `realized-price` a secas como sustituto degradado | El TMM real excluye supply dormida; el proxy será sistemáticamente más bajo → los cruces no coincidirán |
| **7** | **% Supply in Profit** (umbrales 54/60/75/90%) | Derivable si BGeometrics expone la serie; si no, estimable desde URPD (no gratis) | Sin la serie real, no hay proxy fiable → probablemente descartar |
| **8** | **STH-SOPR z-score** (umbral −2 = capitulación) | `sth-sopr` ⚠️ slug sin verificar + z-score móvil 4 años | Si el slug no existe, cae a Tier 3 |
| **9** | **Air gaps / estantes URPD** | Aproximar con perfil de volumen por precio (VPVR) de Binance | El VPVR mide volumen *transado*, no *cost basis* — parecido pero no igual. Ellos avisan de la diferencia |

## Tier 3 — NO BACKTESTEABLE con datos gratis (documentar y dejar al agente)

Accumulation Trend Score · Sell-Side Risk Ratio · Cost Basis Distribution heatmaps por cohorte ·
Realized Supply Density · Supply Quantiles (0,75/0,85/0,95) · Entity-adjusted Realized Loss ·
ETF cost basis · Dealer gamma / GEX.

→ Estas se quedan como **lectura cualitativa del agente** al leer el WoC semanal, no como señal mecánica.
No pasa nada: son el "criterio", igual que la rotación de skew en derivados.

---

## Orden de ataque recomendado

1. **Verificar los slugs STH** (`sth-realized-price`, `sth-sopr`) — desbloquea la estrategia #1, que es la
   más importante. Se sabe en cuanto corra el workflow `onchain.yml`.
2. **Backtest #1 + #5** (régimen STH CB, solo y cruzado con el semáforo de vol) sobre 2022-2026.
   Métricas a reportar: retorno vs hold, drawdown, % tiempo dentro del LP, nº de señales, y —crucial—
   **cuántas veces el nivel aguantó vs falló**.
3. **Backtest #3 y #4** con los umbrales literales de ellos, para tener la línea base "solo on-chain".
4. Si #1 no es viable (slug inexistente) → **#6 con proxy** y etiquetar el resultado como aproximado.

## Cómo se reporta (regla de honestidad)

Cada backtest debe decir: ventana real de datos · nº de señales (si son <10, decirlo) · si el umbral es
**de ellos** o **optimizado por nosotros** (¡lo segundo es sospechoso de overfit!) · y qué pata quedó fuera
por falta de datos. Sin eso, un backtest bonito es una trampa.
