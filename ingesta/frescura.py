#!/usr/bin/env python3
"""frescura.py — ¿está caducado el material del que viven los agentes?

POR QUÉ EXISTE
--------------
El 16-ago-2026 los cinco agentes respondieron con material de entre 4 y 7 semanas
mientras TODOS los workflows salían en verde. Cada pipeline informaba de su propia
ejecución ("he corrido, no he petado") y ninguno informaba de lo único que importa:
si el dato que hay en disco sigue sirviendo.

Este script no mira pipelines. Mira FECHAS DE DATOS. Da igual por qué se quedó atrás
—bug, token que falta, cron inexistente, la fuente caída, YouTube bloqueando— si el
dato está viejo, esto se pone rojo.

Es deliberadamente tonto: no arregla nada, solo se niega a decir que todo va bien.

USO
  python ingesta/frescura.py            # informe + sale 1 si algo está caducado
  python ingesta/frescura.py --aviso    # solo avisa, siempre sale 0
"""
import json, os, re, sys, glob
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOY = datetime.now(timezone.utc).date()

# (etiqueta, cómo se obtiene la fecha, límite en días, por qué ese límite)
# Los límites son ~2x la cadencia real: un margen implica un fallo, no un fin de semana.
FUENTES = []


def _fecha_max_por_nombre(patron):
    """Transcripts: el nombre del archivo es YYYYMMDD-slug.md."""
    mejor = None
    for p in glob.glob(os.path.join(ROOT, patron)):
        m = re.match(r"(\d{8})-", os.path.basename(p))
        if not m:
            continue
        try:
            d = datetime.strptime(m.group(1), "%Y%m%d").date()
        except ValueError:
            continue
        if mejor is None or d > mejor:
            mejor = d
    return mejor


def _fecha_json_series(ruta):
    """data/onchain/*.json → {"series":[{"date": "YYYY-MM-DD", ...}]}"""
    try:
        s = json.load(open(os.path.join(ROOT, ruta)))["series"]
        return datetime.strptime(s[-1]["date"], "%Y-%m-%d").date()
    except Exception:
        return None


def _fecha_json_fechas(ruta):
    """data/checkonchain/*.json → {"fechas": ["YYYY-MM-DD", ...]}"""
    try:
        f = json.load(open(os.path.join(ROOT, ruta)))["fechas"]
        return datetime.strptime(f[-1], "%Y-%m-%d").date()
    except Exception:
        return None


def _fecha_woc():
    try:
        d = json.load(open(os.path.join(ROOT, "data/woc_semana.json")))
        return datetime.strptime(d["woc_fecha"], "%Y-%m-%d").date()
    except Exception:
        return None


COMPROBACIONES = [
    ("Transcripts · Cowen", lambda: _fecha_max_por_nombre("agentes/cowen/yt-transcripts/*.md"),
     7, "publica casi a diario"),
    # 25 y no 14: el 17-ago-2026 esto dio FALSO POSITIVO. La ingesta había corrido bien y
    # LMEC simplemente llevaba 17 días sin publicar (comprobado en su canal). Un monitor que
    # llora sin motivo enseña a ignorar el rojo, que es justo lo que este workflow existe para
    # evitar. Límite holgado: solo salta si de verdad hay un mes sin nada.
    ("Transcripts · LMEC", lambda: _fecha_max_por_nombre("agentes/lmec/yt-transcripts/*.md"),
     25, "publica de forma irregular"),
    ("WoC · informes del agente", lambda: _fecha_max_por_nombre("agentes/glassnode_woc/reports/*.md"),
     14, "semanal (sync_woc_reports.py, jueves)"),
    ("WoC · resumen del dashboard", _fecha_woc,
     14, "semanal, jueves (sync-woc.yml)"),
    ("On-chain · BGeometrics", lambda: _fecha_json_series("data/onchain/mvrv_zscore.json"),
     4, "diario (onchain.yml)"),
    ("On-chain · realized price", lambda: _fecha_json_series("data/onchain/realized_price.json"),
     4, "diario (onchain.yml)"),
    ("Checkonchain · cost basis", lambda: _fecha_json_fechas("data/checkonchain/pricing__pricing_costbasisoriginals.json"),
     5, "diario (checkonchain.yml)"),
    ("Checkonchain · derivados", lambda: _fecha_json_fechas("data/checkonchain/derivatives__options_atmimpliedvolatility.json"),
     5, "diario; alimenta el semáforo de LP"),
    # urpd__urpd.json NO se comprueba: es un snapshot sin eje temporal ("distribuciones",
    # no "fechas"), así que no puede declarar su propia edad. Se refresca en el mismo lote
    # que el resto de checkonchain, de modo que la fila de "cost basis" ya lo cubre.
]



