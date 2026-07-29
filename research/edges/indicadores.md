# Enciclopedia de INDICADORES / SEÑALES

Una ficha por señal. Esquema y tags en `README.md`. Agrupadas por familia.
**Umbrales = los reales observados** en el corpus/analistas, no inventados. Origen citado en cada ficha.

Índice rápido:
- **Ciclo/tiempo:** Halving Cycle Profit · Fractal 2022
- **Precio/TA:** BMSB · RSI semanal · MACD semanal · SMA 200 semanas · Cowen Risk Metric · CHOP Index
- **On-chain:** MVRV Z-Score · Realized Price · STH Cost Basis · SSR (Sell-Side Risk) · True Market Mean · MVRV ratio
- **Derivados/opciones:** Funding · Open Interest · Estimated Leverage Ratio · 25d Skew · Put/Call · DVOL/IV · VRP · Max Pain / Dealer Gamma · Futures Basis

---

## FAMILIA: CICLO / TIEMPO

### Bitcoin Halving Cycle Profit
- **id:** halving-cycle-profit
- **tipo:** ciclo
- **mide:** posición en el ciclo de 4 años medida en semanas desde el halving / desde el techo
- **fuente_dato:** free → solo fechas (halving) + precio
- **tenemos_datos:** sí
- **backtesteable_ya:** sí → es puro calendario sobre el precio #backtesteable #ciclo #free
- **backtest_en:** backtest.html (preset LMEC)
- **usado_por:** estrategia "Ciclo LMEC", confluencia decision.html/btc-plan.html
- **origen:** agentes/lmec/auditoria_ampliada.md §3a

Pilar de LMEC ("nunca ha fallado"). **~54 semanas techo→suelo** (verificado 2018 y 2022 → suelo ~nov-2026).
Post-halving: ~152 sem tramo alcista / ~55 sem bajista; "40 semanas de euforia" post-halving = ventana de venta.
Ventana de venta del ciclo: ene–oct del año post-halving. Es tiempo, no precio. #ciclo

### Fractal 2021-2022
- **id:** fractal-2022
- **tipo:** ciclo
- **mide:** correlación de la estructura de precio actual con la del bear 2021-2022
- **fuente_dato:** free → precio
- **tenemos_datos:** sí
- **backtesteable_ya:** parcial → es descriptivo, difícil de mecanizar sin sobreajuste #precio #free
- **backtest_en:** —
- **usado_por:** narrativa LMEC (suelo ~$60k 2026)
- **origen:** agentes/lmec/auditoria_ampliada.md §3b

LMEC: 93% correlación → rebote a $80-82k, última caída, suelo ~$60k. ⚠️ sin verificar (retrospectivo, riesgo de cherry-pick).

---

## FAMILIA: PRECIO / ANÁLISIS TÉCNICO

### BMSB — Bull Market Support Band (SMA20 + EMA21 semanales)
- **id:** bmsb
- **tipo:** precio-ta
- **mide:** soporte dinámico de mercado alcista (banda entre SMA20 y EMA21 en velas semanales)
- **fuente_dato:** free → precio
- **tenemos_datos:** sí
- **backtesteable_ya:** sí → medias móviles sobre close semanal #backtesteable #precio #free
- **backtest_en:** backtest.html, btc-plan.html (dibujada en la gráfica de confluencia)
- **usado_por:** Ciclo LMEC, confluencia
- **origen:** agentes/lmec/auditoria_ampliada.md §3b

Señal LMEC: **la "2ª ruptura" al alza de la BMSB coincide con inicio de tramo alcista** (4/4 ciclos); la 1ª es trampa.
⚠️ Nomenclatura elástica del autor ("2ª/3ª ruptura" = mismo evento). Recuperar por encima = alcista; perder por debajo = bajista.

### RSI semanal
- **id:** rsi-w
- **tipo:** precio-ta
- **mide:** momentum (0-100) en velas semanales
- **fuente_dato:** free → precio
- **tenemos_datos:** sí
- **backtesteable_ya:** sí #backtesteable #precio #free
- **backtest_en:** backtest.html
- **usado_por:** Ciclo LMEC (recompra)
- **origen:** agentes/lmec/auditoria_ampliada.md §3b

LMEC: **no** comprar por RSI<30; señal de suelo = **recupera 34** tras lateralizar (2m 2015, 3m 2019, 5m 2022).

### MACD semanal
- **id:** macd-w
- **tipo:** precio-ta
- **mide:** cruce de medias (tendencia/momentum) semanal
- **fuente_dato:** free → precio
- **tenemos_datos:** sí
- **backtesteable_ya:** sí #backtesteable #precio #free
- **backtest_en:** backtest.html
- **usado_por:** Ciclo LMEC (confirmación recompra)
- **origen:** agentes/lmec/auditoria_ampliada.md §3b

