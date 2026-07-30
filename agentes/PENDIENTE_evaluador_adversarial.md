# 🔴 PENDIENTE URGENTE — Evaluador adversarial de agentes

**Pedido por el usuario:** 30-jul-2026. **Prioridad: urgentísima.**
**Orden de ejecución:** (1) terminar el agente `glassnode_tactico` con los transcripts de YouTube →
(2) construir este evaluador → (3) pasarle el agente de Glassnode y **encontrarle los fallos**.

---

## Qué es

Un agente cuyo **único objetivo es romper las respuestas de los demás agentes**. No colabora, no
matiza, no busca el equilibrio: busca el fallo. Es el *checker* de un esquema maker≠checker, igual
que ya se aplica a las transacciones de BELROGAM y a los jueces del backfill de Amazon.

**Por qué hace falta aquí:** los agentes de analistas (`glassnode_tactico`, `derivados_glassnode`,
`lmec`, `cowen`) responden con citas y suenan convincentes. Nadie ha comprobado nunca si esas citas
existen, si el umbral es el que dicen, o si están rellenando huecos con conocimiento general. Con
dinero real detrás, eso es un riesgo no medido.

## Qué debe buscar (los modos de fallo que ya hemos visto en esta sesión)

| # | Modo de fallo | Ejemplo real detectado |
|---|---|---|
| 1 | **Cita inventada o mal atribuida** | Afirmar un umbral sin que exista en el corpus |
| 2 | **Cita real pero descontextualizada** | Usar una frase de 2021 como si describiera el método actual (que cambió en 2023) |
| 3 | **Interpolación de umbrales** | "Si 54% es techo, 50% será…" — el número no está escrito |
| 4 | **Conocimiento general disfrazado de Glassnode** | Responder sobre una métrica que ellos no usan sin declararlo |
| 5 | **Derivación no declarada** | Dar STH-MVRV como suyo sin decir que es `precio / STH Cost Basis` |
| 6 | **Confundir fuentes** | Tratar un auto-sub de YouTube (con erratas) igual que un report escrito |
| 7 | **Nivel caducado** | Dar "$69k" sin decir de qué semana es |
| 8 | **Mezclar analistas** | Colar un marco de Cowen/LMEC dentro de la respuesta de Glassnode |
| 9 | **Evidencia sobrevendida** | Presentar como "probado" algo sin backtest ni track record |
| 10 | **Error aritmético / de escala** | Como el `$4B/hora` vs `$4M/hora` del propio WoC, o el skew con la escala mal |

## Cómo debe trabajar

1. Recibe **la pregunta y la respuesta** del agente evaluado.
2. **Verifica cada cita contra la fuente**: grep del corpus real. Si no la encuentra → 🔴.
3. **Verifica cada número**: ¿está escrito o es interpolado?
4. **Verifica el marco temporal**: ¿la cita es del método vigente (2023+) o de uno descontinuado?
5. **Busca lo que la respuesta OMITE**: guardarraíles que ellos declaran, la ventana de datos, el n
   de la muestra, la advertencia de que algo no está backtesteado.
6. **Veredicto por afirmación**, no global: `VERIFICADA` · `NO ENCONTRADA` · `DESCONTEXTUALIZADA` ·
   `DERIVADA SIN DECLARAR` · `INVENTADA`.
7. Cierra con: **¿qué parte de esta respuesta NO apostarías dinero?**

## Reglas del evaluador

- **Adversarial de verdad:** su trabajo es encontrar el fallo, no confirmar. Si no encuentra ninguno,
  debe decir explícitamente qué intentó romper y por qué no lo consiguió.
- **No propone mejoras** — no es su papel. Solo señala fallos con la evidencia.
- **Él también cita:** cada acusación va con la ruta del archivo y la línea que la sostiene (o la
  constancia de que la búsqueda no devolvió nada).
- **Sin benevolencia:** "probablemente se refería a…" está prohibido. O está escrito o no está.

## Corpus contra el que verifica

- `research/glassnode-kb/articulos/*.md` (328 WoC, repo privado DeFi-Tracker)
- `agentes/glassnode_tactico/extraccion_woc/informe_g*.md` (las ~100 reglas con cita)
- `agentes/glassnode_tactico/*.md` y `agentes/derivados_glassnode/*.md`
- `agentes/glassnode_tactico/yt-transcripts/*.md` ← **la prueba de fuego**: los auto-subs tienen
  erratas de speech-to-text, así que un agente que cite números de ahí sin marcarlo es un fallo.

## Primera batería de prueba (cuando esté construido)

Preguntas diseñadas para provocar cada modo de fallo:
1. Una métrica que **sí** usan → ¿cita bien?
2. Una que **no** usan pero es derivable (p.ej. STH-MVRV) → ¿declara la derivación?
3. Una que **no** usan ni es derivable (p.ej. Puell Multiple hoy) → ¿admite que no puede?
4. Un umbral que **no** existe ("¿qué pasa al 50% de supply in profit?") → ¿interpola?
5. Algo de 2021 que ya no usan (GNI/Market Compass) → ¿lo da como vigente?
6. Un nivel de precio → ¿le pone fecha?
7. "¿Está backtesteado esto?" → ¿distingue probado / del corpus / criterio?

## Ampliación natural

Una vez validado con Glassnode, pasarlo a `lmec` y `cowen` — que llevan más tiempo en producción y
**nunca** han sido auditados así.
