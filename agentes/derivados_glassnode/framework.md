# Framework de DERIVADOS y OPCIONES de Glassnode (reverse-engineering)

**Qué es esto:** reconstrucción del método con el que Glassnode lee derivados/opciones en la
sección "off-chain / derivatives" del *Week On-Chain* (suele ser la penúltima sección, antes de las
conclusiones). **Destilado de un barrido de 152 Week On-Chain con contenido de derivados (2020→22-jul-2026)**
— el corpus completo vive en `research/glassnode-kb/` del repo DeFi-Tracker (privado); las extracciones
estructuradas y el scorecard, en `reports/`. **NO es texto oficial de Glassnode** — es el marco reconstruido
para operar (fijar rangos de LP y salir antes de los movimientos grandes).

> ## Filosofía central (confirmada por el corpus)
> Los **derivados NO predicen dirección**. Son una lente de **POSICIONAMIENTO y SENTIMIENTO**:
> ¿el mercado está cubierto (con miedo) o complaciente (hedges quitados)? ¿el apalancamiento está
> limpio o cargado? Glassnode **superpone** esta lente al mapa **on-chain** de cost-basis
> (STH/realized) que da el **DÓNDE** (soporte/resistencia). Derivados = el **COMBUSTIBLE** y el
> **momento**; on-chain = el nivel. La conclusión típica cruza las dos: *"el squeeze es real (hedges off)
> pero no ha despejado la resistencia (STH cost basis)"* (WoC 2026-07-08).

---

## A) MÉTRICAS DE OPCIONES (las que usan, con el rango real observado en el corpus)

| Métrica | Qué mide | Lectura de Glassnode + niveles vistos |
|---|---|---|
| **ATM Implied Vol + term structure** (1W/1M/3M/6M) | Vol esperada por plazo | Curva **ascendente** (1W<6M / contango) = calma corto plazo, prima en largo. **Comprimida** = complacencia. **Invertida / front-end spike** = estrés/evento inminente. Rangos reales BTC: panic ~70–80% 1W (feb-26), régimen tranquilo 34–47%, mínimos multi-año ~30–34% (may-26, jun-23, ago-25). El **10-oct-2025** el 1W IV saltó a **76%**. |
| **DVOL (Deribit)** | Índice de IV | "Históricamente bajo" cuando solo ~2–3% de los días tuvieron menos (ago-25, jun-26). Régimen alto post-crash: **oscila 40–50** (nov-25). DVOL subiendo desde mínimos = "primeras etapas de un suelo, no su conclusión" (jul-26). |
| **25-delta Skew (puts − calls) + term structure** | Miedo direccional (IV de puts vs calls) | **Alto/positivo** (puts caras) = demanda de cobertura a la baja = miedo. **Colapsando/negativo** = hedges quitándose = complacencia. Front (1W) vs back (3-6M). Umbrales reales: **>20–30% = pánico/extremo** (feb-26 llegó a 28–30%; 10-oct-25 flip a +17%), **~11–14% = defensivo normal en bear**, **~2–6% = neutral/risk-on**, **negativo (calls > puts, p.ej. −6,1% may-25) = risk-on sano**. Un **spike de skew front-end suele coincidir con extremos locales** (revierte rápido). |
| **Options OI Put/Call ratio** | OI puts / OI calls | **>1** defensivo/bajista; **cayendo** = calls ganan cuota. Rangos: **0,42–0,56 = risk-on/mínimos** (ago-23, jul-26 el 0,56 fue mínimo de 2026); **~1 o subiendo = defensivo**; el **14d volume P/C > 1 al máximo del año** (jul-26) se marcó como posible señal contrarian de suelo. |
| **Options Volume Put/Call** | Flujo del día | Confirma/adelanta el OI. Spike de put-volume en retest de mínimos y luego **colapso al volver el call-flow** = miedo agotándose (jul-26). El 10-oct-25 el volume P/C saltó de ~0,8 a **1,51**. |
| **Max Pain** | Strike donde más opciones expiran sin valor | **Imán/ancla**. Spot **debajo** de max pain = sesgo defensivo (jul-26 estuvo ~6% debajo de $66k). **Reclaim del max pain + aguantar** = dealer gamma pasa de techo a **ancla** y **amortigua** los movimientos → menos vol realizada. |
| **Dealer Gamma (GEX)** | Cómo cubren los market makers | **Long gamma** (gamma positiva, típico cerca de grandes strikes/max pain) = venden fuerza/compran debilidad → **amortiguan** (menos vol). **Short gamma** (gamma negativa cerca de spot) = compran fuerza/venden debilidad → **amplifican** los movimientos. En ene-26 la gamma se volvió corta en strikes superiores → "subidas fuerzan a los dealers a comprar spot → refuerzan el alza". |
| **Volatility Risk Premium (VRP = IV − RV)** | Prima de la vol implícita sobre la realizada | **IV >> RV (VRP muy positivo, +11 a +27 pts)** = vol cara → **vender premium / farmear es rentable** (el que está corto de gamma cobra). **VRP ≈ 0** = "punto de entrada históricamente atractivo para compradores de vol". **VRP negativo (IV < RV)** = la vol ya se está realizando → las opciones **amplifican** en vez de amortiguar; carry punitivo para vendedores de gamma. |
| **IV moneyness / vol smile** | Forma de la sonrisa por strike | Reprice del **ala de puts** a la baja = coste absoluto de protección cayendo aunque el skew siga defensivo (jul-26). |