LMEC: cruce alcista (azul>naranja) tras tiempo en negativo. Aviso: en 2022 el cruce llegó pero "siguió cayendo meses" → confirmación, no gatillo aislado.

### SMA 200 semanas
- **id:** sma200w
- **tipo:** precio-ta
- **mide:** media de 200 semanas = suelo histórico de mercado
- **fuente_dato:** free → precio
- **tenemos_datos:** sí
- **backtesteable_ya:** sí #backtesteable #precio #free
- **backtest_en:** btc-plan.html (línea en gráfica), backtest.html
- **usado_por:** Ciclo LMEC, floor del roadmap
- **origen:** agentes/lmec/auditoria_ampliada.md §3b

"El precio siempre la visita." feb-2026: ~$58k, no tocada → LMEC: "$60k no es el suelo". Soporte de última instancia del ciclo.

### Cowen Risk Metric
- **id:** cowen-risk
- **tipo:** precio-ta / compuesto
- **mide:** riesgo 0-1 normalizado (regresión log-log walk-forward + medias) — caro arriba, barato abajo
- **fuente_dato:** free → precio
- **tenemos_datos:** sí
- **backtesteable_ya:** sí → ya implementado (riskSeries) #backtesteable #precio #free
- **backtest_en:** backtest.html (preset Cowen), decision.html/btc-plan.html (señal "Cowen")
- **usado_por:** estrategia "Cowen Risk DCA", confluencia
- **origen:** propio (réplica del método de Benjamin Cowen)

DCA inverso al riesgo: comprar más cuando risk<0.4, aligerar cuando risk>0.7-0.8. Nuestra implementación = regresión log-log walk-forward (sin lookahead).

### CHOP Index (Choppiness)
- **id:** chop
- **tipo:** precio-ta
- **mide:** cuán lateral/choppy está el mercado (0-100)
- **fuente_dato:** free → precio (OHLC)
- **tenemos_datos:** sí
- **backtesteable_ya:** sí → **ya backtesteado** #backtesteable #precio #free
- **backtest_en:** volbacktest.html
- **usado_por:** estrategia "CHOP → sal del LP"
- **origen:** propio / volbacktest.html

**CHOP > 60 = mercado lateral → salir del LP** (el LP concentrado sufre en chop sin tendencia). Backtesteado en volbacktest.html.

---

## FAMILIA: ON-CHAIN

### MVRV Z-Score
- **id:** mvrv-z
- **tipo:** onchain
- **mide:** desviación del market cap sobre el realized cap, normalizada (z-score)
- **fuente_dato:** mixto → **free** (Coin Metrics Community da MVRV/realized; z-score calculable)
- **tenemos_datos:** parcial → MVRV ratio y realized cap free; el z-score lo calculamos
- **backtesteable_ya:** parcial → sí si integramos Coin Metrics; hoy no está cableado #backtesteable #onchain #free
- **backtest_en:** —
- **usado_por:** Ciclo LMEC (confluencia con BMSB)
- **origen:** agentes/lmec/auditoria_ampliada.md §3b

LMEC: **franja verde = suelo**; su salida coincidió con fin del bear en 4 ciclos; confluencia temporal casi idéntica con la BMSB.
**Acción free:** cablear Coin Metrics `CapMVRVCur` + realized → calcular z-score histórico. #pendiente-integracion (no de pago)

### Realized Price
- **id:** realized-price
- **tipo:** onchain
- **mide:** precio medio al que se movió por última vez cada moneda (coste medio agregado)
- **fuente_dato:** free → Coin Metrics Community (realized cap / supply)
- **tenemos_datos:** parcial
- **backtesteable_ya:** parcial → sí vía Coin Metrics #onchain #free
- **backtest_en:** —
- **usado_por:** soporte macro, confluencia on-chain
- **origen:** agentes/derivados_glassnode/framework.md §C5 (el "DÓNDE")

Glassnode lo usa como nivel de soporte/coste base agregado. Free vía Coin Metrics. #pendiente-integracion

### STH Cost Basis (Short-Term Holder realized price)
- **id:** sth-cost-basis
- **tipo:** onchain
- **mide:** coste base de los holders de corto plazo (<155 días) = soporte/resistencia clave del ciclo
- **fuente_dato:** paid → Glassnode/CryptoQuant (Coin Metrics no lo da limpio)
- **tenemos_datos:** no
- **backtesteable_ya:** no → **requiere suscripción** #no-backtesteable #onchain #paid #pendiente-suscripcion
- **backtest_en:** —
- **usado_por:** framework Glassnode (el "DÓNDE" que cruza con derivados)
- **origen:** agentes/derivados_glassnode/framework.md §C5

