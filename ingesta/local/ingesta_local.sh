#!/usr/bin/env bash
#
# ingesta_local.sh — baja los transcripts de YouTube DESDE TU MÁQUINA y los sube al repo.
#
# POR QUÉ EXISTE
# --------------
# YouTube bloquea las IPs de datacenter de los runners de GitHub Actions:
#
#   ERROR: [youtube] Sign in to confirm you're not a bot.
#
# Desde una IP doméstica no pasa. Así que la ingesta de transcripts se mueve aquí y
# el workflow de Actions se queda solo como disparador manual de emergencia.
#
# QUÉ HACE
#   1. Sincroniza el repo (pull --rebase; aborta si hay cambios sin commitear).
#   2. Baja los transcripts nuevos de LMEC y Cowen.
#   3. Si hay algo nuevo, commitea y hace push.
#   4. Deja registro en .local/ingesta.log y avisa en el escritorio si falla.
#
# CLAVE DE DISEÑO: distingue "no hay vídeos nuevos" de "no pude leer el canal".
# Ese fue exactamente el bug que tuvo esto parado 4 semanas en verde. fetch_captions.py
# ya sale con código 1 si un canal es ilegible; aquí NO nos lo tragamos.
#
# USO
#   ./ingesta/local/ingesta_local.sh              # normal, últimos 10 días
#   ./ingesta/local/ingesta_local.sh 20260721     # recuperar desde una fecha concreta
#
# Instalación programada: ver ingesta/local/README.md

set -uo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
LOGDIR="$REPO/.local"
LOG="$LOGDIR/ingesta.log"
mkdir -p "$LOGDIR"

# Fecha desde la que buscar. Por defecto 10 días; se puede pasar YYYYMMDD como argumento
# para recuperar un hueco (p.ej. los vídeos del 21-jul al 7-ago que se perdieron).
if [ $# -ge 1 ]; then
  SINCE="$1"
elif date -v-10d +%Y%m%d >/dev/null 2>&1; then
  SINCE="$(date -v-10d +%Y%m%d)"            # BSD/macOS
else
  SINCE="$(date -u -d '10 days ago' +%Y%m%d)"  # GNU/Linux
fi

log(){ printf '%s  %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$*" | tee -a "$LOG"; }

# Aviso visible cuando algo falla. Sin esto volvemos al problema original: un fallo
# silencioso del que no te enteras hasta que preguntas a un agente semanas después.
avisar(){
  local msg="$1"
  if command -v osascript >/dev/null 2>&1; then
    osascript -e "display notification \"$msg\" with title \"Ingesta BTC terminal\"" 2>/dev/null || true
  elif command -v notify-send >/dev/null 2>&1; then
    notify-send "Ingesta BTC terminal" "$msg" 2>/dev/null || true
  fi
}

cd "$REPO" || { log "FATAL: no existe $REPO"; exit 1; }

log "─── inicio (desde $SINCE) ───"

# Nunca tocar un árbol sucio: si hay trabajo a medias, el pull/commit haría destrozos.
if [ -n "$(git status --porcelain -- ':!.local')" ]; then
  log "ABORTA: hay cambios sin commitear en el repo. Límpialos y vuelve a lanzar."
  avisar "Abortada: hay cambios sin commitear"
  exit 1
fi

RAMA="$(git rev-parse --abbrev-ref HEAD)"
if [ "$RAMA" != "main" ]; then
  log "ABORTA: estás en la rama '$RAMA', no en main."
  avisar "Abortada: no estás en main"
  exit 1
fi

if ! git pull --rebase --quiet origin main 2>>"$LOG"; then
  log "ERROR: git pull falló. ¿Sin red, o rebase en conflicto?"
  avisar "git pull falló"
  exit 1
fi

# yt-dlp cambia cada pocas semanas persiguiendo a YouTube. Actualizar siempre antes.
python3 -m pip install --quiet --upgrade yt-dlp 2>>"$LOG" \
  || log "AVISO: no pude actualizar yt-dlp; sigo con la versión instalada"
log "yt-dlp $(python3 -m yt_dlp --version 2>/dev/null || echo '??')"

fallos=0
# fetch_captions.py devuelve 1 si NO PUDO LEER un canal. Cero vídeos leyendo bien
# devuelve 0 y no es un error: puede que simplemente no hayan publicado.
python3 agentes/tools/fetch_captions.py --persona lmec --lang es --max 8 --since "$SINCE" \
  "https://www.youtube.com/@LaMejorEstrategiaCriptomonedas/videos" 2>&1 | tee -a "$LOG"
[ "${PIPESTATUS[0]}" -ne 0 ] && { fallos=$((fallos+1)); log "FALLO leyendo el canal de LMEC"; }

python3 agentes/tools/fetch_captions.py --persona cowen --lang en --max 8 --since "$SINCE" \
  "https://www.youtube.com/@benjaminjcowen/videos" 2>&1 | tee -a "$LOG"
[ "${PIPESTATUS[0]}" -ne 0 ] && { fallos=$((fallos+1)); log "FALLO leyendo el canal de Cowen"; }

# Se commitea lo que haya entrado aunque el otro canal fallara.
if [ -n "$(git status --porcelain agentes/*/yt-transcripts/)" ]; then
  n=$(git status --porcelain agentes/*/yt-transcripts/ | wc -l | tr -d ' ')
  git add agentes/*/yt-transcripts/
  git commit --quiet -m "transcripts: ingesta local ($n nuevos)"
  if git push --quiet origin main 2>>"$LOG"; then
    log "OK: $n transcript(s) nuevos subidos"
    avisar "$n transcripts nuevos"
  else
    log "ERROR: commit hecho pero el push falló. Quedan pendientes en local."
    avisar "Push falló: hay commits sin subir"
    exit 1
  fi
else
  log "Sin transcripts nuevos."
fi

if [ "$fallos" -gt 0 ]; then
  log "─── fin CON $fallos canal(es) ilegibles ───"
  avisar "$fallos canal(es) ilegibles — mira .local/ingesta.log"
  exit 1
fi

log "─── fin OK ───"
