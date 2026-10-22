# Quantifying Support and Resistance: Proximity-Weighted CBD

**Fuente:** Glassnode Research · *Product & Research* — https://research.glassnode.com/quantifying-support-and-resistance-proximity-weighted-cbd/
**Autor:** Vicky Yang (Fountainhead Digital) / Glassnode · **Fecha:** 2026-10-20
**Tipo:** research article / methodology piece (texto), not a weekly newsletter. Cita como `[reports/20261020-quantifying-support-and-resistance-proximity-weighted-cbd.md]`.

---

## Executive Summary
- Cost Basis Distributions (CBD) show where supply last moved across price levels, but as a heatmap they are hard to compare day to day or use as a single signal.
- The article compresses the CBD into time series that weight supply by its distance from spot, so the coins closest to price (the ones most likely to trade next) dominate.
- Main outputs: **Proximity Support Index (PSI)** and **Proximity Resistance Index (PRI)** (together "PSR"), plus proximity versions of valuation metrics: **pMVRV**, **pNUPL** and **Proximity Premium (PP)**.
- **Key threshold: PSI at 50%.** Above it, near-price supply is support-dominant; below it, resistance-dominant.
- Case studies show PSI diverging from a flat price before big moves, in both directions.
- Regressions on BTC and ETH show proximity metrics add more explanatory power for forward returns than short-term-holder (STH) metrics; PP is significant at the **1% level** for both assets.

## Why a Proximity View
- Aggregate cost-basis indicators (MVRV, NUPL, realized price) are dominated by the largest, slowest-moving supply and can underweight clusters just around spot.
- Cohort indicators (e.g. STH metrics) react quickly but can miss large long-term-holder clusters whose cost basis sits near price.
- The author argues cost-basis signals work best when the measured cost basis is close to the current trading range.
- Market-structure argument: deeper derivatives markets add synthetic exposure that absorbs flow, so trends in this cycle (since 2023) tend to be longer two-sided consolidations rather than fast blow-offs. Price therefore spends more time among several relevant cost-basis levels at once, which is the setting PSR is built for.

## Proximity Support–Resistance (PSR): Construction
- Built on Cost-Basis Quantiles (CBQ): 100 percentile buckets, each with its own realized price (RP).
- Each quantile gets a weight that decays exponentially with its distance from spot, scaled by the **30-day rolling standard deviation of price**: weight = exp(−|spot − RP| / σ30).
- Quantiles with RP below spot count as **proximity support (PS)**; those at or above spot count as **proximity resistance (PR)**.
- **PSI = PS / (PS + PR)** and **PRI = PR / (PS + PR)**; both lie in [0, 1] and sum to 1.
- Reading: **PSI > 50% = support-dominant; PSI < 50% = resistance-dominant.** The article's examples use the 7-day EMA of PSI.

## Proximity Market Metrics
- **Proximity Realized Price** = weighted average of the quantile realized prices, using the same distance weights. It is a moving reference level for the supply that matters now, in place of the market-wide average.
- **pMVRV** = spot / proximity realized price.
- **pNUPL** = (spot − proximity RP) / spot.
- **Proximity Premium (PP)** = (spot − proximity RP) / σ30. This is the gap in volatility units, which makes extremes comparable across price levels and regimes.

## Reading the Proximity Signals

### Finding Returning Support Before the Rally
- **2023 case:** From late July to mid-September 2023 BTC drifted from about **29k to 26k** with PSI mostly under 50%. In October PSI moved above 50% and held there. Price then rose from the mid-20Ks to the low 40Ks by December.
  - **Aug 24:** BTC **$26.1k**, PSI (ema7) **35.3%**. **Oct 12:** BTC **$26.7k**, PSI (ema7) **52.8%**. Price was almost flat over the seven weeks while the support structure changed.
- **2025 case (Feb–Apr):** PSI went from deep resistance dominance in February to lighter resistance dominance in March, then support-dominant in April. BTC then rose from the **low-$80Ks to about 120k** by midsummer.
  - Price was similar in mid-March and mid-April, but PSI (ema7) rose from the **high-30%s to the high-50%s**. The article reads this as accumulation under an unchanged price.

### Finding Increasing Resistance Before the Drop
- **Dec 2025 – Jan 2026:** BTC revisited the same area twice in about six weeks: **$85.5k (Dec 18)** and **$86.6k (Jan 25)**. PSI (ema7) fell from **57.5% to 48.7%**, flipping from support- to resistance-dominant. Price then broke down from the high-$80Ks toward **65k**.
- **Mid-April to late May 2026:** BTC returned to roughly the same level, but PSI (ema7) dropped from the **high-60%s to the low-40%s**. A strong resistance band at **$83.6k–$85.4k** had built up above spot. The result was a drop into the **low-$60Ks**.
- Common lesson: a familiar price can hide a worsening structure. Supply that had been support gets sold into the retest and tips the balance to resistance.

### Exhaustion and Capitulation Across Cycles
- High PP readings (spot far above proximity cost basis in vol units) tend to coincide with exhaustion near local and cycle tops.
- Low PP readings (spot well below proximity cost basis) tend to line up with sell-pressure climaxes or late-stage capitulation near lows.
- The article gives no numeric PP thresholds; the extremes are marked only on a chart.

## Predictive Value
- Setup: regressions for BTC and ETH over several forward-return horizons. Forward returns are regressed on lagged price momentum plus one on-chain metric at a time: Proximity MVRV, Proximity Premium, or STH-MVRV. The comparison is the incremental explanatory power over a baseline of past returns alone.
- Result: across all horizons and both assets, proximity metrics add larger and more statistically robust explanatory power than STH-based aggregates.
- **Proximity Premium** stands out, significant at the **1% level** for both BTC and ETH.
- Caveat: this is explanatory power in regressions, not a trading backtest. The article points readers to Glassnode AlphaLab for strategy testing.

## Conclusion
- PSI/PRI summarize how near-price cost basis is positioned against spot. pMVRV, pNUPL and PP restate familiar valuation metrics around the supply most likely to transact next.
- Practical uses named by the author: judge whether rallies will be absorbed by overhead supply, whether pullbacks will find nearby support, and whether volatility-adjusted dislocations have reached historical extremes.

## Scenarios and Invalidation (as implied by the article)
- **Constructive:** PSI (ema7) crossing and holding **above 50%** while price is flat or drifting lower, as in Oct 2023 (52.8%) and Apr 2025 (high-50%s). Support is rebuilding and a rally often follows.
- **Bearish:** PSI (ema7) slipping **below 50%** while price retests a familiar level, as in Jan 2026 (48.7%) and May 2026 (low-40%s, with the **$83.6k–$85.4k** band overhead). Expect the retest to be sold.
- The article does not give formal invalidation levels. PSI at 50% is the implied pivot. The signal is also not a standalone call: the author says cost-basis signals are context-dependent and should be combined with other indicators.
