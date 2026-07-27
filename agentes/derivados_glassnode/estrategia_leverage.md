# Estrategia mecánica de LEVERAGE APIÑADO (flush / squeeze) — reverse-engineering de la señal 8/10 de Glassnode

**Qué es:** destilación de **la señal más fiable** del framework de derivados de Glassnode —
"leverage apiñado → flush/squeeze" (8/10 HIT) + "backwardation/funding extremo → squeeze" (3/3 HIT)—
a una **estrategia mecánica replicable con datos GRATIS** (Deribit, Bybit/OKX, Binance) para gobernar el LP
(corto de gamma/vol): cuándo **salir/ponerse defensivo** y cuándo **re-entrar a farmear**.

**Fuentes:** `reports/track_record.md`, `framework.md` y los **artículos originales** del WoC
(`research/glassnode-kb/articulos/`). **Todas las cifras salen de los artículos reales** — no hay estimaciones inventadas.
Cuando el corpus no da un número exacto, se dice explícitamente.

> **Regla maestra del corpus (framework §E):** lo que precede los movimientos grandes **NO es "IV baja"**, es la
> **CONFLUENCIA de leverage extremo + posicionamiento estirado + on-chain en un nivel clave**. La señal aislada de
> "vol barata" llega semanas/meses antes (todo el verano-2025). Solo se dispara con la confluencia.

---

## A) Tabla de las llamadas ganadoras (lecturas EXACTAS en el momento de la llamada)

### A.1 — Flush a la BAJA (longs apiñados → cascada)

| Fecha WoC | Precio / contexto | Funding | Open Interest | 25d Skew | Put/Call · Opciones | IV / VRP | Leverage ratio · Liquidaciones | Desenlace |
|---|---|---|---|---|---|---|---|---|
| **2021-09-06** (aviso) | ~$50k, HODL fuerte | **BTC +0,03%** (≈ nivel pre-caída de mayo); ETH +0,02% | **En/cerca de ATH** BTC y ETH; ETH perp OI **$7,8B (ATH)** | n/d | n/d | n/d | — | **13-sep: flush** $52,8k→$44,2k, **−$10k en 1h**; long-liq dominance **68%** (tras un breve 80% short-liq que empujó el pico) |
| **2024-03-12** ("Euphoria Zone") | **ATH $72k**, price discovery | **+35% a +45% anualizado** (demanda de leverage largo) | Elevado (no da cifra) | n/d | n/d | — | SOPR on-chain **+27%** | Corrección a **$53–55k** (may–jul) |
| **2025-08-20** ("hallmarks fase madura") | **ATH $124,4k**, inflows cayendo | Positivo (no da cifra; ver 10-08) | **BTC $67B** elevado; **alt OI ATH $60,2B → −$2,6B** (10ª mayor caída); −$2,3B BTC OI | n/d | n/d | — | Liq **shorts $74M / longs $99M** (bajas = cierres **voluntarios**, aún no forzados). OI dom BTC 56,7 / ETH 43,3 | Puente al techo (crowded-long) |
| **2025-10-08** (techo, ~2 días antes) | **ATH ~$126k**, ETF inflows **>$2,2B** | **>8% anualizado** (late longs) | **Nuevos máximos** (crecimiento rápido) | **1W: de ~+18 vol pts put-rich → +3** (swing de **21 pts en <1 semana**) = rotación defensivo→**call-heavy** | Call-heavy domina; dealers **long gamma** | 1W ATM IV **31,75%→36,01%**; term structure subiendo | — | **10-oct: mayor flush de la historia** |
| **2025-10-15** (el flush) | **$126,1k → mid-$110k**, pierde $117–114k | **Se hunde a niveles FTX-2022** (briefly muy negativo) | **−$19B (mayor de la historia)**, >$10B en un día | **1W −1,3% → +17% put-rich** (uno de los mayores repricings del año) | **Put/call volume 0,8 → 1,41 (pico 1,51)** | **1W IV 35% → 76%** (máx desde abr-25) | **Estimated Leverage Ratio colapsa a mínimos multi-mes** | Techo de ciclo confirmado |
| **2025-11-05** ("sin suelo aún") | ~$100k, hedging≠comprando | Directional premium **$338M/mes (abr) → $118M/mes** | Cayendo | Puts caras en strike **$100k** | Flujo put-dominante | **1W IV pico 54%** (−10 pts al formar soporte); **VRP 1M ligeramente + tras 10 días negativo** | — | Sigue a $89k y por debajo |
| **2025-11-19** (más caída) | <$90k intradía | **Cycle lows, neutral-a-negativo** (top-500) | **Cayendo** (under-levered) | **1W ≈ −14% (put-rich), 6M ≈ −5%** | Taker flow compra puts >> calls; **strike $90k** | **DVOL 40 (hace 3 sem) → ~50** (cerca de niveles del 10-oct) | — | Entra en deep-value 2026 |
| **2026-02-04** (VRP→neg, caída) | Retest **$73k** (antiguo ATH) | — | Forzado a la baja; leverage recontruido→**reset forzado** | **Downside skew empinándose** (más puts) | Flujo concentrado en protección; strike **$75k** | **1W IV ~70%** (+20 pts vs 2 sem antes); **VRP 1W: +23 (hace 1 mes) → −5** (1ª vez negativo desde dic) | **Mayor spike de long-liq de todo el drawdown** | Cae a mid-$70k / $60k |

