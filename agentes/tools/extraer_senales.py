#!/usr/bin/env python3
"""extraer_señales.py — prefiltro para la auditoría de framework de los analistas.

QUÉ PROBLEMA RESUELVE
---------------------
Auditar «letra a letra» 397 documentos (277 Cowen + 37 LMEC + 83 WoC) son ~2M tokens si se
leen enteros. Y la mayor parte de un transcript de Cowen es saludo, publicidad de ITC Premium
y despedida: texto que no contiene una sola señal.

Este script lee TODOS los caracteres de TODOS los documentos —de ahí que siga siendo «letra a
letra»— y se queda solo con las frases que llevan **un número Y un término de indicador o de
acción**. Eso es lo que se puede auditar: un umbral sin número no es falsable, y un número sin
indicador no dice nada.

Cada pasaje sale con su contexto para que el que lo lea después pueda juzgar el sentido, no
solo la cifra.

USO
  python3 agentes/tools/extraer_señales.py --persona cowen --desde 20250601
  python3 agentes/tools/extraer_señales.py --persona woc --desde 2025-06-01 --kb /ruta/al/kb
"""
import argparse, os, re, sys, json

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Indicadores: los de los tres marcos, en inglés y español. Se busca por raíz para pillar
# plurales y variantes ("moving average"/"averages", "media móvil"/"medias móviles").
INDICADORES = r"""risk metric|risk metrics|risk band|risk level|risk of|mvrv|z-?score|realized price|realised price|
terminal price|balance price|true market mean|true mean|cost basis|short.?term holder|long.?term holder|\bsth\b|\blth\b|
sopr|nupl|supply in (?:profit|loss)|urpd|quantile|unrealized loss|unrealised loss|realized profit|profit/loss ratio|
200.?week|200w|200.?day|200d|50.?week|50w|20.?week|21.?week|bull market support|bear market resistance|resistance band|
moving average|media m|\bsma\b|\bema\b|\brsi\b|\bmacd\b|bmsb|
funding|open interest|\boi\b|skew|implied vol|\biv\b|dvol|put/call|max pain|basis|liquidat|leverage|apalancamiento|
halving cycle|diminishing return|dominance|dominancia|altseason|
etf flow|coinbase premium|\bdxy\b|yield|10.?year|quantitative tightening|\bqt\b|rate cut|rate hik|fed |
precio objetivo|objetivo de precio|suelo|techo|soporte|resistencia|media m|banda|
capitulat|capitulaci|exhaust|acumulaci|distribuci"""

# Acciones y condiciones: lo que convierte una observación en una llamada auditable.
ACCIONES = r"""\bbuy\b|\bbuying\b|\bsell\b|\bselling\b|\bdca\b|accumulat|take profit|took profit|
comprar|compro|compra|vender|vendo|venta|acumular|acumulo|tomar beneficio|tom[eé] beneficio|
invalidat|invalidaci|if bitcoin|if btc|if we|if price|si bitcoin|si el precio|si rompe|si pierde|
target|objetivo|threshold|umbral|\blevel\b|nivel|expect|espero|creo que|i think|my plan|mi plan|
bottom|\btop\b|low\b|high\b|floor|ceiling"""

# Un número que signifique algo: precio, porcentaje, ratio de riesgo, múltiplo, fecha.
NUMERO = r"""\$\s?\d[\d,\.]*\s?[kKmMbB]?|\d[\d,\.]*\s?(?:k\b|mil\b|000\b)|\d+(?:[\.,]\d+)?\s?%|
0?[\.,]\d+\s*(?:risk|de riesgo)?|\brisk\s+(?:of\s+)?0?[\.,]?\d+|\b\d{4}\b|\b\d+\s*(?:days?|weeks?|months?|d[ií]as?|semanas?|meses)\b"""

RX_IND = re.compile(INDICADORES.replace("\n", ""), re.I)
RX_ACC = re.compile(ACCIONES.replace("\n", ""), re.I)
RX_NUM = re.compile(NUMERO.replace("\n", ""), re.I)


def frases(texto):
    """Trocea en unidades legibles. Los auto-subs no traen puntuación fiable, así que se
    corta también por longitud: sin esto, un transcript entero sería 'una frase'."""
    bruto = re.split(r"(?<=[.!?])\s+|\n{2,}", texto)
    out = []
    for f in bruto:
        f = " ".join(f.split())
        while len(f) > 400:                      # trozos largos: partir por comas
            corte = f.rfind(",", 200, 400)
            corte = corte if corte > 0 else 400
            out.append(f[:corte]); f = f[corte:].lstrip(", ")
        if f:
            out.append(f)
    return out


def señales_de(ruta, ventana=1):
    txt = open(ruta, encoding="utf-8", errors="replace").read()
    cuerpo = txt.split("---", 2)[-1] if "---" in txt[:1200] else txt
    fs = frases(cuerpo)
    marcadas = set()
    for i, f in enumerate(fs):
        if RX_NUM.search(f) and (RX_IND.search(f) or RX_ACC.search(f)):
            for j in range(max(0, i - ventana), min(len(fs), i + ventana + 1)):
                marcadas.add(j)
    return [fs[i] for i in sorted(marcadas)], len(cuerpo)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--carpeta", required=True, help="carpeta con los .md")
    ap.add_argument("--desde", default="", help="prefijo mínimo de fecha en el nombre (AAAAMMDD o AAAA-MM-DD)")
    ap.add_argument("--salida", required=True)
    a = ap.parse_args()

    docs, orig, filt = [], 0, 0
    for nombre in sorted(os.listdir(a.carpeta)):
        if not nombre.endswith(".md") or (a.desde and nombre[:len(a.desde)] < a.desde):
            continue
        pasajes, n = señales_de(os.path.join(a.carpeta, nombre))
        if not pasajes:
            continue
        orig += n; filt += sum(len(p) for p in pasajes)
        docs.append({"doc": nombre, "pasajes": pasajes})

    with open(a.salida, "w", encoding="utf-8") as fh:
        json.dump(docs, fh, ensure_ascii=False, indent=1)
    print(f"{len(docs)} documentos · {orig:,} → {filt:,} caracteres "
          f"({filt/orig*100:.0f}% conservado) → {a.salida}")


if __name__ == "__main__":
    main()
