# Auditoría LMEC — ¿Compró el suelo real de 2022? ¿Cuándo avisó de vender en el ciclo 2023-2025?

**Alcance:** SOLO los 208 transcripts de `/home/user/btcrepo/agentes/lmec/yt-transcripts/` (mar-2022 → jul-2026) + los 4 resúmenes de `/home/user/belrogam/lmec/transcripts/`. Grep exhaustivo por fechas, precios y keywords. Sin conocimiento externo salvo el contexto de precios dado: suelo real BTC ~$15.500-16.000 (nov-2022), techo del ciclo ~$126k (oct-2025).

**Metodología:** se listó el corpus por mes, se identificaron huecos de cobertura, y se grepeó todo el corpus por menciones de precio de BTC + verbos de compra/venta/rotación. Cada cita se verificó releyendo el archivo fuente completo (no solo la línea del grep) para confirmar que la afirmación es *contemporánea al vídeo que la contiene* y no una referencia retrospectiva a un vídeo que no está en el corpus.

---

## 0. Cobertura del corpus (hallazgo estructural, clave para todo lo demás)

Archivos por mes en `yt-transcripts/`:

| Período | Nº vídeos |
|---|---|
| mar-2022 | 1 |
| abr-2022 | 1 |
| ago-2022 | 1 |
| **sep-2022 → ene-2023** | **0 (HUECO TOTAL)** |
| feb-2023 en adelante | cobertura mensual continua (2-12 vídeos/mes) |

**El hueco sep-2022 → ene-2023 cubre exactamente la ventana del suelo real (colapso de FTX, 9-21 nov-2022, BTC ~$15.500-17.000).** No existe en el corpus ningún vídeo publicado en esa ventana. Esto es la limitación central de esta auditoría: **no podemos verificar de primera mano lo que LMEC dijo en tiempo real durante el suelo**, porque esos vídeos no están en el archivo. Solo tenemos lo que él mismo cuenta *después* (jul-2023, sep-2023, may-2025, sep-2025) sobre lo que hizo/dijo entonces.

---

## 1. ¿Compró/recomendó comprar BTC en el suelo real (nov-2022), en tiempo real?

**Veredicto: NO VERIFICABLE con este corpus — no hay evidencia primaria, solo autocitas retrospectivas.**

### Lo que SÍ tenemos (los 3 vídeos de 2022 disponibles)

Ninguno de los tres vídeos de 2022 en el corpus (mar, abr, ago) menciona un precio de BTC ni recomienda comprar BTC en ese momento — son vídeos de estrategias DeFi (Terra, Polkadot/Polygon/Celo/Near, Cosmos) sin llamada operativa sobre BTC. El último disponible es del 19-ago-2022, casi 3 meses antes del suelo real; no hay nada publicado (en el corpus) entre esa fecha y feb-2023.

### Lo que LMEC dice DESPUÉS (2023+) que hizo/dijo en 2022 — no verificable

Se encontraron 4 autocitas, en 4 vídeos distintos y distantes en el tiempo, todas retrospectivas y ninguna contrastable contra el vídeo original (que no está en el corpus):

1. **[20230714]** (14-jul-2023, BTC ~$30.000 en ese momento):
   > "hace siete meses cuando sucedió el colapso de ftx por aquel entonces tocamos mínimos en el mercado bitcoin estaba por debajo de los 15 mil dólares [...] al día siguiente yo os compartí Este vídeo y en la miniatura ya podéis ver claramente el mensaje que os decía optimismo seamos optimistas con las criptomonedas"

2. **[20230912]** (12-sep-2023, BTC $25.000 en ese momento):
   > "si bien en octubre y noviembre de 2022 os comentaban los vídeos que para mí estábamos en precios perfectos para acumular [...] tocamos mínimos en de noviembre de 2022 con el colapso de ftx [...] cuando tocamos los 15.900 aproximadamente"

3. **[20250523]** (23-may-2025, BTC ~$110-112.000 en ese momento) — la cita más precisa, con fecha y precio exactos:
   > "Fíjate, 14 de noviembre del 22, Bitcoin en los $16,000. título, seamos optimistas con las criptomonedas."

4. **[20250912]** (12-sep-2025, BTC ~$115-116.000) — la más detallada, con capturas de pantalla mencionadas (no vídeo, solo transcript, no podemos ver la imagen):
   > "Junio de 2022. En este vídeo con total transparencia, Bitcoin había caído a los $18,000 [...] En mayo compra en 30.000, otra en mayo en 26.000, otra en junio en 23.000 [...] tuve suerte [...] pude comprar el suelo absoluto de Bitcoin. Aquí podéis ver la orden. 9 de noviembre del 22, una compra en los $15,750."

### Por qué esto NO cuenta como evidencia de "compró/recomendó comprar en tiempo real"

