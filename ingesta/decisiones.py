#!/usr/bin/env python3
"""decisiones.py — ¿cuántas de tus decisiones de capital tienen su porqué escrito?

POR QUÉ EXISTE
--------------
`frescura.py` vigila que las FUENTES estén al día. Esto vigila lo mismo sobre lo único que
nadie más puede reconstruir: **lo que pensabas tú al pulsar el botón**.

Lo que dicen Cowen o Glassnode está en YouTube y en el KB — si se pierde, se vuelve a bajar.
Tu razonamiento del 3-ago a las 15:48 no está en ningún sitio salvo que lo escribas, y se
evapora en horas. En este repo había 84 meses de Cowen sin un hueco y 1 de cada 10 decisiones
propias registrada en el momento. Esto mide justo eso.

LAS DOS MÉTRICAS, QUE NO SON LA MISMA
-------------------------------------
  COBERTURA          ¿tiene entrada esta decisión?  → se arregla reconstruyendo, hoy mismo
  REGISTRO EN PLAZO  ¿se escribió ANTES de conocer el resultado?  → solo se arregla hacia
                     adelante, decisión a decisión. Es la que mide conducta.

Reconstruir sube la primera y NO la segunda, a propósito. Si una reconstrucción contase como
registro en plazo, el número mediría memoria en vez de disciplina.

CÓMO SABE SI FUE "EN PLAZO"
---------------------------
`api/journal.js` sella cada entrada con `registrado` (hora del servidor, no editable). Si
`registrado` - `date` <= VENTANA_HORAS, cuenta. Una entrada sin `registrado` es anterior al
sello: se cuenta como reconstruida, que es la lectura conservadora y la correcta.

USO
  python3 ingesta/decisiones.py               # informe
  python3 ingesta/decisiones.py --huerfanas   # solo lo que falta por registrar
  python3 ingesta/decisiones.py --json        # para el dashboard

Datos: los lee del repo privado con GH_TOKEN, o de LOCAL_DATA_DIR si está definido.
"""
import argparse, base64, datetime, json, os, sys, urllib.request, urllib.error

REPO_PRIV = os.environ.get("PRIVATE_REPO", "brovira/DeFi-Tracker")
VENTANA_HORAS = 24     # margen para considerar que se escribió "en el momento"
CICLO = "2026-04-02"   # cycle_start de lp_positions.json


