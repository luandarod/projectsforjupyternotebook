# Brazil inflation pressure and monetary policy regimes

Brazil is a messy macro case, in a useful way. IPCA, USD/BRL, Selic, real rates and credibility all move through the same story. You can see a lot of the policy debate just by putting those series next to each other.

I pulled public data from Banco Central do Brasil and built a monthly panel from IPCA, USD/BRL and Selic. Then I used a regime model to separate long inflation-pressure phases and ran a small rolling pass-through check for the exchange rate.

![Macro regime timeline](assets/01_macro_regime_timeline.png)

## Result

- Data window: **2002-11 to 2026-02**
- Analysis sample: **280 monthly observations**
- Train/test split: **224 train** and **56 test** months
- Regimes selected by train BIC: **4**
- Latest regime: **Inflation/fx pressure**
- Latest IPCA 12m: **3.81%**
- Latest Selic, annualized from daily rate: **14.90%**
- Latest ex-post real policy rate: **11.09%**
- One-month regime persistence: **94.3%**

I would not read the latest label as a crisis headline. The label comes from the cluster's average behavior, not from February 2026 alone. That month lands in a group that has mixed inflation pressure, FX movement and restrictive policy before.

## Model Selection

I fit Gaussian Mixture Models with 2 to 5 regimes on the training window. BIC picks the number of components from train, and the last 20% of months stay out of that choice.

![Model selection](assets/02_model_selection.png)

The model has no memory of Brazilian politics, fiscal news or central-bank communication. It only sees monthly features built from inflation, exchange rate, Selic and real rates. That is a strength for reproducibility and a limit for interpretation.

## Data

All data comes from the public SGS/BCB JSON API.

- IPCA monthly variation: SGS `433`
- USD/BRL exchange rate: SGS `1`
- Selic daily rate: SGS `11`

The daily series are pulled in chunks because the SGS endpoint limits long windows for daily data. After that, everything is monthly.

Features used in the model:

- 12-month IPCA
- 3-month annualized IPCA momentum
- 3-month and 12-month exchange-rate movement
- 63-business-day FX volatility
- annualized Selic from the daily rate
- ex-post real policy rate
- real-rate gap versus a rolling 60-month average

## Method

The regime model runs on standardized monthly features. I compare the selected GMM with KMeans and a plain inflation-quantile baseline so the result is not floating by itself.

For pass-through, I use a 60-month rolling regression. The dependent variable is inflation over the next three months. The inputs are recent USD/BRL movement, current 12-month inflation and Selic. I treat the coefficient as a diagnostic signal. It is not a structural causal estimate.

## Diagnostics

![Policy pressure map](assets/03_policy_pressure_map.png)

The pressure map puts each month in inflation-momentum and real-rate space. Restrictive-policy months sit apart from low-pressure easing periods, although the borders are not clean. Macro data rarely gives you tidy boxes.

![Transition matrix](assets/04_transition_matrix.png)

Regimes persist. One-month persistence is about **94.3%**, so the model is mostly finding long macro phases rather than month-to-month noise.

![Rolling pass-through](assets/05_rolling_pass_through.png)

The rolling pass-through coefficient moves around and turns negative in the latest window. I read that as a warning about the simple regression. Policy reaction, timing and omitted variables are all tangled up in this coefficient.

![Regime profile table](assets/06_regime_profile_table.png)

The table is where the labels become checkable: average IPCA, FX move, Selic, real rate, duration and assignment confidence by regime.

![Baseline and stability](assets/07_baseline_stability.png)

The GMM has low silhouette, and bootstrap stability is modest. Median adjusted Rand index is **0.24**. The broad phases are useful, but I would not treat the exact cut points as facts.

## Bibliographic Base

I built the feature set from three lines of literature:

- inflation targeting in Brazil
- exchange-rate pass-through in emerging markets
- regime-switching and policy-rule work in macroeconomics

The notes are in [LITERATURE_REVIEW.md](LITERATURE_REVIEW.md). The papers do not validate this GMM. They explain why IPCA, USD/BRL, Selic, real rates, credibility and regime changes belong in the same notebook.

## Caveats

This is a portfolio-scale statistical report, not a central-bank model. It does not include inflation expectations, output gap, fiscal variables, administered prices, commodity shocks, credit or survey data.

I would use it as a macro data-science case study: public data, a documented bibliography, readable features, regime diagnostics and limitations kept close to the result.

## Files

- `brazil_inflation_monetary_regimes.ipynb`: clean notebook
- `test_bcb_api.py`: smoke test for the BCB/SGS API
- `LITERATURE_REVIEW.md`: scoping-review notes and references
- `assets/`: charts used in this report
- `results_summary.json`: machine-readable output from the latest notebook run