- El vídeo referido — **"Seamos optimistas con las criptomonedas"**, supuestamente del **14-nov-2022** — **no está en el corpus**. No podemos leer su contenido, ni confirmar si decía literalmente "comprad BTC ahora" o solo un mensaje motivacional/psicológico genérico (el propio LMEC lo describe como "mensaje optimista", no como una orden de compra concreta).
- Los vídeos de mayo/junio de 2022 con las compras en $30k/$26k/$23k/$18k **tampoco están en el corpus** (el corpus no tiene nada entre abr-2022 y ago-2022, ni entre ago-2022 y feb-2023).
- La captura de la "orden de compra" del 9-nov-2022 a $15.750 se **menciona y describe** en el vídeo de sep-2025, pero no podemos verla ni verificar su fecha real (es una captura de pantalla dentro de un vídeo de YouTube; el transcript solo tiene el audio).
- Es exactamente el patrón que se pidió excluir: contarlo después (2023, 2025) como "yo compré ahí", sin el vídeo original en tiempo real disponible para contrastar.

**Lo único objetivamente verificable:** el precio que él mismo cita ($15.750-16.000-15.900 según el vídeo) es consistente con el suelo real (~$15.500-16.000, nov-2022) y la fecha (9 y 14-nov-2022) encaja con la ventana del colapso de FTX. La consistencia entre 4 vídeos distintos a lo largo de 3 años es un indicio de que probablemente ocurrió algo así, pero **no es prueba** — no hay ningún vídeo de 2022 en el corpus donde se pueda leer la recomendación en tiempo real.

---

## 2. Cronología de avisos de venta/rotación 2023-2025

**Matiz importante encontrado en el propio corpus:** LMEC declara repetidamente una política explícita de **no vender BTC nunca** ("Bitcoin... no pretendo venderlo en este ciclo" [20250523]; "con Bitcoin mi estrategia es la de siempre. Nunca vendo y solo acumulo" [20251114]). Sus avisos de "rotar/vender/tomar beneficios" se aplican a **altcoins y al % de cartera en stablecoin**, no a BTC en sí. Esto es clave para leer la cronología: no hay ningún punto en el corpus donde diga "vended vuestro BTC".

### Cronología encontrada (con precio de BTC citado en el propio vídeo)

| Fecha | BTC citado en el vídeo | Qué dice | Archivo |
|---|---|---|---|
| **14-jul-2023** | ~$30.000 (citado explícitamente) | **Primera llamada operativa confirmada en tiempo real**: "Tenemos que ir tomando beneficios parciales y es lo que vengo haciendo en los últimos dos o tres meses" — dice llevar 2-3 meses haciéndolo (implicaría abr/may-2023), pero esa acción previa **no está confirmada** en los vídeos de mayo/junio 2023 disponibles (se grepeó [20230512] y [20230526]: ninguno menciona precio de BTC ni toma de beneficios) | `20230714-victoria-aplastante-de-las-criptomonedas-y-xrp-adi-s-matic-bnb-en-prob.md` |
| 12-sep-2023 | $25.000 (citado) | Es señal de **COMPRA**, no de venta: "ahora mismo que hemos corregido y que tenemos a bitcoin en los 25.000 [...] estoy volviendo a comprar sin miedo" | `20230912-cu-ndo-empezar-el-mercado-alcista-de-bitcoin-y-criptomonedas.md` |
| 19-abr-2024 | ~$63-64k (halving reciente) | **No es señal de venta**, es un marco a futuro: "no digo que ahora no tengas que tomar beneficios" — predice ventana de toma de beneficios recién a partir de ene-2025 hasta oct-2025, con techo estimado en $116k | `20240419-halving-de-bitcoin-no-est-s-preparado-mi-plan-para-los-pr-ximos-2-a-os.md` |
| **6-dic-2024** | justo por encima de $100.000 | **Segunda llamada operativa confirmada**: "hacer una toma parcial de beneficios a modo de cobertura inteligente [...] puede ir desde un 10 hasta un 30% del total de nuestras inversiones" (explícitamente NO vender todo) | `20241206-informaci-n-de-oro-sobre-bitcoin-y-criptomonedas-es-muy-urgente.md` |
| **23-may-2025** | $110.000-112.000 (ATH recién roto) | **La señal más completa y explícita del corpus** — plan de venta escalonado por tramos de precio de BTC: 12% en $?1?0.000 (ilegible en transcript, primer tramo), 10% en $133.100, tramos en $146.8k, $161.6k y 4% final en $165.000. Total 40% adicional a vender + 40% ya en estable + 20% que se mantiene siempre. **Excluye explícitamente BTC** del plan de venta ("con Bitcoin voy a largo plazo, no pretendo venderlo en este ciclo") — el plan vende altcoins usando el precio de BTC como referencia/reloj | `20250523-vende-todo-antes-de-que-bitcoin-toque-este-precio.md` |
| 12-sep-2025 | $115.000-116.000 | Reafirma el plan de mayo; reporta ventas parciales de BNB en $700/$800/$900 y de Hype en $20/$30/$35+ | `20250912-puedes-ganar-mucho-con-estas-inversiones-y-airdrops-de-criptomonedas.md` |
| 16-oct-2025 | tras el crash del viernes 10-oct-2025 (riesgo de perder los $100k) | Confirma que no ha vendido ni comprado nada extra desde el plan; sigue sin vender BTC ("no venderé llegue al precio que llegue") | `20251016-el-aviso-m-s-importante-para-todo-inversor-cripto.md` |
| 14-nov-2025 | BTC ya había perdido los $100.000 | Reporta que su cartera ya está al **65% en stablecoins / 35% invertido** (el plan de may-2025 se ejecutó); reitera "con Bitcoin... nunca vendo y solo acumulo" | `20251114-la-cripto-jugada-que-salvar-a-tu-dinero.md` |

