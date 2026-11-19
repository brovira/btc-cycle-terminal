# Book Churn — How Fast the Order Book Is Being Rewritten

**Fuente:** Glassnode Research — https://research.glassnode.com/book-churn/
**Autor:** Glassnode Research · **Fecha:** 2026-11-18
**Tipo:** artículo de investigación (texto, metodología de métrica). Cita como `[reports/20261118-book-churn.md]`.

---

## Executive Summary
- Book Churn counts how often order-book price levels are revised per ten-minute interval. It is first a measure of order-book activity; volatility is one use. Depth and spread are snapshots and miss this.
- Published as a **zscore** (vs. the same instrument's trailing 30 days, same hour of day) and a **ratio** (to the trailing average). Available in Glassnode Studio (`derivatives.PerpetualOrderbookChurn`).
- Tested in-sample as a volatility indicator on Binance BTCUSDT and ETHUSDT since 2020: a **zscore ≥ 2** is followed by an above-median-volatility hour about **63%** of the time (baseline **50%**).
- Main caveat: the reading from 24 hours earlier already scores **~59%**, and a causal price-range signal does as well as churn. Churn peaks with the price move; it does not lead it and has no direction.

## What the metric is
- One "update" = one price-level row in the exchange's L2 depth feed (either side of the book). Snapshot rows are excluded. Not L3 / order-level data.
- Median ten-minute interval: about **607,000** updates on BTCUSDT, **548,000** on ETHUSDT.
- Limits: several changes to one price within a feed message collapse into one row; absolute counts are exchange-specific; a feed reconnect reads as low activity (a feed event, not a market event). Repricing risk is only one reason to revise quotes (queue management, latency defense are others).
- Depth moves less than updates. BTCUSDT typical month 2025-26, 95th vs 5th percentile interval: updates **~3.9x**, depth within 1% of price **~1.9x**. Month by month: depth **1.4x–2.3x**, updates **3.0x–5.5x**.

## Relation to depth, spread and price range
- Churn score correlation (2020–Sep 2026): vs depth within 100 bps **−0.40** BTC / **−0.36** ETH; vs spread **+0.49** BTC / **+0.43** ETH. Heavy revision tends to mean a somewhat thinner book and wider spread.
- Depth (25 and 100 bps) plus spread explain **31%** of score variation on BTC and **25%** on ETH overall. Per year 2020–2022: **45%–73%** BTC, **40%–70%** ETH. Since 2023: **21%** BTC and **15%** ETH. Reason for the decline unknown.
- The ten-minute high-low price range, scored the same way, explains about **70%** alone (**61%–76%** per year); adding depth and spread adds under one point. About **30%** is unexplained by any of the three (noise, feed artifacts, any new information).
- Example, 27 Apr 2026 (picked after the fact): three intervals from 05:10 UTC with **1.8–2.1M** updates (vs **0.6–0.9M** the hour before), scores **4.34, 3.83, 3.41**. Depth within 100 bps **$377M–$412M** (vs **$400M–$464M** before), then **$565M**. Spread stayed ~one tick (**0.013–0.016 bps**). Range was **95 bps** in the first interval, then **28** and **39 bps**. Of BTCUSDT scores ≥ 3, about **7%** came with depth within one s.d. of norm and a range score below 2.

## Construction
- `zscore = (ln(1 + updates) − mean) / s.d.`, using the same instrument's intervals at the same hour of day over the previous 30 days (up to **180** intervals, all prior to the scored one). Uses only the interval's own count, known at close. Delay between close and API availability is not published; measure it before using for execution.
- **ratio** = updates / average of the previous 30 days across all hours (intervals with any updates). Not hour-adjusted; ratio 5 = five times the trailing mean.
- Log used because counts are skewed: 99.9th percentile is **5.4x** the median on BTC (**5.6x** ETH); the maximum is **10x** (BTC) and **13x** (ETH). Not tested without the log.
- Score scale: mean **0.01 / 0.03**, s.d. **1.09**; range **−8.04 to +8.24** BTC, **−7.61 to +9.10** ETH.
- Not normal: a normal with s.d. 1.09 would give ~**3.3%** above 2 and **0.30%** above 3. Actual is **4.3% / 4.6%** and **0.94% / 0.98%** (BTC / ETH). Set thresholds from observed frequencies, not standard deviations.
- Very low scores (down to about **−8**) from intervals at **10%–25%** of normal activity are likely data gaps, not quiet markets.

## How often it fires (BTCUSDT / ETHUSDT, since 2020)
| Threshold | Share of intervals | Intervals/day | Episodes/day |
|---|---|---|---|
| zscore ≥ 2 | **4.3% / 4.6%** | **6.2 / 6.5** | **2.7 / 2.9** |
| zscore ≥ 3 | **0.94% / 0.98%** | **1.4 / 1.4** | **0.7 / 0.8** |

For alerts count episodes (consecutive crossings = one event): under three per day above 2, under one per day above 3.

## Volatility test
Setup: every reading ≥ 2, 1 Jan 2020 – 30 Sep 2026; next-hour volatility vs the median of ordinary intervals in the same year, same hour of day and similar trailing volatility (including the interval just closed). Runs of readings count as one episode. ± = one standard error.

| Threshold | BTCUSDT hit | ETHUSDT hit | Median vol ratio | Episodes BTC / ETH |
|---|---|---|---|---|
| zscore ≥ 2 | **63.2% ± 1.8** | **63.4% ± 1.5** | **1.18 / 1.19** | **6,699 / 7,236** |
| zscore ≥ 3 | **69.1% ± 2.5** | **68.2% ± 2.2** | **1.31 / 1.29** | **1,780 / 1,935** |

- Placebos: random fake spikes **51.2% / 50.5%** (≈ 50%, as expected). The churn score from 24h earlier: **58.9% / 58.4%**. Current reading adds only **4–5 points** over the day-old one (wider gap from 2022). Much of the edge is multi-day volatile regimes.
- By year (zscore ≥ 2, BTC / ETH): 2020 **53.3% / 56.0%**; 2021 **56.5% / 55.0%**; 2022 **64.6% / 63.3%**; 2023 **68.3% / 67.2%**; 2024 **70.6% / 68.7%**; 2025 **66.5% / 70.0%**; 2026 **64.4% / 63.7%**. 2020–21 are close to chance (95% CIs include 50%) and hold about a third of episodes; from 2022 on: **67.1% ± 2.0** BTC, **66.8% ± 1.5** ETH.
- By trailing-volatility decile (BTC, ≥ 2): deciles 1–4 have few episodes (**13, 31, 42, 91**; hit **92.3%, 83.9%, 78.6%, 71.4%**), not reliable. Decile 5: **58.6% ± 5.3** (not distinguishable from 50%). Deciles 6–10: **64.8%, 64.5%, 61.7%, 61.2%, 63.7%** (episodes **321, 485, 838, 1,570, 3,122**), holding 95% of episodes. Vol ratio flat at **1.14–1.22** across deciles 5–10.
- Absolute effect is modest: next-hour vol after a spike **40–78 bps** vs **35–68 bps** control in the main deciles, a gap of **5–10 bps**. ETH: hit rate above 50% in every decile but noisier; decile 3 **51.2%** on 43 episodes.

## Churn vs a price-range signal
- Range signal = ln(1 + high-low range in bps), scored against the previous 30 days at the same hour, matched on episode count. Churn **63.2%** vs range **63.7%** (BTC); **63.4%** vs **63.5%** (ETH). Paired difference **−0.53 pts** (95% interval **−1.7 to +1.1**) BTC and **−0.15 pts** (**−1.8 to +1.3**) ETH: indistinguishable from zero.
- A simpler range signal ranked against the whole calendar year beats churn but uses future data, so it is not tradable and not the benchmark.
- Correlation between the two scores **0.84**, yet in about half of churn-firing intervals the range signal is silent (**51.5%** BTC, **50.6%** ETH; ~**58%** if the range signal is built on all hours). Those are heavy-revision markets whose range is not unusual enough.
- Example, 21 Sep 2026 08:30 UTC: ~**3.4M** updates, **4.13x** the ~**821,000** 30-day average, score **4.60**, range **226 bps**. Next intervals: **4.40** (08:40), **2.43, 2.77, 2.07, 3.62**, peak **4.70** at 09:30 (range **117 bps**); ETH peaked at **4.60**. Against all hours the 08:30 score would be only **3.65**; ratio rose from **4.13x** to **4.59x** at 09:30. One episode picked after the fact, and the range signal would also have fired.

## Interpretation and limits (declared by the article)
- A high reading means the book is being rewritten heavily now; historically the next hour was above-median volatile ~**63%** of the time. It does not warn of volatility in a calm market. About **37%** of high readings are followed by an ordinary hour: it shifts odds, not a forecast.
- No direction. Could be a filter alongside depth imbalance or order flow; untested.
- BTC and ETH results are highly correlated, so close to one test, not two. Binance only; re-test elsewhere.
- Deciles and control medians are computed within each calendar year, so the figures describe the sample and are not a live-achievable hit rate.
- No trading or execution use evaluated.
- Hour-of-day adjustment is incomplete: share of readings above 2 by UTC hour **2.3%–5.1%** BTC, **2.8%–5.3%** ETH, lowest at 14:00. The top-of-hour slot reads above 2 in **5.6%** of cases vs **3.3%** at :50 (BTC; **5.9%** vs **3.5%** ETH). Excess of :00/:30 slots grew from ~**1.2x** before 2024 to ~**1.4x** (BTC) / **1.5x** (ETH).
- Other Binance perpetuals (BNB, DOGE, SOL, XRP, TRX, data to 19 Oct 2026): hit rates ~**60%–65%** vs **57%–61%** day-old placebo; churn not measurably worse than the range signal. Thresholds not validated there. HYPEUSDT (since May 2025) too short.

## Data and availability
- Ten-minute resolution for Binance BTCUSDT, ETHUSDT, BNBUSDT, DOGEUSDT, SOLUSDT, XRPUSDT, TRXUSDT, HYPEUSDT perps. BTC/ETH backfilled to 1 Jan 2020, scores from 15 Jan 2020. Point-in-Time version starts October 2026.
- Sample: **705,719** scored of **709,920** expected intervals; **4,201** unscored (**4,032** in warm-up, **169** by exclusions).
- Score is null: first 14 days; same-hour window with under 14 days of usable data; no updates; interval under **10%** of trailing all-hours average (once that rests on ≥ **84** intervals); zero variation in window. Partial-feed intervals are scored as quiet. The 180-value window makes extremes more common.

## Conclusion
Book Churn directly measures order-book revision activity. As a volatility indicator it matches, but does not beat, a causal price-range signal on hit rate; a day-old reading recovers most of the apparent edge, and it moves with price rather than leading. Since 2023 depth and spread explain only about a fifth of its variation, while price range explains **61%–76%** each year. About half of its high readings occur when the range signal is silent.
