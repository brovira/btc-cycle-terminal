# Glassnode · DERIVADOS y OPCIONES — material del agente `derivados_glassnode`

Reverse-engineering del framework con que Glassnode lee la sección off-chain/derivatives
(la última antes de conclusiones en su Week On-Chain).

## Estructura
- `framework.md` — el MARCO destilado (métricas + interpretación + cómo concluyen). La base del agente.
- `reports/*.md` — datos/lecturas fechadas (tweets, secciones de derivados), `AAAAMMDD-titulo.md`.

## Objetivo
Codificar su método de derivados para: (1) leer posicionamiento en vivo con nuestro cockpit
(que ya calcula skew/put-call/IV/funding/OI gratis), y (2) **evaluar su track record** — marcar
sus llamadas vs lo que pasó (scorecard). Para el track record completo hace falta el corpus de
artículos (la KB de 1000, en local) — subirla al privado y alimentar `reports/`.

## Copyright
Solo resúmenes/datos/framework propio (transformativo). Nada de reproducir reportes verbatim en público.
