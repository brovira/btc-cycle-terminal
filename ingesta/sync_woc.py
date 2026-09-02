#!/usr/bin/env python3
"""Puente automático: KB de Glassnode (repo privado DeFi-Tracker) → `data/woc_semana.json`.

EL PROBLEMA QUE ARREGLA
-----------------------
La sección "🗞️ Qué hacemos esta semana" de vol.html lee `data/woc_semana.json`. Ese archivo se
escribió A MANO (WoC del 22-jul-2026) y **nada lo actualizaba**: aunque el pipeline semanal del repo
privado ingiera el Week On-Chain nuevo y emita su recomendación, el dashboard seguía mostrando la
semana vieja para siempre. Este script cierra ese hueco.

CADENA COMPLETA (ahora sí, de punta a punta)
--------------------------------------------
  1. DeFi-Tracker · `semanal.py` (jueves 13:00 UTC): ingiere el WoC nuevo, emite la recomendación de
     LP con niveles y **evalúa la de la semana anterior** (narrativa + precio real).
  2. **este script** (jueves 14:00 UTC): lee esa recomendación vía la API de GitHub y la traduce al
     formato que consume el dashboard.
  3. vol.html la muestra: resumen, niveles, qué hacemos y las llamadas en test.

QUÉ SE AUTOMATIZA Y QUÉ NO (importante)
---------------------------------------
El pipeline automático da: acción de LP, régimen, niveles, lectura, por qué, métricas, señal a vigilar
y la evaluación de la semana previa. Todo eso se rellena solo.
Lo que **NO** puede rellenar una máquina y queda a criterio del agente `glassnode_tactico`:
`fiabilidad_tipo` (cuánto vale ESE tipo de llamada según el track record) y `cambios_de_fiabilidad`.
Se marcan con `_pendiente_agente` para que se vea que están sin curar, en vez de inventarlos.

Requiere: GH_TOKEN con lectura de Contents sobre brovira/DeFi-Tracker.

Uso:
  python ingesta/sync_woc.py            # escribe data/woc_semana.json si hay algo más nuevo
  python ingesta/sync_woc.py --forzar   # reescribe aunque la fecha coincida
"""
import argparse, base64, json, os, sys, urllib.request, urllib.error
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST = os.path.join(ROOT, "data", "woc_semana.json")
REPO = "brovira/DeFi-Tracker"
RUTA_JSONL = "research/glassnode-kb/recomendaciones/recomendaciones.jsonl"

# Fiabilidad por tipo de llamada, del scorecard (agentes/derivados_glassnode/reports/track_record.md).
# Heurística de palabras clave; el agente `glassnode_tactico` puede refinarla.
#
# ⚠️ OJO con las siglas cortas: se usan REGEX con límites de palabra (\b) a propósito. Con simple
# substring, "iv" hacía match dentro de "decisIVo" y clasificaba un reclaim de nivel como
# «IV baja → expansión» (1/4). Los patrones van del MÁS específico al más genérico.
FIABILIDAD = [
    (r"reset de funding|funding reset",
     "«reset de funding → constructivo» — 1/3 (falla cerca de techos de ciclo)"),
    # OJO 2 (17-ago-2026): `\bbasis\b` a secas hacía match dentro de "STH Cost Basis" y le
    # colgaba el 3/3 de backwardation a TODA llamada de nivel on-chain, que es un tipo
    # distinto (8/10, patrón de más abajo). Mismo bicho que el `iv` dentro de "decisIVo"
    # avisado arriba: una palabra corta de derivados que también vive en el vocabulario
    # on-chain. Aquí "basis" solo cuenta si es el basis de futuros, no un cost basis.
    (r"backwardation|contango|(?<!cost )(?<!coste )\bbasis\b(?!\s*(?:de\s+coste|cost))",
     "backwardation/funding extremo → squeeze — 3/3 histórico"),
    (r"\bfunding\b|leverage|apiñad|crowded|\bflush\b|squeeze|open interest|\bOI\b",
     "posicionamiento/leverage — 8/10 histórico (su punto fuerte)"),
    (r"cost basis|\bSTH\b|\bLTH\b|realized price|realised price|true market mean|reclaim|shelf|estante",
     "posicionamiento + nivel on-chain — 8/10 histórico"),
    (r"\bIV\b|\bDVOL\b|vol barata|volatilidad implícita|implied vol|compresi[óo]n de vol",
     "«IV baja → expansión de vol» — 1/4 histórico (prematuro y ciego de dirección)"),
]


