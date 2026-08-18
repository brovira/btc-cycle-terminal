#!/usr/bin/env python3
"""N1 — ¿el STH cost basis es techo en bear y suelo en bull? (backtest de caracterización)

QUÉ AFIRMA EL FRAMEWORK
-----------------------
`framework_direccion.md §B` recoge la asimetría que Glassnode repite: el STH cost basis es
"soporte en tendencia alcista, RESISTENCIA en bajista". Es la pieza sobre la que se apoya casi
todo lo de rangos de LP, así que es el primer backtest de `backtest_repertorio.md` (N1).

CÓMO SE PRUEBA
--------------
Dos preguntas distintas, porque no son la misma:

  1) COMO NIVEL — cuando el precio cruza el STH CB, ¿aguanta el cruce o lo rechazan?
     Es la afirmación literal del framework.
  2) COMO BRÚJULA — sin mirar si el nivel aguanta: ¿de qué lado está el precio, y qué ha
     rentado históricamente cada lado?

DATOS
-----
- precio: reconstruido como MVRV × realized price (BGeometrics, `data/onchain/*_largo.json`).
  NO es el cierre spot; es una serie derivada. Muy cercana, no idéntica.
- STH Cost Basis y True Mean Price: checkonchain (`data/checkonchain/pricing__*.json`).
- Solape: 2011-01-01 → 2026-08-16, 5.707 días, 4 ciclos completos.

DECISIONES DE DISEÑO (son mías, no de Glassnode — cambiarlas mueve los números)
------------------------------------------------------------------------------
- Régimen bull/bear = precio por encima/debajo de la True Market Mean. Glassnode la describe
  como "the dividing line between bear and bull market regimes", pero no consta que la usen
  exactamente así para etiquetar régimen.
- "Cruce" = cambio de lado respecto al STH CB, con 14 días de veda entre cruces (si no, una
  misma pelea alrededor del nivel cuenta como diez eventos).
- "Aguantó" = 8 semanas después el precio sigue del lado al que cruzó.

Uso:  python3 agentes/glassnode_tactico/backtests/n1_sth_cost_basis.py
"""
import json, os, statistics as st

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
VEDA, HORIZONTE = 14, 56


def _bgeo(nombre):
    d = json.load(open(os.path.join(ROOT, "data", "onchain", nombre + ".json")))
    return {p["date"]: p["value"] for p in d["series"] if p["value"] is not None}


def _checkonchain(clave):
    d = json.load(open(os.path.join(ROOT, "data", "checkonchain",
                                    "pricing__pricing_costbasisoriginals.json")))
    return {f: v for f, v in zip(d["fechas"], d["series"][clave]) if v is not None and v > 0}


def cargar():
    mvrv, rp = _bgeo("mvrv_largo"), _bgeo("realized_price_largo")
    precio = {d: mvrv[d] * rp[d] for d in mvrv if d in rp}
    sth, tmm = _checkonchain("STH Cost Basis"), _checkonchain("True Mean Price")
    f = sorted(set(precio) & set(sth) & set(tmm))
    return f, [precio[d] for d in f], [sth[d] for d in f], [tmm[d] for d in f]


def main():
    F, P, S, T = cargar()
    n = len(F)
    ret = lambda i, d: (P[min(i + d, n - 1)] / P[i] - 1) * 100
    lado_arriba = lambda i, d: P[min(i + d, n - 1)] > S[min(i + d, n - 1)]

    print(f"N1 · STH cost basis · {F[0]} → {F[-1]} · {n:,} días\n")

    # ---------- 1) COMO NIVEL ----------
    eventos, ult = [], -99
    for i in range(1, n):
        if (P[i - 1] > S[i - 1]) == (P[i] > S[i]) or i - ult < VEDA:
            continue
        ult = i
        eventos.append({"i": i, "fecha": F[i],
                        "dir": "rompe_arriba" if P[i] > S[i] else "pierde_abajo",
                        "regimen": "bull" if P[i] > T[i] else "bear"})

    print(f"1) COMO NIVEL — {len(eventos)} cruces\n")
    print(f"   {'régimen':8s} {'dirección':13s} {'n':>3s} {'aguanta':>8s} {'rechaza':>8s} {'mediana +8sem':>14s}")
    print("   " + "-" * 60)
    for reg in ("bear", "bull"):
        for dr in ("rompe_arriba", "pierde_abajo"):
            sub = [e for e in eventos if e["regimen"] == reg and e["dir"] == dr]
            if not sub:
                continue
            ok = sum(lado_arriba(e["i"], HORIZONTE) == (e["dir"] == "rompe_arriba") for e in sub)
            med = st.median([ret(e["i"], HORIZONTE) for e in sub])
            print(f"   {reg:8s} {dr:13s} {len(sub):>3d} {ok:>8d} {len(sub)-ok:>8d} {med:>+13.1f}%")

    # ---------- 2) COMO BRÚJULA ----------
    print(f"\n2) COMO BRÚJULA — ¿de qué lado está el precio?\n")
    print(f"   {'régimen':8s} {'lado':8s} {'n días':>7s} {'+4 sem':>9s} {'+8 sem':>9s} {'% al alza':>10s}")
    print("   " + "-" * 60)
    for reg, rc in (("todo", lambda i: True), ("bull", lambda i: P[i] > T[i]), ("bear", lambda i: P[i] <= T[i])):
        for lado, lc in (("arriba", lambda i: P[i] > S[i]), ("abajo", lambda i: P[i] <= S[i])):
            idx = [i for i in range(n - HORIZONTE - 1) if rc(i) and lc(i)]
            if len(idx) < 40:
                continue
            m4 = st.median([ret(i, 28) for i in idx])
            m8 = st.median([ret(i, HORIZONTE) for i in idx])
            alza = sum(ret(i, HORIZONTE) > 0 for i in idx) / len(idx) * 100
            print(f"   {reg:8s} {lado:8s} {len(idx):>7,d} {m4:>+8.1f}% {m8:>+8.1f}% {alza:>9.0f}%")

    h = n - 1
    print(f"\nHOY ({F[h]}): precio {P[h]:,.0f} · STH CB {S[h]:,.0f} ({(P[h]/S[h]-1)*+100:+.1f}%) "
          f"· TMM {T[h]:,.0f} ({(P[h]/T[h]-1)*100:+.1f}%)")
    print(f"   casilla: {'bull' if P[h]>T[h] else 'bear'} · {'arriba' if P[h]>S[h] else 'abajo'} del STH CB")


if __name__ == "__main__":
    main()
