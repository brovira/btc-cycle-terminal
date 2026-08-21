# Traspaso a una sesión LOCAL de Claude Code

**Cómo usar este documento:** abre la Terminal, ve al repo y arranca Claude Code:

```bash
cd ~/dev/btc-cycle-terminal
claude
```

Y dile: *«Lee `sops/sesion_local.md` y sigue desde ahí»*.

**Para qué existe:** las sesiones de Claude Code en la web no tienen acceso a esta máquina.
Hay tareas que **solo se pueden hacer aquí** —YouTube bloquea las IPs de los runners de GitHub,
launchd vive en este Mac, y algunas wallets no están en ningún pipeline—. Este documento es la
lista de esas tareas con sus comandos exactos.

> **Última actualización:** 18-ago-2026, tras cuadrar el registro de posiciones con la cadena.

---

## 0. Antes de tocar nada

```bash
cd ~/dev/btc-cycle-terminal && git pull --rebase origin main && python3 ingesta/frescura.py
```

`frescura.py` es el juez: mira **fechas de datos**, no procesos. Si sale verde, el material
está al día. Si sale rojo, dice qué fuente y desde cuándo.

Desde el 18-ago también vigila **el registro propio**: cuántas decisiones de capital de este
ciclo tienen su porqué escrito. Va en el mismo sitio a propósito — el material de terceros y
el diario fallan igual de callados, y el diario es el único dato que no se puede volver a
bajar de ninguna parte. Detalle con `python3 ingesta/decisiones.py`.

**Ojo con los clones.** Hay tres copias del repo en este Mac:

| Ruta | Estado |
|---|---|
| `~/dev/btc-cycle-terminal` | ✅ **La buena.** Usa esta siempre |
| `~/btc-cycle-terminal` | ⚠️ vieja, ignorar |
| `~/Desktop/btc-cycle-terminal` | ⚠️ vieja, ignorar |

---

## 1. Contexto imprescindible

Terminal personal de inversión en BTC. Agrega el método de varios analistas (Glassnode,
Cowen, LMEC), guarda sus llamadas como **tests puntuables**, y gestiona capital real.

**El repo es PÚBLICO.** Nunca commitear cifras reales de cartera ni del negocio. Los números
privados viven en `brovira/DeFi-Tracker`. Del material de terceros van **resúmenes propios**,
nunca el texto íntegro.

### La lección de agosto de 2026 — léela antes de escribir cualquier ingesta

Durante cuatro semanas los cinco agentes respondieron con material caducado **mientras todos
los workflows salían en verde**. Se encontraron cinco variantes del mismo fallo:

1. `fetch_captions.py` devolvía `[]` en silencio cuando yt-dlp fallaba → «0 vídeos», indistinguible de un día tranquilo
2. `checkonchain.yml` no tenía cron: no fallaba, es que nadie lo llamaba
3. `sync-woc.yml` llevaba 3 ejecuciones fallando por un `GH_TOKEN` vacío
4. `pip install --upgrade yt-dlp` decía «already satisfied» sobre una versión de 10 meses (Python 3.9 de Xcode)
5. Un `\bbasis\b` en el clasificador hacía match dentro de «Cost Basis» y colgaba la nota equivocada

Ninguno salía en rojo. **Todos decían «bien» sin que nadie mirara el resultado.**

> **Regla para cualquier código nuevo de ingesta:** distinguir siempre *«no hay nada nuevo»*
> de *«no pude leer la fuente»*, y verificar **el resultado**, no que el proceso terminara con 0.

---

## 2. Estado de las automatizaciones

| Qué | Dónde corre | Estado |
|---|---|---|
| Transcripts YouTube (Cowen, LMEC) | **Este Mac**, launchd 8:30 | ✅ |
| Informes WoC → agente | GitHub Actions, jueves | ✅ |
| Resumen WoC → dashboard | GitHub Actions, jueves | ✅ |
| checkonchain | GitHub Actions, diario 7:30 UTC | ✅ |
| On-chain (BGeometrics) | GitHub Actions, diario 7:00 UTC | ✅ |
| **Vigilante de frescura** | GitHub Actions, diario 20:00 UTC | ✅ |

