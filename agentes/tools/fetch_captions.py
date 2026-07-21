#!/usr/bin/env python3
"""
fetch_captions.py — descarga los subtítulos (captions) de vídeos de YouTube
y los guarda como .md en la carpeta del agente correspondiente.

Uso:
  python agentes/tools/fetch_captions.py --persona cowen --lang es <URL> [<URL> ...]

<URL> puede ser un vídeo, una playlist o un canal (yt-dlp los expande).

Requisitos:
  pip install yt-dlp        (única dependencia; hace el trabajo pesado)

Qué hace:
  - Baja los subtítulos (primero los "de verdad", si no los auto-generados) en el
    idioma pedido, SIN descargar el vídeo.
  - Limpia el VTT (quita timestamps, etiquetas y las líneas repetidas típicas de
    los auto-subs) y lo deja como texto corrido.
  - Escribe agentes/<persona>/yt-transcripts/<fecha>-<slug>.md con cabecera que
    marca la FUENTE = vídeo (auto-generado ⇒ puede tener erratas).
  - No sobreescribe si el archivo ya existe (idempotente); usa --force para rehacer.

El agente (.claude/agents/<persona>.md) ya cubre esa carpeta: grepea y cita.

Nota: los auto-subs son speech-to-text, tienen erratas y muletillas. Por eso se
marcan como fuente "vídeo". Un pase posterior de LLM puede limpiarlos si quieres.
"""
import argparse, json, os, re, subprocess, sys, tempfile, glob

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
# Llamamos a yt-dlp como MÓDULO del mismo Python que ejecuta este script,
# así funciona aunque el binario 'yt-dlp' no esté en el PATH.
YTDLP = [sys.executable, "-m", "yt_dlp"]

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)

def check_ytdlp():
    if run(YTDLP + ["--version"]).returncode != 0:
        sys.exit("ERROR: yt-dlp no está instalado para este Python. Instálalo con:  python3 -m pip install yt-dlp")

def slug(s):
    s = re.sub(r"[^A-Za-z0-9]+", "-", s or "").strip("-").lower()
    return (s or "video")[:70]

def list_videos(url, limit=0):
    """Expande vídeo/playlist/canal a una lista de {id,title,url,date}."""
    cmd = YTDLP + ["-J", "--flat-playlist", "--ignore-errors"]
    if limit:
        cmd += ["--playlist-end", str(limit)]
    r = run(cmd + [url])
    if r.returncode != 0 and not r.stdout.strip():
        print(f"  ! no pude leer {url}: {r.stderr.strip()[:200]}"); return []
    try:
        data = json.loads(r.stdout)
    except Exception:
        return []
    entries = data.get("entries")
    if entries is None and limit:
        pass
    if entries is None:  # es un vídeo suelto
        vid = data.get("id");
        return [{"id": vid, "title": data.get("title"), "url": data.get("webpage_url") or url,
                 "date": data.get("upload_date")}]
    out = []
    for e in entries:
        if not e: continue
        vid = e.get("id")
        out.append({"id": vid, "title": e.get("title"),
                    "url": e.get("url") or f"https://www.youtube.com/watch?v={vid}",
                    "date": e.get("upload_date")})
    return out

def clean_vtt(path):
    """VTT/SRT -> texto corrido, sin timestamps, etiquetas ni líneas repetidas."""
    txt = open(path, encoding="utf-8", errors="ignore").read()
    lines = []
    for ln in txt.splitlines():
        ln = ln.strip()
        if not ln or ln == "WEBVTT" or ln.startswith(("Kind:", "Language:", "NOTE")):
            continue
        if "-->" in ln:            # línea de tiempos
            continue
        if re.fullmatch(r"\d+", ln):  # número de cue (SRT)
            continue
        ln = re.sub(r"<[^>]+>", "", ln)                 # etiquetas <...>
        ln = re.sub(r"\[[^\]]*\]", "", ln).strip()      # [Música], [Aplausos]
        ln = re.sub(r"&nbsp;?", " ", ln)
        if ln:
            lines.append(ln)
    # dedup: los auto-subs repiten la línea anterior en cada cue
    out = []
    for ln in lines:
        if not out or out[-1] != ln:
            out.append(ln)
    # une en párrafos legibles
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip()

def fetch_one(v, persona, lang, force):
    outdir = os.path.join(REPO, "agentes", persona, "yt-transcripts")
    os.makedirs(outdir, exist_ok=True)
    date = (v.get("date") or "")[:8] or "0000"
    name = f"{date}-{slug(v.get('title') or v['id'])}.md"
    out = os.path.join(outdir, name)
    if os.path.exists(out) and not force:
        print(f"  = ya existe, salto: {name}"); return False
    with tempfile.TemporaryDirectory() as td:
        cmd = YTDLP + ["--skip-download", "--write-subs", "--write-auto-subs",
               "--sub-langs", f"{lang}.*,{lang}", "--sub-format", "vtt/srv3/best",
               "--convert-subs", "vtt", "-o", os.path.join(td, "%(id)s.%(ext)s"),
               "--ignore-errors", v["url"]]
        run(cmd)
        vtts = sorted(glob.glob(os.path.join(td, "*.vtt")))
        if not vtts:
            print(f"  ! sin subtítulos ({lang}) para: {v.get('title') or v['id']}"); return False
        text = clean_vtt(vtts[0])
    if not text:
        print(f"  ! subtítulo vacío: {v.get('title') or v['id']}"); return False
    header = (
        f"# {v.get('title') or v['id']}\n\n"
        f"**Fuente (VÍDEO):** {persona} · YouTube — {v['url']}\n"
        f"**Publicado:** {date} · **Subtítulos:** {lang} (pueden ser auto-generados)\n"
        f"**Tipo:** transcript de vídeo (speech-to-text; posibles erratas/muletillas). "
        f"Cita como `[yt-transcripts/{name}]`.\n\n---\n\n"
    )
    open(out, "w", encoding="utf-8").write(header + text + "\n")
    print(f"  ✓ {name}  ({len(text)} chars)")
    return True

def main():
    ap = argparse.ArgumentParser(description="YouTube captions -> .md por vídeo")
    ap.add_argument("--persona", required=True, help="carpeta destino: agentes/<persona>/yt-transcripts/")
    ap.add_argument("--lang", default="es", help="idioma de subtítulos (por defecto es)")
    ap.add_argument("--force", action="store_true", help="rehacer aunque ya exista")
    ap.add_argument("--max", type=int, default=0, help="limitar a los N vídeos más recientes por URL (0 = todos)")
    ap.add_argument("urls", nargs="+", help="vídeo(s), playlist(s) o canal(es)")
    a = ap.parse_args()
    check_ytdlp()
    total = 0
    for url in a.urls:
        vids = list_videos(url, a.max)
        print(f"{url} → {len(vids)} vídeo(s)")
        for v in (vids[:a.max] if a.max else vids):
            if fetch_one(v, a.persona, a.lang, a.force):
                total += 1
    print(f"\nListo. {total} transcript(s) nuevos en agentes/{a.persona}/yt-transcripts/")

if __name__ == "__main__":
    main()
