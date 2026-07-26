# Track record del framework de derivados de Glassnode — scorecard

**Qué es:** evaluación de las **llamadas forward** (predicciones/avisos) de la sección de derivados del
*Week On-Chain* frente a lo que **realmente pasó** después. Fuente = las 152 extracciones estructuradas
del corpus 2020→jul-2026 (`research/glassnode-kb/`, DeFi-Tracker) + el propio corpus como verdad
(cada semana describe lo ocurrido la anterior). **No se inventan precios**: cada resultado se ancla a lo
que dice el propio WoC posterior o a hitos de precio conocidos. Cita como `[reports/track_record.md]`.

**Escala:** ✅ HIT (se cumplió, buen timing) · 🟡 PARCIAL (idea correcta pero prematura/direccion equivocada) · ❌ MISS · ⏳ PENDIENTE (el corpus termina antes del desenlace).

---

## 1) Scorecard cronológico

| Fecha (WoC) | Señal / llamada forward | Métricas clave | Qué pasó después | Veredicto |
|---|---|---|---|---|
| 2021-04-19 | Reset de funding a −0,017% tras $1,847B de long-liq → "constructivo en las semanas siguientes" | funding cycle-low, long-liq récord | Era el **primer techo local** (~$64k abr). Rebote débil y **crash de mayo −50% a $30k** | ❌ MISS (falló cerca de techo de ciclo) |
| 2021-07-12 | Derivados comprimidos, "calma antes de la tormenta", próximo gran movimiento lo lleva el spot | OI −57% vs pico, options OI −67% | Suelo ~$29k fin-jul → **rally spot a $69k** oct | ✅ HIT (expansión + spot-driven, al alza) |
| 2021-07-26 | Funding negativo + strikes anchos → "vol esperada", short-squeeze | funding negativo, put $25k/call $80k OI | Squeeze +30% en 1h ya; tendencia al alza continuó | ✅ HIT |
| 2021-09-06 | Funding +0,03% + OI en máximos → "riesgo de cascada de long-liq" | funding pre-mayo levels, OI ATH | **Flush 2021-09-13**: $4B/30% del OI en 1h, $52,8k→$44k | ✅ HIT (en 1 semana) |
| 2021-10-18 | OI alto/volumen bajo + calls >$100k → "probabilidad elevada de cascada de liquidación", cautela | options OI +107% oct, call OI >> put OI | ATH $69k el 10-nov (subió ~15% más primero), luego **cascada de dic** | 🟡 PARCIAL (riesgo correcto, ~3 semanas pronto) |
| 2022-01-31 | "Posible short-squeeze contra-tendencia" a mínimos de 6 meses | put/call 59%, funding negativo, OI ~1,3% mcap | Squeeze parcial early-feb (rebote a ~$45k mar) dentro del bear | 🟡 PARCIAL (squeeze corto sí; bear siguió) |
| 2022-03-21 | IV y premiums históricamente bajos → "precede vol muy alta, casi siempre al alza" | IV baja, basis <3% | Vol **explotó** (LUNA may, −60% a $17k jun) pero **a la BAJA** | 🟡 PARCIAL (vol acertó, dirección al revés) |
| 2022-08-08 | ETH: backwardation → "sell-the-news" en el Merge | calls ETH + backwardation | Merge 2022-09: ETH $1.777→$1.288 | ✅ HIT |
| 2022-12-12 | Backwardation (−2,5%/−0,3%) → "cubierto para más caída / cargado de shorts" | leverage ratio cayendo, backwardation | **Short-squeeze de ene-2023** (85% dominancia short-liq) | ✅ HIT |
| 2023-06-19 → 08-07 | IV en mínimos de ciclo/históricos → "pricing vol históricamente baja por delante" | 1W IV 36%, put/call 0,42, skew ATL | **2023-08-21: sell-off −7,2%**, $2,5B OI, IV se dobló | ✅ HIT (expansión ~2-6 sem después) |
| 2023-08-21 | $2,5B de deleveraging (mayor desde LUNA) → "potencial de cambio de tendencia" | OI −24,5% en 1 día, skew −10%→+10% | Chop/bajada a $26k en sep, **breakout a $35k en oct** | 🟡 PARCIAL (cambio de tendencia llegó ~6-8 sem después) |
| 2024-03-12 | Funding 35-45% anualizado → "Euphoria Zone" (cautela) | funding pre-bull-2021, SOPR +27% | **ATH $73k 14-mar**, corrección a $53-55k may-jul | ✅ HIT (euforia cerca del techo local) |
| 2024-07-24 | Flush $53-55k = "candidato ideal a pivote de suelo de corrección" | long-liq pivot, funding <0,01% | Rebote, pero **otro flush el 5-ago** (yen-carry) a ~$49k | 🟡 PARCIAL (otro flush antes del suelo real) |
| 2024-08-07 | "Reset completo" de futuros → el spot llevará la recuperación | OI −11% en 1 día (−3σ), $365M liq | Recuperación → **breakout post-elección a $100k** nov | ✅ HIT |
| 2024-10-08 | OI residual grande → "vulnerable a cascadas si estalla la vol… en cualquier dirección" | $2,5B OI cerrado, OI aún alto | Vol de elección → **gran movimiento (al alza)** | ✅ HIT (expansión; ellos cubrieron dirección) |
| 2024-11-06 | Opciones pricing vol extrema bidireccional en la elección (VRP 27,9%) | put/call even, VRP top 1,4% días | BTC **+~40% en nov** (elección → $100k) | ✅ HIT (movimiento enorme realizado) |
| 2025-04-24 | OI +15,6% + funding −0,023% → "setup de short-squeeze si el momentum continúa" | OI 243k→281k BTC, funding negativo | **Rally de $85k a ATH $111k** (may) | ✅ HIT |
| 2025-05-15 | Reset sano, skew −6,1% risk-on → "base para uptrend más robusto" | OI −10% (short flush), funding neutral | Nuevos ATH may-ago | ✅ HIT |
| 2025-06-10 / 07-10 / 08-12 | Contrarian: "IV/DVOL en mínimos → precede expansión de vol" (repetido) | ATM IV multi-año, DVOL solo 2,6% días menor | La expansión llegó… el **10-oct** (meses después); verano fue grind | 🟡 PARCIAL (correcto pero **prematuro meses**) |
| 2025-08-20 → 10-08 | "Hallmarks de fase madura" → **crowded-long, fragilidad creciente**; "funding spikes preceden enfriamiento" | funding >8%, OI ATH de "late longs", calls apiñadas | **10-oct-2025: mayor liquidación de la historia** (>$19B OI), techo de ciclo | ✅ HIT (la mejor llamada; ~2 días antes) |
| 2025-11-05 | "Hedging, no comprando el dip → sin suelo todavía" | directional premium ↓, puts caras $100k | BTC siguió a $89k y por debajo | ✅ HIT |
| 2025-11-19 | DVOL subiendo → "mercado pricing movimientos mayores, preparándose para acción inestable" | IV cerca de niveles del 10-oct, DVOL ~50 | Más caída / entra en deep-value 2026 | ✅ HIT |
| 2026-02-04 | VRP a negativo → "los rallies de alivio son correctivos, no de cambio de tendencia; riesgo a la baja" | 1W IV→70%, VRP −5 | BTC cae a $60k y por debajo (feb-jun) | ✅ HIT |
| 2026-05 (W18-21) | Tesis de short-squeeze (funding neg sostenido, record short bias abr) | funding negativo récord, VRP+ | **$66k→$80k** en mayo | ✅ HIT (tramo) |
| 2026-06-10 | "Más profundo en capitulación" | 1W IV >60%, skew 1W ~30% | Bajó a $58k, rebotó poco después | 🟡 PARCIAL (fase correcta, suelo cerca) |
| 2026-07-01 | DVOL subiendo desde mínimos = "primeras etapas de un suelo, pero un último spike de vol no puede descartarse" | put/call 14d >1 máx del año, DVOL recuperando | 22-jul: ETF flows a positivo, reclaim de max pain $66k | ✅ HIT (suelo desarrollándose; el "último spike" queda como hedge abierto) |
| 2026-07-22 | Squeeze "hedges-off" → "retrace menos violento que uno de funding"; necesita reclaim de $69k; rechazo → vuelta a $63k | put/call mínimo del año, funding <neutral, spot > max pain | Corpus termina aquí (hoy 26-jul-2026) | ⏳ PENDIENTE |

