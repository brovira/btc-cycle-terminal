#!/usr/bin/env python3
"""Forward-call + evaluación para los analistas (Cowen / LMEC).

Mismo patrón que el pase semanal de Glassnode, pero para VÍDEOS (transcripts que ya
ingesta `ingest-transcripts.yml` a diario):
  1. Detecta transcripts NUEVOS por persona (fecha en el nombre > última llamada logueada).
  2. Si hay ANTHROPIC_API_KEY, llama a Claude para extraer la LLAMADA FORWARD del/los vídeo(s)
     nuevos: sesgo (alcista/bajista/neutral), fase de ciclo, niveles, acción y tesis.
     Sin API key → deja la llamada PENDIENTE (la rellenamos en chat, coste 0).
  3. SIEMPRE (gratis, CoinGecko) re-evalúa TODAS las llamadas pasadas por PRECIO real a
     MÚLTIPLES HORIZONTES (7/30/90d) — sus llamadas son de ciclo, no de una semana, así que
     cada semana se re-puntúan a medida que pasa el tiempo.
  4. Escribe `agentes/<persona>/forward/forward_calls.jsonl` + `RESUMEN.md`.

Stdlib only. Uso:
  python agentes/tools/personas_forward.py            # todas las personas
  python agentes/tools/personas_forward.py --regrade  # solo re-evaluar por precio (no LLM)
"""
import os, re, sys, json, ssl, glob, urllib.request, urllib.parse
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # repo root
CTX = ssl.create_default_context()
UA = {"User-Agent": "btc-personas-forward/1.0"}
API_KEY = os.environ.get("ANTHROPIC_API_KEY", "").strip()
MODEL = os.environ.get("PERSONAS_MODEL", "claude-sonnet-5")

PERSONAS = {
    "cowen": {"nombre": "Benjamin Cowen", "tema": "ciclo de 4 años, risk metric, dominancia, macro BTC/ETH", "lang": "en"},
    "lmec": {"nombre": "LMEC", "tema": "ciclo BTC, Bull Market Support Band, DCA con órdenes, altcoins, farming", "lang": "es"},
}
HORIZONS = [7, 30, 90]


# ---------------- precio (CoinGecko, gratis) ----------------
def _http_json(url, timeout=60):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
        return json.loads(r.read().decode())


def fetch_btc_daily(days=400):
    try:
        j = _http_json("https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
                       "?vs_currency=usd&days=%d&interval=daily" % days)
        return [(int(ms), float(p)) for ms, p in j.get("prices", [])]
    except Exception as e:
        print("  ! error precio:", e)
        return []


def _date_ms(dstr):
    return datetime.strptime(dstr[:10], "%Y-%m-%d").replace(tzinfo=timezone.utc).timestamp() * 1000


def price_on(prices, ms):
    best = None
    for t, p in prices:
        if t <= ms + 864e5:
            best = p
        else:
            break
    return best


def grade_directional(call, prices):
    """Puntúa una llamada direccional a 7/30/90d con el precio real. Devuelve dict de grados."""
    bias = (call.get("bias") or "").lower()
    if bias not in ("alcista", "bajista", "neutral") or not prices:
        return {}
    t0 = _date_ms(call["fecha"])
    p0 = price_on(prices, t0)
    if not p0:
        return {}
    now = prices[-1][0]
    out = {}
    for h in HORIZONS:
        th = t0 + h * 864e5
        if th > now + 3 * 864e5:  # aún no ha pasado ese horizonte
            continue
        ph = price_on(prices, th)
        if not ph:
            continue
        ret = ph / p0 - 1
        if bias == "alcista":
            v = "HIT" if ret > 0.05 else ("MISS" if ret < -0.05 else "NEUTRO")
        elif bias == "bajista":
            v = "HIT" if ret < -0.05 else ("MISS" if ret > 0.05 else "NEUTRO")
        else:  # neutral
            v = "HIT" if abs(ret) < 0.05 else "MISS"
        out["%dd" % h] = {"ret_pct": round(ret * 100, 1), "verdict": v}
    return out


# ---------------- transcripts ----------------
def transcripts_dir(persona):
    return os.path.join(ROOT, "agentes", persona, "yt-transcripts")


def forward_dir(persona):
    d = os.path.join(ROOT, "agentes", persona, "forward")
    os.makedirs(d, exist_ok=True)
    return d


def list_transcripts(persona):
    out = []
    for fp in glob.glob(os.path.join(transcripts_dir(persona), "*.md")):
        base = os.path.basename(fp)
        m = re.match(r"(\d{8})-", base)
        if not m:
            continue
        d = m.group(1)
        out.append({"date": "%s-%s-%s" % (d[:4], d[4:6], d[6:8]), "file": base, "path": fp})
    out.sort(key=lambda x: x["date"])
    return out


def load_log(persona):
    fp = os.path.join(forward_dir(persona), "forward_calls.jsonl")
    if not os.path.exists(fp):
        return []
    return [json.loads(l) for l in open(fp, encoding="utf-8").read().splitlines() if l.strip()]


def save_log(persona, recs):
    fp = os.path.join(forward_dir(persona), "forward_calls.jsonl")
    with open(fp, "w", encoding="utf-8") as f:
        for r in recs:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


# ---------------- LLM ----------------
SCHEMA = """Devuelve SOLO un JSON valido (sin markdown) con esta forma:
{
  "bias": "alcista" | "bajista" | "neutral",
  "fase_ciclo": "acumulacion" | "alcista" | "distribucion/techo" | "bajista" | "incierto",
  "horizonte": "semanas" | "meses",
  "niveles": {"objetivo": num_usd_o_null, "invalidacion": num_usd_o_null, "soporte": num_usd_o_null, "resistencia": num_usd_o_null},
  "accion": "acumular/DCA" | "mantener" | "tomar profit" | "reducir" | "fuera",
  "tesis": "1-2 frases con su llamada, en sus terminos",
  "confianza": "alta" | "media" | "baja"
}
Extrae SU llamada direccional / de ciclo del vídeo. Niveles = numeros USD sin simbolo o null. No inventes; si no lo dice, deja null / incierto."""