Los tres secrets del repo: `GH_TOKEN`, `CLAUDE_CODE_OAUTH_TOKEN`, `BGAPI_TOKEN`.

**Por qué los transcripts corren aquí y no en Actions:** YouTube bloquea las IPs de datacenter
con *«Sign in to confirm you're not a bot»*. Verificado el 17-ago en ambos canales. Desde una
IP doméstica funciona. Por eso `ingest-transcripts.yml` se quedó **sin cron**, solo manual.

---

## 3. Tareas pendientes

### 3.1 · Verificar que launchd funciona de verdad ⏳ *(era el paso en curso)*

Se cargó y se disparó a mano, pero faltó confirmar que llegó al final.

```bash
tail -20 ~/dev/btc-cycle-terminal/.local/ingesta.log
launchctl list | grep btc-ingesta
```

Se busca `─── fin OK ───`. La segunda columna de `launchctl list` es el código de la última
salida: **0 es bueno**, otra cosa hay que investigarla en `.local/launchd.err.log`.

Si nunca llegó a ejecutarse, lo más probable es un problema de entorno: launchd arranca con un
`PATH` mucho más pelado que la terminal. El script ya localiza yt-dlp por rutas absolutas
(`~/.local/bin/yt-dlp`), así que ese caso está cubierto, pero conviene mirarlo ahí.

### 3.2 · Cuadrar el registro de posiciones (repo privado) — ✅ *hecho el 18-ago, salvo HyperEVM*

Todo lo de **Orca** ya cuadra con la cadena (`data/normalized/orca_positions.json` + `orca_pnl.json`).
Lo que se arregló:

- `7dr1M3W9` y `6BtNv8qo` seguían como `abierta`: la cadena dice que se **cerraron el 3-ago-2026**.
  Ya están marcadas, con cifras, y con entrada en el `journal.json`.
- `CNuoBMmr` estaba anotada como **cbBTC/USDC** y es **cbBTC/WBTC** — un par de *peg* entre dos
  wrappers de BTC (rango 1,0008–1,0033). No es «acumular BTC en la bajada»: es delta 100% BTC de
  principio a fin. La nota vieja describía una posición que no existe.
- **La sospecha sobre ProjectX era mía y era falsa.** La retirada del 21-jul del journal es
  `6moFSGpH` (Orca, techo $74.850), no la de ProjectX (techo $74.001). Que las dos tuvieran un
  techo cerca de $74K era coincidencia. El journal siempre estuvo bien.

Sigue abierto solo lo de **HyperEVM**, y por una razón de fondo: *no hay lector de HyperEVM*.
`data/raw/` solo tiene `solana/`. Así que:

- **ProjectX (UBTC/USD0)** — marcada `abierta-SIN-VERIFICAR`. Sin fecha, sin fees, sin PnL.
- **HYPE** — marcada `cerrada-SIN-REGISTRAR`. No aparece en `normalized/`, ni en
  `manual_assets.json`, ni en el journal: solo consta de palabra.

O se meten a mano con capturas del explorador, o se escribe un lector de HyperEVM. **Lo que no se
puede reconstruir no se puede puntuar**, así que hasta entonces esas dos no entran en el recuento
del ciclo.

### 3.2b · Llegar al 10 de 10 — ⏳ *lo único que hace falta de ti*

La métrica que gobierna el resto: **% de decisiones de capital con su porqué escrito ANTES de
conocer el resultado.** No es PnL — todavía no hay muestra para que el PnL signifique nada.

Estado a 18-ago: **cobertura 7/10 · en plazo 0/10.**

Son dos números distintos y conviene no confundirlos:

| | Qué mide | Cómo sube |
|---|---|---|
| **Cobertura** | ¿existe la entrada? | reconstruyendo, hoy mismo |
| **En plazo** | ¿se escribió sin saber el resultado? | solo hacia adelante, decisión a decisión |