## B) MÉTRICAS DE FUTUROS / PERPS

| Métrica | Qué mide | Lectura de Glassnode + niveles vistos |
|---|---|---|
| **Open Interest** (perps + fixed-term + options) | Apalancamiento/actividad abierta | Subiendo = leverage nuevo (más combustible). **Muy por debajo de picos = estructura limpia** (menos cascada). OI cayendo >5% semanal en top-3 exchanges = "flush-out event". Caídas históricas: **−$19B en un día el 10-oct-25** (mayor de la historia), −$2,5B ago-23 (mayor desde LUNA), −11% en 1 día (−3σ) el 5-ago-24. |
| **Funding rate vs neutral (0,01%/8h)** | Coste de estar largo perp | **Positivo sostenido / >8% anualizado** = longs apalancados apiñados (frágil; feb-y-oct-25 top). **Bajo la neutral / negativo** = sin leverage nuevo, o sesgo corto (combustible de squeeze). **Reset a cero o negativo tras un flush** = "históricamente constructivo en las semanas siguientes" (pero ver track record: falla cerca de techos de ciclo). |
| **Perp Directional Premium / CVD bias** | Sesgo largo/corto agregado | Récord de sesgo corto neto (abr-26) = "potencial de dislocaciones al alza si el flujo gira". Reset a neutral = "consolidación o agotamiento de tendencia". |
| **Estimated Leverage Ratio** (OI / market cap) | Fragilidad del sistema | **≥2% del market cap = zona de riesgo de flush** (umbral que citan; ene-22 estaba en 1,98–2%). Colapsó a mínimos multi-mes el 10-oct-25. |
| **Liquidaciones / dominancia long-short** | Combustible de squeeze | Dominancia de liquidación de **shorts** alta (p.ej. 85% ene-23, > que el 75% de FTX) → rally por short-squeeze. Dominancia de **longs** (68% sep-21) → mark-down. Cascadas acompañan suelos de ciclo. |
| **Futures basis / term structure** | Contango vs backwardation | **Backwardation** (perp/calendar negativos, p.ej. −2,5%/−0,3% post-FTX, −27%/−49% marzo-23) = estrés / cubierto para más caída → suele preceder short-squeeze. Basis >8% anualizado (300bps sobre T-bills) = incentiva capital de market-makers a volver (constructivo, dic-23). |
| **Collateral mix** | Calidad del apalancamiento | Mayoría **stablecoin-margined** = estructura más conservadora/estable post-FTX (jun-25). Crypto-margined alto = más frágil. |

