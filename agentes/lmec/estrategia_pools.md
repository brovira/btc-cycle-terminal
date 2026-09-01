# LMEC · cómo elige sus pools de liquidez

**Fuente:** sus propios vídeos, jul-2026 → 20-ago-2026. Citas literales del corpus en
`agentes/lmec/yt-transcripts/`.

---

## El método de cribado — vídeo del 11-jul, la parte que vale

Es el único sitio donde enseña el proceso paso a paso, sobre una pool BNB/ETH:

1. **Coge el contrato del par** desde la pool y **pégalo en DexScreener**
   > *«Entramos en la pool, le damos al par, cogemos el contrato y lo pegamos en Dex Screener»*

2. **Mira la liquidez depositada.** La suya tenía **$91.000**
   > *«lo primero que vemos es que es una pool totalmente desconocida. Solamente hay $91,000 de liquidez depositada»*

3. **Mira la CONSISTENCIA del volumen**, no el pico
   > *«vemos abajo en las barras como el volumen de esta pool es bastante consistente, algo que nos interesa porque de ahí vienen nuestras comisiones»*

4. ⭐ **LA MÉTRICA CLAVE — volumen diario ÷ liquidez de la pool**
   > *«y casi lo más importante, vemos que el **volumen diario de media es casi la mitad de la liquidez de la pool**, o sea, una rentabilidad muy alta»*

   Ratio ≈ **0,5 diario**. Es su medida real de «pool rentable», y es la que hay que
   copiar: mide cuántas comisiones genera cada dólar depositado, no el APR anunciado.

5. **Cambia la denominación: el par contra el otro token, NO contra dólares**
   > *«si este par de monedas en vez de verlo en dólares lo vemos contra la otra criptomoneda, pues ya podemos hacernos una idea de con qué rangos trabajar»*

6. **Mira el rango histórico plurianual** y mete el rango ahí
   > *«desde 2024, son ya 2 años, BNB y Ethereum **siempre se han movido dentro de este rango**. No es que sea un rango pequeño, ya que es de un **140%**»*

---

## Sus rangos son ANCHOS, no acotados

| Pool | Rango total | APR |
|---|---|---|
| **BNB/ETH** (Uniswap, red Ethereum) | **140 %** | 83 % |
| **BNB/ZEC** (Uniswap, BNB Chain) | **128 %** (0,51 – 1,20) | 23 % |

> *«yo con estas posiciones trabajo con **rangos de precios muy amplios**, aunque mi rentabilidad decaiga bastante»* (20-ago)

Y lo asume como coste consciente:
> *«Yo trabajo con rangos de precios muy amplios, eso también afecta para que la rentabilidad sea menor, pero de media me viene pagando **entre un 20 y 30 anual**»*

---

## Qué pares elige

**Solo las que quiere acumular igualmente.** La pool es el vehículo, no el objetivo:
> *«me interesa farmear principalmente con las monedas Blue Chip: **Bitcoin, ETH, Hype, BNB** y alguna otra que pueda ser tendencia»*

**La volatilidad es una VENTAJA, no un riesgo** — su lógica con ZEC:
> *«si es una moneda tan volátil, tan comerciada, eso significará que va a generar mucho volumen y **el volumen se traduce en comisiones** para nosotros si agregamos liquidez»*

**Entra con APR baja a propósito**, apostando a que vuelve el volumen:
> *«Ahora mismo la Pool me está dando solo un 23% anual, pero este dato no me importa porque yo sé que en cualquier momento va a volver la atención»*
> *«estar dentro de la pool de liquidez antes de que vuelva la atención, antes de que vuelva el volumen»*

---

## Sus reglas de gestión

**Mide en MONEDAS, no en dólares** (11-jul):
> *«Yo no me fijo en los dólares, cuánto vale mi liquidez, ni cuánto valen mis ganancias. Yo lo que veo son **6,2 monedas hype y 0,0033 Bitcoin más** que tengo en mi cartera»*

**Fuera de rango:** espera 1-2 semanas; si no vuelve, abre posición nueva (20-ago)

**Salida por rentabilidad:** retiró de Liminal Money por estar *«siempre por debajo de un 5% anual»* (27-feb)

**Interés compuesto, y cambia según el ciclo:**
- **Alcista:** dividendos → **pool NUEVA** que luego se vuelve pool base
- **Bajista (ahora):** dividendos → **la MISMA pool**, para acumular moneda

**Incentivos de Merkl** — su mejor rentabilidad/riesgo actual, en la cadena de Robinhood:
> *«puedes emparejar a la acción de Tesla con el SP500, rentabilidad de los incentivos **114% anual**»*, con RWAs y acciones. Avisa de que caducan (3-sep) y suelen extenderse.

**Cartera (20-ago):** 55 % en BTC/alts/farming · 45 % en estables

---

## Sus pools abiertas a 20-ago-2026

