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

## ⚠️ Hueco conocido: el corpus de 2022

**56 de 328 artículos son stubs** (solo intro; el cuerpo no se archivó): **78% de 2022** y **26% de 2021**.
2023→2026 está completo. El método actual (la escalera de cost basis) es de 2023+, así que el framework es
válido — pero el **bear de 2022**, que es el análogo del régimen actual, está mal cubierto.

### Re-ingesta de 2022 (pendiente, requiere red)

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

**Advertencia:** puede que no funcione. Los stubs contienen intro + índice y cortan justo donde empieza el
cuerpo, lo que sugiere que **las ediciones antiguas están cerradas a miembros**. Si tras re-ingestar siguen
en <3KB, el texto no es recuperable por esta vía y el hueco se queda.

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
