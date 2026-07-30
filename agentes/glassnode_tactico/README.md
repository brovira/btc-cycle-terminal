# Glassnode TÁCTICO — dirección, niveles y gestión activa de capital

Material del agente `glassnode_tactico`. Cubre la **operativa a semanas–meses** (LP concentrado + algún
trade direccional), que es la capa distinta del sesgo de ciclo (`lmec`, `cowen`) y complementaria al
posicionamiento/vol (`derivados_glassnode`).

```
on-chain (aquí)  → el DÓNDE y la DIRECCIÓN   ┐
                                             ├── juntos = la decisión táctica
derivados        → el COMBUSTIBLE y el MOMENTO ┘
```

## Archivos

| Archivo | Qué es |
|---|---|
| `framework_direccion.md` | El marco destilado: escalera de cost basis, 4 regímenes, asimetría soporte/resistencia, osciladores con umbrales literales, guardarraíles, evolución del método |
| `backtest_repertorio.md` | Qué se puede backtestear con datos gratis, en 3 tiers, con el orden de ataque |

## De dónde sale

Barrido de los **328 Week On-Chain** archivados (2019→jul-2026) en `research/glassnode-kb/articulos/` del
repo **privado DeFi-Tracker**, leídos íntegros por 12 extractores en paralelo (jul-2026). Los informes
crudos por lote no se versionan aquí (son intermedios); lo que queda es la destilación.

## ✅ El hueco de 2022, CUBIERTO por los vídeos (30-jul-2026)

Se bajaron **214 transcripts** del canal oficial (`yt-transcripts/`, 2021-06 → 2026-06, todos con
fecha). Reparto por año: 2021 (37) · **2022 (67)** · 2023 (62) · 2024 (18) · 2025 (6) · 2026 (24).

**Lo importante:** esos 67 vídeos de 2022 son **las mismas ediciones del Week On-Chain** en formato
vídeo (`the-week-on-chain-…-week-N-2022`) — justo donde los artículos están 78% truncados. Las dos
fuentes se **complementan**:

| Periodo | Artículos | Vídeos |
|---|---|---|
| 2021 | 26% stubs | 37 vídeos |
| **2022** | **78% stubs** ❌ | **67 vídeos** ✅ |
| 2023 | completo ✅ | 62 vídeos |
| 2024-25 | completo ✅ | pocos (24) |
| 2026 | completo ✅ | 24 vídeos |

⚠️ **Pero pesan menos:** son auto-subs (speech-to-text) con erratas y sin las cifras de los gráficos.
El agente debe marcarlos como **fuente VÍDEO** al citarlos. Sirven para el *razonamiento y el marco*,
no como fuente de un número exacto.

Cobertura de indicadores en los vídeos: cost basis (113) · realized price (76) · MVRV (58) ·
SOPR (17) · true market mean (9).

## ⚠️ Hueco original: el corpus de 2022 (ya mitigado, ver arriba)

**56 de 328 artículos son stubs** (solo intro; el cuerpo no se archivó): **78% de 2022** y **26% de 2021**.
2023→2026 está completo. El método actual (la escalera de cost basis) es de 2023+, así que el framework es
válido — pero el **bear de 2022**, que es el análogo del régimen actual, está mal cubierto.

### Re-ingesta de 2022 — ❌ PROBADA Y DESCARTADA (30-jul-2026)

**Resultado: 0 recuperados de 56.** Se ejecutó `agentes/tools/reingestar_glassnode.py` en local
(el sandbox no tiene salida a glassnode.com): borró los stubs, los quitó de `_state.json` y
relanzó `run.py`. Volvieron a bajarse **exactamente igual de truncados**.

**Conclusión firme: Glassnode cerró las ediciones antiguas a miembros.** El texto de 2020-2022
no es recuperable por la Content API pública. **No volver a intentarlo por esta vía.**

Lo que queda como cobertura de ese periodo: los **67 vídeos de 2022** del canal (mismas
ediciones del WoC), con la salvedad de que son auto-subs — sirven para el razonamiento,
no para citar cifras exactas.

<details><summary>Cómo se hizo (por si algún día cambia el acceso)</summary>


`research/glassnode-kb/run.py` (en DeFi-Tracker) **no necesita API key**, solo salida a
`research.glassnode.com`. Desde el sandbox de Claude Code el proxy lo bloquea (403 en CONNECT), así que
hay que correrlo **en local** o vía la GitHub Action del repo privado.

Como `run.py` deduplica por slug en `_state.json`, para **re-bajar** los stubs hay que borrarlos primero:

```bash
cd research/glassnode-kb/articulos
# 1. localizar los stubs (<3KB) y quitarlos del estado
python3 - <<'EOF'
import json, os, glob
stubs = [f for f in glob.glob('*.md') if os.path.getsize(f) < 3000]
st = json.load(open('_state.json'))
slugs = {s[11:-3] for s in stubs}          # AAAA-MM-DD-<slug>.md
if isinstance(st, dict): st = {k: v for k, v in st.items() if k not in slugs}
else:                    st = [s for s in st if s not in slugs]
json.dump(st, open('_state.json', 'w'), indent=1)
for f in stubs: os.remove(f)
print('quitados', len(stubs))
EOF
# 2. re-ingestar
cd .. && python run.py
```

</details>

## Archivos (actualizado 30-jul-2026)

| Archivo | Qué es |
|---|---|
| `framework_direccion.md` | El marco: escalera de cost basis, 4 regímenes, asimetría, osciladores con umbrales literales, guardarraíles |
| `catalogo_indicadores.md` | Qué indicadores **deciden** hoy (medido sobre sus conclusiones 2025-26) vs cuáles murieron |
| `backtest_repertorio.md` | Qué se puede backtestear, en tiers, por disponibilidad de datos |
| **`especificacion_backtest.md`** | **La traducción a código**: cada regla → serie exacta + archivo, decisiones de diseño abiertas, y qué NO se puede testear |
| `extraccion_woc/informe_g*.md` | Los 12 informes crudos del barrido (2019→2026), con las ~100 reglas literales y sus citas |
| `extraccion_woc/_frecuencia.py` | El script que mide el uso real de cada indicador por año |

> **Los informes crudos son la materia prima.** Si hace falta una regla exacta con su cita, están ahí;
> el framework es la destilación, no el original.
