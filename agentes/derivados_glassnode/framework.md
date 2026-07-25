# Framework de DERIVADOS y OPCIONES de Glassnode (reverse-engineering)

**Qué es esto:** reconstrucción del método con el que Glassnode lee derivados/opciones en su
sección "off-chain / derivatives" del *Week On-Chain* (suele ser la última sección antes de las
conclusiones) y en sus tweets/informes. Destilado por Beltrán a partir de su material publicado +
metodología conocida. **NO es texto oficial de Glassnode** — es el marco reconstruido para operar.

> Filosofía central: los **derivados NO predicen dirección**. Son una lente de **POSICIONAMIENTO
> y SENTIMIENTO**: ¿el mercado está cubierto (con miedo) o complaciente (hedges quitados)?
> ¿el apalancamiento está limpio o cargado? Glassnode **superpone** esta lente al mapa **on-chain**
> de cost-basis (STH/realized) que da el DÓNDE (soporte/resistencia). Derivados = el COMBUSTIBLE.

---

## A) MÉTRICAS DE OPCIONES (las que usan)
| Métrica | Qué mide | Lectura de Glassnode |
|---|---|---|
| **ATM Implied Vol + term structure** (1W/1M/3M/6M) | Vol esperada por plazo | Curva **ascendente** (1W<6M) = riesgo de evento cercano descontado, calma corto plazo, prima en largo. **Comprimida** = complacencia. **Invertida** = estrés/evento inminente. *(Ej. tweet: 1W 34,3% vs 6M 40,8% = ascendente.)* |
| **25-delta Skew + term structure** | IV de puts vs calls (miedo direccional) | **Alto/positivo** (puts caras) = demanda de cobertura a la baja = miedo. **Colapsando** = hedges quitándose = complacencia/alcista. Front-end (1W) vs back (3-6M). *(Ej. tweet: 1W ~4% vs 3-6M 11-12% = miedo cercano quitado, prima defensiva en largo.)* |
| **Options OI Put/Call ratio** | OI puts / OI calls | **>1** defensivo/bajista; **cayendo** = calls ganan cuota = **unwind de coberturas**. *(Ej. tweet: 0,52 desde 0,76 = desarme defensivo.)* |
| **Options Volume Put/Call** | Flujo del día | Confirma el OI; caída = menos compra de protección. |
| **Max Pain** | Precio donde más opciones expiran sin valor | Actúa de **imán/ancla**. Precio **sobre** max pain + aguantar = dealer gamma **amortigua** movimientos (techo→ancla). |
| **Options OI por strike / notional** | Muros de posicionamiento | Concentraciones = imanes/resistencias. |
| **DVOL + IV vs RV (VRP)** | Vol implícita index vs realizada | IV>>RV = vol cara (vender premium); IV<RV = barata (comprar vol). |

## B) MÉTRICAS DE FUTUROS / PERPS
| Métrica | Qué mide | Lectura de Glassnode |
|---|---|---|
| **Open Interest** (perps + term futures + options) | Apalancamiento/actividad abierta | Subiendo = leverage nuevo (más combustible). Muy por debajo de picos = **estructura limpia**, menos riesgo de cascada. |
| **Funding rate vs neutral** | Coste de estar largo perp | Positivo sostenido = sesgo largo apalancado. **Bajo la neutral** = sin leverage nuevo (optimismo "sano"). |
| **Estimated Leverage Ratio** | OI / market cap del exchange | Alto = frágil a desapalancamiento. |
| **Liquidations / dominance** | Combustible de squeeze | Cascadas de liquidación acompañan suelos de ciclo. |
| **Futures basis / term structure** | Contango vs backwardation | Backwardation = estrés. |

## C) CÓMO LLEGAN A CONCLUSIONES (el razonamiento)
1. **Posicionamiento (¿cubierto o complaciente?):** combinan **skew + put/call + funding**.
   - Skew colapsando + put/call cayendo + funding bajo neutral → *"el optimismo viene de quitar
     coberturas, no de leverage nuevo → los squeezes retracen MENOS violentamente"*. (Week On-Chain 22-jul.)
2. **Event risk (¿cuándo?):** la **pendiente de la IV term structure**. Ascendente = calma cercana;
   invertida = evento/estrés inminente.
3. **Riesgo de desapalancamiento (¿frágil?):** **OI + funding + leverage ratio**. Estructura limpia
   = poca cascada; **longs apalancados subiendo = vulnerable a un desapalancamiento del tipo que
   acompaña suelos de ciclo** (Charting Crypto Q3).
4. **Dealer hedging (¿amortigua o persigue?):** **max pain**. Reclaim del max pain + aguantar =
   dealer gamma amortigua los movimientos (de techo a ancla).
5. **Cruce SIEMPRE con on-chain:** los derivados dan el POSICIONAMIENTO; el **STH cost basis /
   realized price** dan el DÓNDE. Conclusión típica: *"el squeeze es real (hedges off) pero no ha
   despejado la resistencia (STH cost basis $69K)"*.

## D) VOCABULARIO DE SEÑALES (traducción a acción)
- **Skew alto + put/call>1 + funding+++** = miedo/cobertura máxima → históricamente cerca de suelos (contrarian alcista).
- **Skew colapsado + put/call bajo + funding bajo neutral** = complacencia/hedges off → rally sin combustible fresco; vigilar si es techo local.
- **OI alto + funding alto + leverage alto** = frágil → riesgo de flush/desapalancamiento.
- **IV comprimida + term structure plana** = calma → posible expansión (comprar vol / fuera de LP).
- **Precio sobre max pain sostenido** = dealer amortigua → menos volatilidad hasta el vencimiento.

## E) LÍMITES DEL FRAMEWORK (honesto)
- Es **sentimiento/posicionamiento**, NO dirección. Un mercado "complaciente" puede seguir subiendo.
- Los umbrales (skew "alto", put/call "bajo") son **relativos a su propia historia**, no absolutos.
- La calidad depende del **track record**: hay que marcar sus llamadas vs resultado (ver `reports/`).
