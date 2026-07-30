# Framework de STRATEGY WATCH — flujos institucionales y rendimiento de fondos

**Qué es:** el marco del **Strategy Watch** de Glassnode (mensual, en colaboración con Crypto Insights
Group). Es un producto **distinto** al Week On-Chain: no analiza niveles de precio ni cohortes de
holders, sino **qué está haciendo el dinero institucional** — flujos de capital, rendimiento de fondos
por estrategia, y posicionamiento de gestores.

**Lanzamiento:** enero 2026 (edición #1). Mensual. **Material propio en el repo privado**
(`research/glassnode-kb/strategy-watch/`, PDFs); aquí solo resúmenes, por copyright.

---

## Dónde encaja (y dónde NO)

| Agente | Pregunta que responde | Horizonte |
|---|---|---|
| `lmec` / `cowen` | ¿En qué fase del ciclo estamos? | 4 años |
| `glassnode_tactico` | ¿Dónde está el precio en la escalera de cost basis? | semanas-meses |
| `derivados_glassnode` | ¿Quién está apiñado y qué se romperá? | 0-3 semanas |
| **`glassnode_strategy`** (este) | **¿Está entrando o saliendo dinero institucional, y qué hacen los fondos?** | **mensual** |

**No sirve para:** decidir un nivel de entrada, un rango de LP ni un trade táctico. Sirve para
**contexto de demanda estructural** — si el dinero grande se está retirando, los rallies son más
frágiles aunque el on-chain diga otra cosa.

---

## A) LAS 5 SECCIONES FIJAS

### 1. Institutional Flow Monitor — ¿entra o sale capital?
Cuatro medidas, todas mensuales:

| Métrica | Qué mide (definición suya del glosario) |
|---|---|
| **Capital Flow** | Cambio mensual acumulado del **realized cap** — despliegue neto de capital, valorando cada unidad a su último precio transaccionado. Se mide por separado para BTC, ETH y stablecoins |
| **ETF / DAT Flow** | Entradas/salidas netas mensuales en los ETF spot de EE.UU. y en los *Digital Asset Treasuries* (empresas con BTC en balance), en BTC o ETH |
| **DeFi TVL & Stablecoin Cap** | Valor total bloqueado en DeFi de Ethereum + capitalización de las stablecoins principales |
| **CME Basis Yield** | Valor en dólares que ganan las instituciones al mes con el *cash-and-carry* (prima entre spot y futuros CME). Es el **incentivo de las estrategias market-neutral** |

**La lectura clave que repiten:** si el capital sale de BTC/ETH **y además** las stablecoins se
contraen, es **de-risking real**, no rotación dentro del ecosistema. Si las stablecoins crecen mientras
sale de BTC, es rotación (menos grave).

### 2. Fund & SMA Performance — ¿qué estrategias funcionan?
Tabla del **CIG Universe** (cientos de gestores) con rendimiento del mes, YTD, 3 años anualizado,
volatilidad 3a y máximo drawdown 3a. Dos familias:

- **Directional** (exposición neta larga/corta): Fundamental · Macro · Event Driven · Quant Directional ·
  Quant Trend Following
- **Market-Neutral** (exposición neta minimizada): Statistical Arbitrage · Relative Value · DeFi/Yield ·
  Volatility Arbitrage · Market Making
- **Crypto Share Classes**: las mismas market-neutral pero denominadas en BTC o ETH

### 3. On-chain Vault Performance — ¿rinde el yield on-chain?
Benchmarks de *curators* (vaults gestionados) frente a su alternativa sin riesgo:
- **USD Curator Benchmark** vs **U.S. Treasury Rate**
- **ETH Curator Benchmark** vs **Ethereum Staking Yield**

Solo entran vaults con ≥$10M de TVL, equiponderados, rentabilidad **neta y solo del yield base**
(excluye tokens de incentivo). Datos validados por CIG con inputs de Vaults.fyi.

### 4. Manager Monitor — ¿qué piensan los gestores?
Encuesta agregada a fondos: **nivel medio de caja** (% de AUM), previsión a 3 meses, **fondos vs SMA**,
**directional vs market-neutral**, desglose por AUM y por tipo de LP, y ranking de ecosistemas por foco.

### 5. Allocation Update — quién asigna y quién lanza
Noticias de asignadores (fondos soberanos, family offices, pensiones) y de gestores (lanzamientos,
rondas, licencias). Es cualitativo, útil como señal de adopción institucional.

---

## B) CÓMO SE LEE (la lógica del producto)

1. **¿El dinero entra o sale?** → Capital Flow + ETF/DAT. Negativo sostenido = demanda estructural débil.
2. **¿Hay incentivo para el dinero market-neutral?** → CME Basis Yield. Si se comprime, las estrategias
   de carry pierden atractivo y ese capital se retira → menos liquidez de base.
3. **¿Los gestores están dentro o en liquidez?** → nivel de caja. Subir caja = defensivo.
4. **¿Qué estrategia paga?** → tabla de rendimiento. Cuando *market-neutral* bate a *directional* de
   forma sostenida, el mercado no premia la dirección.
5. **¿El yield on-chain compensa el riesgo?** → curator vs Treasury / staking. Si la prima es mínima,
   no compensa la complejidad.

---

## C) UMBRALES Y REFERENCIAS QUE ELLOS DAN

No es un producto de umbrales mecánicos como el Week On-Chain. Los puntos de referencia observados:

- **Prima de los curators USD sobre Treasuries:** en jun-2026 fueron **~27 puntos básicos** a 12 meses
  (4,29% vs 4,02%) — lo describen como *"prima fina"*, y concluyen que los vaults curados son
  **"una asignación estructural de crédito on-chain, no un sustituto de Treasuries"**.
- **Los curators ETH llevan retrasando al staking directo** de forma consistente en todos los periodos
  → *"la prima por complejidad es negativa"*.
- **Nivel de caja de los hedge funds:** ~12% del AUM (ene-26) · ~15% (feb-26) · ~11% (may-26) →
  **~16% (jun-26)**. Ellos lo interpretan contra su media de 1 año, no contra un umbral fijo.
- **Score de fundraising** (escala 0-10): pico ~6,8 en dic-2024 → **3,28 en jun-2026**, mínimo de la
  serie. Lo leen como *"fatiga de fin de ciclo, no deterioro repentino"*.

---

## D) GUARDARRAÍLES (suyos y nuestros)

- **Disclaimer estándar en todas las ediciones:** no es asesoramiento de inversión.
- **Los balances de exchange** vienen de su clustering propietario y *"pueden no capturar la totalidad
  de las reservas"*.
- **Los datos de fondos son autodeclarados** (recogidos vía gestores, administradores y validación de
  CIG) → sesgo de supervivencia y de selección. Ellos lo dicen: el CIG Universe *"no constituye
  asesoramiento"* y está diseñado para análisis comparativo.
- **Serie MUY corta:** empezó en enero de 2026. Con 6 ediciones **no hay histórico para backtestear
  nada**. Es contexto cualitativo, no señal mecánica. ⚠️ **No inventar tendencias con n=6.**
- **Falta la edición #5 (mayo 2026)** en nuestro archivo.
