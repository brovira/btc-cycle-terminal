# SOP — Gestión de caja e inversión (BELROGAM → BTC)

**Para qué:** decidir cuánto efectivo puede salir del negocio sin comprometer la operación, y cómo usar la sección **Inversión** del dashboard. La estrategia de compra (precio, timing, cuánto BTC) NO está aquí: vive en el terminal/journal de Bel.

> **Nota de privacidad:** este archivo vive en un repo PÚBLICO, así que contiene **solo el método** — la fórmula, las reglas y el calendario. **Las cifras reales (saldos, suelo, disponible, revenue, márgenes) NO se publican aquí**: son datos privados del negocio y se leen en vivo desde la sección **Inversión** del dashboard de BELROGAM (endpoint `/api/cash`, con token). Si necesitas un número concreto, pídelo al dashboard, no lo escribas aquí.

> ## ⚠️ SI ESTÁS LEYENDO ESTO PARA PLANIFICAR — lee primero esto
>
> **Distingue lo estructural de la foto.** Lo que importa de este documento es estable (fórmula, reglas, calendario). Cualquier cifra concreta (saldo, suelo, disponible, ritmo) **caduca en días** y por eso NO está aquí.
>
> **No planifiques con cifras de memoria.** El suelo se mueve cada día: sube cuando entran reservas, baja cuando se paga. Pide el número actual de la sección **Inversión** del dashboard antes de proponer nada.
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
El **grueso del gasto mensual sale entre los días 1 y 5** (renta el 1, Strmngnt el 3), mientras los cobros entran repartidos por todo el mes. Medido sobre 12 meses, ese tramo días 1-5 tiene un neto **fuertemente negativo** → arrastra el saldo hacia abajo justo a principio de mes.

Consecuencia: mirar el saldo de hoy engaña. El saldo de un día cualquiera puede ser muy superior al **suelo** proyectado unas semanas después — un "bache" de varios miles de euros que es invisible en el saldo de hoy. (El número concreto, en la sección Inversión del dashboard.)

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

| Capa | Qué es | Protege de |
|---|---|---|
| **Impuestos pendientes** | Reserva para el Sociedades (Modelo 200). El IVA/IRPF **no** van aquí: el flujo ya los descuenta en su fecha real (día 20 de ene/abr/jul/oct). Meterlos también sería contarlos dos veces. | Quedarte sin caja para Hacienda |
| **Margen extra** | N meses de coste fijo (configurable 0-3 meses). | Que el modelo se quede corto: un mes malo, una cancelación, un gasto imprevisto |

Referencia: el peor mes de flujo neto de los últimos 12 fue claramente negativo. Un mes malo existe y hay que poder pagarlo sin vender nada. (Importe concreto, en el dashboard.)

---

## 5. Los dos escenarios

| | Qué cuenta | Para qué |
|---|---|---|
| **Confirmado** | Solo reservas ya hechas | Decidir lo que sacas HOY. Es dinero que ya está o ya está reservado. |
| **Esperado** | + meses sin reservar rellenos al nivel del año pasado | PLANIFICAR el ritmo, no ejecutar. Es una previsión. |

**Regla de uso:**
- **Confirmado** → para ejecutar.
- **Esperado** → para planificar.

El panel arranca siempre en confirmado a propósito.

Por qué el esperado es creíble: los meses cercanos suelen ir llenándose hasta el nivel del año anterior; los ceros de meses lejanos son **falta de datos, no falta de negocio** (el año pasado esos meses sí facturaron). Las cifras de llenado, en el dashboard.

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

Parámetros en `parametros_financieros` (editables — los valores concretos viven en la BD, no aquí):

| Clave | Qué es |
|---|---|
| `btc_objetivo_eur` | Caja total a deployar en el ciclo |
| `btc_fecha_inicio` | Inicio de la ventana |
| `btc_meses` | Horizonte en meses |
| `btc_invertido_eur` | Lo ya deployado |

El dashboard compara dos ritmos: el **ritmo necesario** (objetivo ÷ meses) contra el **ritmo que genera el negocio** (caja neta ex-CAPEX, media 12m). Si el segundo supera al primero, el objetivo es factible sin apretar. Ambos números, en la vista `v_objetivo_btc`.

**Este objetivo mide solo EUROS DEPLOYADOS.** Cuánto BTC salga de esa caja depende del precio medio, que no controla ni el negocio ni este sistema.

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

- **La comisión de Strmngnt** se proyecta a un porcentaje medido sobre facturas reales, algo por encima del que declara su factura (sobre una base que no se puede reconstruir con nuestros datos). **Pendiente de aclarar con Strmngnt.**
- **La reserva fiscal es estimación propia**, no dato de la gestoría.
- **"Otros recurrentes"** es una media de 12 meses (CAPEX, mobiliario, tarjeta, mantenimiento sin piso). Si hay una compra grande puntual, el modelo no la ve venir.
- **Los meses sin reservas** (más allá del horizonte fiable) no sirven para decidir: el ingreso cae a cero pero el coste no.
- **Mérida**: algún mes proyecta ocupación muy baja en los locales. Si se mantiene, el suelo bajará.

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
