# Catálogo de ESTRATEGIAS

Una ficha por estrategia = combinación de indicadores (`indicadores.md`) con reglas de entrada/salida.
Esquema y tags en `README.md`. **Grounded:** cada estrategia cita su origen y dónde (si) está backtesteada.

Índice:
1. Ciclo LMEC (tiempo + TA) — #backtesteable ✅
2. Cowen Risk DCA — #backtesteable ✅
3. Leverage flush / squeeze (derivados) — #parcial
4. LP short-vol governance (CHOP + VRP + gamma) — #parcial
5. DCA + comprar por niveles (el plan operativo actual) — #backtesteable ✅
6. Confluencia 3 señales (LMEC + Cowen + Patrón) — #backtesteable ✅

---

## 1. Ciclo LMEC (tiempo + TA)
- **id:** ciclo-lmec
- **indicadores:** halving-cycle-profit + bmsb + rsi-w + macd-w + sma200w + mvrv-z
- **fuente_dato:** free (todo precio; MVRV-z free vía Coin Metrics)
- **backtesteable_ya:** sí #backtesteable #ciclo #free
- **backtest_en:** backtest.html (preset LMEC), btc-plan.html §5
- **origen:** agentes/lmec/auditoria_ampliada.md

**Regla:** acumular en la ventana bajista (post-techo, hacia las ~54 sem al suelo); **vender parcial** (nunca el BTC core) en la ventana de euforia post-halving (ene-oct del año post-halving); recomprar cuando confluyen RSI recupera 34 + MACD cruza + BMSB 2ª ruptura + MVRV sale de zona verde. **Veredicto auditoría: 7/10** de acierto de ciclo; coherencia discurso↔ejecución alta. Nunca vende BTC núcleo.

## 2. Cowen Risk DCA
- **id:** cowen-risk-dca
- **indicadores:** cowen-risk
- **fuente_dato:** free (precio)
- **backtesteable_ya:** sí #backtesteable #precio #free
- **backtest_en:** backtest.html (preset Cowen)
- **origen:** propio (método Benjamin Cowen)

**Regla:** tamaño de compra ∝ (1 − risk); comprar agresivo con risk<0.4, aligerar con risk>0.7-0.8. DCA continuo modulado por riesgo. Sin lookahead (regresión walk-forward).