---

## 2) Tasa de acierto por TIPO de llamada (lo importante para operar)

| Tipo de llamada | Muestra | ✅ | 🟡 | ❌ | Lectura |
|---|---|---|---|---|---|
| **Leverage apiñado → flush / squeeze** (posicionamiento) | 10 | 8 | 2 | 0 | **Su punto fuerte.** Buen acierto y buen timing (0–3 sem). Incluye el techo del 10-oct-25 y el short-squeeze de ene-23. |
| **Backwardation / funding extremo → squeeze direccional** | 3 | 3 | 0 | 0 | Muy fiable cuando el signo del funding/basis es claro. |
| **"IV/DVOL baja → expansión de vol"** (contrarian de vol) | 4 | 1 | 3 | 0 | **Punto débil.** Acaba llegando, pero **prematuro (semanas-meses) y ciego de dirección**. |
| **"Reset de funding → constructivo"** | 3 | 1 | 1 | 1 | Funciona en bull/mid-cycle; **falla cerca de techos de ciclo** (abr-21). |

**Conclusión operativa:** el framework es **fuerte en posicionamiento/leverage** (qué está apiñado y frágil) y
**débil como cronómetro de vol** (cuándo exactamente expande). Para el LP → **dispara la salida con la confluencia
de leverage extremo + on-chain en nivel clave**, NO con un aviso aislado de "vol barata". Ver `framework.md §E`.

## 3) Sesgos observados en su método
- **Prematuros en la compresión:** avisan de expansión de vol demasiado pronto (todo el verano-2025). El carry favorece al vendedor de vol mientras siguen avisando.
- **Direccionalmente honestos:** rara vez dan dirección desde derivados; cuando lo hacen es cruzando con on-chain, y ahí aciertan más.
- **Mejores en extremos:** las llamadas más certeras salen cuando el posicionamiento está en un extremo medible (funding >8%, skew >20%, record short bias), no en el "medio" del rango.
- **Sesgo constructivo tras flush:** tienden a leer los resets de leverage como constructivos; correcto en bull, peligroso en techos de ciclo.

## 4) Llamadas abiertas a seguir (actualizar al llegar el WoC nuevo)
- **2026-07-22 (⏳):** ¿el reclaim de max pain $66k + ETF flows positivos → despeja $69k (STH cost basis) y confirma cambio de régimen, o rechaza y vuelve a $63k? Es la bisagra actual. Seguimiento con el próximo WoC.
- **"Último spike de capitulación" (jul-26):** hedge que dejaron abierto — vigilar si aparece un spike de vol final antes del suelo durable.