| Pool | Dónde | Notas |
|---|---|---|
| ETH/cbBTC | PancakeSwap · Base | abierta en marzo, $19.000 → +$1.320 en comisiones, 55 % APR |
| BNB/ETH | Uniswap · red Ethereum | 83 % APR, rango 140 % |
| BNB/ZEC | Uniswap · BNB Chain | 23 % APR, rango 128 % |
| HYPE/BTC | HyperEVM | estuvo fuera de rango bastante tiempo |
| RWA/acciones | Robinhood chain | Amazon-SP500, Nvidia, Tesla-SP500, con incentivos UNI de Merkl |

---

## Filtro para funding rates (estrategia distinta, criterio explícito)

Del 20-ago, sus tres umbrales:
> *«lo que busco es algo muy claro, una **rentabilidad por encima de al menos un 40%**, después una **constancia o sostenibilidad por encima de un 80 o 90%** y un **riesgo de spread bajo o medio**»*

Y el aviso que más vale del vídeo:
> *«la mayoría de monedas que ofrecen una buena rentabilidad **no tienen liquidez suficiente**. Aunque tú veas una rentabilidad del 500% y pienses que es dinero gratis, no es así, porque esa rentabilidad tan alta es debido a que **no hay liquidez en los libros de órdenes**»*

Por eso comprueba a mano volumen y open interest de cada moneda, y descarta las herramientas
que no se lo muestran.

---

## LO QUE SU MÉTODO NO MIRA — y hay que decirlo

**1. No hay ni una mención al impermanent loss / divergencia.** El ratio volumen/TVL mide
lo que la pool GENERA, no lo que la posición PIERDE si el par diverge. Son las dos mitades
del resultado y solo mira una. Un LP es un short straddle sobre el ratio del par: si BNB/ETH
tiende a un lado durante el bajista, las comisiones pueden no cubrir la divergencia.

**2. $91.000 de TVL es diminuto, y él lo cuenta como ventaja.** Es cierto que poca liquidez
compartida = más comisiones por dólar. Pero también es riesgo de contrato, de salida y de
dilución: si metes tamaño, tu propio capital hunde el ratio volumen/TVL que te hizo entrar.

**3. Su serie de referencia es corta.** *«Desde 2024, son ya 2 años»* — para BNB/ETH eso
excluye 2021 y 2022, donde el ratio se movió mucho más. Un rango calibrado sobre dos años
laterales es exactamente el que se rompe cuando vuelve la tendencia.

**4. La rentabilidad declarada baja al contacto con la realidad:** 83 % y 55 % de APR
nominal contra *«de media me viene pagando entre un 20 y 30 anual»* por trabajar con rangos
anchos. La cifra que enseña no es la que cobra.

---

# Filtro propio — antes de entrar en cualquier pool

Nace del caso cbBTC/SOL del 1-sep-2026: dos pools del **mismo par**, una con 64,6 % y
otra con 31,9 %. La buena era la segunda.

| | A (0,05 %) | B (0,16 %) |
|---|---|---|
| Yield/TVL | **64,6 %** | 31,9 % |
| TVL | $10.608 | $6.877.251 |
| Volumen 24h | $37.567 | $3.751.077 |
| Volumen/TVL | 3,54 | **0,545** |

## 1. Test de dilución — ¿ese número sigue siendo tuyo al entrar?

```
yield_real ≈ yield_mostrado × TVL / (TVL + tu_aporte)
```

Un yield alto sobre un TVL diminuto **no es tuyo**: es de quien ya está dentro. Si el
número se hunde al meter tu tamaño, nunca existió para ti.

## 2. Test de enrutamiento — el que de verdad decidió el caso

**Compara los distintos fee tiers del MISMO par.** Si el tier más BARATO mueve MENOS
volumen, ese pool **no lo está enrutando nadie**: los agregadores calculan impacto de
precio y mandan el flujo al pool profundo aunque cobre el triple.

Es una trampa de liquidez: no lo enrutan porque es fino, y sigue fino porque no lo
enrutan. **Añadir capital no lo arregla** — solo te hace dueño de un pool que nadie usa.

## 3. Selección adversa — de quién viene ese volumen

En un pool fino, buena parte del volumen son **arbitrajistas corrigiendo tu precio
desfasado**. Las comisiones que cobras son la compensación por una pérdida que ya te
hicieron. Volumen no es lo mismo que demanda.

## 4. Suelo de TVL

LMEC llamaba *«totalmente desconocida»* a una pool de **$91.000**. Por debajo de eso,
el yield mostrado es ruido. Y cuidado con la fila que delata una tabla rota: en la misma
lista, `SCP/cbBTC` con **$221** de TVL y **$0** de comisiones aparecía al **46 %**.

## 5. Anchura del rango según el par, no fija

La correlación en dólares **no** predice la estabilidad del ratio, que es lo único que
saca una posición de rango:

```
σ²(ratio) = σ²a + σ²b − 2·ρ·σa·σb
```

| Par | ρ (1a) | σ del ratio | Rango sugerido |
|---|---|---|---|
| cbBTC/ETH | 0,90 | ~33 % | ~130 % ✓ |
| cbBTC/SOL | 0,86 | ~45-50 % | **180-200 %** |
| BTC/HYPE | 0,50 | mucho mayor | el más divergente de todos |

**Regla:** ρ más baja y/o el segundo activo más volátil ⇒ rango más ancho. Copiar el mismo
rango de un par a otro es el error.
