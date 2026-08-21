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

# yt-dlp cambia cada pocas semanas persiguiendo al antibot de YouTube: actualizar SIEMPRE.
#
# Se prefiere el binario autónomo antes que `pip install`. En macOS el python3 del
# sistema es el 3.9 de Xcode, y pip ahí se queda clavado en la última versión que aún
# soportaba 3.9 (2025.10.14 a 17-ago-2026, diez meses vieja) diciendo "Requirement
# already satisfied". Silenciosamente inútil, que es el patrón que llevamos todo el día
# eliminando. El binario trae su propio intérprete y se actualiza con `-U`.
YTDLP_BIN="${YTDLP_BIN:-}"
if [ -z "$YTDLP_BIN" ]; then
  if command -v yt-dlp >/dev/null 2>&1;      then YTDLP_BIN="$(command -v yt-dlp)"
  elif [ -x "$HOME/.local/bin/yt-dlp" ];     then YTDLP_BIN="$HOME/.local/bin/yt-dlp"
  fi
fi

if [ -n "$YTDLP_BIN" ]; then
  export YTDLP_BIN                     # fetch_captions.py lo lee y usa el mismo
  "$YTDLP_BIN" -U >>"$LOG" 2>&1 || log "AVISO: 'yt-dlp -U' falló; sigo con la instalada"
  log "yt-dlp $("$YTDLP_BIN" --version 2>/dev/null || echo '??')  ($YTDLP_BIN)"
else
  log "AVISO: no hay binario de yt-dlp; tiro del módulo de python3, que puede estar viejo."
  log "       Instálalo:  mkdir -p ~/.local/bin && curl -L \\"
  log "       https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp_macos \\"
  log "       -o ~/.local/bin/yt-dlp && chmod +x ~/.local/bin/yt-dlp"
fi

fallos=0
# fetch_captions.py devuelve 1 si NO PUDO LEER un canal. Cero vídeos leyendo bien
# devuelve 0 y no es un error: puede que simplemente no hayan publicado.
python3 agentes/tools/fetch_captions.py --persona lmec --lang es --max 8 --since "$SINCE" \
  "https://www.youtube.com/@LaMejorEstrategiaCriptomonedas/videos" 2>&1 | tee -a "$LOG"
[ "${PIPESTATUS[0]}" -ne 0 ] && { fallos=$((fallos+1)); log "FALLO leyendo el canal de LMEC"; }

python3 agentes/tools/fetch_captions.py --persona cowen --lang en --max 8 --since "$SINCE" \
  "https://www.youtube.com/@benjaminjcowen/videos" 2>&1 | tee -a "$LOG"
[ "${PIPESTATUS[0]}" -ne 0 ] && { fallos=$((fallos+1)); log "FALLO leyendo el canal de Cowen"; }

# LATIDO. Sin esto, el repo no puede distinguir "LMEC no ha publicado" de "el Mac
# llevaba cuatro dias apagado y esto no se ejecuto". Las dos cosas se ven identicas desde
# fuera: un archivo con fecha vieja. Es la misma trampa de agosto, un piso mas arriba.
mkdir -p ingesta/local
cat > ingesta/local/estado.json <<JSON
{
  "_": "Lo escribe ingesta_local.sh en cada ejecucion. Lo lee ingesta/frescura.py. Si esta viejo, la ingesta local NO se esta ejecutando -- da igual lo que digan las fechas de los transcripts.",
  "ultima_ejecucion": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "desde": "$SINCE",
  "canales_ilegibles": $fallos,
  "maquina": "$(hostname -s 2>/dev/null || echo desconocida)"
}
JSON

# Se commitea lo que haya entrado aunque el otro canal fallara. El latido va siempre,
# incluso cuando no hay transcripts nuevos: sobre todo cuando no hay transcripts nuevos.
if [ -n "$(git status --porcelain agentes/*/yt-transcripts/ ingesta/local/estado.json)" ]; then
  n=$(git status --porcelain agentes/*/yt-transcripts/ | wc -l | tr -d ' ')
  git add agentes/*/yt-transcripts/ ingesta/local/estado.json
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