def leer(ruta):
    """El JSON de `ruta` dentro del repo privado (o de LOCAL_DATA_DIR)."""
    local = os.environ.get("LOCAL_DATA_DIR")
    if local:
        # LOCAL_DATA_DIR apunta a .../DeFi-Tracker/data, así que se prueba la ruta relativa
        # completa (data/normalized/x.json → normalized/x.json) antes que el nombre suelto.
        for cand in (os.path.join(local, ruta[5:] if ruta.startswith("data/") else ruta),
                     os.path.join(local, os.path.basename(ruta))):
            if os.path.isfile(cand):
                return json.load(open(cand, encoding="utf-8"))
    token = os.environ.get("GH_TOKEN", "").strip()
    if not token:
        sys.exit("ERROR: falta GH_TOKEN (o LOCAL_DATA_DIR) para leer el repo privado.")
    req = urllib.request.Request(
        f"https://api.github.com/repos/{REPO_PRIV}/contents/{ruta}",
        headers={"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json",
                 "User-Agent": "btc-cycle-terminal/decisiones",
                 "X-GitHub-Api-Version": "2022-11-28"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            d = json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        sys.exit(f"ERROR HTTP {e.code} leyendo {ruta}: {e.read().decode('utf-8','replace')[:200]}")
    return json.loads(base64.b64decode(d["content"]).decode("utf-8", "replace"))


def decisiones():
    """Toda decisión de capital de este ciclo: cada apertura y cada cierre, una por una.

    Las de Orca salen de la cadena (verdad dura). Las de cadenas sin lector salen de
    lp_positions.json, marcadas, porque no poder verificarlas no las borra del recuento.
    """
    out = []
    for p in leer("data/normalized/orca_positions.json"):
        if not p.get("isConfirmedPosition"):
            continue
        abre = datetime.datetime.utcfromtimestamp(p["firstSeen"]).strftime("%Y-%m-%d")
        if abre < CICLO:
            continue
        m = p["positionMint"][:8]
        out.append({"id": f"{m}-abre", "fecha": abre, "que": f"abrir LP {m}", "fuente": "cadena"})
        if p.get("closed"):
            cierra = datetime.datetime.utcfromtimestamp(p["lastSeen"]).strftime("%Y-%m-%d")
            out.append({"id": f"{m}-cierra", "fecha": cierra, "que": f"cerrar LP {m}", "fuente": "cadena"})

    for pos in leer("data/lp_positions.json").get("positions", []):
        if str(pos.get("pair", "")).lower().find("orca") >= 0:
            continue                       # ya viene de la cadena, más fiable
        m = str(pos.get("mint", "?"))[:20]
        for campo, verbo in (("opened", "abrir"), ("closed", "cerrar")):
            f = pos.get(campo)
            if campo == "closed" and "cerrada" not in str(pos.get("status", "")):
                continue
            out.append({"id": f"{m}-{verbo}", "fecha": f if f and f != "?" else None,
                        "que": f"{verbo} {m}", "fuente": "declarada"})
    # Operativa que no deja posición en ningún fichero de LP —perps, spot, coberturas—.
    # Se declara en el propio diario, así que la decisión y su registro son la misma cosa:
    # cuenta para el total y se cubre a sí misma. Sin esto, todo lo que no sea un LP de Orca
    # quedaba fuera del recuento, que era un agujero grande.
    conocidas = {d["id"] for d in out}
    for e in leer("data/journal.json").get("entries", []):
        if str(e.get("type", "")).lower() not in ("venta", "compra", "loop"):
            continue
        f = str(e.get("date", ""))[:10]
        if f < CICLO or any(abs_dias(f, d["fecha"]) <= 3 for d in out if d["fecha"]):
            continue                       # ya cubierta por una posición conocida
        out.append({"id": e["id"], "fecha": f, "que": e.get("action", "operativa")[:40],
                    "fuente": "diario"})
    return sorted(out, key=lambda d: (d["fecha"] or "9999"))


def abs_dias(a, b):
    try:
        return abs((datetime.date.fromisoformat(a) - datetime.date.fromisoformat(b)).days)
    except (ValueError, TypeError):
        return 999


def casa(dec, entradas):
    """La entrada del diario que cubre esta decisión, si la hay.

    Se casa por proximidad de fecha (±3 días) porque el diario no guarda el mint: una entrada
    escrita el 3-ago sobre 'cerrar las dos posiciones' cubre las dos decisiones de ese día.
    """
    if not dec["fecha"]:
        return None
    d0 = datetime.date.fromisoformat(dec["fecha"])
    for e in entradas:
        try:
            d1 = datetime.date.fromisoformat(str(e.get("date", ""))[:10])
        except ValueError:
            continue
        if abs((d1 - d0).days) <= 3 and str(e.get("type", "")).lower() in ("lp", "compra", "venta", "loop"):
            return e
    return None


def en_plazo(entrada):
    """¿Se escribió ANTES de conocer el resultado? Sin sello, no cuenta.

    Un sello puesto por algo que no sea `api/journal.js` (p. ej. una sesión de Claude
    escribiendo directa al repo) lleva `registrado_por` y SÍ cuenta —el testigo entonces es
    la marca de tiempo del commit de git, que es de un tercero— pero se contabiliza aparte.
    Si la métrica mezclara los dos orígenes dejaría de ser auditable, que es justo lo que
    hace inútil a un número.
    """
    if not entrada or entrada.get("reconstruido"):
        return False
    reg = entrada.get("registrado")
    if not reg:
        return False
    try:
        r = datetime.datetime.fromisoformat(str(reg).replace("Z", "+00:00"))
        d = datetime.datetime.fromisoformat(str(entrada["date"])[:10]).replace(tzinfo=r.tzinfo)
    except ValueError:
        return False
    return 0 <= (r - d).total_seconds() / 3600 <= VENTANA_HORAS


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--huerfanas", action="store_true", help="solo las decisiones sin entrada")
    ap.add_argument("--json", action="store_true", help="salida para el dashboard")
    a = ap.parse_args()

    entradas = leer("data/journal.json").get("entries", [])
    decs = decisiones()
    filas = []
    for d in decs:
        e = casa(d, entradas)
        filas.append({**d, "entrada": (e or {}).get("id"), "cubierta": bool(e), "en_plazo": en_plazo(e)})

    n = len(filas)
    cub = sum(f["cubierta"] for f in filas)
    plazo = sum(f["en_plazo"] for f in filas)

    if a.json:
        print(json.dumps({"total": n, "cubiertas": cub, "en_plazo": plazo,
                          "cobertura_pct": round(cub / n * 100) if n else 0,
                          "plazo_pct": round(plazo / n * 100) if n else 0,
                          "huerfanas": [f["que"] for f in filas if not f["cubierta"]],
                          "generado": datetime.date.today().isoformat()}, ensure_ascii=False))
        return 0

    if a.huerfanas:
        h = [f for f in filas if not f["cubierta"]]
        print(f"{len(h)} decisión(es) sin entrada en el diario:" if h else "Todas las decisiones tienen entrada.")
        for f in h:
            print(f"  · {f['fecha'] or '(sin fecha)'}  {f['que']}  [{f['fuente']}]")
        return 1 if h else 0

    print(f"DECISIONES DE CAPITAL DEL CICLO (desde {CICLO})\n")
    print(f"  {'fecha':11s} {'decisión':28s} {'fuente':10s} {'entrada':8s} {'en plazo':9s}")
    print("  " + "-" * 70)
    for f in filas:
        print(f"  {(f['fecha'] or '?'):11s} {f['que'][:28]:28s} {f['fuente']:10s} "
              f"{'sí' if f['cubierta'] else 'NO':8s} {'sí' if f['en_plazo'] else '—':9s}")

    agente = sum(1 for f in filas if f["en_plazo"]
                 and (casa(f, entradas) or {}).get("registrado_por"))
    print(f"\n  COBERTURA          {cub}/{n}  ({cub/n*100:.0f}%)   ← se arregla reconstruyendo")
    print(f"  REGISTRO EN PLAZO  {plazo}/{n}  ({plazo/n*100:.0f}%)   ← solo se arregla hacia adelante")
    if agente:
        print(f"                     de esos, {agente} con sello de agente y no del servidor "
              f"(testigo: el commit de git)")
    print()
    if plazo < n:
        print("  El objetivo es 10 de 10 en la SEGUNDA. La primera solo dice que no se ha perdido")
        print("  el rastro; la segunda dice que el porqué se escribió sin saber el resultado.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
