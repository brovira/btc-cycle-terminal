# On Chain Mind — material del agente

Canal: **On Chain Mind** (@OnChainMind) — https://www.youtube.com/@OnChainMind/videos
Enfoque: **análisis on-chain** de Bitcoin (métricas de cadena, cohortes, flujos de exchange, señales de ciclo).

## Estructura
- `yt-transcripts/*.md` — transcripts de sus vídeos (fuente **HABLADA**, speech-to-text). Es lo que lee el agente `onchainmind`.

## Cómo poblar / actualizar los transcripts

Desde la raíz del repo, en tu Mac:

```
cd ~/btc-cycle-terminal
python3 -m pip install -U yt-dlp
python3 agentes/tools/fetch_captions.py --persona onchainmind --lang en --since 20210101 "https://www.youtube.com/@OnChainMind/videos"
```

- `--lang en` porque el canal es en inglés. Si algún vídeo no tiene subs en inglés, prueba también `--lang es`.
- `--since 20210101` = cobertura de ciclo completo (desde 2021).
- El script es **idempotente**: no reescribe lo ya bajado (usa `--force` para rehacer).
- Al terminar: `git add -A && git commit -m "onchainmind: transcripts" && git push`.

El agente vive en `.claude/agents/onchainmind.md` y solo responde con este material, citándolo.
