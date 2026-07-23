// risk.js — Métrica de riesgo de Cowen (APROXIMACIÓN abierta; su métrica exacta es propietaria).
// FUENTE ÚNICA compartida por decision.html e index.html — antes estaba copiada a mano en los dos
// y podían divergir en cualquier edición. Aquí vive una sola vez.
//
// Método: desviación de log(precio) sobre una regresión log-log (precio ~ semanas desde el génesis
// de Bitcoin), normalizada 0-1 con el min/max de TODA la serie.
//
// Nota: backtest.html usa a propósito una variante distinta (walk-forward / expanding window, sin
// lookahead, para no hacer trampa mirando el futuro) y NO depende de este archivo.
(function (g) {
  function riskNow(D) {
    const t0 = Date.parse("2009-01-03");
    let n = 0, sx = 0, sy = 0, sxx = 0, sxy = 0; const pts = [];
    for (let i = 0; i < D.t.length; i++) {
      const w = (D.t[i] - t0) / (7 * 864e5), c = D.c[i];
      if (!(w > 0) || !(c > 0)) continue;
      const x = Math.log(w), y = Math.log(c);
      n++; sx += x; sy += y; sxx += x * x; sxy += x * y; pts.push([x, y]);
    }
    if (n < 52) return null;
    const den = n * sxx - sx * sx; if (!(den > 0)) return null;
    const b = (n * sxy - sx * sy) / den, a = (sy - b * sx) / n;
    let dmin = Infinity, dmax = -Infinity, last = null;
    for (const [x, y] of pts) { const dv = y - (a + b * x); if (dv < dmin) dmin = dv; if (dv > dmax) dmax = dv; last = dv; }
    if (!(dmax > dmin)) return null;
    return (last - dmin) / (dmax - dmin);
  }
  g.BTCRisk = { riskNow };
})(typeof window !== "undefined" ? window : globalThis);
