# Crypto market regime detection

BTC changes mood fast. Some stretches are calm and directional. Others look like a rally with too much heat behind it, or a drawdown that has not fully washed out.

I wanted a compact way to label those periods without pretending to forecast price. This notebook pulls recent BTC/USDT and ETH/USDT daily candles from Binance, builds market-structure features, fits a Gaussian Mixture Model, and checks whether the regimes hold up outside the training window.

![BTC regime timeline](assets/01_btc_regime_timeline.png)

## Result

- Data window: **2023-03-31 to 2026-07-06**
- Feature-complete BTC rows: **1,194**
- Train/test split: **955 train** and **239 test** daily observations
- Regimes selected by train BIC: **4**
- Latest BTC regime: **Stress / drawdown**
- Latest regime probability: **66.1%**
- Median assignment probability: **99.3%**
- Test-window median assignment probability: **99.9%**
- One-day regime persistence: **71.2%**

The latest label is not a slam dunk. A **66.1%** posterior probability means BTC sits near a regime boundary, not deep inside a clean state. I prefer that answer to a falsely confident one.

## Model Selection

I fit Gaussian Mixture Models with 2 to 6 components on the training window only. BIC picks the number of regimes from train, and the last 20% of the timeline is left for a basic out-of-sample check.

![Model selection and validation](assets/00_model_selection_validation.png)

That split matters. If the model gets to choose regimes after seeing the full series, the report can look sharper than the evidence deserves.

## Data

- Source: Binance public market data endpoint
- Symbols: `BTCUSDT`, `ETHUSDT`
- Interval: daily candles
- Authentication: none
- BTC rows pulled: `1,283`
- Feature-complete BTC rows: `1,194`

The feature set is built from price, volatility, volume, and ETH/BTC relative strength:

- BTC log return
- 14-day and 30-day trend
- 7-day and 30-day realized volatility
- 30-day downside volatility
- 90-day drawdown
- intraday range
- volume shock
- trade-intensity shock
- ETH/BTC 7-day relative strength

## Method

The main model is a Gaussian Mixture Model on standardized features. It gives each day a regime label and a posterior probability.

I added three checks because regime models can fool you:

- temporal validation: train on the first 80%, evaluate the final 20%
- baseline comparison: GMM against KMeans and volatility buckets
- bootstrap stability: refit the same number of regimes on resampled training windows and compare assignments with adjusted Rand index

## Diagnostics

![Trend volatility map](assets/02_return_volatility_map.png)

The regimes split trend and volatility in a readable way, but they overlap. Crypto does that. Clean separability would make me suspicious.

![Transition matrix](assets/03_transition_matrix.png)

The transition matrix gives the model a quick reality check. One-day persistence is about **71.2%**, so regimes have some memory without becoming frozen labels.

![Risk table](assets/04_regime_risk_table.png)

The risk table turns each regime into numbers a market reader can use: annualized return, annualized volatility, daily VaR 95%, expected shortfall, average duration, and median assignment probability.

![Assignment confidence and stability](assets/05_assignment_confidence.png)

Assignment confidence is high across most days. Bootstrap stability is more modest: median ARI is **0.42**, with a 10th to 90th percentile range from **0.22** to **0.67**. I read that as useful structure, not a fixed taxonomy.

![Baseline comparison](assets/06_baseline_comparison.png)

The baseline chart keeps the model grounded. GMM is more flexible than volatility buckets, but the silhouette score stays low because the feature space is messy. That is normal for market data.

## Interpretation

The current BTC state looks stress/drawdown-like, with moderate confidence. I would use that as context for risk discussion, not as a trading signal.

The best part of the project is the discipline around the model: recent data, train/test separation, BIC selection, out-of-sample checks, transition diagnostics, risk metrics, baselines, and bootstrap stability.

## Caveats

These are analyst labels, not ground truth. Binance spot candles do not include macro news, funding, open interest, order-book depth, ETF flows, or liquidity across exchanges.

I read this as a statistical regime report. No trade recommendation is hiding in the charts.

## Files

- `crypto_market_regime_detection.ipynb`: clean notebook
- `test_binance_market_data.py`: smoke test for the Binance kline endpoint
- `assets/`: report charts
- `results_summary.json`: machine-readable output from the latest notebook run