**El nivel más importante del método Glassnode.** Reclaim del STH-CB = alcista; rechazo = techo local (cluster $114-117k oct-25).
Se cruza SIEMPRE con la lente de derivados. **Prioridad #1 al contratar la suscripción.**

### SSR — Sell-Side Risk Ratio
- **id:** ssr
- **tipo:** onchain
- **mide:** presión vendedora realizada vs tamaño del activo (equilibrio de mercado)
- **fuente_dato:** paid → Glassnode
- **tenemos_datos:** no
- **backtesteable_ya:** no → **requiere suscripción** #no-backtesteable #onchain #paid #pendiente-suscripcion
- **backtest_en:** —
- **usado_por:** (pendiente — el usuario lo mencionó como métrica objetivo)
- **origen:** solicitado por el usuario

Valores bajos = equilibrio/poca presión (los holders no realizan) → suele marcar suelos/consolidación. Alto = mucha realización → riesgo. Documentar mejor al tener acceso.

### True Market Mean
- **id:** true-market-mean
- **tipo:** onchain
- **mide:** coste base de los participantes activos (excluye monedas perdidas) — soporte de "valor justo"
- **fuente_dato:** paid → Glassnode (modelo Cointime)
- **tenemos_datos:** no
- **backtesteable_ya:** no #no-backtesteable #onchain #paid #pendiente-suscripcion
- **backtest_en:** —
- **usado_por:** framework Glassnode (nivel de soporte de ciclo)
- **origen:** agentes/derivados_glassnode/framework.md §C5

### MVRV ratio (simple)
- **id:** mvrv-ratio
- **tipo:** onchain
- **mide:** market cap / realized cap (sin normalizar)
- **fuente_dato:** free → Coin Metrics Community
- **tenemos_datos:** parcial
- **backtesteable_ya:** parcial → sí vía Coin Metrics #onchain #free
- **backtest_en:** —
- **usado_por:** base del MVRV Z-Score
- **origen:** Coin Metrics

>3.7 histórico = zona de techo; <1 = por debajo de coste base = suelo profundo. Free.

---

## FAMILIA: DERIVADOS / OPCIONES

> Todo esto sale del framework de Glassnode (`agentes/derivados_glassnode/framework.md`). Deribit da los
> básicos **gratis** pero **con historia corta** (no 2021). La historia larga y las métricas derivadas
> (GEX, VRP con serie) son `#paid`.

### Funding rate (perps)
- **id:** funding
- **tipo:** derivados
- **mide:** coste de mantener largo perp vs neutral (0.01%/8h)
- **fuente_dato:** free → Binance/Bybit/Deribit public (histórico limitado en algunos)
- **tenemos_datos:** parcial → free reciente; histórico largo limpio es #paid
- **backtesteable_ya:** parcial → sí desde que hay datos (≈2019+ en Binance) #backtesteable #derivados #free
- **backtest_en:** — (candidato: estrategia leverage flush/squeeze)
- **usado_por:** estrategia "Leverage flush/squeeze", playbook LP
- **origen:** agentes/derivados_glassnode/estrategia_leverage.md

**≥ +8% anualizado sostenido = longs apiñados → riesgo de flush.** Negativo sostenido pese a precio subiendo = shorts apiñados → combustible de squeeze. **El signo da la dirección.** Marcó el techo del 10-oct-25 ~2 días antes.

### Open Interest (OI)
- **id:** oi
- **tipo:** derivados
- **mide:** apalancamiento/actividad abierta (perps + fixed-term + opciones)
- **fuente_dato:** free → exchanges public (Binance/Bybit); agregado limpio = #paid
- **tenemos_datos:** parcial
- **backtesteable_ya:** parcial #backtesteable #derivados #free
- **backtest_en:** —
- **usado_por:** Leverage flush/squeeze
- **origen:** agentes/derivados_glassnode/estrategia_leverage.md

En **máximos/ATH** = combustible cargado (flush). Muy por debajo de picos = estructura limpia (menos cascada). Caída >5% sem = flush event. Récord: −$19B en 1 día (10-oct-25).

### Estimated Leverage Ratio
- **id:** leverage-ratio
- **tipo:** derivados
- **mide:** OI / market cap (o OI / balance en exchange) = fragilidad del sistema
- **fuente_dato:** paid → Glassnode (necesita OI agregado + supply en exchange)
- **tenemos_datos:** no (proxy free posible con OI/mcap aproximado)
- **backtesteable_ya:** parcial → con proxy free #derivados #paid #pendiente-suscripcion
- **backtest_en:** —
- **usado_por:** Leverage flush/squeeze
- **origen:** agentes/derivados_glassnode/framework.md §B

**≥2% del market cap = zona de riesgo de flush.** Colapsó a mínimos multi-mes el 10-oct-25 (desapalancamiento).