## 3. Leverage flush / squeeze (derivados)
- **id:** leverage-flush-squeeze
- **indicadores:** funding + oi + leverage-ratio + skew-25d + put-call + vrp + basis
- **fuente_dato:** mixto → básicos free (Deribit/Binance reciente), serie larga + leverage-ratio limpio = paid
- **backtesteable_ya:** parcial → sí en ventana con datos Deribit/Binance; completo requiere suscripción #derivados #pendiente-suscripcion
- **backtest_en:** — (candidato #1 a construir con datos free recientes)
- **origen:** agentes/derivados_glassnode/estrategia_leverage.md (señal 8/10 HIT flush + 3/3 HIT squeeze)

**Firma FLUSH (bajista):** funding ≥+8% ann sostenido + OI en ATH + skew rotando put-rich→call-heavy + on-chain rechazando resistencia. → salir/defensivo. Marcó el 10-oct-25 ~2 días antes del mayor flush de la historia.
**Firma SQUEEZE (alcista):** funding negativo/backwardation + OI subiendo + shorts apiñados. → combustible al alza.
**Regla maestra:** NO operar por una señal aislada de "vol barata"; solo con la CONFLUENCIA (leverage extremo + posicionamiento estirado + on-chain en nivel clave).

## 4. LP short-vol governance (gobierno del LP)
- **id:** lp-shortvol
- **indicadores:** chop + vrp + gex-maxpain + funding + oi
- **fuente_dato:** mixto → chop/vrp free; gex = paid
- **backtesteable_ya:** parcial → CHOP ya backtesteado; VRP backtesteable free #backtesteable #pendiente-suscripcion
- **backtest_en:** volbacktest.html (rama CHOP)
- **origen:** agentes/derivados_glassnode/framework.md §E + volbacktest.html

El LP concentrado = corto de gamma/vol. **Semáforos:** VRP+ y leverage limpio y dealer long-gamma → **farmea**; VRP≈0 o short-gamma → **ensancha**; confluencia de flush o VRP negativo → **sal**. Regla ya backtesteada: **CHOP>60 → sal del LP** (volbacktest.html). Añadir VRP (free) es el siguiente paso backtesteable.

## 5. DCA + comprar por niveles (plan operativo actual)
- **id:** dca-niveles
- **indicadores:** halving-cycle-profit (ventana) + niveles de precio (55/50/45k)
- **fuente_dato:** free
- **backtesteable_ya:** sí #backtesteable #free
- **backtest_en:** btc-plan.html §5, montecarlo.html
- **origen:** propio (plan del ciclo, coherente con decision.html)

**El plan que ejecuto hoy:** DCA en la ventana de acumulación (jun-2026 →), reforzado con **órdenes límite escalonadas** a 55k/50k/45k (% creciente cuanto más baja), floor esperado oct-nov 2026, DCA ligero hasta jun-2027, luego hold. No vender el core. Mismo método que predica LMEC (§DCA con órdenes límite).

## 6. Confluencia 3 señales (LMEC + Cowen + Patrón)
- **id:** confluencia-3
- **indicadores:** ciclo-lmec + cowen-risk + patrón(halving/estacional)
- **fuente_dato:** free
- **backtesteable_ya:** sí #backtesteable #free
- **backtest_en:** btc-plan.html §5 (columna Consensus), decision.html (gráfica de ventanas)
- **origen:** propio

Motor de confluencia por intervalos (inclusión-exclusión): las 3 señales votan ventana de compra/venta; el consenso (2+ de acuerdo) es la señal operativa. Backtesteado 2015→hoy en btc-plan.html.

## 7. On-chain momentum régimen (modelos Glassnode — replicados)
- **id:** onchain-momentum
- **indicadores:** sth-mvrv + sopr + realized-pl + supply-in-profit + rhodl + sma200(dia) + realized-price + onchain-misc
- **fuente_dato:** paid-barato (Bitbo) o free-parcial (200D + realized price)
- **backtesteable_ya:** parcial → **el subconjunto free ya**; completo con Bitbo #pendiente-suscripcion
- **backtest_en:** — (a construir con NUESTRO walk-forward, no el de Glassnode)
- **origen:** dashboard Glassnode "On-chain Trading Models" (pegado por el usuario, jul-2026)

Familia de osciladores de Glassnode: **cuenta cuántas condiciones on-chain son alcistas → dentro de BTC si ≥umbral, a cash si menos.** 5 variantes (todas la misma idea):
1. **Tracking Market Momentum** — 4-de-8 condiciones (actividad, profitability STH-MVRV/AVIV, spending SOPR/realized-P/L, distribución SLRV). Dentro si ≥4.
2. **STH Realized P/L momentum** — solo STH: dentro si el oscilador de profit/loss realizado es positivo.
3. **Confluence Summary ("recovering bear")** — 3-de-4 bloques (precio>200D & >realized · red · profitability aSOPR/realized-P/L · distribución RHODL/supply-in-profit). Dentro si ≥3.
4. **ML Sharpe** — caja negra, plan Enterprise. ❌ descartado (no auditable).
5. **ETH Tracking Momentum** — la variante 1 para ETH (4-de-6).

> ⚠️ **AVISO (navaja de Occam + honestidad):** son **market-timing long-only** (venden a cash en bear) → **chocan con "DCA + no vender el core"**. NO adoptar literalmente. **Uso correcto:** UN régimen on-chain como **filtro** (¿DCA agresivo o ligero? ¿farmeo LP o me salgo?), no como sistema que vende BTC. Y sus backtests ($1k desde 2014, in-sample, long-only en un bull secular) son **de escaparate** → cuando tengamos los datos, **rehacemos el backtest walk-forward** nosotros antes de creerlo.
>
> **Subconjunto GRATIS y backtesteable YA:** de la variante 3, `precio > SMA200D` **Y** `precio > realized price` (ambos free) ≈ el 70% del valor con 2 métricas. Primer experimento a construir sin pagar nada.

---

## 🔭 Qué podemos backtestear YA (con datos free) vs qué espera a la suscripción

| Estrategia | Backtest hoy (free) | Falta (paid) |
|---|---|---|
| Ciclo LMEC | ✅ completo | — |
| Cowen Risk DCA | ✅ completo | — |
| DCA + niveles | ✅ completo | — |
| Confluencia 3 | ✅ completo | — |
| LP short-vol | 🟡 CHOP ✅; **añadir VRP (free)** | GEX/dealer gamma, leverage-ratio limpio |
| Leverage flush/squeeze | 🟡 ventana reciente con funding+OI+skew de Binance/Deribit | serie larga (2021), STH cost basis para el cruce on-chain, leverage-ratio |
| On-chain momentum (Glassnode) | 🟡 subconjunto free: precio>200D & >realized | STH-MVRV, SOPR, supply-in-profit, RHODL (= **Bitbo**, barato) |

**Fuente recomendada (NO Glassnode Pro):** **Bitbo Pro++** (barato, 150k req/mes) da STH cost basis, STH-MVRV, SOPR, MVRV-Z, supply-in-profit → cubre casi todo el on-chain de un tirón. Alternativa free por verificar: **bgeometrics**. Ver README §fuentes.

**Prioridad de dato** (orden): (1) **STH cost basis / STH-MVRV** — el "DÓNDE" que le falta a todo (Bitbo); (2) SOPR + supply-in-profit — completan el régimen on-chain; (3) leverage-ratio + GEX — flush/squeeze y LP; (4) serie histórica larga de derivados.

**Siguiente backtest construible SIN pagar nada:** (a) `precio>SMA200D & >realized price` (Coin Metrics) = régimen on-chain minimalista; (b) VRP de Deribit (IV−RV) = semáforo LP. Cierran 3 casillas 🟡 → verde parcial. Ver `indicadores.md` #pendiente-integracion.
