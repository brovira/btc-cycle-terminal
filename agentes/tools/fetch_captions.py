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
# YouTube bloquea el cliente "web" (SABR / "page needs to be reloaded", issue #12482).
# Forzamos clientes que sí funcionan para extraer + subtítulos.
CLIENT = ["--extractor-args", "youtube:player_client=web_safari,mweb,tv,android"]

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)

def check_ytdlp():
    if run(YTDLP + ["--version"]).returncode != 0:
        sys.exit("ERROR: yt-dlp no está instalado para este Python. Instálalo con:  python3 -m pip install yt-dlp")

def slug(s):
    s = re.sub(r"[^A-Za-z0-9]+", "-", s or "").strip("-").lower()
    return (s or "video")[:70]

class CanalIlegible(Exception):
    """No se pudo LEER el canal/playlist.

    Es un estado DISTINTO de "el canal no tiene vídeos nuevos", y confundirlos fue
    exactamente el bug que tuvo la ingesta parada 4 semanas en verde: la rama --dateafter
    se tragaba el error de yt-dlp, devolvía [] y el workflow imprimía "0 vídeo(s)" como si
    fuera un día tranquilo. Cowen publica casi a diario; 0 vídeos nunca fue creíble.
    """

def _err_tail(r, n=3):
    errln = [x for x in (r.stderr or "").splitlines() if x.strip()]
    return " | ".join(errln[-n:])[:400] if errln else "(yt-dlp no reportó nada en stderr)"

def _parse_filas(stdout):
    filas = []
    for ln in (stdout or "").splitlines():
        p = ln.strip().split("|||")
        if p and p[0].strip() and not p[0].startswith("{"):
            vid = p[0].strip()
            fecha = p[2].strip() if len(p) > 2 else ""
            filas.append({"id": vid, "title": (p[1] if len(p) > 1 else vid),
                          "url": f"https://www.youtube.com/watch?v={vid}",
                          "date": fecha if re.fullmatch(r"\d{8}", fecha) else ""})
    return filas

def list_videos(url, limit=0, since=None):
    """Expande vídeo/playlist/canal a una lista de {id,title,url,date}.

    Lanza CanalIlegible si no se pudo leer la URL. Devolver [] significa SIEMPRE
    "leído correctamente, cero vídeos que cumplan el filtro".
    """
    if since:  # filtra por fecha (más lento: extrae cada vídeo, pero respeta --dateafter)
        cmd = YTDLP + CLIENT + ["--dateafter", since, "--skip-download", "--ignore-errors",
                       "--print", "%(id)s|||%(title)s|||%(upload_date)s"]
        if limit:
            cmd += ["--playlist-end", str(limit)]
        r = run(cmd + [url])
        filas = _parse_filas(r.stdout)
        if not filas:
            if r.returncode != 0:
                raise CanalIlegible(_err_tail(r))
            # returncode 0 y 0 filas: probablemente legítimo, pero volcamos stderr igualmente
            # para que el log diga POR QUÉ y no haya que adivinarlo desde fuera.
            print(f"  · 0 vídeos tras --dateafter {since} → {_err_tail(r)}")
        return filas
    # OJO: --flat-playlist es rapido pero NO devuelve upload_date -> los archivos salian como
    # "0000-titulo.md". La fecha importa: el metodo de los analistas cambia con los anos y el agente
    # necesita saber si una cita es vigente o vieja. Por eso se pide el print con la fecha.
    cmd = YTDLP + CLIENT + ["--flat-playlist", "--ignore-errors", "--no-warnings",
                            "--print", "%(id)s|||%(title)s|||%(upload_date)s"]
    if limit:
        cmd += ["--playlist-end", str(limit)]
    r = run(cmd + [url])
    if r.returncode != 0 and not r.stdout.strip():
        raise CanalIlegible(_err_tail(r))
    filas = _parse_filas(r.stdout)
    if filas:
        return filas
    try:
        data = json.loads(r.stdout)
    except Exception:
        if r.returncode != 0:
            raise CanalIlegible(_err_tail(r))
        print(f"  · 0 vídeos legibles en {url} → {_err_tail(r)}")
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

