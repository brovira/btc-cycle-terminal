# N1 · STH cost basis — resultado

**Corrido:** 18-ago-2026 · **Script:** `n1_sth_cost_basis.py` (reproducible) ·
**Ventana:** 2011-01-01 → 2026-08-16, **5.707 días, 4 ciclos completos**.

> **Es el primer backtest del repertorio que se corre de verdad.** Todo lo anterior en este repo
> son *auditorías de track record* (calificar lo que dijeron), que es otra cosa: dicen si ellos
> acertaron, no si el método se sostiene.

---

## La afirmación bajo prueba

`framework_direccion.md §B`, destilado de los Week On-Chain: el STH cost basis es
**«soporte en tendencia alcista, resistencia en bajista»**. Es la pieza que sostiene casi todo lo
de rangos de LP, así que era la primera que había que probar.

## Veredicto corto

**Como NIVEL no replica. Como BRÚJULA sí, y bien.**

La asimetría concreta que afirma el framework —techo en bear, suelo en bull— no aparece. Lo que
sí aparece, con muestra grande y monótona, es que **el lado del nivel en el que cotiza el precio
separa regímenes de rentabilidad muy distintos**. Es un indicador de *estado*, no de *soporte*.

---

## 1) Como nivel: no

*«Aguanta»* = 8 semanas después el precio sigue del lado al que cruzó.

| Régimen | Dirección del cruce | n | Aguanta | Rechaza | Mediana +8 sem |
|---|---|---:|---:|---:|---:|
| **bear** | rompe hacia **arriba** | 14 | **11** | **3** | **+19,1%** |
| bear | pierde hacia abajo | 13 | 6 | 7 | +8,0% |
| bull | rompe hacia arriba | 18 | 9 | 9 | −4,9% |
| **bull** | pierde hacia **abajo** | 30 | 16 | **14 (47%)** | −0,1% |

- **«Suelo en bull»**: el 47% de las pérdidas del nivel se recuperan. Es una moneda al aire, con
  mediana −0,1%. **Sin señal.**
- **«Techo en bear»**: no solo no rechaza — **hace lo contrario**. 11 de 14 recuperaciones del STH
  CB en bear aguantaron, con mediana **+19,1%** a 8 semanas. En un bear, reclamar el STH cost
  basis ha sido históricamente una señal **alcista**, no una resistencia.

Los 3 fallos son informativos: **2015-03**, **2018-09** y **2022-11**. El de 2022 falló porque FTX
quebró cuatro días después. Los otros dos precedieron tramos finales de capitulación. O sea: la
señal se rompe cuando algo se rompe, no por sí sola.

## 2) Como brújula: sí

Sin mirar si el nivel aguanta. Solo: ¿de qué lado está el precio?

| Régimen | Lado del STH CB | n días | +4 sem | +8 sem | % al alza |
|---|---|---:|---:|---:|---:|
| todo | arriba | 3.345 | +4,4% | **+10,3%** | 63% |
| todo | abajo | 2.305 | +0,9% | **+1,6%** | 52% |
| bull | arriba | 2.814 | +4,7% | +11,5% | 63% |
| **bull** | **abajo** | 773 | −1,6% | **−5,8%** | **42%** ← la casilla de aviso |
| bear | arriba | 531 | +3,5% | +7,7% | 63% |
| bear | abajo | 1.532 | +1,6% | +5,3% | 57% |

Dos lecturas que sirven para operar:

1. **La única casilla negativa de las cuatro es `bull · abajo del STH CB`** (−5,8%, 42% al alza).
   Perder el STH cost basis *dentro de un bull* es el aviso real. No al revés.
2. **`arriba del STH CB` renta igual en bull que en bear** (63% al alza en las dos). El nivel
   discrimina más que el régimen — lo cual es justo lo contrario de la asimetría afirmada.

---

## Qué NO prueba esto

- **El régimen lo defino yo** con la True Market Mean. Glassnode la describe como la línea
  divisoria bull/bear, pero no consta que la usen así para etiquetar. Otra definición mueve la tabla.
- **El precio es reconstruido** (MVRV × realized price), no el cierre spot. Cercano, no idéntico.
- **Las 8 semanas y la veda de 14 días entre cruces son elecciones mías.** El test de cruces tiene
  13-30 casos por celda: poco. La tabla de la brújula (n=531 a 2.814) me la creo bastante más.
- No prueba que el framework de Glassnode sea malo. Prueba que **esta afirmación concreta, medida
  así, no se sostiene** — mientras que un uso más simple del mismo dato sí.

## Consecuencia operativa

- **Dejar de usar el STH cost basis como borde de rango de LP** esperando que rechace. No rechaza.
- **Usarlo como interruptor de estado**: por encima = viento a favor; por debajo **y en bull** =
  la única configuración históricamente negativa.
- Y ojo con la intuición contraria: en bear, **recuperarlo ha sido alcista 11 de 14 veces**.

## Dónde estamos hoy (16-ago-2026)

```
precio 62.818 · STH CB 66.964 (−6,2%) · TMM 75.733 (−17,1%)
casilla: bear · abajo  →  n=1.532 · mediana +5,3% a 8 sem · 57% al alza
```

Ni la casilla buena ni la mala: la tibia. Si el precio recupera los ~67k pasa a `bear · arriba`
(+7,7%, 63%), que históricamente **no** ha sido un rechazo.

---

## Siguiente

N1 está hecho. Lo que hace falta ahora **no es otro backtest, es replicar este con otra
definición de régimen** (p. ej. 200W MA, o la clasificación de 4 regímenes de
`framework_direccion.md §C`) para ver si el resultado aguanta o era un artefacto de usar la TMM.
Un resultado que solo existe con una definición no es un resultado.


---

## Ampliación (21-ago-2026) — qué separa los 3 fallos de los 11 aciertos

Pregunta que surgió operando: si recuperar el STH cost basis en bear aguantó 11 de 14 veces,
**¿hay algo que distinga las 3 que fallaron?** Sí, y es limpio: **si además recupera la True
Market Mean.**

| Recuperación del STH CB en bear | n | Aguantó | Mediana +8 sem |
|---|---:|---:|---:|
| **También tomó la TMM** (≤4 semanas) | 7 | **7 de 7** | **+34,1%** |
| **Se quedó bajo la TMM** | 7 | 4 de 7 | +8,0% |

**Los 3 fallos —2015-03, 2018-09, 2022-11— están todos en la segunda fila.** Ninguno tomó la TMM.

(Se excluye del recuento el evento del 19-ago-2026, que es el actual y aún no tiene 8 semanas
por delante. Contarlo inflaría la fila de abajo con un resultado que todavía no existe.)

**Cómo se usa:** la TMM es la línea. Mientras el precio se quede debajo, la base histórica de
una recuperación del STH CB es 4 de 7 — floja, y con todos los fracasos dentro. En cuanto la
toma **en cierre**, la muestra dice 7 de 7 y hay que dejar de pelearse con el movimiento.

⚠️ n=7 y n=7. Es un indicio para colocar una invalidación, **no** una probabilidad. Y ojo con la
precisión: el test mide **cierres diarios**, no toques intradía. Estar por encima unas horas no
es haberla tomado.
