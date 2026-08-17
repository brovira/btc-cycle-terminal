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

> **Última actualización:** 17-ago-2026, al final de la sesión que arregló toda la ingesta.

---

## 0. Antes de tocar nada

```bash
cd ~/dev/btc-cycle-terminal && git pull --rebase origin main && python3 ingesta/frescura.py
```

`frescura.py` es el juez: mira **fechas de datos**, no procesos. Si sale verde, el material
está al día. Si sale rojo, dice qué fuente y desde cuándo.

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

### 3.2 · Cuadrar el registro de posiciones (repo privado)

Dos huecos en `DeFi-Tracker/data/`:

- **ProjectX no cuadra.** `journal.json` dice que el 21-jul se retiró la posición de rango más
  alto (techo ~$74K), pero en `lp_positions.json` la única marcada `cerrada` es `6moFSGpH`, y la
  de rango hasta 74.001 (ProjectX, HyperEVM) sigue como `abierta`.
- **La posición de HYPE se cerró y no está registrada** en ningún sitio.

Ninguna de las dos está en el pipeline de Orca, así que **no se van a reconstruir solas**. Sin
esto no se pueden clasificar esas operaciones — y no se puede puntuar lo que no se puede
reconstruir.

### 3.3 · Conectar las hojas de decisión con el terminal

`sops/psicologia_trading.md` define cuatro tipos de operación y `sops/hojas_psicologia.html` son
las hojas imprimibles. Falta que el terminal los cuente solo. Añadir a cada entrada de
`journal.json`:

```json
"tipo": null,              // 1-4, se rellena cuando hay resultado
"estado_interno": ""       // salida de la hoja 1: cuerpo, emoción, las 3 preguntas
```

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