### A.2 — Squeeze al ALZA (shorts apiñados → combustible)

| Fecha WoC | Precio / contexto | Funding | Open Interest | Opciones / basis | Liquidaciones · leverage | Desenlace |
|---|---|---|---|---|---|---|
| **2021-07-26** (short-squeeze) | $29,5k→$35–38k | **Negativo sostenido** (sesgo neto corto, incluso con precio **+30%**) | Perp **+$1,4B** en la semana (desde rango $10–12B) | Strikes anchos: **Put $25k OI 1.388 BTC · Call $80k OI 1.513 BTC** (vol esperada) | **$120M shorts liq en 1h**; crypto-margined dominance **70%→52,5%** (estructura más limpia) | Squeeze **+30%**; rally spot a $69k (oct) |
| **2022-12-12** (backwardation→squeeze) | ~$17k, post-FTX, muy quieto | Implícito negativo (backwardation) | **BTC leverage ratio 3,46%→2,50% del mcap**; ETH 4,75%→3,10% | **Backwardation: perp −2,5% · calendar −0,3% anualizado** (cubierto p/ más caída / cargado de shorts). RV 1w **22%** / 2w **28%** (mín. multi-año) | Leverage cayendo | **Short-squeeze de ene-2023** |
| **2023-01-30** (el squeeze) | Mejor mes desde oct-21 | Vuelve positivo | **OI −36%** (650k→414k BTC desde mid-nov); leverage ratio (OI/saldo exch) **40%→25%** | **Basis vuelve a positivo: perp +7,3% · calendar +3,3% anualizado** (contango sano) | **>$495M shorts liq (3 olas)**; **long-liq dominance 15% = 85% shorts** (> FTX 75%) | Rally confirmado |
| **2025-04-24** (setup short-squeeze) | $94,7k, reclaim STH-CB $92,9k | **−0,023%** (negativo pese a precio subiendo) | Perp **243k → 281k BTC (+15,6%)** desde mínimo de marzo | 7d MA de long-funding pagado **$88k/h y cayendo** (sesgo a corto) | — | Rally **$85k → ATH $111k** (may) |

> **Lectura clave:** en el **flush**, el OI está **en máximos** y el funding **muy positivo**; en el **squeeze**, el OI **sube pero el funding es negativo** (divergencia) o el basis está en **backwardation**. El **signo del funding/basis** es el que da la dirección — nunca los derivados solos.

---

## B) La FIRMA COMÚN

