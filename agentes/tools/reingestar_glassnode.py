#!/usr/bin/env python3
"""Re-baja los Week On-Chain que quedaron TRUNCADOS en el KB (los `stubs`).

EL PROBLEMA
-----------
De los 328 artículos archivados, **56 son stubs**: solo tienen la intro y el índice, y cortan justo
donde empieza el análisis. Se reparten en **78% de 2022** (39 de 50) y **26% de 2021** (14 de 52).
2023→2026 está completo.

Duele porque **2022 es el bear market**, el análogo del régimen actual: es justo el periodo del que
más querríamos aprender.

POR QUÉ NO SE ARREGLA SOLO
--------------------------
`run.py` deduplica por slug en `_state.json`: como esos artículos "ya están", no los vuelve a bajar
aunque estén incompletos. Hay que **borrarlos y quitarlos del estado** primero. Eso hace este script.

⚠️ EXPECTATIVA HONESTA
----------------------
Puede que no funcione. Los stubs cortan exactamente donde empieza el cuerpo, lo que sugiere que las
ediciones antiguas están **cerradas a miembros**. Si tras re-bajar siguen siendo pequeños, el texto
no es recuperable por esta vía (y los 67 vídeos de 2022 del canal de YouTube siguen cubriendo el
hueco, aunque con menos precisión numérica).

USO (desde la carpeta btc-cycle-terminal, con el repo DeFi-Tracker clonado en el Mac)
------------------------------------------------------------------------------------
  python3 agentes/tools/reingestar_glassnode.py --kb ~/DeFi-Tracker --dry-run   # mirar sin tocar
  python3 agentes/tools/reingestar_glassnode.py --kb ~/DeFi-Tracker             # hacerlo
"""
import argparse, json, os, shutil, subprocess, sys

UMBRAL = 3000       # bytes: por debajo de esto, el artículo está truncado


def encontrar_stubs(carpeta):
    out = []
    for n in sorted(os.listdir(carpeta)):
        if not n.endswith(".md") or n.startswith("_"):
            continue
        p = os.path.join(carpeta, n)
        t = os.path.getsize(p)
        if t < UMBRAL:
            out.append((n, t))
    return out


def comprobar_dependencias():
    """run.py necesita requests + trafilatura, y trafilatura arrastra lxml_html_clean (que se
    separó de lxml en 2024). Se comprueba ANTES de borrar nada: si falta algo, el script abortaba
    después de haber borrado los stubs y había que restaurar la copia. Mejor fallar pronto."""
    faltan = []
    for mod, paquete in [("requests", "requests"), ("trafilatura", "trafilatura"),
                         ("lxml_html_clean", "lxml_html_clean")]:
        try:
            __import__(mod)
        except ImportError:
            faltan.append(paquete)
    if faltan:
        print("Faltan librerías. Instálalas con:\n")
        print(f"  {sys.executable} -m pip install -U " + " ".join(faltan) + "\n")
        sys.exit(1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kb", required=True, help="ruta al clon del repo DeFi-Tracker")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    if not a.dry_run:
        comprobar_dependencias()

    raiz = os.path.expanduser(a.kb)
    base = os.path.join(raiz, "research", "glassnode-kb")
    arts = os.path.join(base, "articulos")
    estado = os.path.join(arts, "_state.json")
    if not os.path.isdir(arts):
        sys.exit(f"No encuentro {arts}\n¿Seguro que --kb apunta al clon de DeFi-Tracker?")

    stubs = encontrar_stubs(arts)
    total = len([n for n in os.listdir(arts) if n.endswith('.md')])
    print(f"Artículos en el KB: {total} · truncados (<{UMBRAL} bytes): {len(stubs)}")
    if not stubs:
        print("Nada que reparar.")
        return
    por_año = {}
    for n, _ in stubs:
        por_año[n[:4]] = por_año.get(n[:4], 0) + 1
    print("  por año: " + " · ".join(f"{k}: {v}" for k, v in sorted(por_año.items())))

    if a.dry_run:
        print("\n(simulación) se borrarían y se volverían a bajar. Nada tocado.")
        return

    # copia de seguridad: si la re-ingesta falla o trae menos, se puede volver atrás
    resp = os.path.join(base, "_stubs_backup")
    os.makedirs(resp, exist_ok=True)
    for n, _ in stubs:
        shutil.copy2(os.path.join(arts, n), os.path.join(resp, n))
    print(f"\nCopia de seguridad en {resp}")

    # quitar del estado para que run.py NO los considere ya descargados
    slugs = {n[11:-3] for n, _ in stubs}          # AAAA-MM-DD-<slug>.md
    if os.path.exists(estado):
        try:
            st = json.load(open(estado))
            antes = len(st)
            st = {k: v for k, v in st.items() if k not in slugs} if isinstance(st, dict) \
                else [x for x in st if x not in slugs]
            json.dump(st, open(estado, "w"), indent=1)
            print(f"_state.json: {antes} → {len(st)} entradas")
        except Exception as e:
            print(f"AVISO: no pude limpiar _state.json ({e}). Sigo igualmente.")

    for n, _ in stubs:
        os.remove(os.path.join(arts, n))
    print(f"Borrados {len(stubs)} stubs. Lanzando la re-ingesta…\n")

    r = subprocess.run([sys.executable, "run.py"], cwd=base)
    if r.returncode != 0:
        print("\nrun.py terminó con error. Restauro la copia de seguridad para no perder nada.")
        for n, _ in stubs:
            dst = os.path.join(arts, n)
            if not os.path.exists(dst):
                shutil.copy2(os.path.join(resp, n), dst)
        sys.exit(1)

    # ¿mejoró?
    ahora = {n: os.path.getsize(os.path.join(arts, n))
             for n, _ in stubs if os.path.exists(os.path.join(arts, n))}
    recuperados = [n for n, t in ahora.items() if t >= UMBRAL]
    perdidos = [n for n, _ in stubs if n not in ahora]

    print("\n" + "=" * 60)
    print(f"RECUPERADOS (ahora completos): {len(recuperados)} de {len(stubs)}")
    print(f"Siguen truncados: {len(ahora) - len(recuperados)}")
    if perdidos:
        print(f"No volvieron a bajarse: {len(perdidos)} → restaurando de la copia")
        for n in perdidos:
            shutil.copy2(os.path.join(resp, n), os.path.join(arts, n))
    if recuperados:
        print("\nEjemplos recuperados:")
        for n in recuperados[:5]:
            print(f"  {n[:60]}  {ahora[n]//1024} KB")
        print("\nAhora súbelo:")
        print(f"  cd {raiz}")
        print("  git add research/glassnode-kb/")
        print('  git commit -m "KB: recuperar articulos truncados"')
        print("  git push origin main")
    else:
        print("\nNinguno mejoró → las ediciones antiguas están cerradas a miembros.")
        print("El texto no es recuperable por esta vía. Los 67 vídeos de 2022 siguen cubriendo el hueco.")
        print(f"(la copia de seguridad sigue en {resp}, se puede borrar)")


if __name__ == "__main__":
    main()
