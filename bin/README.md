# `bin/btc` — CLI de la terminal de ciclo

**Aviso primero: el "Glassnode CLI" no existe.** No hay CLI oficial de Glassnode, ni en npm,
ni en PyPI, ni como binario. Lo único que hay con ese nombre es `glassnode` en PyPI, un wrapper
de terceros en versión 0.0.2 mantenido por un particular — y que además necesita una API key de
Glassnode para servir de algo, así que no ahorra ningún paso.

Esto es otra cosa: lee los datos que **este repo ya ingiere** (bitcoin-data.com, checkonchain,
coinmetrics) y los presenta con los umbrales que salieron de `agentes/auditoria/`.
Sin dependencias — solo stdlib. Sin API keys. Sin coste.

## Comandos

```bash
bin/btc                          # escalera de cost basis (por defecto)
bin/btc niveles --spot 77709     # ídem, fijando el precio a mano
bin/btc ratio                    # Realized P/L Ratio vs umbrales 0,5 / 1 / 2
bin/btc funding --size 3000 --lev 3 --meses 6
bin/btc urpd --spot 77709        # dónde están los muros de oferta
bin/btc serie <nombre> -n 20     # cualquier métrica
bin/btc ls                       # qué hay disponible
bin/btc frescura                 # edad de cada fichero (sale 1 si algo está viejo)
bin/btc actualizar               # re-ingesta
```

## Las tres decisiones de diseño que importan

**1. Los umbrales llevan fuente.** Cada uno cita el fichero de auditoría y la fecha de la que
sale. Si un umbral no está citado, no está en el CLI. Es lo contrario de lo que hacen ellos:
la auditoría encontró que Glassnode introdujo el umbral de 0,5 el 19-ago-2026 sin decir que era
nuevo, y abandonó el STH MVRV y la Realized Cap sin cerrarlos.

**2. La frescura se ve siempre.** Cada comando estampa la fecha del dato y grita si tiene más de
3 días. `frescura` sale con código 1 para poder colgarlo de un cron. Mismo principio que
`ingesta/frescura.py`: **un «no pude mirar» nunca debe parecerse a un «todo bien»**.

**3. Los umbrales se comparan contra la serie correcta.** El marco define 0,5 y 2 sobre **SMA de
90 días**, no sobre la lectura diaria. El CLI enseña las tres (diaria, SMA30, SMA90) y solo
compara la que toca. La lectura diaria de hoy es 1,33 y la SMA90 es 0,77: comparar la primera
contra el umbral daría exactamente la conclusión contraria.

## Notas de unidades (verificadas, no supuestas)

- **`realisedpnl_ratio_all` viene en `ln(ratio)`**, partido en trazas `+ve`/`-ve`.
  Validación: SMA90 del 19-ago-2026 = **0,762** contra el **0,75** que publicó Glassnode ese
  mismo día. La lectura en log10 daría 0,598 — descartada.
- **`derivatives_futures_fundingrate` es anualizado en fracción** (×100 = %).
  Validación: el 6-oct-2025 marca `0,0750` y Glassnode escribió el 8-oct
  *«annualized funding now exceeds 8%»*.
- **URPD**: los buckets de $1.000-1.500 son monedas de la era Satoshi (~1,25M BTC, perdidas y no
  negociables) y aplastan la escala. Por defecto se acota a 0,45×–1,60× del precio.

## Lo que reproduce solo

Con datos gratis, `bin/btc` saca las mismas cifras que Glassnode publica de pago:

| | `bin/btc` | Glassnode (19-ago-2026) |
|---|---|---|
| True Market Mean | 75.780 $ | 75,8K $ |
| Realised Price | 52.692 $ | 52,8K $ |
| Realized P/L Ratio (SMA90) | 0,77 | 0,75 |
| Muro LTH | 84.000-85.000 $ | *«$83K-$86K wall»* |
| Shelf de demanda | 62.000-65.500 $ | *«$62K to $68K shelf»* |

El air gap entre 67.500 $ y 84.000 $ que enseña `bin/btc urpd` es el *«air pocket»* que citaron
el 22-jul. **Esto es la razón por la que `research/edges/README.md` descarta Glassnode
Professional (~$800/mes):** los niveles que mueven decisiones salen de fuentes gratuitas.
