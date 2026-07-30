#!/usr/bin/env python3
"""Frecuencia de uso de cada indicador de Glassnode por año, sobre el corpus completo.

Cuenta ARTICULOS que mencionan cada indicador (no menciones totales) para no
inflar por repeticion dentro de un mismo texto. Solo cuenta articulos COMPLETOS
(>3KB) para que los stubs de 2021-22 no falseen a la baja.
"""
import glob, os, re, json
from collections import defaultdict

ART = "/workspace/defi-tracker/research/glassnode-kb/articulos"

# nombre -> regex (case-insensitive). Variantes reales vistas en el corpus.
IND = {
    # --- escalera de cost basis (modelos de nivel) ---
    "Realized Price":            r"realized price|realised price",
    "True Market Mean":          r"true market mean",
    "Active Investor Price":     r"active investor.{0,12}price|active realized price|active realised price",
    "STH Cost Basis":            r"short[- ]term holder cost basis|sth cost basis|short[- ]term holder.{0,15}cost basis",
    "LTH Cost Basis":            r"long[- ]term holder cost basis|lth cost basis",
    "URPD / Cost Basis Distr.":  r"\burpd\b|utxo realized price distribution|cost basis distribution|cost-basis distribution",
    "Supply Quantiles (0.75/85/95)": r"supply quantile|quantile cost basis|0\.(75|85|95) quantile",
    "Air gap":                   r"air.?gap|air pocket",
    "Delta Price / Investor Price": r"delta price|investor price",
    "Thermocap":                 r"thermocap|thermo cap",
    "Mayer Multiple":            r"mayer multiple",
    "Medias móviles (200D/200W/111D)": r"200d[- ]?ma|200 ?day moving|200w[- ]?ma|200 ?week moving|111d|111 ?day",

    # --- osciladores de valoración / rentabilidad ---
    "MVRV":                      r"\bmvrv\b",
    "MVRV Z-Score":              r"mvrv z[- ]?score",
    "STH-MVRV":                  r"sth[- ]mvrv|short[- ]term holder mvrv",
    "LTH-MVRV":                  r"lth[- ]mvrv|long[- ]term holder mvrv",
    "SOPR":                      r"\bsopr\b",
    "STH-SOPR":                  r"sth[- ]sopr|short[- ]term holder sopr",
    "aSOPR (adjusted)":          r"asopr|adjusted sopr",
    "NUPL":                      r"\bnupl\b|net unrealized profit|net unrealised profit",
    "% Supply in Profit":        r"supply in profit|supply in loss|percent.{0,10}profit",
    "Realized P/L Ratio":        r"realized profit/loss ratio|realised profit/loss ratio|realized p/?l ratio|profit/loss ratio",
    "Realized Profit/Loss ($)":  r"realized profit|realised profit|realized loss|realised loss",
    "AVIV Ratio":                r"\baviv\b",
    "Relative Unrealized Loss":  r"relative unrealized|relative unrealised",

    # --- comportamiento / cohortes ---
    "LTH/STH Supply":            r"long[- ]term holder supply|short[- ]term holder supply|lth supply|sth supply",
    "Accumulation Trend Score":  r"accumulation trend score",
    "Sell-Side Risk Ratio":      r"sell[- ]side risk ratio",
    "Liveliness":                r"liveliness",
    "CDD / Coin Days Destroyed": r"coin days destroyed|\bcdd\b",
    "Dormancy / ASOL":           r"dormancy|\basol\b",
    "HODL Waves":                r"hodl wave|rhodl|realized cap hodl",
    "Reserve Risk":              r"reserve risk",
    "Illiquid Supply":           r"illiquid supply|liquid supply",
    "Hodler Net Position Change":r"hodler net position|net position change",

    # --- flujo de capital ---
    "Realized Cap":              r"realized cap|realised cap",
    "Exchange flows/balances":   r"exchange (in|out)flow|exchange balance|exchange net position|netflow",
    "ETF flows":                 r"\betf\b.{0,20}(flow|inflow|outflow)|spot etf",
    "Stablecoin / SSR":          r"stablecoin supply ratio|\bssr\b|stablecoin",
    "Spot CVD":                  r"\bcvd\b|cumulative volume delta",

    # --- red / minería ---
    "Active Addresses/Entities": r"active address|active entit",
    "Miner metrics":             r"puell multiple|hash ribbon|miner (net position|revenue|capitulation)",
    "NVT":                       r"\bnvt\b",

    # --- derivados (para ver el peso relativo, no es el foco) ---
    "Funding rate":              r"funding rate",
    "Open Interest":             r"open interest",
    "25d Skew":                  r"25[- ]?delta skew|25d skew",
    "IV / DVOL":                 r"\bdvol\b|implied volatility",
    "Max Pain":                  r"max pain",
    "Dealer Gamma / GEX":        r"dealer gamma|\bgex\b|short gamma|long gamma",

    # --- índices propietarios (para probar la tesis de que murieron) ---
    "GNI / Market Compass":      r"glassnode network index|\bgni\b|market compass",
    "Altseason Indicator":       r"altseason indicator",
}

rx = {k: re.compile(v, re.I) for k, v in IND.items()}
per_year = defaultdict(lambda: defaultdict(int))
arts_year = defaultdict(int)

for f in sorted(glob.glob(f"{ART}/*.md")):
    if os.path.getsize(f) < 3000:      # saltar stubs
        continue
    year = os.path.basename(f)[:4]
    arts_year[year] += 1
    txt = open(f, encoding="utf-8", errors="replace").read()
    for k, r in rx.items():
        if r.search(txt):
            per_year[k][year] += 1

years = sorted(arts_year)
print("Artículos COMPLETOS por año:", {y: arts_year[y] for y in years})
print()
# % de artículos del año que mencionan el indicador
rows = []
for k in IND:
    tot = sum(per_year[k].values())
    recent = sum(per_year[k].get(y, 0) for y in ("2025", "2026"))
    recent_n = arts_year.get("2025", 0) + arts_year.get("2026", 0)
    rows.append((k, tot, 100 * recent // recent_n if recent_n else 0,
                 [100 * per_year[k].get(y, 0) // arts_year[y] for y in years]))
rows.sort(key=lambda r: -r[2])   # ordenar por vigencia reciente

hdr = "indicador".ljust(32) + "tot  " + "vig%  " + "  ".join(y[2:] for y in years)
print(hdr); print("-" * len(hdr))
for k, tot, vig, pcts in rows:
    print(k.ljust(32) + f"{tot:3d}  {vig:4d}  " + "  ".join(f"{p:2d}" for p in pcts))
json.dump({k: dict(v) for k, v in per_year.items()},
          open("/tmp/claude-0/-home-user-belrogam/609fb195-25dd-5a0e-8efc-4875d4b45678/scratchpad/freq.json", "w"), indent=1)
