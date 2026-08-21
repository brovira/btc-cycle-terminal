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

## Salvedades

- **Cowen y LMEC son subtítulos automáticos.** Hay erratas de dictado, sobre todo en los números
  (LMEC: «80.000» por «180.000»). Las cifras dudosas van marcadas con `?` y con la cita literal.
- **El WoC es texto escrito**, así que sus cifras son fiables.
- El prefiltro **decide qué merece leerse, no qué significa**. Si una afirmación importante no
  lleva número ni condición, no entra — y eso es deliberado.
