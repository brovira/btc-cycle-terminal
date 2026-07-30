# Catálogo de indicadores de Glassnode — ¿cuáles deciden DE VERDAD hoy?

**Para qué:** antes de backtestear nada, saber **qué indicadores mueven sus decisiones hoy** (no cuáles
aparecen de pasada, ni cuáles usaban en 2021). Sin esto, se acaba backtesteando lo que es fácil de medir
en vez de lo que el método realmente usa.

## Cómo se midió (y sus límites)

Dos pasadas automáticas sobre los **272 artículos completos** (los 56 stubs se excluyen para no falsear
2021-22 a la baja):

1. **Texto completo** — % de artículos del año que mencionan cada indicador.
2. **Solo secciones de decisión** — resumen ejecutivo (bullets de cabecera) + conclusión. **Esta es la
   buena**: es donde declaran la postura, no donde explican una métrica de pasada.

> **Límites honestos:** cuenta *menciones*, no peso causal. Un patrón amplio (p.ej. "realized profit/loss")
> captura más que uno estrecho. Y una métrica puede decidir sin nombrarse en la conclusión. Úsalo como
> **señal de tendencia** (0%→68% o 66%→0% son reales), no como medida exacta.

---

## 🎯 Lo que decide HOY (% de conclusiones que lo citan, 2025-26)

**Columna de datos verificada el 30-jul-2026** (`data/onchain/_disponibilidad.json`).

| # | Indicador | Vigencia | 2026 | Tipo | ¿Tenemos el dato? |
|---|---|---|---|---|---|
| 1 | **Realized Profit/Loss ($)** | 53% | 67% | Flujo | ✅ **`realized-profit` / `realized-loss`** |
| 2 | **ETF flows** | 42% | **67%** | Flujo | ❌ **hueco** (fuente gratis: Farside) |
| 3 | **IV / DVOL** | 42% | **82%** | Vol | ✅ ya construido (Deribit) |
| 4 | **Open Interest** | 30% | 17% | Posicionam. | ✅ ya construido (Bybit) |
| 5 | **True Market Mean** | 28% | **50%** | Nivel | ✅ **`true-market-mean`** |
| 6 | **STH Cost Basis** | 28% | 32% | Nivel | ✅ **`sth-realized-price`** |
| 7 | **Dealer Gamma / GEX** | 18% | 42% | Vol | 🟡 parcial (max pain sí, GEX no) |
| 8 | **Funding rate** | 16% | 10% | Posicionam. | ✅ ya construido |
| 9 | **Realized Price** | 14% | 17% | Nivel | ✅ `realized-price` |
| 10 | **Realized Cap** | 13% | 10% | Flujo | 🟡 derivable |
| 11 | **Spot CVD** | 13% | 32% | Flujo | ❌ hueco |
| 12 | **Realized P/L Ratio** | 12% | 25% | Oscilador | ✅ **derivable de #1** |
| 13 | **LTH/STH Supply** | 12% | 14% | Cohorte | 🟡 `lth-sopr` sí, supply no |
| 14 | **% Supply in Profit** | 10% | 17% | Oscilador | ⏳ slug 404, buscando variante |

**Resultado: 9 de los 14 drivers cubiertos, 2 parciales, 3 huecos.** La escalera de cost basis completa
(True Market Mean + STH Cost Basis + Realized Price) y los flujos de beneficio/pérdida realizados —el
driver nº1— **están disponibles gratis** en BGeometrics, con 1.461 puntos (ventana móvil de 4 años).

## ☠️ Lo que MURIÓ (aparece en ≤5% de las conclusiones recientes)