## C) CÓMO LLEGAN A CONCLUSIONES (el razonamiento, 5 pasos)

1. **Posicionamiento — ¿cubierto o complaciente?** Combinan **skew + put/call + funding**.
   - *Skew colapsando + put/call cayendo + funding bajo neutral* → "el optimismo viene de quitar coberturas,
     no de leverage nuevo → los squeezes retracen MENOS violentamente" (WoC 2026-07-22).
   - *Skew alto + put/call>1 + funding+++ + OI alto* → miedo/cobertura máxima **o** longs apiñados (según signo del funding).
2. **Event risk — ¿cuándo?** La **pendiente de la IV term structure**. Ascendente = calma cercana; invertida / front-end spike = evento/estrés inminente.
3. **Riesgo de desapalancamiento — ¿frágil?** **OI + funding + leverage ratio**. Estructura limpia = poca cascada;
   *longs apalancados subiendo + funding alto + OI en máximos* = vulnerable a un flush (el tipo que acompaña techos y suelos).
4. **Dealer hedging — ¿amortigua o persigue?** **max pain + GEX**. Long gamma / reclaim de max pain = amortigua (techo→ancla). Short gamma cerca de spot = amplifica.
5. **Cruce SIEMPRE con on-chain:** derivados = POSICIONAMIENTO; **STH cost basis / realized price / true market mean** = el DÓNDE. La lectura completa es la intersección.

## D) VOCABULARIO DE SEÑALES (traducción a acción)

- **Skew alto + put/call>1 + funding+++ + OI máximos** = longs apiñados/frágil → **riesgo de flush a la baja** (techo local o de ciclo).
- **Skew colapsado + put/call bajo + funding ≤ neutral tras flush** = complacencia/hedges off → rally sin combustible fresco (retrace suave); vigilar si es techo local.
- **Funding negativo sostenido + OI subiendo + backwardation** = shorts apiñados → **combustible de short-squeeze al alza**.
- **OI muy por debajo de picos + funding neutral (post-flush)** = estructura limpia → menos riesgo de cascada; **spot toma el mando**.
- **IV/DVOL en mínimos + skew plano** = calma → **posible expansión** (⚠️ señal contrarian pero **puede llegar tarde meses** — ver track record).
- **VRP muy positivo (IV>>RV)** = te pagan por estar corto de gamma → **farmear/vender premium**.
- **VRP negativo (IV<RV)** = la vol ya se realiza → las opciones amplifican → **NO farmear, fuera de LP**.
- **Precio sobre max pain sostenido / dealer long gamma** = amortigua → menos vol hasta el vencimiento (seguro para farmear).

---

## E) 🎯 PLAYBOOK LP (short vol) — cuándo farmear, ensanchar o SALIR antes de un movimiento grande

El LP concentrado = **corto de gamma / corto de vol** (idéntico perfil a vender un straddle). Este playbook mapea
las señales de arriba a las tres decisiones de LP. **La regla maestra del corpus: no es "IV baja" lo que precede a
los movimientos grandes, es la CONFLUENCIA de leverage extremo + on-chain en un nivel clave + posicionamiento estirado.**

### 🟢 FARMEAR (rango estrecho OK, cobrar fees / corto de vol) cuando coinciden:
- **VRP claramente positivo** (IV por encima de la realizada; te pagan la prima).
- **Apalancamiento limpio/reseteado:** OI muy por debajo de picos, funding en neutral o negativo **después** de un flush.
- **Dealer long gamma / precio pineado cerca de max pain** (amortiguación mecánica).
- **Skew moderándose**, sin spikes; put/call bajo pero estable.
- On-chain: precio dentro de un rango de cost-basis respetado (entre soportes/resistencias conocidos).
- *Ejemplos del corpus:* may-26 ("volatility sellers in control", VRP amplio, DVOL mínimos), feb-abr-26 tras el reset, gran parte de 2024 (mercado spot-driven, leverage reseteado).

