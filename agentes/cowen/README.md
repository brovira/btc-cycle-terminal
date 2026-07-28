# Benjamin Cowen — material del agente

Canal: **Benjamin Cowen** (@benjaminjcowen) — https://www.youtube.com/@benjaminjcowen/videos — su canal propio. **Es el que usa la ingesta** (elección del usuario: es el que sigue).
Enfoque: risk metric, ciclos de Bitcoin, calendario electoral, DCA por riesgo.

## Estructura
- **`reports/`** — sus memos/reports ya extraídos a texto (fuente **ESCRITA**, precisa). Fuente principal, grepable.
- **`reports-pdf/`** — los PDFs originales (figuras/tablas).
- **`yt-transcripts/*.md`** — transcripts de sus vídeos (fuente **HABLADA**, speech-to-text), según se añadan.

## Cómo poblar / actualizar los transcripts

```
python3 -m pip install -U yt-dlp
python3 agentes/tools/fetch_captions.py --persona cowen --lang en --since 20210101 "https://www.youtube.com/@benjaminjcowen/videos"
```

- `--lang en` (canal en inglés). `--since 20210101` = ciclo completo desde 2021. **Ojo:** su canal tiene MUCHOS vídeos; usa `--max N` para acotar o deja que tarde.
- Idempotente (no reescribe; `--force` para rehacer). **Automático:** `ingest-transcripts.yml` (diario) y `backfill-transcripts.yml` (manual, histórico) en GitHub Actions.

Agente: `.claude/agents/cowen.md`. Cita como `[agentes/cowen/reports/<archivo>.md]` o `[agentes/cowen/yt-transcripts/<archivo>.md]`.