### Conclusión de la cronología

- No hay ninguna llamada de venta de BTC entre nov-2022 y jul-2023 en el corpus (el mercado seguía plano/bajista).
- La **primera** llamada operativa real de "tomar beneficios" es **14-jul-2023, BTC ~$30.000** — bastante temprano en el ciclo (BTC subiría después hasta ~$126k, oct-2025), y de hecho el propio LMEC vuelve a comprar en sep-2023 a $25.000, así que no fue una salida definitiva sino toma de beneficios parcial + reentradas.
- La señal más **estructurada y pública** ("VENDE TODO...") llega muy tarde en el ciclo: **23-may-2025, BTC $110-112k**, a solo ~5 meses del techo real (~$126k, oct-2025) — es decir, bastante cerca del techo, aunque el plan es de venta escalonada (tramos hasta $165k) y no de salida total inmediata.
- En ningún momento del corpus recomienda vender el propio BTC; su venta/rotación es siempre altcoins → stablecoin, usando el precio de BTC como reloj/referencia del ciclo.

---

## 3. Resumen de los vídeos de 2022 disponibles (mar-ago)

### [20220330] "Tres oportunidades en Terra" (30-mar-2022)
**Tesis:** yield farming en el ecosistema Terra (LUNA/UST) — pools nuevas en Lunc Markets pagando 90-155% APY, estrategia de interés compuesto en Astroport (LUNA-UST, ASTRO-UST, XDEFI-UST). **Precio BTC:** no se menciona. **Nota irónica:** Terra/LUNA colapsaría por completo 6 semanas después (may-2022); el vídeo no lo anticipa en absoluto.

### [20220405] "Siguen siendo rentables estas inversiones" (5-abr-2022)
**Tesis:** actualización de estrategias DeFi multi-cadena — subastas de parachain de Polkadot (GLMR, ASTR, ACA), yield farming en Polygon (Balancer, Aave, Beefy), Moonbeam, Celo (Mobius, Immortal DAO) y Near/Aurora (Trisolaris). **Precio BTC:** no se menciona en ningún momento. Sin llamada sobre BTC.

### [20220819] "Clase completa... Cosmos" (19-ago-2022)
**Tesis:** estrategia de staking + farming en el ecosistema Cosmos (ATOM, JUNO, OSMO) vía Osmosis/Junoswap/Crescent. Menciona explícitamente que "hoy mismo estamos viviendo una corrección bastante fuerte" y que es buen momento para acumular — pero es una observación genérica sobre la corrección de esa semana (BTC rondaba los $21-24k, bajando desde ~$24k), **no sobre el suelo del ciclo**. Cita DOT a ~$75 como "buen precio". **No hay mención de precio de BTC** ni llamada específica a comprarlo. Es el último vídeo disponible antes del hueco sep-2022→ene-2023 que cubre el colapso de FTX y el suelo real.

**Conclusión de la sección 3:** los tres vídeos de 2022 disponibles son puramente tácticos/DeFi (yield farming, subastas, staking), sin ningún análisis de precio de BTC ni llamada de compra/venta sobre BTC. La ventana crítica (suelo real, nov-2022) simplemente no está cubierta por ningún archivo del corpus.

---

## Notas de rigor

- Todas las citas incluyen el archivo fuente exacto entre backticks.
- Se marcó explícitamente como "no verificable" o "retrospectivo" cualquier afirmación sobre 2022 que proviniera de un vídeo de 2023+ y no del propio vídeo de 2022.
- Se comprobó negativamente (grep sin resultado) que los vídeos de mayo/jun-2023 disponibles no contienen las menciones de precio de BTC ni de toma de beneficios que un vídeo posterior (sep-2023) les atribuye retrospectivamente.