### B.1 — Firma de FLUSH a la baja (longs apiñados)
Presente en 2021-09, 2024-03, 2025-08→10, 2026-02:

1. **Funding fuertemente positivo y sostenido:** **≥ +8% anualizado** (10-oct-25) — en euforia **+35% a +45%** (mar-24), o "niveles pre-caída" (sep-21). Es demanda de leverage **largo**, no cobertura.
2. **Open Interest en máximos / ATH**, típicamente con **crecimiento rápido** justo antes (late longs entrando). El Estimated Leverage Ratio en zona alta (**≥2% del market cap** es el umbral que citan como riesgo).
3. **Skew rotando de defensivo (put-rich) a neutral/call-heavy.** El sello exacto: **1W de +18 → +3 vol pts en <1 semana** (swing de 21 pts, oct-25). "De hedging defensivo a posicionamiento oportunista." *Ojo:* es la **rotación**, no un skew put-rich alto (eso suele ser suelo).
4. **On-chain:** precio en/rechazando una **resistencia de cost-basis** (cluster $114–117k en oct-25) con demanda spot/ETF **cayendo**.
5. **Disparador de vol (confirmación):** **VRP girando a negativo** (IV<RV, feb-26: +23→−5) y/o **front-end IV spike + put/call volume >1,0**.

**Firma en una línea:** `funding ≥+8% ann sostenido + OI en top-decil/ATH + skew rotando put-rich→call-heavy` **→ techo/flush** (el trío que marcó el 10-oct-25 ~2 días antes).

### B.2 — Firma de SQUEEZE al alza (shorts apiñados)
Presente en 2021-07, 2022-12→2023-01, 2025-04:

1. **Funding negativo sostenido** (−0,017% a −0,023%) **o basis en backwardation** (perp −2,5% / calendar −0,3% anualizado). Sesgo corto neto = combustible.
2. **OI subiendo mientras el precio sube pero el funding es negativo** (divergencia OI↑ + funding<0, abr-25: +15,6% con funding −0,023%). O leverage ratio **reseteado/limpio** (post-flush).
3. **Estructura de opciones:** calls con OI **muy por encima del spot** (call $80k) y **put/call bajo**.
4. **Dominancia de liquidación de shorts alta** cuando dispara (**85%** ene-23 > FTX 75%; 80% breve sep-21).
5. **On-chain:** precio **recuperando un soporte clave** (STH cost basis $92,9k, abr-25) con demanda spot real.

**Firma en una línea:** `funding negativo sostenido (o backwardation) + OI subiendo + precio reclaim de soporte on-chain` **→ short-squeeze al alza**.

---

## C) ESTRATEGIA MECÁNICA REPLICABLE (datos gratis, server-side)

**Fuentes y cómputo (todo gratis):**
- **Bybit/OKX:** `funding` (8h) y `open_interest` de BTC perp; `long/short ratio`. Funding anualizado = `funding_8h × 3 × 365`.
- **Deribit:** `DVOL`; option chain → **25d skew** por tenor = `IV(put 25Δ) − IV(call 25Δ)`; **put/call** (OI y volumen); options OI.
- **Binance klines** (diario): **RV** realizada (close-to-close, anualizada): `RV30` (30d) y `RV7` (7d).
- **Derivados:** `VRP = DVOL(30d) − RV30`. `Leverage ratio proxy = OI_notional / market_cap_BTC` (umbral riesgo ≥2%).

**Ventanas / normalización:** funding y OI se evalúan en **media móvil de 3 días** (evita blips). OI se mide como **percentil sobre 180 días** (proxy de "máximos/limpio"). Skew: lectura **diaria** del tenor **1W (7d)** y **1M (30d)**.

### 🔴 TRIGGER DE SALIR / PONERSE DEFENSIVO (cerrar LP) — flush a la baja
Dispara si se cumple **`EXIT_CROWDED_LONG` O `EXIT_VOL_REALIZING`:**