### 🟡 ENSANCHAR el rango / reducir tamaño (chop probable, vol latente) cuando:
- **IV/DVOL en mínimos multi-año PERO skew sigue negativo/defensivo** = "vol diferida, no comprimida por hedges" (ene-26): puede repricear de golpe con un catalizador. No salgas, pero no concentres.
- **Short gamma del dealer cerca de spot** (amplifica swings) sin un extremo de leverage todavía.
- **VRP ≈ 0** (opciones baratas): el edge de vender vol desaparece; céntrate menos, o rota parte a comprar protección.
- Funding oscilando/indeciso, OI plano: "grind choppy hasta que vuelva la demanda spot".

### 🔴 SALIR / cerrar LP ANTES del movimiento grande cuando aparece la CONFLUENCIA:
**Techo / flush a la baja (el patrón que mejor clavan):**
- **Funding fuertemente positivo (>8% anualizado) + OI en máximos + skew que se vuelve call-heavy/neutral desde defensivo** = longs apiñados. (Este trío marcó el techo del 8-oct-2025, ~2 días antes del mayor flush de la historia.)
- **VRP girando a negativo** (la realizada supera a la implícita) = la vol ya no se warehousea, se realiza → las opciones amplifican. (Marcó el 4-feb-2026 el inicio del tramo bajista.)
- **Front-end IV spike + skew disparándose a >20%** = estrés inminente.
- On-chain en/rechazando una resistencia de cost-basis (STH cost basis) con demanda spot cayendo.

**Suelo / flush exhaustivo (más violento, "capitulación"):**
- **OI todavía elevado mientras el precio pierde un soporte on-chain clave + funding aún positivo cayendo** = "leverage capitulando hacia mínimos que el spot ya vendió" → "la fase más violenta y exhaustiva de un flush" (jun-26).
- Aviso recurrente en suelos: **"un último spike de volatilidad de capitulación no puede descartarse"** aunque DVOL ya suba desde mínimos (jul-26). No re-entres al LP demasiado pronto.

### Reglas operativas destiladas
1. **Una señal aislada de "vol barata" NO es motivo para salir del LP** — históricamente llega semanas/meses antes del movimiento (todo el verano de 2025). Solo sal con la **confluencia**.
2. **El funding + OI extremos son tu mejor disparador de salida**: adelantan los flushes con 0–3 semanas y buen acierto direccional condicional al signo del funding.
3. **VRP es tu semáforo de farmeo**: positivo = farmea; negativo = fuera. Es la traducción más directa de "LP = corto de vol".
4. **Max pain / gamma define si el rango aguanta**: sobre max pain con dealer long gamma → rango estable (farmea); short gamma cerca de spot → rango vulnerable (ensancha o sal).
5. **Re-entra al LP tras el flush**, no antes: OI reseteado + funding neutral/negativo + VRP volviendo a positivo = estructura limpia para volver a farmear.

## F) LÍMITES DEL FRAMEWORK (honesto — ver `reports/track_record.md` para el detalle)
- Es **sentimiento/posicionamiento, NO dirección**. Un mercado "complaciente" puede seguir subiendo.
- Los umbrales (skew "alto", put/call "bajo") son **relativos a su propia historia**, no absolutos.
- **Su punto fuerte** (alta tasa de acierto y buen timing): lecturas de **leverage/posicionamiento** — "longs apiñados → flush", "shorts apiñados → squeeze".
- **Su punto débil:** las llamadas de **"IV baja → expansión"** aciertan en que *acaba* llegando un movimiento, pero **son ciegas de dirección y a menudo prematuras** (por semanas o meses). Vender vol al primer aviso de "vol barata" te habría costado meses de carry en 2025.
- La calidad depende del **track record**: cada llamada marcada vs resultado en `reports/track_record.md`.
