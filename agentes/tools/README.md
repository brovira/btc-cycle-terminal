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

## `extraer_senales.py` — prefiltro para auditar a los analistas

Auditar «letra a letra» todo lo que han dicho Cowen, LMEC y Glassnode desde jun-2025 son 397
documentos y ~6,3M de caracteres: unos 2M de tokens si se leen enteros. Y la mayor parte de un
transcript de YouTube es saludo, publicidad y despedida.

Este script **lee todos los caracteres de todos los documentos** —por eso sigue siendo letra a
letra— y conserva solo las frases que llevan **un número Y un término de indicador o de acción**,
con una frase de contexto a cada lado. Esa es la parte auditable: un umbral sin número no es
falsable, y un número sin indicador no dice nada.

Reducción medida el 21-ago-2026: **6,3M → 1,33M caracteres (21%)**. Por analista: Cowen 21%,
LMEC 9%, WoC 45% — el WoC conserva mucho más porque es texto escrito y denso, sin relleno.

```bash
python3 agentes/tools/extraer_senales.py \
  --carpeta agentes/cowen/yt-transcripts --desde 20250601 --salida /tmp/cowen.json
```

Sale un JSON `[{doc, pasajes[]}]` listo para repartir entre agentes por ventanas temporales.
**No sustituye al criterio**: decide qué merece leerse, no qué significa.
