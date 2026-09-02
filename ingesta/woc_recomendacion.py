#!/usr/bin/env python3
"""Recomendación de LP de la semana cuando el pipeline privado la deja PENDIENTE.

EL HUECO
--------
`semanal.py` (DeFi-Tracker) ingiere el Week On-Chain y pide la recomendación a la API de
Anthropic con ANTHROPIC_API_KEY. Esa clave no está configurada, así que desde julio TODAS
las entradas de recomendaciones.jsonl llevan `recomendacion_lp: "PENDIENTE"` y el dashboard
mostraba «Acción de LP: PENDIENTE» semana tras semana sin que nada se pusiera rojo.

Aquí se rellena con la suscripción (`claude -p` + CLAUDE_CODE_OAUTH_TOKEN), igual que los
informes destilados y las lecturas diarias. Mismo framework y mismo esquema que semanal.py
(copiados, no importados: el repo privado no está en el runner). El artículo se baja del KB.

La salida se marca con `generado_por` para que nadie la confunda con la del pipeline privado.

Uso directo:
  python ingesta/woc_recomendacion.py <articulo.md del KB> [recomendacion_previa.json]
"""
import json, os, re, subprocess, sys, tempfile

FRAMEWORK = """Eres un analista de DERIVADOS y OPCIONES que razona con el framework de Glassnode.
FILOSOFIA: los derivados leen POSICIONAMIENTO/SENTIMIENTO, no direccion. Se cruzan con on-chain
(STH cost basis / realized price / true market mean) que da el DONDE. El LP concentrado = CORTO DE VOL.

CALIBRACION (track record de 152 Week On-Chain 2020-2026):
- Senal MAS FIABLE (8/10): LEVERAGE APINADO.
    * funding >8% anual + OI en maximos + skew pasando de defensivo a call-heavy = LONGS APINADOS -> flush a la baja.
    * funding negativo sostenido + OI subiendo + backwardation = SHORTS APINADOS -> short-squeeze al alza.
- Senal DEBIL (1/4, prematura y ciega de direccion): "IV/DVOL baja -> expansion". NO salgas del LP solo por "vol barata".

UMBRALES: 25d skew (>20-30% panico; 11-14% defensivo; 2-6% neutral; negativo=risk-on); put/call OI (0.42-0.56 risk-on; >1 defensivo);
funding vs 0.01%/8h; OI vs picos (limpio si muy debajo); VRP=IV-RV (muy positivo=vender vol/farmear; ~0=opciones baratas; negativo=vol se realiza, amplifica);
max pain (spot debajo=defensivo; reclaim+aguantar=dealer gamma de techo a ancla, amortigua); DVOL.

PLAYBOOK LP:
- FARMEAR (rango estrecho): VRP positivo + OI reseteado + funding neutral/negativo post-flush + dealer long gamma / precio en max pain.
- ENSANCHAR (rango ancho, menos tamano): IV/DVOL minimos PERO skew defensivo (vol diferida) / short gamma cerca de spot / VRP~0.
- SALIR (cerrar LP): CONFLUENCIA de leverage extremo + on-chain en/rechazando cost-basis; o VRP a negativo; o front-end IV spike + skew>20%.
REGLA MAESTRA: dispara la SALIDA con la confluencia (leverage extremo + on-chain en nivel clave), NUNCA con un aviso aislado de "vol barata"."""