**`EXIT_CROWDED_LONG`** (el trío del 10-oct) = **las 3**:
- `funding_ann_3d ≥ +8%` (Bybit/OKX), sostenido ≥ 3 días **Y**
- `OI_notional ≥ percentil 90 de 180d` **O** `OI a ≤5% de su máximo de 180d` **Y**
- `skew_1w` **rotó de ≥ +10 a ≤ +5 vol pts en ≤ 7 días** (Deribit) — defensivo→call-heavy

**`EXIT_VOL_REALIZING`** (el disparador del 4-feb) = **cualquiera**:
- `VRP = DVOL − RV30 < 0` durante ≥ 2 días (la vol se realiza, no se warehousea) **O**
- `skew_1w` salta a **> +15 vol pts** con `put/call_volume` subiendo de ~0,8 a **> 1,0** (front-end IV spike/estrés)

> Además, **refuerza** (no requerido, pero sube convicción) si el precio rechaza una resistencia de cost-basis on-chain y los ETF flows/spot CVD giran a negativo.

### 🟢 TRIGGER DE RE-ENTRAR / FARMEAR (abrir LP estrecho) — estructura limpia
Dispara solo si se cumplen **TODAS** (`REENTRY_CLEAN`):
- **OI reseteado:** hubo un flush (`OI cayó ≥ 15% en ≤ 3 días`) **Y** ahora `OI_notional ≤ percentil 40 de 180d`
- **Funding neutralizado:** `funding_ann_3d ≤ +11%` e idealmente `≤ 0` (post-flush)
- **VRP vuelve positivo:** `DVOL − RV30 ≥ +5` (te vuelven a pagar la prima)
- **Skew normalizado:** `skew_1w` entre **0 y +12 vol pts**, **sin** front-end spike
- **On-chain:** precio **por encima** de un soporte de cost-basis recuperado (no haciendo mínimos decrecientes)

### 🟩 (Opcional) BIAS LARGO / re-entrada agresiva — short-squeeze al alza
`funding_ann_3d < 0` sostenido ≥ 3–5 días **Y** `OI subiendo (+10% en 2–4 sem)` **Y** (`basis en backwardation` **O** call-OI construyéndose por encima del spot) **Y** precio recupera soporte on-chain. Es sesgo **direccional**, no solo LP.

| Indicador | Fuente gratis | Ventana | Umbral flush (salir) | Umbral squeeze/limpio (entrar) |
|---|---|---|---|---|
| Funding anualizado | Bybit/OKX | MM 3d | **≥ +8%** | ≤ 0 (squeeze) / ≤ +11% (limpio) |
| Open Interest | Bybit/OKX/Deribit | percentil 180d | **≥ p90** o ≤5% del máx | subiendo +10% con funding<0 (squeeze) / ≤ p40 tras flush (limpio) |
| 25d skew 1W | Deribit chain | diaria | **rotó +10→≤+5 en ≤7d** o spike **>+15** | 0 a +12, estable |
| VRP = DVOL − RV30 | Deribit + Binance | 2d | **< 0** | **≥ +5** |
| Put/Call volume | Deribit | diaria | spike **>1,0** (desde ~0,8) | bajo y estable |
| Basis perp/calendar | OKX/Deribit | — | — | **backwardation (<0)** = squeeze |
| Liq long-dominance | streams exch | evento | confirma flush | short-dominance alta = squeeze |

---

## D) Anti-falsos-positivos (guardas cruzadas con los FALLOS/prematuros)

