#!/usr/bin/env python3
"""test_fiabilidad.py — que el clasificador de fiabilidad no vuelva a mentir en silencio.

POR QUÉ EXISTE
--------------
`fiabilidad_de()` decide con qué nota del track record se muestra cada llamada del WoC
en el dashboard. Si clasifica mal, el número que usas para ponderar una recomendación
está mal atribuido — y no hay nada que se ponga rojo, porque devolver una etiqueta
equivocada es indistinguible de devolver la correcta.

Ya ha fallado dos veces por lo mismo: una palabra corta del vocabulario de derivados que
también vive en el vocabulario on-chain.

  1. `\\biv\\b` hacía match dentro de "decisIVo"  → arreglado con límites de palabra.
  2. `\\bbasis\\b` hacía match dentro de "STH Cost Basis" → colgaba el 3/3 de
     backwardation a las llamadas de nivel on-chain, que son 8/10. Detectado el
     17-ago-2026 sobre la llamada real del WoC del 12-ago.

Los casos de abajo son llamadas REALES del corpus, no inventadas.

USO
  python ingesta/test_fiabilidad.py     # sale 1 si alguna clasificación es incorrecta
"""
import importlib.util
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_spec = importlib.util.spec_from_file_location("sync_woc", os.path.join(RAIZ, "ingesta", "sync_woc.py"))
_sw = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_sw)

# (texto de la llamada, fragmento que DEBE aparecer en la etiqueta, por qué)
CASOS = [
    ("Reclaim sostenido de $68,7k (STH Cost Basis) CON volumen en aumento y ETF inflows detrás",
     "nivel on-chain",
     "cost basis es un NIVEL on-chain (8/10), no el basis de futuros (3/3)"),

    ("Pérdida del estante de $63k con vuelta de entradas a exchanges",
     "nivel on-chain",
     "estante/shelf es nivel on-chain"),

    ("El realized price marca el suelo estructural del ciclo",
     "nivel on-chain",
     "realized price es nivel on-chain"),

    ("Backwardation en la curva de futuros -> squeeze al alza inminente",
     "backwardation",
     "backwardation de verdad SÍ es el patrón 3/3"),

    ("El basis de CME comprimido pero positivo, el carry se estrecha",
     "backwardation",
     "el basis de futuros, sin 'cost' delante, sí es el patrón de derivados"),

    ("Funding fuertemente positivo con OI en máximos: longs apiñados, riesgo de flush",
     "posicionamiento/leverage",
     "funding + OI extremos es el patrón fuerte 8/10"),

    ("IV en mínimos de meses, vol barata -> expansión inminente",
     "IV baja",
     "compresión de vol es el patrón débil 1/4"),

    ("Un movimiento decisivo por encima de la resistencia confirmaría el giro",
     "sin clasificar",
     "'decisIVo' NO debe disparar el patrón de IV (regresión de 2026)"),
]


def main():
    fallos = []
    for texto, esperado, motivo in CASOS:
        obtenido = _sw.fiabilidad_de(texto)
        ok = esperado.lower() in obtenido.lower()
        print(f"{'  ok  ' if ok else ' FALLO'} │ {texto[:58]:<58} → {obtenido[:46]}")
        if not ok:
            fallos.append((texto, esperado, obtenido, motivo))

    print()
    if not fallos:
        print(f"{len(CASOS)} casos correctos.")
        return 0

    for texto, esperado, obtenido, motivo in fallos:
        print(f"FALLO: {texto[:70]}")
        print(f"  esperaba una etiqueta con : {esperado}")
        print(f"  obtuve                    : {obtenido}")
        print(f"  por qué importa           : {motivo}\n")
    print("El dashboard mostraría la nota del track record equivocada. Revisa FIABILIDAD "
          "en ingesta/sync_woc.py — el orden importa: de más específico a más genérico.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