def _decisiones_sin_registrar():
    """Decisiones de capital de este ciclo que no tienen su porqué escrito.

    Va aquí y no en un workflow propio a propósito. El material de terceros y el registro
    propio fallan igual —en silencio y en verde— y merecen la misma alarma. Además evita
    otra pieza de infraestructura: el problema de este repo nunca fue tener pocas
    herramientas.

    Devuelve (cubiertas, total, [huérfanas]) o None si no se puede leer el repo privado
    (no se penaliza: sin GH_TOKEN esto no es un fallo del registro, es falta de acceso).
    """
    try:
        import decisiones                                  # mismo directorio
        decs = decisiones.decisiones()
        entradas = decisiones.leer("data/journal.json").get("entries", [])
    except SystemExit:
        return None
    except Exception:
        return None
    huerfanas = [d["que"] for d in decs if not decisiones.casa(d, entradas)]
    return len(decs) - len(huerfanas), len(decs), huerfanas


def main():
    solo_aviso = "--aviso" in sys.argv
    caducados, ausentes, filas = [], [], []

    for etiqueta, fn, limite, nota in COMPROBACIONES:
        fecha = fn()
        if fecha is None:
            ausentes.append(etiqueta)
            filas.append(("SIN DATO", etiqueta, "—", "", nota))
            continue
        dias = (HOY - fecha).days
        mal = dias > limite
        if mal:
            caducados.append((etiqueta, fecha, dias, limite))
        filas.append(("  RANCIO" if mal else "      ok", etiqueta,
                      fecha.isoformat(), f"{dias}d / máx {limite}d", nota))

    ancho = max(len(f[1]) for f in filas)
    print(f"\nFrescura del material · {HOY.isoformat()}\n")
    for estado, etiqueta, fecha, edad, nota in filas:
        print(f"{estado} │ {etiqueta.ljust(ancho)} │ {fecha:<12} {edad:<16} {nota}")

    # --- registro propio ---------------------------------------------------------------
    # El material de terceros es recuperable: si se pierde, se vuelve a bajar. El porqué de
    # una decisión propia no lo es. Por eso se mira aquí, junto a lo demás.
    reg = _decisiones_sin_registrar()
    sin_registrar = []
    if reg is None:
        # NO se pasa por alto en silencio. Un "no pude mirar" que se ve igual que un "todo
        # bien" es el fallo exacto que llevó a construir este archivo. Cuenta como ausente.
        ausentes.append("decisiones registradas (sin acceso al repo privado)")
        print(f"SIN DATO │ {'decisiones registradas'.ljust(ancho)} │ {'—':<12} "
              f"{'':<16} falta GH_TOKEN o LOCAL_DATA_DIR")
    else:
        cub, tot, sin_registrar = reg
        marca = "      ok" if not sin_registrar else "  RANCIO"
        print(f"{marca} │ {'decisiones registradas'.ljust(ancho)} │ {f'{cub}/{tot}':<12} "
              f"{f'{cub/tot*100:.0f}% cobertura':<16} el único dato del que eres la única fuente")

    print()
    if not caducados and not ausentes and not sin_registrar:
        print("Todo al día.")
        return 0

    for etiqueta, fecha, dias, limite in caducados:
        print(f"CADUCADO: {etiqueta} — última fecha {fecha}, {dias} días (máx {limite}).")
    for etiqueta in ausentes:
        print(f"SIN DATO: {etiqueta} — el archivo no existe o no se pudo leer.")

    if sin_registrar:
        print(f"SIN REGISTRAR: {len(sin_registrar)} decisión(es) de capital sin su porqué escrito:")
        for q in sin_registrar:
            print(f"    · {q}")
        print("  (detalle: python3 ingesta/decisiones.py)")

    print("\nUn dato caducado se siente igual de convincente que uno fresco.")
    print("No decidas capital con esto hasta arreglarlo.")
    return 0 if solo_aviso else 1


if __name__ == "__main__":
    sys.exit(main())
