# tools — utilidades para alimentar a los agentes

## `fetch_captions.py` — captions de YouTube → `.md`
Descarga los subtítulos de vídeos/playlists/canales y los guarda como transcript
`.md` en `agentes/<persona>/yt-transcripts/` (fuente = vídeo).

```bash
pip install yt-dlp
# un vídeo, una playlist o un canal entero:
python agentes/tools/fetch_captions.py --persona lmec  --lang es "https://www.youtube.com/watch?v=XXXX"
python agentes/tools/fetch_captions.py --persona cowen --lang en "https://www.youtube.com/@IntoTheCryptoverse/videos"
```

- No sobreescribe lo ya bajado (idempotente); `--force` para rehacer.
- Los auto-subs son speech-to-text → se marcan como fuente vídeo (menos fiables que un report escrito).
- El agente correspondiente ya grepea y cita esa carpeta automáticamente.
