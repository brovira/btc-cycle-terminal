#!/usr/bin/env python3
"""Extractor de datos de Checkonchain (charts públicos, gratis) — on-chain, derivados, ETFs, treasury.

CONTEXTO / POR QUÉ
------------------
checkonchain.com publica GRATIS cientos de gráficos estilo Glassnode (on-chain, técnico, derivados,
ETFs, treasury companies). Nuestras fuentes actuales están limitadas:
  · BGeometrics: la escalera de cost basis completa, pero solo **4 años en ventana móvil**.
  · Coin Metrics: histórico largo, pero solo métricas agregadas (realized price derivado, MVRV).
Si Checkonchain expone sus series, cubre los dos huecos a la vez (cohortes + histórico largo).

CÓMO FUNCIONA SU SITIO (descubierto por sondeo, 30-jul-2026)
-----------------------------------------------------------
  1. `charts.checkonchain.com/<ruta>.html` → **cáscara** de ~860 bytes (título + favicon + iframe).
  2. La cáscara apunta a `charts-cdn.checkonchain.com/<misma ruta>.html` ← **aquí está el chart real**.
  3. Ese HTML es un export de Plotly: los datos van embebidos en `Plotly.newPlot("id", [traces], ...)`.
Extraer = localizar ese array de traces y leer los pares x/y de cada serie.

USO PERSONAL. No redistribuir sus series. Se respeta un retardo entre peticiones.

Uso:
  python ingesta/checkonchain.py --catalogo              # lista todos los charts por categoría
  python ingesta/checkonchain.py --inspeccionar RUTA     # diagnóstico crudo de un chart (formato)
  python ingesta/checkonchain.py --extraer RUTA          # extrae las series a JSON
  python ingesta/checkonchain.py --auto                  # catálogo + inspección + extracción de prueba
"""
import argparse, json, os, re, sys, time, urllib.request, urllib.error

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTDIR = os.path.join(ROOT, "data", "checkonchain")
WEB = "https://charts.checkonchain.com/"
CDN = "https://charts-cdn.checkonchain.com/"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
PAUSA = 1.2   # segundos entre peticiones (educado con su servidor)


def get(url, timeout=45, binario=False):
    req = urllib.request.Request(url, headers={
        "User-Agent": UA, "Accept": "text/html,application/json,*/*",
        "Accept-Language": "en-US,en;q=0.9", "Referer": WEB})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            raw = r.read()
            return r.status, raw if binario else raw.decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        try: body = e.read().decode("utf-8", "replace")[:200]
        except Exception: body = ""
        return e.code, body
    except Exception as e:
        return 0, f"__EXC__ {e}"


# ───────────────────────────── catálogo ─────────────────────────────
def catalogo():
    st, raw = get(WEB)
    if st != 200:
        print(f"índice HTTP {st}", file=sys.stderr); return {}
    rutas = sorted(set(re.findall(r'href="([^"]+\.html)"', raw)))
    rutas = [r.lstrip("./") for r in rutas if not r.startswith("http")]
    porcat = {}
    for r in rutas:
        partes = r.split("/")
        cat = partes[1] if len(partes) > 2 else (partes[0] if partes else "?")
        porcat.setdefault(cat, []).append(r)
    return porcat


def ver_robots():
    st, raw = get("https://charts.checkonchain.com/robots.txt")
    return {"http": st, "contenido": raw[:400] if st == 200 else raw[:120]}


# ─────────────────── extracción del JSON de Plotly ───────────────────
def _json_balanceado(txt, i):
    """Devuelve el substring JSON que empieza en txt[i] ('[' o '{') respetando anidamiento y strings."""
    if i >= len(txt) or txt[i] not in "[{":
        return None
    apertura, cierre = txt[i], {"[": "]", "{": "}"}[txt[i]]
    prof, en_str, esc = 0, False, False
    for j in range(i, len(txt)):
        c = txt[j]
        if en_str:
            if esc:      esc = False
            elif c == "\\": esc = True
            elif c == '"':  en_str = False
            continue
        if c == '"':      en_str = True
        elif c == apertura: prof += 1
        elif c == cierre:
            prof -= 1
            if prof == 0:
                return txt[i:j + 1]
    return None


