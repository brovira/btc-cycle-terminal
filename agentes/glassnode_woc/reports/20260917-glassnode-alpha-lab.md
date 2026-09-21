# Glassnode Alpha Lab

**Fuente:** Glassnode Research — https://research.glassnode.com/glassnode-alpha-lab/
**Autor:** Glassnode · **Fecha:** 2026-09-17
**Tipo:** artículo de producto (texto). Cita como `[reports/20260917-glassnode-alpha-lab.md]`.

---

## Executive Summary
- Glassnode launched **Alpha Lab**, a quantitative research platform that mines its own metric catalogue for simple, human-readable trading heuristics on Bitcoin (and other assets), instead of forcing users to build their own testing pipelines.
- The engine labels every historical day as a "good" buying/shorting opportunity or not, based on what price actually did afterward, then grows shallow decision trees over transformed versions of the chosen metrics to isolate the thresholds that separated good days from the rest.
- Tree depth is capped at **two**, so every surfaced rule collapses to **one or two metric conditions** — a readable heuristic rather than a black-box prediction.
- Each rule ships with its historical return, Sharpe ratio, maximum drawdown, hit rate, trading frequency and equity curve, and reported performance is **net of slippage**.
- Three access modes share the same engine: **Easy mode** (pick asset, direction, metrics, search effort, get ranked signal cards), **Advanced mode** (full control over source metrics, transformations — z-scores, RSI, moving averages, volatility, percentiles — and custom-painted labels), and an **MCP server** that lets AI agents run the same search-evaluate-refine loop autonomously.
- Validation runs in **three stages**: walk-forward testing on chronologically ordered data, an **out-of-sample holdout on the most recent 20% of history** (excluded from the search), and live evaluation once a rule is catalogued, tracked on data that could not have influenced its selection.
- The methodology builds on Glassnode's proprietary research workflow for the **Bitcoin Sharpe Signal**, which has **more than three years** of live track record.
- A **Catalogue**, **My Catalogue** and **Market Pulse** layer turns one-off backtests into ongoing monitoring: users can see whether saved rules are still firing, whether their edge is decaying, and get an aggregate read of how the catalogued long/short rules are currently leaning.
- Alpha Lab is **currently in beta, available to a limited group of clients** via Glassnode representatives; its outputs are explicitly framed as research, not investment advice or a performance guarantee.

## The Problem It Addresses
Glassnode's data catalogue spans thousands of on-chain, exchange-flow, derivatives, spot and order-book metrics. Turning that breadth into a specific, testable decision rule has typically required a quant team's own pipeline — more time, code and specialist knowledge than most investors have on hand. Alpha Lab is positioned as the shortcut from "a chart in Studio" to a systematic, evaluable rule.

## How the Search Engine Works
1. **Question and labeling:** the user defines the asset and objective (e.g., stronger risk-adjusted returns via Sharpe ratio, or greater absolute return). Every day in the available history is then labeled a "good" opportunity or not, based on subsequent price action — the labeling is described as defining "the truth" the model learns from.
2. **Feature expansion:** each selected metric is expanded into many transformed versions of itself (statistical variants across different windows).
3. **Decision trees:** hundreds of shallow decision trees (**depth capped at two**) are grown and continually re-optimized, each branch representing a threshold that separates good days from the rest, scored the way a trader would score a strategy.
4. **Rule extraction:** the strongest branches are extracted as standalone heuristics — a rule reads like *"when metric A is below X and metric B is above Y, this is a favorable zone to improve risk-adjusted return"* — each judged on how often it was right and how much history supports it.

## Three Ways to Access the Engine
- **Easy mode:** choose asset, long/short direction, metrics and search effort; the engine runs in the background and returns ranked, filterable signal cards (by drawdown, risk-adjusted return, hit rate, evaluation period), viewable as metric pairs or single-metric rules. Designed as an iterative loop: refine metrics, rerun, compare against prior results.
- **Advanced mode:** exposes the full pipeline — choice of source metrics and transformations (z-score, RSI, moving averages, volatility, percentile-based features), adjustable transformation windows, and custom labeling (users can paint their own zones onto price history, e.g., local bottoms, market tops, volatility regimes, parabolic moves). Shows the full path from model to rule: model comparison, feature influence, the complete heuristic table, and per-rule detail.
- **Agent mode (MCP server):** compatible AI agents get access to the same metric catalogue and optimization engine as the human interface, allowing an investor to hand off a research objective and let the agent run, evaluate and refine successive searches, then feed the strongest findings back into the visual interface or a saved catalogue.

## Stress-Testing and Invalidation of Heuristics
The platform explicitly flags a **warning sign**: if a rule only works at one exact threshold or lookback window, that fragility should be treated as suspect. A credible relationship is expected to remain **reasonably stable when nearby parameters are varied**; Alpha Lab surfaces this parameter sensitivity directly, so a "finely tuned historical accident" can be distinguished from a potentially durable pattern. This sensitivity check functions as the article's invalidation criterion for any given heuristic.

## From Discovery to Ongoing Monitoring
- **Catalogue:** strategies already identified and saved by the Glassnode team, browsable by asset, direction and risk/performance profile, with visibility into full history, out-of-sample period and live window since cataloguing.
- **My Catalogue:** lets users build their own saved research universe; over time the platform can flag rules whose recent behavior has weakened, surface overlapping strategies, and highlight coverage gaps. A **Lindy effect** logic applies — the longer a strategy keeps performing live on unseen data, the higher the confidence it reflects a robust relationship rather than overfitting.
- **Market Pulse:** an aggregate view of which catalogued long/short rules are currently active, giving a compact read of how the accumulated evidence is leaning while preserving drill-down into individual rules.

## Validation Methodology (Numbers)
- **Search:** random forest over a fixed trial budget; **tree depth capped at two**, limiting each rule to roughly two conditions.
- **Validation stage 1 — walk-forward:** trains on earlier data, evaluates on later periods, preserving chronological order.
- **Validation stage 2 — out-of-sample holdout:** the most recent **20%** of history is excluded from the search and used only for independent evaluation.
- **Validation stage 3 — live evaluation:** once catalogued, a rule is tracked on newly arriving data that could not have influenced its selection.
- **Reporting:** performance (return and Sharpe ratio) is reported **net** of slippage assumptions.
- **Track record basis:** methodology draws on Glassnode's proprietary Bitcoin Sharpe Signal research, with **more than three years** of live track record informing the approach.

## Who It's For
- **Discretionary investors:** surfaces which metrics and thresholds deserve attention ahead of a market decision.
- **Quantitative researchers:** a configurable environment for feature discovery, model comparison and robustness testing.
- **Teams building AI agents:** a measurable autoresearch loop grounded in the same data and evaluation framework as the human interface.

## Status
Alpha Lab is **currently in beta**, available to a limited group of clients; Glassnode is recruiting research teams and investors to test it against real workflows. Access is via a Glassnode representative. The article closes with an explicit disclaimer: outputs are based on historical data and **do not constitute investment advice or a guarantee of future performance**.
