# LMEC — material del agente

Canal: **La Mejor Estrategia Criptomonedas** (@LaMejorEstrategiaCriptomonedas) — https://www.youtube.com/@LaMejorEstrategiaCriptomonedas/videos
Enfoque: **ciclos de Bitcoin** (indicador *Bitcoin Halving Cycle Profit*), BMSB, RSI/MACD/MVRV Z semanales, DCA con órdenes límite escalonadas y **psicología de inversión**.

## Estructura
- **`yt-transcripts/*.md`** — transcripts de sus vídeos (fuente **HABLADA**, speech-to-text). Es lo que lee el agente `lmec`.
- `audit_2022_bottom_2025_top.md`, `track_record.md` — auditorías destiladas del corpus (cuándo compró/vendió, con fecha+precio).

## Cómo poblar / actualizar los transcripts

```
python3 -m pip install -U yt-dlp
python3 agentes/tools/fetch_captions.py --persona lmec --lang es --since 20210101 "https://www.youtube.com/@LaMejorEstrategiaCriptomonedas/videos"
```

- `--lang es` (canal en español). `--since 20210101` = ciclo completo desde 2021 (su psicología y el origen de su plan).
- Idempotente: no reescribe lo ya bajado (usa `--force` para rehacer). `--max N` limita a los N más recientes.
- **Automático:** workflows `ingest-transcripts.yml` (diario, vídeos nuevos) y `backfill-transcripts.yml` (manual, histórico completo). Corren en GitHub Actions (allí sí hay salida a YouTube).

El agente vive en `.claude/agents/lmec.md` y solo responde con este material, citándolo como `[agentes/lmec/yt-transcripts/<archivo>.md]`.
