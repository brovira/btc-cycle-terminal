# Glassnode · The Week On-Chain — material del agente

Fuente: **The Week On-Chain**, newsletter semanal de Glassnode Research.
https://research.glassnode.com/tag/newsletter/

El agente `glassnode_woc` lee **solo** los informes de `reports/` y responde citándolos.

## Estructura
- `reports/*.md` — una edición semanal por archivo, nombrada `AAAAMMDD-titulo.md`.

## Cómo se actualiza (y qué hacer cuando Glassnode bloquea)

**Vía automática (la normal).** El repo privado archiva el artículo y de ahí sale el informe
de este agente:

1. `DeFi-Tracker · research/glassnode-kb/run.py` archiva el artículo (workflow
   `glassnode-weekly`, jueves 13:00 UTC) y `semanal.py` emite la recomendación de LP.
2. `btc-cycle-terminal · ingesta/sync_woc_reports.py` (workflow `sync-woc`, jueves 14:00 UTC)
   destila los que falten a `reports/`, y `ingesta/sync_woc.py` lleva la recomendación a
   `data/woc_semana.json`, que es lo que muestra el panel.

Si el pipeline privado deja la recomendación en `PENDIENTE` (no hay `ANTHROPIC_API_KEY`),
`sync_woc.py` la rellena con la suscripción (`claude -p`) y lo declara en `fuentes`.

**Cuando Cloudflare bloquea (pasó el 2-sep-2026: 403 a los dos sitios y al lector de
respaldo).** El archivador sale en ROJO en vez de decir "no hay artículo nuevo" —una lista
vacía es ceguera, no ausencia—. La vía manual, en el repo privado:

```bash
# 1. pega el texto del artículo en un fichero y mételo al KB
python research/glassnode-kb/ingerir_manual.py articulo.txt \
    --url https://insights.glassnode.com/<slug>/ --titulo "Título" --fecha AAAA-MM-DD
# 2. recomendación de LP + evaluación de la semana previa (no toca la web)
python research/glassnode-kb/semanal.py --articulo research/glassnode-kb/articulos/<fichero>.md
```

Después, en el repo público, lanza el workflow `sync-woc`: destila el informe a `reports/`
y actualiza el panel. El pase de lecturas diarias lo recoge en la sección Decisiones.

**Qué entra aquí.** No solo el Week On-Chain: cualquier artículo de Glassnode posterior al
informe más reciente de `reports/` (un especial sobre rangos de BTC, un Market Pulse). La
recomendación semanal de LP sigue saliendo solo del Week On-Chain.

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
