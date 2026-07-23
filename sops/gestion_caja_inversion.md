# SOP — Gestión de caja e inversión (BELROGAM → BTC)

**Última actualización:** 23 julio 2026
**Para qué:** decidir cuánto efectivo puede salir del negocio sin comprometer la operación, y cómo usar la sección **Inversión** del dashboard. La estrategia de compra (precio, timing, cuánto BTC) NO está aquí: vive en el terminal/journal de Bel.

> ## ⚠️ SI ESTÁS LEYENDO ESTO PARA PLANIFICAR — lee primero esto
>
> **Distingue lo estructural de la foto.** En este documento hay dos tipos de contenido:
>
> | Estructural (estable) | Foto del 23-jul-2026 (caduca) |
> |---|---|
> | La fórmula del disponible | Saldos, suelo, disponible |
> | El calendario de pagos (día 1, 3, 7, 8, 9, 15, 20) | Importes concretos de cada partida |
> | El desfase de cobro (Airbnb +1d, Booking +7d) | Ritmo necesario vs generado |
> | Las 5 reglas invariantes | Los dos escenarios y sus cifras |
> | Los dos escenarios como concepto | El % de llenado de cada mes |
>
> **No planifiques con las cifras de este documento si ha pasado más de un mes.** El suelo se mueve cada día: sube cuando entran reservas, baja cuando se paga. Pide a Bel el número actual de la sección **Inversión** del dashboard antes de proponer nada.
>
> **Y no recalcules el disponible por tu cuenta.** Ya está resuelto y auditado; duplicar el cálculo con datos viejos o supuestos propios es la forma más fácil de equivocarse. Trátalo como una restricción dada.

---

## 1. La fórmula

```
disponible = MIN(saldo proyectado día a día)  ←  el "suelo"
             − impuestos pendientes
             − margen extra (N meses de coste fijo)
```

**El colchón YA está restado.** El disponible es lo que sobra *por encima* de la línea de seguridad. Sacarlo no toca la protección: los impuestos y el margen se quedan en el banco.

### Por qué el suelo y no el saldo de hoy
El **53% del gasto mensual sale entre los días 1 y 5** (renta el 1, Strmngnt el 3), mientras los cobros entran repartidos por todo el mes. Medido sobre 12 meses: el tramo días 1-5 tiene un neto de **−150.814 €** (≈ −12.568 €/mes).

Consecuencia: mirar el saldo de hoy engaña. El 22-jul había 61.896 € y el suelo proyectado era **39.769 €** (9 de octubre). Un bache de **22.127 €** invisible en el saldo.

---

## 2. Cuándo se calcula

**En vivo, en cada carga de la página.** No hay cálculo mensual ni proceso programado (`force-dynamic` → consulta la BD en cada request).

| Ingrediente | Frescura |
|---|---|
| Saldo bancario (Caixa + Wise) | cada hora (BudgetBakers) |
| Reservas futuras | diario 08:10 (Hospitable) |
| Costes fijos, gestión, limpieza, impuestos | recalculado en cada consulta |

El número sube solo cuando entran reservas o cobros; baja cuando se paga.

---

## 3. NO es una asignación mensual

Es un **límite sobre el stock**, no un presupuesto que se renueva:

- Si no sacas nada, **no se pierde: se acumula**. El disponible crece conforme sube el suelo.
- Si lo agotas hoy, **no aparece más capacidad por el paso del tiempo**. Solo aparece cuando entran reservas nuevas que suben el suelo.
- Ahorrar es el comportamiento por defecto: el dinero se queda en la cuenta y el número sube.

---

## 4. Las dos capas de seguridad (qué protege cada una)

| Capa | Importe hoy | Protege de |
|---|---|---|
| **Impuestos pendientes** | 3.482 € | El Sociedades del Modelo 200. El IVA/IRPF **no** van aquí: el flujo ya los descuenta en su fecha real (día 20 de ene/abr/jul/oct). Meterlos también sería contarlos dos veces. |
| **Margen extra** | 12.169 €/mes | Que el modelo se quede corto: un mes malo, una cancelación, un gasto imprevisto. Configurable 0-3 meses. |

Referencia: el peor mes de flujo neto de los últimos 12 fue **−10.167 €**. Un mes malo existe y hay que poder pagarlo sin vender nada.

---

## 5. Los dos escenarios

| | Qué cuenta | Suelo hoy | Disponible (margen 1m) |
|---|---|---|---|
| **Confirmado** | Solo reservas ya hechas | 39.769 € (9-oct) | **24.119 €** |
| **Esperado** | + meses sin reservar rellenos al nivel del año pasado | 51.884 € (9-ago) | **36.233 €** |

**Regla de uso:**
- **Confirmado** → para decidir lo que sacas HOY. Es dinero que ya está o ya está reservado.
- **Esperado** → para PLANIFICAR el ritmo, no para ejecutar. Es una previsión.

El panel arranca siempre en confirmado a propósito.

Por qué el esperado es creíble: agosto ya va al **137%** del año pasado, septiembre 61%, octubre 20%, nov/dic 0% — pero el año pasado nov hizo 27.156 € y dic 29.772 €. Los ceros son falta de datos, no falta de negocio.

---

## 6. Procedimiento antes de sacar dinero