def extraer_traces(html):
    """Localiza el array de traces de Plotly. Prueba varias formas de export."""
    intentos = []
    # A) Plotly.newPlot("id", [traces], {layout}, ...)
    for m in re.finditer(r'Plotly\.(?:newPlot|react)\s*\(\s*(?:"[^"]*"|\'[^\']*\'|[\w$]+)\s*,\s*', html):
        s = _json_balanceado(html, m.end())
        if s: intentos.append(("Plotly.newPlot", s))
    # B) <script type="application/json">{"data":[...]}</script>  (plotly.js moderno / dash)
    for m in re.finditer(r'<script[^>]+type="application/json"[^>]*>(.*?)</script>', html, re.S):
        intentos.append(("script/json", m.group(1).strip()))
    # C) "data": [ ... ] dentro de una figura serializada
    for m in re.finditer(r'"data"\s*:\s*', html):
        s = _json_balanceado(html, m.end())
        if s and s.startswith("["): intentos.append(('"data":', s))

    for etiqueta, blob in intentos:
        try:
            d = json.loads(blob)
        except Exception:
            continue
        if isinstance(d, dict):
            d = d.get("data") or d.get("figure", {}).get("data")
        if isinstance(d, list) and d and isinstance(d[0], dict) and ("x" in d[0] or "y" in d[0]):
            return etiqueta, d
    return None, None


def _a_fecha(x):
    """Plotly usa fechas ISO ('2018-01-01', '2018-01-01T00:00:00') o epoch numérico (s o ms)."""
    if isinstance(x, str):
        f = x[:10]
        return f if re.match(r"^\d{4}-\d{2}-\d{2}$", f) else None
    if isinstance(x, (int, float)):
        import datetime as dt
        v = float(x)
        # heurística: >1e11 = milisegundos · >1e9 = segundos · si no, no es una fecha
        seg = v / 1000.0 if v > 1e11 else v
        if not (9.4e8 < seg < 4e9):      # ~2000-01-01 … ~2096
            return None
        try:
            return dt.datetime.utcfromtimestamp(seg).strftime("%Y-%m-%d")
        except (OverflowError, OSError, ValueError):
            return None
    return None


def traces_a_series(traces):
    """Convierte los traces de Plotly en {nombre: [{date, value}]}."""
    out = {}
    for i, t in enumerate(traces):
        if not isinstance(t, dict):
            continue
        xs, ys = t.get("x"), t.get("y")
        if not isinstance(xs, list) or not isinstance(ys, list) or not xs or not ys:
            continue
        nombre = t.get("name") or t.get("legendgroup") or f"trace_{i}"
        serie = []
        for x, y in zip(xs, ys):
            if y is None:
                continue
            fecha = _a_fecha(x)
            if not fecha:
                continue
            try:
                serie.append({"date": fecha, "value": float(y)})
            except (TypeError, ValueError):
                continue
        if serie:
            # si el nombre se repite (traces partidos), acumular en vez de sobrescribir
            if nombre in out:
                out[nombre].extend(serie)
                out[nombre].sort(key=lambda p: p["date"])
            else:
                out[nombre] = serie
    return out


def bajar_chart(ruta):
    """Baja el chart desde el CDN (con la web pública como respaldo)."""
    ruta = ruta.lstrip("/")
    for base in (CDN, WEB):
        st, html = get(base + ruta)
        if st == 200 and len(html) > 2000:      # la cáscara son ~860 bytes
            return base + ruta, html
        time.sleep(PAUSA)
    return None, None


def inspeccionar(ruta):
    """Diagnóstico: qué formato tiene el chart. Guarda una muestra para poder afinar el parser."""
    url, html = bajar_chart(ruta)
    r = {"ruta": ruta, "url": url, "bytes": len(html) if html else 0}
    if not html:
        r["error"] = "no se pudo bajar (o solo devolvió la cáscara)"
        return r
    r["tiene_plotly"] = "Plotly" in html
    r["marcadores"] = {k: html.count(k) for k in
                       ["Plotly.newPlot", "Plotly.react", "application/json", '"data"', '"x":', '"y":']}
    etiqueta, traces = extraer_traces(html)
    r["estrategia_que_funciono"] = etiqueta
    if traces:
        series = traces_a_series(traces)
        r["n_traces"] = len(traces)
        r["series"] = {k: {"puntos": len(v), "desde": v[0]["date"], "hasta": v[-1]["date"]}
                       for k, v in series.items()}
    else:
        os.makedirs(OUTDIR, exist_ok=True)
        p = os.path.join(OUTDIR, "_muestra_html.txt")
        with open(p, "w") as f:
            f.write(html[:20000])
        r["muestra_guardada"] = "data/checkonchain/_muestra_html.txt (primeros 20k para afinar el parser)"
    return r


