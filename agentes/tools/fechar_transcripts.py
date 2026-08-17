#!/usr/bin/env python3
"""Repara la FECHA de los transcripts bajados con `0000` en el nombre.

POR QUÉ HACE FALTA
------------------
`fetch_captions.py` lista los vídeos del canal en modo `--flat-playlist`, que es rápido pero **no
devuelve la fecha de publicación** → los archivos salen como `0000-titulo.md`.

Para el agente eso no es cosmético: el método de Glassnode **cambió** (lo que decían en 2021 —GNI,
Market Compass— está descontinuado; el marco vigente es de 2023 en adelante). Sin fecha, el agente
no puede cumplir su regla de "lo más reciente manda" ni avisar de que una cita es vieja.

QUÉ HACE
--------
Lee la URL del vídeo de la cabecera de cada `.md`, pregunta a YouTube **solo la fecha** (sin bajar
nada más), y luego: renombra el archivo a `AAAAMMDD-titulo.md` y corrige la línea "Publicado:".
No toca los que ya tienen fecha. Es idempotente: se puede cortar y volver a lanzar.

Uso (desde la raíz del repo):
  python3 agentes/tools/fechar_transcripts.py --persona glassnode_tactico
  python3 agentes/tools/fechar_transcripts.py --persona glassnode_tactico --dry-run   # solo mirar
"""
import argparse, os, re, subprocess, sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# Reutiliza la resolución de fetch_captions (binario autónomo antes que módulo de Python).
# Sin esto, en un Mac con el Python 3.9 de Xcode esto llamaría a un yt-dlp de hace meses:
# yt-dlp ya no publica para 3.9, así que pip se queda clavado en la última compatible y
# falla contra el antibot de YouTube con errores que parecen otra cosa.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch_captions import _localizar_ytdlp  # noqa: E402

YTDLP = _localizar_ytdlp()
CLIENT = ["--extractor-args", "youtube:player_client=web_safari,mweb,tv,android"]
LOTE = 40      # vídeos por llamada: una sola petición para muchos, mucho más rápido


def fechas_de(urls):
    """{id: AAAAMMDD} preguntando solo metadatos (sin descargar subtítulos ni vídeo)."""
    out = {}
    for i in range(0, len(urls), LOTE):
        trozo = urls[i:i + LOTE]
        cmd = YTDLP + CLIENT + ["--skip-download", "--ignore-errors", "--no-warnings",
                                "--print", "%(id)s|||%(upload_date)s"] + trozo
        r = subprocess.run(cmd, capture_output=True, text=True)
        for ln in (r.stdout or "").splitlines():
            p = ln.strip().split("|||")
            if len(p) == 2 and p[0] and re.fullmatch(r"\d{8}", p[1]):
                out[p[0]] = p[1]
        print(f"  {min(i+LOTE, len(urls))}/{len(urls)} consultados · {len(out)} fechas obtenidas")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--persona", required=True)
    ap.add_argument("--dry-run", action="store_true", help="enseñar qué haría, sin tocar nada")
    a = ap.parse_args()

    carpeta = os.path.join(REPO, "agentes", a.persona, "yt-transcripts")
    if not os.path.isdir(carpeta):
        sys.exit(f"No existe {carpeta}")

    pendientes = []          # (ruta, video_id)
    for nombre in sorted(os.listdir(carpeta)):
        if not nombre.endswith(".md") or not nombre.startswith("0000-"):
            continue
        ruta = os.path.join(carpeta, nombre)
        txt = open(ruta, encoding="utf-8", errors="replace").read(1500)
        m = re.search(r"youtube\.com/watch\?v=([\w-]+)", txt)
        if m:
            pendientes.append((ruta, m.group(1)))

    if not pendientes:
        print("Nada que reparar: no hay archivos con 0000.")
        return
    print(f"{len(pendientes)} transcripts sin fecha. Consultando YouTube (solo metadatos)…")

    mapa = fechas_de([f"https://www.youtube.com/watch?v={vid}" for _, vid in pendientes])

    ok = fallo = 0
    for ruta, vid in pendientes:
        fecha = mapa.get(vid)
        if not fecha:
            fallo += 1
            continue
        base = os.path.basename(ruta)
        nuevo = os.path.join(os.path.dirname(ruta), fecha + base[4:])   # 0000- → AAAAMMDD-
        if a.dry_run:
            print(f"  [dry] {base[:58]} → {os.path.basename(nuevo)[:58]}")
            ok += 1
            continue
        txt = open(ruta, encoding="utf-8", errors="replace").read()
        txt = txt.replace("**Publicado:** 0000", f"**Publicado:** {fecha}")
        txt = txt.replace(f"yt-transcripts/{base}", f"yt-transcripts/{os.path.basename(nuevo)}")
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(txt)
        os.replace(ruta, nuevo)
        ok += 1

    print(f"\n{'(simulación) ' if a.dry_run else ''}reparados: {ok} · sin fecha: {fallo}")
    if fallo:
        print("Los que fallaron pueden ser vídeos privados/borrados; se quedan como 0000 (inofensivo).")
    if not a.dry_run and ok:
        print("\nAhora súbelo:")
        print(f"  git add agentes/{a.persona}/yt-transcripts/")
        print('  git commit -m "transcripts: añadir fechas de publicación"')
        print("  git push origin main")


if __name__ == "__main__":
    main()