1. Abrir **Inversión**. Comprobar la fecha del saldo (debe ser de hoy).
2. Escenario en **Confirmado**.
3. Elegir margen (recomendado: **1 mes**).
4. Mirar el **disponible**.
5. Antes de ejecutar, meter la cifra en el **simulador**: enseña el suelo tras la retirada y el suelo **mes a mes**, y avisa si algún mes se va por debajo del mínimo.
6. Si sale ≤ 0 o algún mes queda bajo mínimo → **no se saca**.

### Sacar por tramos
Como el suelo sube con las reservas, sacar por tramos y revisar cada mes captura ese crecimiento sin comprometer nada. Sacar el máximo de golpe deja el margen a cero hasta que entren reservas nuevas.

---

## 7. Parkear dinero en el exchange

Para el modelo de caja es **idéntico a invertir**: en cuanto el dinero sale de la cuenta, el suelo baja. El disponible ya contempla eso.

La única diferencia real es la **reversibilidad**:

| | Recuperable si algo va mal |
|---|---|
| EUR parkeados en exchange | Sí (en horas/días) |
| BTC comprado | No, por regla propia: horizonte ~3 años |

Los euros parkeados son un colchón *extra* más allá del margen diseñado. No sustituyen al margen, pero dan aire en un escenario peor que el modelo.

**Ojo:** una vez en el exchange, la tentación de desplegarlos antes de tiempo es real. Es una decisión de disciplina, no del sistema.

---

## 8. Reglas invariantes

1. **Manda el suelo, no el saldo.** El saldo de hoy miente por el bache de principios de mes.
2. **Impuestos apartados antes que nada.**
3. **Solo caja real.** Las reservas futuras no son caja hasta que se cobran.
4. **Si el disponible sale ≤ 0, ese mes no sale dinero.** Sin excepciones, sin "ya lo repongo".
5. **La restricción de caja manda sobre el objetivo de acumulación.** Si un mes el excedente no llega al ritmo, no se compensa metiendo más otro mes ni buscando financiación.

---

## 9. Objetivo de acumulación (parte de caja)

Parámetros en `parametros_financieros` (editables):

| Clave | Valor | Qué es |
|---|---|---|
| `btc_objetivo_eur` | 55.000 | Caja total a deployar |
| `btc_fecha_inicio` | 20260901 | Inicio de la ventana |
| `btc_meses` | 18 | Horizonte (→ marzo 2028) |
| `btc_invertido_eur` | 0 | Lo ya deployado |

- Ritmo necesario: **3.056 €/mes**
- Lo que genera el negocio: **4.009 €/mes** (caja neta ex-CAPEX, 12m)
- Margen: **+950 €/mes** → factible sin apretar

Respaldo: caja neta 12m = 33.269 €, pero incluye 19.360 € de CAPEX que no se repite (puesta en marcha de pisos). El revenue crece +43% (últimos 6m 246.198 € vs 172.292 € anteriores).

**Este objetivo mide solo EUROS DEPLOYADOS.** Cuánto BTC salga de esos 55.000 € depende del precio medio, que no controla ni el negocio ni este sistema.

---

## 10. Qué revisar cada mes

| Comprobación | Por qué |
|---|---|
| ¿Ha subido el suelo confirmado? | Es la señal de que hay más capacidad real |
| ¿Se está llenando la cartera de los próximos 2-3 meses? | Si no sube, el escenario esperado no se cumple y manda el confirmado |
| ¿La reserva fiscal sigue siendo correcta? | Confirmar con la gestoría; es una estimación |
| ¿Ha entrado algún gasto grande no modelado? | CAPEX, obras, imprevistos |

---

## 11. Limitaciones conocidas del modelo

- **La comisión de Strmngnt se proyecta al 27,5%** (medido sobre facturas reales), pero su factura declara 23% sobre una base que no se puede reconstruir con nuestros datos (~2.000 €/mes de diferencia). **Pendiente de aclarar con Strmngnt.**
- **La reserva fiscal es estimación propia**, no dato de la gestoría.
- **"Otros recurrentes" (1.903 €/mes)** es una media de 12 meses: CAPEX, mobiliario, tarjeta, mantenimiento sin piso. Si hay una compra grande puntual, el modelo no la ve venir.
- **Los meses sin reservas** (más allá del horizonte fiable) no sirven para decidir: el ingreso cae a cero pero el coste no.
- **Mérida**: agosto proyecta ocupación muy baja en los locales (L2 al 0%). Si se mantiene, el suelo bajará.

---

## Vistas y componentes

| Objeto | Qué hace |
|---|---|
| `v_cashflow_diario` | Flujo día a día con dos escenarios (confirmado / esperado) |
| `v_cashflow_semanal` | Agregado semanal para la gráfica |
| `v_excedente_caja` | Suelo, impuestos, arrears, horizonte fiable |
| `v_escenario_inversion` | Relleno de meses sin reservar con el año pasado |
| `v_objetivo_btc` | Ritmo necesario vs generado |
| `v_coste_futuro_mes` / `_resumen` | Coste proyectado por piso y mes |
| `ExcedenteCaja.tsx` | Panel del disponible |
| `SimuladorInversion.tsx` | "¿Y si saco X hoy?" |
| `CashFlowSemanal.tsx` | Gráfica semanal |

Calendario de pagos modelado (mediana real de 12 meses): renta **día 1** · Strmngnt **día 3** · servicios de piso **día 7** · mantenimiento **día 8** · limpieza **día 9** · overhead **día 15** · impuestos/CAPEX **día 20**.
Cobros: Airbnb **check-in + 1 día**, Booking **check-in + 7 días** (medido).
