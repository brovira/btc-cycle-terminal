# Glassnode · DERIVADOS y OPCIONES — material del agente `derivados_glassnode`

Reverse-engineering del framework con que Glassnode lee la sección off-chain/derivatives
(la última antes de conclusiones en su Week On-Chain).

## Estructura
- `framework.md` — el MARCO destilado (métricas + interpretación + cómo concluyen) **+ §E PLAYBOOK LP** (cuándo farmear/ensanchar/SALIR antes de un movimiento grande). La base del agente.
- `reports/track_record.md` — **scorecard**: sus llamadas forward vs lo que pasó, 2020→jul-2026, con tasa de acierto por tipo de llamada.
- `reports/AAAAMMDD-titulo.md` — datos/lecturas fechadas (tweets, secciones de derivados).

## Objetivo
Codificar su método de derivados para: (1) leer posicionamiento en vivo con nuestro cockpit
(que ya calcula skew/put-call/IV/funding/OI gratis), (2) **fijar rangos de LP y salir antes de los
movimientos grandes** (framework.md §E), y (3) **evaluar su track record** (`reports/track_record.md`).

## Cómo se construyó (jul-2026)
Barrido de las **152 Week On-Chain con contenido de derivados** del corpus (`research/glassnode-kb/`
en DeFi-Tracker, 328 artículos 2020→22-jul-2026): 5 agentes extrajeron por artículo las métricas+valores,
la lectura de posicionamiento y la llamada forward → síntesis en `framework.md` + `track_record.md`.
**Hallazgo clave:** su punto fuerte es leer **leverage apiñado** (flush/squeeze, 8/10 aciertos); su punto
débil es **cronometrar la vol** ("IV baja → expansión" acierta pero llega prematura y sin dirección). El
disparador de salida de LP debe ser la **confluencia** leverage extremo + on-chain en nivel clave, no un
aviso aislado de vol barata.

## Copyright
Solo resúmenes/datos/framework propio (transformativo). Nada de reproducir reportes verbatim en público.