| Patrón débil | Evidencia en el corpus | Guarda mecánica |
|---|---|---|
| **"IV/DVOL baja → expansión"** (acertó **1/4**, prematuro **meses**) | jun/jul/ago-25: ATM IV en mínimos multi-año → "expansión inminente"; la expansión llegó **el 10-oct** | **Vol baja NO es trigger de salida por sí sola.** Solo dispara con `EXIT_CROWDED_LONG` (funding+OI+skew). Un percentil bajo de DVOL a lo sumo justifica *ensanchar* rango, no cerrar. |
| **"Reset de funding → constructivo"** (falla cerca de **techos de ciclo**) | **2021-04-19**: funding a mínimo de ciclo **−0,017%** + long-liq récord **$1,847B** + OI ATH $27,4B → "constructivo"; era el **1er techo local** → crash **−50%** a $30k | **Funding reset ≠ re-entrada.** `REENTRY_CLEAN` exige **también** OI reseteado + VRP>0 + **precio sobre soporte on-chain y sin máximos decrecientes**. Si el reset ocurre tras un techo estructural, **no** re-entrar por funding solo. |
| **Skew put-rich extremo = "bajista"** | 10-oct-25 el skew 1W **flipeó a +17% justo en el mínimo** y revirtió | **No shortear/salir contra un skew put-rich alto:** suele ser suelo (mean-reverting). El trigger es la **rotación put-rich→call-heavy**, no el nivel put-rich. |
| **OI cayendo = "flush" (pero voluntario)** | 20-ago-25: unwind de −$2,3B con liq **bajas ($74M/$99M)** = cierres **voluntarios/risk-managed**, aún no el flush | Exigir **confluencia sostenida ≥3 días** y ≥2–3 indicadores. Un unwind de OI **sin** funding≥8% ni rotación de skew ni liq forzada = todavía no. |
| **Un solo print / ruido de datos** | blips de funding, `bb_record_id` inestable, etc. | Todo en **MM 3 días** y **percentiles**, nunca sobre un tick. |
| **VRP negativo como señal direccional** | feb-26 VRP<0 marcó tramo bajista, pero VRP<0 también aparece cerca de suelos de capitulación | Usar `VRP<0` para **"no farmear / fuera de LP"**, **no** para inferir dirección. |

---

## E) Límites honestos (por qué la regla captura solo parte del 8/10)

1. **El nivel ("DÓNDE") es on-chain, no derivados.** El verdadero edge de Glassnode es **cruzar** el posicionamiento con **STH cost basis, realized price, true market mean, URPD** ($92,9k reclaim, cluster $114–117k, $73k soporte). Con datos de derivados gratis tienes el **combustible y el momento**, pero **no el nivel**. Sin el overlay on-chain, la regla no distingue **techo local de techo de ciclo** — exactamente el modo de fallo del 19-abr-2021.
2. **Timing más ruidoso y temprano.** Su mejor llamada fue ~2 días antes; los umbrales mecánicos disparan antes y a veces chopean (las llamadas de "vol barata" prematuras por meses). Espera **salidas más tempranas y con más falsos amagos** que su juicio.
3. **Catalizadores macro/exógenos** que ellos nombran cualitativamente **no están en los datos**: yen-carry (5-ago-24), aranceles US-China (oct-25), FOMC. La regla ve la fragilidad, no la mecha.
4. **Demanda institucional / flujos.** ETF netflows ($2,2B in, −2,3k BTC), spot CVD, treasury demand son parte de sus lecturas y **no salen** de Deribit/Bybit/OKX/Binance.
5. **Juicios cualitativos parcialmente mecanizables:** "liquidación voluntaria vs forzada", **collateral mix** (stablecoin vs crypto-margined), **signo del dealer gamma** (long→amortigua / short→amplifica). Se aproximan, pero ellos los leen con criterio.
6. **El 8/10 incluye dirección que vino del on-chain, no de derivados.** La parte **mecanizable** es el diagnóstico de **fragilidad/posicionamiento** (~5–6/10 equivalente); la **confirmación direccional** que subió su acierto es la que exige el juicio y el cruce on-chain.

> **Conclusión operativa:** mecaniza el **semáforo de fragilidad** (funding+OI+skew+VRP) para gobernar el LP con disciplina;
> mantén el **cruce on-chain manual** para el nivel y para vetar el modo-fallo "reset de funding cerca de techo de ciclo".
