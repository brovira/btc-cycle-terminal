# Glassnode · The Week On-Chain — material del agente

Fuente: **The Week On-Chain**, newsletter semanal de Glassnode Research.
https://research.glassnode.com/tag/newsletter/

El agente `glassnode_woc` lee **solo** los informes de `reports/` y responde citándolos.

## Estructura
- `reports/*.md` — una edición semanal por archivo, nombrada `AAAAMMDD-titulo.md`.

## Cómo actualizarlo CADA SEMANA

Glassnode Research está **protegido con Cloudflare**, así que no se puede bajar de
forma automática (ni yo desde el entorno ni un script). El flujo manual (2 min):

1. Abre la edición de la semana en https://research.glassnode.com/tag/newsletter/
   (te llega también por email si estás suscrito a Glassnode).
2. Copia el texto del artículo (o guarda la página) y pégalo en un archivo nuevo:
   `agentes/glassnode_woc/reports/AAAAMMDD-the-week-onchain.md`
   - La fecha (`AAAAMMDD`) = fecha de publicación. Pon un título corto arriba.
3. `git add -A && git commit -m "glassnode_woc: week on-chain AAAA-MM-DD" && git push`

Con eso el agente ya cubre esa edición. Pregúntale "¿cuál es la lectura on-chain de
esta semana?" y responderá con la de fecha más alta, citando el archivo.

> **Nota:** si en algún momento **contratas la API de Glassnode**, podemos además
> alimentar los dashboards con sus métricas reales (MVRV, SOPR, STH/LTH, supply in
> profit…) vía un backend con la key como secret (`api/glassnode.js`, mismo patrón
> que Coinglass/Coin Metrics). El newsletter (análisis escrito) y la API (datos)
> son cosas distintas: este agente es el **newsletter**; los dashboards usarían la **API**.

## Ejemplo de cabecera para cada informe
```
# The Week On-Chain — 2026-07-15 (Week 29)

**Fuente:** Glassnode Research · The Week On-Chain · https://research.glassnode.com/...
**Publicado:** 2026-07-15

---

(pega aquí el texto del informe)
```
