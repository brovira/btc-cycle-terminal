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

## Transcripts de Glassnode (canal oficial)

Completa al agente `glassnode_tactico` con lo que dicen **en vídeo**, además de sus reports escritos.
Se ejecuta **en local** (YouTube bloquea las IPs de los runners de CI).

```bash
python3 -m pip install -U yt-dlp        # -U importante: YouTube rompe versiones viejas a menudo

# 1) prueba con 3 vídeos para confirmar que hay subtítulos disponibles
python agentes/tools/fetch_captions.py --persona glassnode_tactico --lang en --max 3 \
  "https://www.youtube.com/@glassnode/videos"

# 2) si funcionó, el histórico completo (tarda; es idempotente, se puede cortar y reanudar)
python agentes/tools/fetch_captions.py --persona glassnode_tactico --lang en \
  "https://www.youtube.com/@glassnode/videos"
```

Destino: `agentes/glassnode_tactico/yt-transcripts/<fecha>-<slug>.md`, con cabecera que marca
**FUENTE = vídeo** (auto-subs ⇒ erratas). El agente ya tiene esa carpeta en su material y sabe que
pesa menos que un report escrito.

Opciones útiles: `--since 20240101` (solo desde una fecha) · `--max N` · `--force` (rehacer).
Si YouTube da error de cliente, actualiza yt-dlp: es la causa habitual.