SCHEMA = """Devuelve SOLO un objeto JSON valido (sin markdown, sin texto fuera del JSON) con esta forma:
{
  "evaluacion_anterior": {
    "habia_recomendacion_previa": true/false,
    "veredicto": "HIT" | "MISS" | "PARCIAL" | "PENDIENTE" | "N/A",
    "comentario": "1-2 frases: se cumplio lo que decia la recomendacion previa, a la luz de lo que reporta este articulo?"
  },
  "regimen_leverage": "limpio" | "apinado-long" | "apinado-short" | "reseteando" | "mixto",
  "metricas": "las cifras de derivados que cita el articulo (funding, OI, skew, put/call, VRP, DVOL, max pain), en una linea",
  "niveles": {
    "sth_cost_basis": numero_usd_o_null, "realized_price": numero_usd_o_null,
    "true_market_mean": numero_usd_o_null, "soporte_shelf": numero_usd_o_null,
    "resistencia_wall": numero_usd_o_null, "max_pain": numero_usd_o_null
  },
  "lectura_posicionamiento": "2-3 frases: cubierto o complaciente? apalancado o limpio? quien esta offside?",
  "recomendacion_lp": "FARMEAR" | "ENSANCHAR" | "SALIR",
  "porque": "1-2 frases justificando la accion de LP con la confluencia (leverage + on-chain), no con 'vol barata' aislada",
  "senal_a_vigilar": "el gatillo concreto que cambiaria la recomendacion la proxima semana",
  "confianza": "alta" | "media" | "baja"
}
En "niveles" extrae solo NUMEROS en USD sin simbolo (ej. 69000), o null si el articulo no lo dice. Estos niveles fijan el rango de LP."""

CAMPOS = ("evaluacion_anterior", "regimen_leverage", "metricas", "niveles", "lectura_posicionamiento",
          "recomendacion_lp", "porque", "senal_a_vigilar", "confianza")


def recomendar(texto_articulo, fecha, previa=None):
    """Devuelve el dict con los campos del esquema, o (None, motivo)."""
    if not os.environ.get("CLAUDE_CODE_OAUTH_TOKEN", "").strip():
        return None, "sin CLAUDE_CODE_OAUTH_TOKEN"
    prev_txt = json.dumps(previa, ensure_ascii=False, indent=2) if previa else "No hay recomendacion previa."
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as fh:
        fh.write(texto_articulo[:14000]); tmp = fh.name
    prompt = (FRAMEWORK + "\n\nRECOMENDACION DE LA SEMANA ANTERIOR (a evaluar con lo que diga el nuevo articulo):\n"
              + prev_txt + f"\n\nEl NUEVO ARTICULO WEEK ON-CHAIN ({fecha}) esta en el fichero {tmp}: leelo entero.\n\n"
              "=== TU TAREA ===\n1) Evalua la recomendacion previa a la luz de lo que reporta este articulo.\n"
              "2) Emite la recomendacion de LP de esta semana, priorizando la lectura de LEVERAGE APINADO,\n"
              "   y extrae los NIVELES numericos on-chain para fijar el rango.\n\n" + SCHEMA)
    try:
        r = subprocess.run(["claude", "-p", prompt, "--allowedTools", "Read", "--output-format", "text"],
                           capture_output=True, text=True, timeout=600)
    except Exception as e:
        return None, f"claude -p: {e}"
    finally:
        os.unlink(tmp)
    m = re.search(r"\{.*\}", r.stdout or "", re.S)
    if not m:
        return None, "el modelo no devolvio JSON: " + (r.stderr or r.stdout or "")[-300:]
    try:
        d = json.loads(m.group(0))
    except Exception as e:
        return None, f"JSON invalido: {e}"
    if d.get("recomendacion_lp") not in ("FARMEAR", "ENSANCHAR", "SALIR"):
        return None, f"recomendacion fuera de vocabulario: {d.get('recomendacion_lp')!r}"
    out = {k: d.get(k) for k in CAMPOS}
    out["generado_por"] = "claude -p en sync-woc (btc-cycle-terminal), con la suscripcion; el pipeline privado la dejo PENDIENTE"
    return out, None


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    texto = open(sys.argv[1], encoding="utf-8").read()
    previa = json.load(open(sys.argv[2])) if len(sys.argv) > 2 else None
    fecha = re.search(r"(\d{4}-\d{2}-\d{2})", os.path.basename(sys.argv[1]))
    d, err = recomendar(texto, fecha.group(1) if fecha else "?", previa)
    print(json.dumps(d, ensure_ascii=False, indent=1) if d else "ERROR: " + err)
