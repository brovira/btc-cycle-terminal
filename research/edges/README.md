# research/edges — Enciclopedia de señales, indicadores y estrategias

**Qué es:** el **catálogo maestro** del terminal para que cualquier LLM/agente sepa, sin adivinar:
qué **indicadores** existen, qué **estrategias** los combinan, de qué **fuente** salen los datos
(gratis vs de pago), y **cuáles podemos backtestear ya** con lo que tenemos.

> **Regla de oro (usuario):** cero invención. Cada entrada dice de dónde sale el dato y, si es una
> lectura de un analista/Glassnode, enlaza el archivo de origen (`agentes/…`). Si algo es estimación
> o no está verificado, se marca `⚠️ sin verificar`.

## 📂 Archivos

| Archivo | Qué contiene | Cuándo abrirlo |
|---|---|---|
| **`README.md`** (este) | Índice, esquema de las fichas, mapa de fuentes de datos, estado de suscripción | siempre primero |
| **`indicadores.md`** | **Enciclopedia de señales/indicadores** — uno por ficha (on-chain, derivados, precio/TA). Qué mide, cómo se lee, umbrales reales, fuente, backtesteable | antes de usar/backtestear una señal |
| **`estrategias.md`** | **Catálogo de estrategias** — combinaciones de señales con reglas de entrada/salida. Qué indicadores usa, dónde está backtesteada, veredicto | antes de operar o backtestear una estrategia |

## 🧩 Esquema de cada FICHA (mismo formato en indicadores y estrategias, para grepear)

Cada entrada empieza con un bloque de campos `clave: valor` en una línea, para búsqueda mecánica:

```
### <NOMBRE>
- **id:** slug-unico
- **tipo:** onchain | derivados | precio-ta | ciclo | compuesto
- **mide:** (1 frase)
- **fuente_dato:** free | paid | mixto  →  <de dónde: Coin Metrics / Deribit / precio / Glassnode…>
- **tenemos_datos:** sí | parcial | no
- **backtesteable_ya:** sí | parcial | no   →  <por qué / con qué>
- **backtest_en:** <archivo.html o "—">
- **usado_por:** <estrategias que lo usan>
- **origen:** <archivo de conocimiento: agentes/… o "propio">
```

Debajo del bloque: lectura, umbrales reales observados, y notas.

**Tags inline** para grepear dentro del texto: `#free` `#paid` `#backtesteable` `#no-backtesteable`
`#onchain` `#derivados` `#precio` `#ciclo` `#pendiente-suscripcion`.

## 💳 Fuentes de datos — estado actual

| Fuente | Coste | Qué da | Estado |
|---|---|---|---|
| **Precio OHLC** (Binance klines → CoinGecko → Coin Metrics) | **free** | close semanal/diario BTC desde 2015+ | ✅ en uso (loaders de `btc-plan.html`, `backtest.html`) |
| **Coin Metrics Community** | **free** | MVRV, realized price, algunas on-chain agregadas | ✅ disponible, integración parcial |
| **bgeometrics** (`charts.bgeometrics.com`) | **free** (por confirmar) | on-chain: MVRV, realized price, SOPR, etc. — API "free" anunciada | 🟡 **verificar desde tu IP** (el proxy datacenter la bloquea con 403) |
| **Deribit public API** | **free** | DVOL, IV ATM, 25d skew, funding, OI (BTC/ETH) | ✅ disponible; **historial limitado** (no cubre 2021) |
| **Bitbo Pro++** (`charts.bitbo.io/api`) | **paid barato** | **STH realized price (=STH cost basis), STH-MVRV, SOPR, STH-SOPR, MVRV-Z, supply in profit, NUPL, RHODL/Rainbow…** API JSON/CSV, 150k req/mes, 5 req/60s | 🎯 **CANDIDATO recomendado** (cubre el "DÓNDE" que falta, 20× más barato que Glassnode Pro) |
| **Glassnode Professional** | **paid caro** (~$800/mes) | los 5 "trading models" empaquetados + serie completa | ❌ **NO recomendado** (backtests in-sample de escaparate; replicamos la lógica nosotros con Bitbo) |

> **Decisión de fuentes (jul-2026):** para el "DÓNDE" on-chain (STH cost basis, SOPR, MVRV-Z, supply
> in profit) el camino es **Bitbo Pro++** (barato) o **bgeometrics** (free, a verificar) — **NO** Glassnode
> Professional. Con esos datos **replicamos** los modelos de momentum/confluencia de Glassnode con NUESTRO
> backtest walk-forward honesto, en vez de pagar 20× por sus backtests in-sample. Mientras no haya fuente,
> lo `#paid`/`#pendiente-suscripcion` se documenta pero no se backtestea.

## 🔗 Conocimiento ya existente que alimenta este catálogo

- `agentes/derivados_glassnode/framework.md` — método de derivados/opciones de Glassnode (152 WoC).
- `agentes/derivados_glassnode/estrategia_leverage.md` — señal 8/10 flush/squeeze, mecánica con datos free.
- `agentes/derivados_glassnode/reports/track_record.md` — aciertos/fallos por llamada.
- `agentes/lmec/auditoria_ampliada.md` — método de ciclo de LMEC (Halving Cycle Profit, BMSB, MVRV Z, RSI/MACD).
- Backtests vivos: `backtest.html` (señales de ciclo), `volbacktest.html` (CHOP→sal del LP), `montecarlo.html`.

## ✍️ Cómo mantenerlo

- Indicador o estrategia **nueva** → añade una ficha con el esquema completo.
- Cuando pegues contenido de Glassnode → cae en `estrategias.md` (si es una estrategia) o `indicadores.md`
  (si es una señal/métrica), citando el origen.
- Al contratar la suscripción → barre los `#pendiente-suscripcion` y actualiza `backtesteable_ya`.
