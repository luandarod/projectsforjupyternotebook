# Crypto market regime detection

BTC does not trade in one constant market mode. Some periods are quiet and directional. Others are noisy, stressed, or stuck in low-momentum chop.

This notebook pulls recent BTC/USDT and ETH/USDT daily candles from Binance and uses a Gaussian Mixture Model to segment BTC market days into regimes. The model uses returns, realized volatility, drawdown, volume shock, and ETH/BTC relative strength.

![BTC regime timeline](assets/01_btc_regime_timeline.png)

## Result

- Data window: **2024-01-31 to 2026-07-06**
- Selected regimes: **5**
- Latest BTC regime: **Sideways / low momentum**
- Latest regime probability: **99.8%**
- Median assignment probability: **95.0%**

The useful part is not prediction. The model gives a compact read of market behavior: when BTC is in a calm uptrend, a volatile rally, a drawdown/stress state, or a low-momentum regime.

## Data

- Source: Binance public market data endpoint
- Symbols: `BTCUSDT`, `ETHUSDT`
- Interval: daily candles
- Authentication: none
- Features: log return, 7-day volatility, 30-day volatility, drawdown, volume shock, ETH/BTC relative return

## Method

I fit Gaussian Mixture Models with 2 to 5 components and choose the regime count by BIC. After assigning each day to a regime, I inspect transition behavior and risk statistics.

This is a regime model, not a trading system.

## Diagnostics

![Return volatility map](assets/02_return_volatility_map.png)

The regimes separate return and volatility behavior. That is the first sanity check.

![Transition matrix](assets/03_transition_matrix.png)

The transition matrix shows which regimes persist and which ones tend to flip quickly.

![Risk table](assets/04_regime_risk_table.png)

The risk table gives each regime a practical interpretation: average return, volatility, drawdown, and assignment confidence.

![Assignment confidence](assets/05_assignment_confidence.png)

Assignment probabilities are high in both the full sample and the out-of-sample tail. That does not make the model predictive, but it suggests the clusters are not random mush.

## Caveats

This is unsupervised learning on market features. Regime names are analyst labels, not ground truth. Binance data covers crypto market behavior, not macro causes. The model should be read as market structure analysis, not financial advice.

## Files

- `crypto_market_regime_detection.ipynb`: clean notebook
- `test_binance_market_data.py`: smoke test for the Binance kline endpoint
- `assets/`: report charts
- `results_summary.json`: latest run summary