def fiabilidad_de(texto):
    import re
    t = texto or ""
    for patron, etiqueta in FIABILIDAD:
        if re.search(patron, t, re.I):
            return etiqueta
    return "sin clasificar — pendiente de que el agente lo calibre"


def gh_get(ruta):
    token = os.environ.get("GH_TOKEN", "").strip()
    if not token:
        print("ERROR: falta GH_TOKEN (lectura de Contents sobre DeFi-Tracker).", file=sys.stderr)
        return None
    url = f"https://api.github.com/repos/{REPO}/contents/{ruta}"
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json",
        "User-Agent": "btc-cycle-terminal/sync-woc", "X-GitHub-Api-Version": "2022-11-28"})
    try:
        with urllib.request.urlopen(req, timeout=40) as r:
            j = json.loads(r.read().decode())
        return base64.b64decode(j["content"]).decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        print(f"ERROR HTTP {e.code} leyendo {ruta}: {e.read().decode('utf-8','replace')[:200]}", file=sys.stderr)
    except Exception as e:
        print(f"ERROR leyendo {ruta}: {e}", file=sys.stderr)
    return None


def euros(v):
    return f"${v:,.0f}".replace(",", ".") if isinstance(v, (int, float)) else None


def construir(rec, previo):
    """Traduce una entrada del pipeline al formato del dashboard."""
    niveles = []
    mapa = [("sth_cost_basis", "STH cost basis (resistencia/soporte)"),
            ("true_market_mean", "True Market Mean (línea bull/bear)"),
            ("realized_price", "Realized Price (suelo del ciclo)"),
            ("soporte_shelf", "Estante de demanda (soporte)"),
            ("resistencia_wall", "Muro de oferta (resistencia)"),
            ("max_pain", "Max pain de opciones")]
    for k, etiqueta in mapa:
        v = (rec.get("niveles") or {}).get(k)
        if isinstance(v, (int, float)):
            niveles.append({"k": etiqueta, "v": euros(v)})

    accion = rec.get("recomendacion_lp") or "—"
    que = f"<b>Acción de LP: {accion}</b>"
    if rec.get("regimen_leverage"):
        que += f" · régimen de leverage: <b>{rec['regimen_leverage']}</b>"
    if rec.get("confianza"):
        que += f" · confianza: {rec['confianza']}"
    if rec.get("porque"):
        que += f".<br>{rec['porque']}"

    abiertas = []
    if rec.get("senal_a_vigilar"):
        abiertas.append({
            "llamada": rec["senal_a_vigilar"],
            "tipo": "señal a vigilar (del WoC)",
            "fiabilidad_tipo": fiabilidad_de(rec["senal_a_vigilar"]),
            "criterio_exito": "se evalúa el jueves siguiente: narrativa del WoC nuevo + movimiento real de precio",
            "estado": "pendiente",
        })

    evaluadas = []
    ev = rec.get("evaluacion_anterior") or {}
    if ev.get("habia_recomendacion_previa") and ev.get("veredicto") not in (None, "", "N/A"):
        evaluadas.append({
            "llamada": (previo or {}).get("senal_a_vigilar") or "recomendación de la semana anterior",
            "veredicto": str(ev.get("veredicto")).upper(),
            "nota": ev.get("comentario") or "",
        })
    evp = rec.get("evaluacion_anterior_precio")
    if isinstance(evp, dict) and evp.get("veredicto"):
        evaluadas.append({
            "llamada": "misma llamada, juzgada por PRECIO real (maker≠checker)",
            "veredicto": str(evp.get("veredicto")).upper(),
            "nota": evp.get("comentario") or "",
        })

    return {
        "_como_se_actualiza": ("AUTOMÁTICO desde jul-2026: ingesta/sync_woc.py lee la recomendación del "
                               "pipeline semanal del repo privado (DeFi-Tracker) y la traduce a este formato. "
                               "Workflow: sync-woc.yml, jueves 14:00 UTC (1h después del pipeline)."),
        "_pendiente_agente": ("`fiabilidad_tipo` se asigna por heurística de palabras clave y "
                              "`cambios_de_fiabilidad` queda vacío: eso lo calibra el agente "
                              "glassnode_tactico contra track_record.md."),
        "updated": rec.get("fecha"),
        "woc_fecha": rec.get("fecha"),
        "woc_titulo": rec.get("titulo") or "Week On-Chain",
        "fuentes": [rec.get("articulo", ""), "recomendaciones.jsonl (pipeline semanal, DeFi-Tracker)"],
        "resumen": rec.get("lectura_posicionamiento") or "",
        "que_hacemos": que,
        "niveles": niveles,
        "metricas": rec.get("metricas") or "",
        "llamadas_abiertas": abiertas,
        "evaluadas_recientes": evaluadas,
        "cambios_de_fiabilidad": "",
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--forzar", action="store_true")
    a = ap.parse_args()

    raw = gh_get(RUTA_JSONL)
    if raw is None:
        sys.exit(1)
    entradas = [json.loads(l) for l in raw.splitlines() if l.strip()]
    if not entradas:
        print("El log de recomendaciones está vacío — nada que sincronizar.")
        return
    entradas.sort(key=lambda x: str(x.get("fecha") or ""))
    rec = entradas[-1]
    previo = entradas[-2] if len(entradas) > 1 else None

    actual = {}
    if os.path.exists(DEST):
        try:
            actual = json.load(open(DEST))
        except Exception:
            pass
    if actual.get("woc_fecha") == rec.get("fecha") and not a.forzar:
        print(f"Sin novedad: el dashboard ya muestra el WoC del {rec.get('fecha')}.")
        print("(el pipeline del repo privado corre los jueves 13:00 UTC; si hoy es jueves antes de esa hora, "
              "el artículo nuevo aún no está ingerido)")
        return

    # El pipeline privado deja la recomendacion PENDIENTE cuando no tiene clave de API (desde
    # julio, siempre). Aqui se rellena con la suscripcion, con el mismo framework y esquema.
    if str(rec.get("recomendacion_lp", "")).upper() == "PENDIENTE" and rec.get("articulo"):
        from woc_recomendacion import recomendar
        texto = gh_get(f"research/glassnode-kb/articulos/{rec['articulo']}")
        if texto:
            d, err = recomendar(texto, rec.get("fecha", "?"), previo)
            if d:
                rec = {**rec, **d}
                print("Recomendacion rellenada con claude -p (el pipeline privado la dejo PENDIENTE).")
            else:
                print(f"AVISO: la recomendacion sigue PENDIENTE: {err}", file=sys.stderr)
    nuevo = construir(rec, previo)
    if rec.get("generado_por"):
        nuevo["fuentes"].append(rec["generado_por"])
    # Un WoC que SABEMOS que existe pero que no hemos podido leer (Cloudflare) se arrastra
    # como 'pendiente' para que el panel no presente el anterior como si fuera el vigente.
    # Se cae solo en cuanto sincronizamos uno de esa fecha o posterior.
    pend = actual.get("pendiente")
    if pend and str(pend.get("fecha") or "") > str(nuevo.get("woc_fecha") or ""):
        nuevo["pendiente"] = pend
    with open(DEST, "w") as f:
        json.dump(nuevo, f, indent=2, ensure_ascii=False)
    print(f"Actualizado: {actual.get('woc_fecha','(vacío)')} → {nuevo['woc_fecha']} · «{nuevo['woc_titulo']}»")
    print(f"  niveles: {len(nuevo['niveles'])} · llamadas abiertas: {len(nuevo['llamadas_abiertas'])} · "
          f"evaluadas: {len(nuevo['evaluadas_recientes'])}")


if __name__ == "__main__":
    main()