def parse_json3(path):
    d = json.load(open(path, encoding="utf-8", errors="ignore"))
    out = []
    for ev in d.get("events", []):
        line = "".join(s.get("utf8", "") for s in (ev.get("segs") or [])).strip()
        if line and (not out or out[-1] != line):
            out.append(line)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip()

def parse_xmlsubs(path):
    raw = open(path, encoding="utf-8", errors="ignore").read()
    chunks = re.findall(r"<(?:text|p)\b[^>]*>(.*?)</(?:text|p)>", raw, re.S)
    out = []
    for c in chunks:
        c = re.sub(r"<[^>]+>", " ", c)
        for a, b in (("&amp;","&"),("&lt;","<"),("&gt;",">"),("&#39;","'"),("&quot;",'"'),("&nbsp;"," ")):
            c = c.replace(a, b)
        c = re.sub(r"\s+", " ", c).strip()
        if c and (not out or out[-1] != c):
            out.append(c)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip()

def parse_any(path):
    p = path.lower()
    if p.endswith((".json3", ".json")):
        try: return parse_json3(path)
        except Exception: return ""
    if p.endswith((".srv1", ".srv2", ".srv3", ".ttml", ".xml")):
        return parse_xmlsubs(path)
    return clean_vtt(path)

def fetch_one(v, persona, lang, force):
    outdir = os.path.join(REPO, "agentes", persona, "yt-transcripts")
    os.makedirs(outdir, exist_ok=True)
    date = (v.get("date") or "")[:8] or "0000"
    name = f"{date}-{slug(v.get('title') or v['id'])}.md"
    out = os.path.join(outdir, name)
    if os.path.exists(out) and not force:
        print(f"  = ya existe, salto: {name}"); return False
    with tempfile.TemporaryDirectory() as td:
        cmd = YTDLP + CLIENT + ["--skip-download", "--write-subs", "--write-auto-subs",
               "--sub-langs", f"{lang}.*,{lang}", "--sub-format", "vtt/json3/srv3/srv1/best",
               "-o", os.path.join(td, "%(id)s.%(ext)s"), "--ignore-errors", v["url"]]
        res = run(cmd)
        subs = []
        for ext in ("*.vtt", "*.srt", "*.json3", "*.srv3", "*.srv2", "*.srv1", "*.ttml", "*.xml"):
            subs += glob.glob(os.path.join(td, ext))
        subs = sorted(subs)
        if not subs:
            errln = [x for x in (res.stderr or "").splitlines() if x.strip()]
            tail = " | ".join(errln[-2:])[:300] if errln else "(yt-dlp no reportó error; ¿quizá no hay subs en ese idioma?)"
            print(f"  ! sin subtítulos ({lang}) para: {v.get('title') or v['id']}  →  {tail}")
            return False
        text = parse_any(subs[0])
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
    ap.add_argument("--since", default=None, help="solo vídeos desde esta fecha YYYYMMDD (p.ej. 20210101)")
    ap.add_argument("urls", nargs="+", help="vídeo(s), playlist(s) o canal(es)")
    a = ap.parse_args()
    check_ytdlp()
    total = 0
    ilegibles = []
    for url in a.urls:
        try:
            vids = list_videos(url, a.max, a.since)
        except CanalIlegible as e:
            print(f"  ! NO PUDE LEER {url} → {e}")
            ilegibles.append(url)
            continue
        print(f"{url} → {len(vids)} vídeo(s)")
        for v in (vids[:a.max] if a.max else vids):
            if fetch_one(v, a.persona, a.lang, a.force):
                total += 1
    print(f"\nListo. {total} transcript(s) nuevos en agentes/{a.persona}/yt-transcripts/")
    # Salir en rojo: un canal ilegible NO es "no hay vídeos nuevos". Si esto se traga,
    # la ingesta se para en silencio y los agentes responden con material caducado.
    if ilegibles:
        sys.exit(f"ERROR: {len(ilegibles)} canal(es) ilegibles: {', '.join(ilegibles)}")

if __name__ == "__main__":
    main()