| Indicador | Su época | Hoy |
|---|---|---|
| **GNI / Market Compass** | 66% de los artículos de 2020 | **0%** — descontinuado |
| **NUPL** | 15-18% (2020-23) | ~0% |
| **MVRV** (a secas) | 43% del texto en 2024 | 10% texto · **ausente de conclusiones** |
| **MVRV Z-Score** | nunca fue suyo | **5 artículos en 7 años** |
| **SOPR** | 47% en 2021 | 10% texto · 5% conclusiones |
| **Liveliness · CDD · Dormancy/ASOL · HODL Waves** | 23-39% en 2021 | **0%** |
| **Reserve Risk · NVT · Thermocap · Mayer Multiple** | 2020-21 | **0%** |
| **Active Addresses/Entities** | 50% en 2019 | **0%** |

## 📈 El giro de 2025-26: de valoración a FLUJOS y POSICIONAMIENTO

El cambio más fuerte del corpus no es qué nivel miran, sino **de qué hablan al concluir**:

| | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|
| IV / DVOL | 2% | 0% | 19% | **82%** |
| ETF flows | 0% | 12% | 27% | **67%** |
| Dealer Gamma | 0% | 0% | 4% | **42%** |
| Spot CVD | 0% | 2% | 2% | **32%** |
| True Market Mean | 2% | 4% | 14% | **50%** |

Glassnode 2026 concluye con **flujos (ETF, CVD, realized P/L) + posicionamiento de opciones (IV, gamma)**,
anclados a **dos niveles** (True Market Mean y STH Cost Basis). Los osciladores clásicos de valoración
(MVRV, NUPL, SOPR) han pasado a contexto explicativo.

---

## 🔴 Las 3 consecuencias para el backtest

**1. Los datos que tenemos NO son los que ellos usan.**
Tenemos confirmados **MVRV Z-Score y SOPR** — y son precisamente dos de los que **ya no deciden nada**
en su método (MVRV Z aparece en 5 artículos de 328; SOPR en el 5% de las conclusiones recientes).
Backtestearlos mediría indicadores populares en retail, **no el método de Glassnode**. Sigue siendo
legítimo hacerlo — pero llamándolo por su nombre, no "backtest del framework de Glassnode".

**2. Casi la mitad de lo que deciden hoy YA lo tenemos.**
IV/DVOL (82%), Open Interest, funding, max pain — toda la capa de derivados está construida y es gratis.
Sumando #3+#4+#7+#8, la pata de posicionamiento/vol cubre buena parte de su conclusión semanal actual.
**El backtest más fiel al método no es on-chain puro: es el cruce dirección × posicionamiento.**

**3. Hay un hueco nuevo que no habíamos visto: los flujos de ETF.**
Segundo driver de sus conclusiones en 2026 (67%) y **no lo cubrimos en absoluto**. Hay fuentes gratis
(Farside Investors publica netflows diarios por emisor). Antes valía cero; con ETFs desde 2024, es
estructural. **Candidato serio a añadir.**

---

## ⏳ Lo que queda abierto

1. **`% supply in profit`** — el slug `supply-in-profit` da 404. Es el oscilador con los umbrales
   **54,2% (techo de rally de bear) / 60% / 75% / 90%**, de los más citables del corpus. Buscar variante:
   `Actions → Descubrir métricas → slugs: supply`.
2. **ETF flows** — 2º driver de 2026 (67%) y sin cobertura. Fuente gratis: Farside Investors (netflows
   diarios por emisor). Requiere un ingestor nuevo.
3. **Spot CVD** — 32% en 2026. Derivable de trades de Binance, pero es pesado de reconstruir.
4. **Coin Metrics** — el catálogo devolvió HTTP 400 (endpoint cambiado); ya se prueban 4 variantes en el
   script. No es bloqueante: BGeometrics cubre la escalera.

## 🧾 El techo de datos que condiciona TODO backtest

BGeometrics gratis devuelve **1.461 puntos = 4 años exactos en ventana móvil** (hoy jul-2022 → jul-2026).
El backtest cubre **~1 ciclo**: suelo 2022 → bull 2024-25 → techo oct-2025 → bear 2026. Es suficiente para
validar la *mecánica* de una regla y ver cómo se comportó en un bear, un bull y un techo — pero **no** para
afirmar que funciona "en todos los ciclos". Cada resultado debe llevar esa etiqueta.