Las 4 aperturas de Orca se reconstruyeron el 18-ago y **están marcadas como tales**: suben la
cobertura y NO el «en plazo», a propósito. Si una reconstrucción contase, el número mediría
memoria en vez de disciplina.

**Lo que falta para cerrar la cobertura (necesita al usuario, no se puede sacar de la cadena):**
las 3 decisiones de HyperEVM — abrir ProjectX, abrir HYPE, cerrar HYPE. Hacen falta fecha y,
si se puede, importe. Con capturas del explorador vale.

**Cómo funciona el candado:** `api/journal.js` sella cada entrada con `registrado` (hora del
servidor, que el formulario **no** puede enviar). El diario de `lp.html` avisa al guardar algo
de hace más de un día y lo marca como reconstruida. Sin ese sello la métrica mediría intención.

### 3.3 · Conectar las hojas de decisión con el terminal — ✅ *hecho el 18-ago*

Los campos `tipo` (1-4) y `estado_interno` ya están en cada entrada de `journal.json`, en el
formulario de `lp.html` y en el whitelist de `api/journal.js`. El diario ahora enseña arriba una
línea de **disciplina**: qué % de las operativas con resultado siguieron el plan (tipo 1 + tipo 2),
con el contador de tipo 4 destacado en ámbar.

`tipo` se deja en `null` al abrir a propósito: solo se puede clasificar cuando hay resultado, y
obligar a ponerlo antes invita a inventárselo.

Los cuatro tipos, en corto:

|  | Siguió el plan | Fuera de plan |
|---|---|---|
| **Ganó** | Tipo 1 | **Tipo 4** ← el peligroso |
| **Perdió** | Tipo 2 *(el plan funcionando)* | Tipo 3 |

El tipo 2 **no es un error**: comprar un tramo de DCA y ver caer el precio es el plan haciendo
su trabajo. Confundirlo con tipo 3 es la vía rápida a abandonar un plan que estaba bien.

### 3.4 · Pendientes de más calado

- **Backtests Tier 1** de `agentes/glassnode_tactico/backtest_repertorio.md`. Están
  especificados y con datos disponibles; ninguno se ha corrido. Empezar por N1 (STH cost basis
  como techo en bear / suelo en bull). Ventana de 4 años: un ciclo, sirve para validar la
  mecánica, no para generalizar.
- **Evaluador adversarial**: `agentes/PENDIENTE_evaluador_adversarial.md`. Pedido el 30-jul,
  nunca construido. Es el checker que verificaría si las citas de los agentes existen de verdad.
- **Alertas de LP**: el semáforo de `agentes/derivados_glassnode/framework.md §E` (funding >8% +
  OI en máximos + skew girando, o VRP a negativo) está destilado pero no salta solo. `alerts/`
  hoy solo mira señales de ciclo.

---

## 3.5 · El punto ciego del monitor — arreglado el 21-ago

`frescura.py` daba **VERDE** el 21-ago con LMEC en rojo de verdad: sus transcripts tenían 21
días y el límite eran 25. Pero LMEC **sí había publicado** — lo que había fallado era la
ingesta local (Mac apagado, o launchd sin disparar).

**El fallo de fondo no era el número.** Un límite de cadencia no puede distinguir *«no ha
publicado»* de *«no lo hemos leído»*: las dos cosas se ven igual desde fuera, un archivo con
fecha vieja. Es la lección de agosto repetida un piso más arriba — el vigilante tenía su propio
punto ciego.

**La solución:** `ingesta_local.sh` escribe ahora `ingesta/local/estado.json` en cada
ejecución (fecha, canales ilegibles, máquina) y lo commitea **incluso cuando no hay transcripts
nuevos** — sobre todo entonces. `frescura.py` lo lee: si el latido tiene más de 2 días, sale
rojo aunque las fechas de los datos parezcan aceptables.

De paso el límite de LMEC baja de 25 a 20 días (su cadencia real es de 12 a 22), pero eso es
secundario: **el que tiene que cazar los fallos es el latido, no el umbral.**