### 25-delta Skew (puts − calls)
- **id:** skew-25d
- **tipo:** derivados
- **mide:** miedo direccional (IV de puts vs calls) por plazo (1W/1M/3M/6M)
- **fuente_dato:** free → Deribit public (reciente); serie larga = #paid
- **tenemos_datos:** parcial
- **backtesteable_ya:** parcial #derivados #free
- **backtest_en:** —
- **usado_por:** Leverage flush/squeeze (rotación defensivo→call-heavy = techo)
- **origen:** agentes/derivados_glassnode/framework.md §A

Umbrales reales: **>20-30% = pánico/extremo** (feb-26: 28-30%), ~11-14% = defensivo normal en bear, ~2-6% = neutral/risk-on, **negativo (calls>puts) = risk-on sano**. La **rotación** put-rich→call-heavy (1W +18→+3 en <1 sem, oct-25) marca techo, no el nivel alto (eso es suelo).

### Options Put/Call ratio (OI y volumen)
- **id:** put-call
- **tipo:** derivados
- **mide:** defensividad del posicionamiento en opciones
- **fuente_dato:** free → Deribit public
- **tenemos_datos:** parcial
- **backtesteable_ya:** parcial #derivados #free
- **backtest_en:** —
- **usado_por:** Leverage flush/squeeze
- **origen:** agentes/derivados_glassnode/framework.md §A

**0.42-0.56 = risk-on/mínimos** (contrarian de suelo); ~1 o subiendo = defensivo. Volumen adelanta al OI.

### DVOL / IV ATM (term structure 1W/1M/3M/6M)
- **id:** dvol-iv
- **tipo:** derivados
- **mide:** volatilidad implícita esperada e índice DVOL de Deribit
- **fuente_dato:** free → Deribit public (DVOL desde ~2021 en Deribit)
- **tenemos_datos:** parcial → free reciente
- **backtesteable_ya:** parcial #derivados #free
- **backtest_en:** —
- **usado_por:** playbook LP, timing de eventos
- **origen:** agentes/derivados_glassnode/framework.md §A

Curva **ascendente** (contango) = calma; **invertida/front-end spike** = evento inminente. DVOL en mínimos = "primeras etapas de suelo, no conclusión". Rangos BTC: pánico ~70-80% 1W, tranquilo 34-47%, mínimos ~30-34%. ⚠️ "IV baja → expansión" a menudo llega semanas/meses tarde (ver track record).

### VRP — Volatility Risk Premium (IV − RV)
- **id:** vrp
- **tipo:** derivados
- **mide:** prima de la vol implícita sobre la realizada
- **fuente_dato:** mixto → **RV es free** (precio); IV free reciente (Deribit) → VRP calculable free reciente
- **tenemos_datos:** parcial → sí desde que hay IV de Deribit
- **backtesteable_ya:** parcial → sí en ventana con datos Deribit #backtesteable #derivados #free
- **backtest_en:** —
- **usado_por:** semáforo de farmeo LP (estrategia LP short-vol)
- **origen:** agentes/derivados_glassnode/framework.md §A

**Semáforo LP:** VRP muy positivo (IV>>RV) = te pagan por estar corto de gamma → **farmea**. VRP negativo (IV<RV) = la vol se realiza → **fuera del LP** (marcó el 4-feb-26 el inicio del tramo bajista). Es la métrica derivados **más backtesteable con datos free** (IV Deribit + RV de precio).

### Max Pain / Dealer Gamma (GEX)
- **id:** gex-maxpain
- **tipo:** derivados
- **mide:** strike de máximo dolor + cómo cubren los market makers (gamma)
- **fuente_dato:** paid → GEX necesita cadena de opciones completa (Glassnode/proveedores); max pain aproximable free
- **tenemos_datos:** no (max pain parcial free)
- **backtesteable_ya:** no #no-backtesteable #derivados #paid #pendiente-suscripcion
- **backtest_en:** —
- **usado_por:** playbook LP (¿el rango aguanta?)
- **origen:** agentes/derivados_glassnode/framework.md §A

**Long gamma / precio sobre max pain = amortigua** (rango estable, farmea). **Short gamma cerca de spot = amplifica** (ensancha o sal).

### Futures basis / term structure
- **id:** basis
- **tipo:** derivados
- **mide:** contango vs backwardation (perp/calendar)
- **fuente_dato:** free → exchanges public
- **tenemos_datos:** parcial
- **backtesteable_ya:** parcial #derivados #free
- **backtest_en:** —
- **usado_por:** Leverage squeeze (backwardation → squeeze)
- **origen:** agentes/derivados_glassnode/estrategia_leverage.md

**Backwardation** (perp/calendar negativos) = cubierto para más caída / shorts cargados → precede short-squeeze (dic-22→ene-23). Basis >8% anualizado = capital market-maker vuelve (constructivo).
