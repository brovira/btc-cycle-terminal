# Auditoría de framework — Cowen, LMEC y Glassnode

**Qué es:** lo que cada analista dijo, **con fecha, cifra y cita**, desde junio de 2025 hasta hoy.
No es un resumen de sus opiniones: es el material para **puntuarles**.

**Por qué existe.** Un resumen de lo que piensa un analista no sirve para decidir capital, porque
no se puede fallar. Lo que sirve es *«el 17-nov-2025 dijo que el suelo estaría en 40K y dejó de
mencionarlo doce días después»*. Sin fecha y sin cifra, un analista nunca se equivoca.

## Qué se registra

Solo afirmaciones **auditables**: las que llevan un **número** (nivel, umbral, %, plazo) o una
**condición falsable** («si X entonces Y»). Lo demás se descarta.

Y por encima de todo, **los cambios**: el mismo indicador con otro umbral, un objetivo que se
abandona sin post-mortem, una regla que se reinterpreta cuando falla, un indicador que deja de
aparecer. Un cambio silencioso vale más que diez observaciones, porque es lo que un resumen
normal nunca enseña.

## Cómo se hizo

1. `agentes/tools/extraer_senales.py` lee **todos los caracteres de todos los documentos** y
   conserva las frases con número + indicador o acción, con contexto. Reducción: 6,3M → 1,33M
   caracteres (21%), quitando saludos, publicidad y despedidas.
2. Los pasajes se reparten en **14 ventanas cronológicas**, una por agente, para que cada uno
   pueda ver la evolución dentro de su tramo.
3. Cada ventana produce un `.md` con registros, cambios detectados y notas.

## Corpus

| Analista | Documentos | Periodo |
|---|---|---|
| Cowen | 271 transcripts | jun-2025 → 21-ago-2026 |
| LMEC | 37 transcripts | jun-2025 → 20-ago-2026 |
| Glassnode WoC | 62 artículos | jun-2025 → 19-ago-2026 |

## Las 14 ventanas

| Analista | Ventana | Fichero |
|---|---|---|
| Cowen | jun → sep 2025 | `cowen_2025-06_a_2025-09.md` |
| Cowen | sep → nov 2025 | `cowen_2025-09_a_2025-11.md` |
| Cowen | nov → dic 2025 | `cowen_2025-11_a_2025-12.md` |
| Cowen | dic 2025 → feb 2026 | `cowen_2025-12_a_2026-02.md` |
| Cowen | feb → mar 2026 | `cowen_2026-02_a_2026-03.md` |
| Cowen | mar → may 2026 | `cowen_2026-03_a_2026-05.md` |
| Cowen | may → jul 2026 | `cowen_2026-05_a_2026-07.md` |
| Cowen | jul → ago 2026 | `cowen_2026-07_a_2026-08.md` |
| LMEC | jun 2025 → ene 2026 | `lmec_2025-06_a_2026-01.md` |
| LMEC | feb → ago 2026 | `lmec_2026-02_a_2026-08.md` |
| Glassnode WoC | jun → sep 2025 | `woc_2025-06_a_2025-09.md` |
| Glassnode WoC | sep 2025 → ene 2026 | `woc_2025-09_a_2026-01.md` |
| Glassnode WoC | feb → may 2026 | `woc_2026-02_a_2026-05.md` |
| Glassnode WoC | **may → ago 2026** | `woc_2026-05_a_2026-08.md` ← **ventana vigente** |

## El hallazgo transversal

> **Los niveles casi nunca se mueven. Lo que se mueve siempre es el plazo — y no se anuncia.**

Cada uno tiene su forma de no equivocarse nunca:

- **Cowen** mantiene sus cifras durante años (risk metric 0,25 · 66% de drawdown · 10T$ · 300K)
  mientras **las fechas rotan**. Su escudo: predecir las dos salidas y el desdoblamiento del
  1-jul-2026 — *«pivoting my view and buying are two different things»*.
- **Glassnode** mantiene el diagnóstico y **mueve los niveles**. El objetivo de +2σ pasó de ~130K
  a 141,6K a 144K mientras el ciclo hacía techo en **126K**. El soporte «más probable» se ha
  reescrito a la baja **seis veces** en el último trimestre, sin marcar ninguno como fallo. Su
  escudo: escenarios simétricos sin probabilidad asignada.
- **LMEC** simplemente **falla sus objetivos y llama al plan «intacto»**. Prometió 80% en estables
  para nov-dic y se quedó en 65%. El precio de entrada de HYPE subió **+115%** en seis revisiones.
  Su escudo: declarar los objetivos numéricos de venta *«un error tremendo»* el mismo día en que
  se alcanzaba el suyo.

**Qué se salva de cada uno.** Cowen: los niveles y la disciplina de la risk metric. Glassnode: el
STH Cost Basis y el Realized Price como anclas — las únicas dos cifras que publican todas las
semanas. LMEC: los cuatro niveles escalonados de BTC (70/65/60/55), que no ha movido desde febrero.

**Qué no se puede usar de ninguno:** su calendario.

## Salvedades

- **Cowen y LMEC son subtítulos automáticos.** Hay erratas de dictado, sobre todo en los números
  (LMEC: «80.000» por «180.000»). Las cifras dudosas van marcadas con `?` y con la cita literal.
- **El WoC es texto escrito**, así que sus cifras son fiables.
- El prefiltro **decide qué merece leerse, no qué significa**. Si una afirmación importante no
  lleva número ni condición, no entra — y eso es deliberado.