def call_claude(persona, transcripts):
    if not API_KEY:
        return None
    p = PERSONAS[persona]
    corpus = "\n\n".join("### %s (%s)\n%s" % (t["date"], t["file"], open(t["path"], encoding="utf-8").read()[:9000])
                         for t in transcripts[-2:])
    system = ("Eres un analista que resume la llamada de mercado de %s (%s). Los vídeos son transcripts "
              "speech-to-text (posibles erratas). Extrae SU postura direccional/de ciclo actual, no la tuya. "
              "No inventes cifras." % (p["nombre"], p["tema"]))
    user = "TRANSCRIPT(S) MAS RECIENTES:\n" + corpus + "\n\n=== TAREA ===\nExtrae la llamada forward.\n\n" + SCHEMA
    payload = json.dumps({"model": MODEL, "max_tokens": 900, "system": system,
                          "messages": [{"role": "user", "content": user}]}).encode()
    req = urllib.request.Request("https://api.anthropic.com/v1/messages", data=payload,
                                 headers={"x-api-key": API_KEY, "anthropic-version": "2023-06-01",
                                          "content-type": "application/json", **UA})
    try:
        with urllib.request.urlopen(req, timeout=120, context=CTX) as r:
            j = json.loads(r.read().decode())
        txt = "".join(b.get("text", "") for b in j.get("content", []) if b.get("type") == "text")
        m = re.search(r"\{.*\}", txt, re.S)
        return json.loads(m.group(0)) if m else None
    except Exception as e:
        print("  ! error API:", e)
        return None


# ---------------- render ----------------
def _grades_line(g):
    if not g:
        return "sin horizonte cumplido aún"
    return " · ".join("%s %s (%s%%)" % (h, g[h]["verdict"], g[h]["ret_pct"]) for h in ("7d", "30d", "90d") if h in g)


def write_resumen(persona, recs):
    p = PERSONAS[persona]
    head = ("# Llamadas forward · %s (auto)\n\n> Postura direccional/de ciclo extraída de sus vídeos, "
            "evaluada por precio real (CoinGecko) a 7/30/90d. Lo último arriba. No es asesoramiento "
            "financiero.\n\n" % p["nombre"])
    blocks = []
    for r in reversed(recs):
        niv = r.get("niveles") or {}
        nl = " · ".join("%s $%s" % (k, format(int(niv[k]), ",")) for k in ("objetivo", "invalidacion", "soporte", "resistencia") if niv.get(k)) or "—"
        blocks.append(
            "## %s · %s\n\n" % (r["fecha"], r.get("titulo", r.get("video", "")))
            + "**Sesgo:** %s  ·  **Fase:** %s  ·  **Acción:** %s  ·  **Confianza:** %s\n\n" % (
                r.get("bias", "?"), r.get("fase_ciclo", "?"), r.get("accion", "?"), r.get("confianza", "?"))
            + "- **Tesis:** %s\n" % r.get("tesis", "—")
            + "- **Niveles:** %s\n" % nl
            + "- **Resultado (precio real):** %s\n\n---\n" % _grades_line(r.get("grades")))
    open(os.path.join(forward_dir(persona), "RESUMEN.md"), "w", encoding="utf-8").write(head + "\n".join(blocks))


# ---------------- main ----------------
def process(persona, prices, regrade_only=False):
    recs = load_log(persona)
    last_date = recs[-1]["fecha"] if recs else "0000-00-00"
    added = None
    if not regrade_only:
        nuevos = [t for t in list_transcripts(persona) if t["date"] > last_date]
        if nuevos:
            data = call_claude(persona, nuevos)
            latest = nuevos[-1]
            titulo = open(latest["path"], encoding="utf-8").readline().lstrip("# ").strip()
            if data is None:
                data = {"bias": "pendiente", "fase_ciclo": "incierto", "accion": "—",
                        "tesis": "Pendiente de análisis (sin API key). Rellenar en chat.",
                        "niveles": {}, "confianza": "baja"}
            rec = {"fecha": latest["date"], "persona": persona, "video": latest["file"], "titulo": titulo, **data}
            recs.append(rec)
            added = rec
    # re-grade all past calls by price (multi-horizonte)
    for r in recs:
        r["grades"] = grade_directional(r, prices)
    save_log(persona, recs)
    write_resumen(persona, recs)
    return added, len(recs)


def main():
    regrade = "--regrade" in sys.argv
    prices = fetch_btc_daily(400)
    lines = []
    for persona in PERSONAS:
        if not os.path.isdir(transcripts_dir(persona)):
            continue
        added, n = process(persona, prices, regrade_only=regrade)
        if added:
            lines.append("**%s %s** — %s / %s (%s). %s" % (
                PERSONAS[persona]["nombre"], added["fecha"], added.get("bias", "?"),
                added.get("accion", "?"), added.get("fase_ciclo", "?"), added.get("tesis", "")))
        print("%s: %d llamadas en log%s" % (persona, n, " (+1 nueva)" if added else ""))
    summary = ("### Llamadas forward de analistas\n\n" + "\n\n".join(lines)) if lines else "Sin vídeos nuevos que analizar."
    print("\n==== RESUMEN ====\n" + summary)
    gp = os.environ.get("GITHUB_STEP_SUMMARY")
    if gp:
        open(gp, "a").write(summary + "\n")


if __name__ == "__main__":
    main()