def extraer(ruta):
    url, html = bajar_chart(ruta)
    if not html:
        print(f"  no se pudo bajar {ruta}", file=sys.stderr); return None
    etiqueta, traces = extraer_traces(html)
    if not traces:
        print(f"  sin traces reconocibles en {ruta}", file=sys.stderr); return None
    series = traces_a_series(traces)
    if not series:
        print(f"  traces sin pares fecha/valor en {ruta}", file=sys.stderr); return None
    os.makedirs(OUTDIR, exist_ok=True)
    nombre = re.sub(r"[^a-z0-9]+", "_", ruta.lower().replace(".html", "")).strip("_")[:90]
    dest = os.path.join(OUTDIR, f"{nombre}.json")
    with open(dest, "w") as f:
        json.dump({"ruta": ruta, "url": url, "estrategia": etiqueta,
                   "series": {k: v for k, v in series.items()}}, f, indent=1)
    print(f"  → data/checkonchain/{nombre}.json  ({len(series)} series, "
          f"{sum(len(v) for v in series.values())} puntos)")
    for k, v in list(series.items())[:6]:
        print(f"      · {k[:52]:54s} {len(v):5d} pts  {v[0]['date']} → {v[-1]['date']}")
    return series


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--catalogo", action="store_true")
    ap.add_argument("--inspeccionar", default="")
    ap.add_argument("--extraer", default="")
    ap.add_argument("--auto", action="store_true", help="catálogo + inspección + extracción de prueba")
    a = ap.parse_args()

    informe = {}
    if a.catalogo or a.auto:
        print("=" * 72, "\nROBOTS.TXT\n", "=" * 72)
        rb = ver_robots(); informe["robots"] = rb
        print(json.dumps(rb, indent=1, ensure_ascii=False)[:500])

        print("\n" + "=" * 72, "\nCATÁLOGO\n", "=" * 72)
        cat = catalogo(); informe["catalogo"] = cat
        print(f"categorías: {len(cat)} · charts: {sum(len(v) for v in cat.values())}\n")
        for c, rs in sorted(cat.items()):
            print(f"  {c:22s} {len(rs):4d}  ej: {rs[0][:70] if rs else ''}")

    objetivos = []
    if a.inspeccionar: objetivos = [a.inspeccionar]
    elif a.auto:
        cat = informe.get("catalogo") or catalogo()
        todas = [r for rs in cat.values() for r in rs]
        # priorizar lo que nos falta: cost basis de cohortes, realized, ETF, derivados
        pref = [r for r in todas if re.search(r"realis|realiz|cost.?basis|sth|short.?term|true.?market", r, re.I)]
        objetivos = (pref[:2] or todas[:1])
        if any("etf" in r.lower() for r in todas):
            objetivos.append(next(r for r in todas if "etf" in r.lower()))

    if objetivos:
        print("\n" + "=" * 72, "\nINSPECCIÓN\n", "=" * 72)
        informe["inspeccion"] = []
        for ruta in objetivos:
            print(f"\n→ {ruta}")
            r = inspeccionar(ruta); informe["inspeccion"].append(r)
            print(json.dumps(r, indent=1, ensure_ascii=False)[:1500])
            time.sleep(PAUSA)

    if a.extraer:
        print("\n" + "=" * 72, "\nEXTRACCIÓN\n", "=" * 72)
        extraer(a.extraer)
    elif a.auto and informe.get("inspeccion"):
        ok = next((r for r in informe["inspeccion"] if r.get("series")), None)
        if ok:
            print("\n" + "=" * 72, "\nEXTRACCIÓN DE PRUEBA\n", "=" * 72)
            extraer(ok["ruta"])

    if informe:
        os.makedirs(OUTDIR, exist_ok=True)
        with open(os.path.join(OUTDIR, "_informe.json"), "w") as f:
            json.dump(informe, f, indent=2, ensure_ascii=False)
        print("\nInforme en data/checkonchain/_informe.json")


if __name__ == "__main__":
    main()