## 4. Comandos útiles

```bash
# Ingesta de transcripts a mano (normal: últimos 10 días)
./ingesta/local/ingesta_local.sh

# Recuperar un hueco concreto
./ingesta/local/ingesta_local.sh 20260721

# ¿Está todo al día?
python3 ingesta/frescura.py

# ¿El clasificador de fiabilidad sigue bien?
python3 ingesta/test_fiabilidad.py

# Qué informes del WoC faltan (sin llamar al modelo)
python3 ingesta/sync_woc_reports.py --listar
```

**Antes de tocar el `PATH` o instalar nada:** `python3` en este Mac es el **3.9 de Xcode**.
yt-dlp ya no publica para 3.9, así que **no uses `pip install yt-dlp`** — usa el binario
autónomo de `~/.local/bin/yt-dlp`, que se actualiza con `yt-dlp -U`.

---

## 5. Los agentes

En `.claude/agents/`. Responden **solo** con su material y citan archivo + sección:

| Agente | Para qué |
|---|---|
| `glassnode_woc` | Semanal táctico. 4 informes seguidos (22-jul → 12-ago) |
| `glassnode_tactico` | Escalera de cost basis, rangos de LP, dirección |
| `derivados_glassnode` | IV, skew, funding, OI, semáforo de LP |
| `glassnode_strategy` | Mensual/trimestral, flujos institucionales |
| `cowen` | Ciclo, risk metric, calendario del suelo |
| `lmec` | Plan de DCA, BMSB, farming |

**Al pedirles algo, exige siempre la fecha del material.** Un dato caducado se siente igual de
convincente que uno fresco — es exactamente lo que pasó el 16-ago.

---

## 6. Foto del mercado al cerrar la sesión (17-ago-2026)

Caduca rápido. Para lo vigente: `python3 ingesta/frescura.py` y preguntar a los agentes.

```
BTC ~$64.400 · bear confirmado, mes 10 de ~12 según Cowen

TECHO   LMEC · BMSB                $68.000–69.000
        Checkonchain · 200 DMA     $69.133
        Glassnode · STH cost basis $66.963   (ellos citan $68.700 — otra fuente)
SUELO   Cowen · ya comprando       <$60.000
        LMEC · orden límite        $55.000
        Glassnode · realized price $52.646
```

Cuatro marcos independientes sitúan el suelo del ciclo en **oct-nov 2026**. Los tres coinciden
también en que la volatilidad está comprimida (RV 1 semana ~12,6%) y va a expandirse — pero ese
tipo de llamada es el que peor timing tiene en el track record (1/4).

**Relevante para el LP:** el usuario es vendedor de volatilidad (LP concentrado = corto de
gamma). El WoC del 12-ago recomienda **ensanchar el rango y reducir tamaño**, con el suelo por
debajo de $58,5K en vez de en el estante de $62K.

**Estado real del LP a 18-ago: no hay ninguna posición de Orca abierta.** Las tres se cerraron
(21-jul y 3-ago) y las tres batieron a HOLD. Queda `CNuoBMmr`, que no es una LP direccional sino
un par de *peg* cbBTC/WBTC, y las dos de HyperEVM sin verificar.

---

## 7. Reglas de trabajo

1. **Un paso cada vez.** El usuario lo ha pedido explícitamente: un comando, esperar el
   resultado, y entonces el siguiente. No encadenar cinco pasos en un mensaje.
2. **Nunca `git push` sin `git pull --rebase` antes.** Hay bots commiteando a `main` a diario;
   pasó dos veces el 17-ago.
3. **Verificar el resultado, no el proceso.** Ver el archivo escrito, no que el comando saliera 0.
4. **Repo público.** Cero cifras personales o del negocio.
5. **Si algo falla, leer el mensaje completo antes de proponer solución.** El 17-ago se dio por
   supuesto que un push fallido era de autenticación y era un `fetch first`. Se perdió tiempo
   mandando al usuario a crear un token que no hacía falta.
