# Jupyter notebook projects

This repo is where I keep notebook-first data projects that are worth showing, rerunning, and improving later.

The rule is simple: a notebook should not be a loose dump of cells. Each project needs a short README, a way to test the outside data source, and a clean notebook committed without bulky outputs.

[![Notebook checks](https://github.com/luandarodrigues/projectsforjupyternotebook/actions/workflows/notebook-checks.yml/badge.svg)](https://github.com/luandarodrigues/projectsforjupyternotebook/actions/workflows/notebook-checks.yml)

## Projects

| Project | Theme | Status |
| --- | --- | --- |
| [GLP-1 Bayesian pharmacovigilance](notebooks/glp1-bayesian-farmacovigilancia/) | Semaglutide vs Tirzepatide adverse-event reports from openFDA/FAERS, modeled with a Beta-Binomial approach | Published |
| [Remote work salary premium](notebooks/remote-work-salary-causal-inference/) | Causal inference on whether fully remote data roles still show a salary premium after adjustment | Published |
| [Crypto market regime detection](notebooks/crypto-market-regime-detection/) | Recent BTC/ETH Binance data segmented into volatility, drawdown, and momentum regimes | Published |
| [Brazil inflation and monetary regimes](notebooks/brazil-inflation-monetary-regimes/) | BCB/SGS macro series used to identify inflation-pressure regimes with a literature-backed feature set | Published |

## Project ideas still worth adding

The published notebooks already cover causal inference, financial regimes, and Brazilian macro regimes. A business-survival project would round out the portfolio with time-to-event modeling.

| Project idea | Why it works | Main visuals |
| --- | --- | --- |
| **Customer churn survival analysis** | A business-heavy project with real statistical depth: estimate churn timing and where the risk curve accelerates. This can use Kaplan-Meier curves, Cox-style hazard modeling, calibration, and cohort-level diagnostics. | Survival curves by segment, hazard ratio plot, calibration curve, churn-risk timeline |

New projects should keep the same report shape: one clean narrative, charts saved as images, model diagnostics, and a README that shows the actual results without making someone open Jupyter first.

## README-report format

Each project README should work like a small report:

```text
1. One-paragraph question
2. 3-bullet result summary
3. Main chart image
4. Data and identification/modeling assumptions
5. Supporting charts and diagnostics
6. Sensitivity checks or validation
7. Caveats
8. Link to the notebook
```

Recommended folder shape:

```text
notebooks/project-name/
|-- README.md
|-- notebook_name.ipynb
|-- assets/
|   |-- 01_main_result.png
|   |-- 02_breakdown.png
|   `-- 03_model_check.png
`-- test_data_source.py
```

For LinkedIn, this gives a clean flow: one hero chart, one supporting chart, a short explanation, and the GitHub link.

## LinkedIn post flow

The post should come from the README, not from a blank page.

```text
1. Hook: the question the notebook answers
2. Context: where the data came from
3. Result: one number or one clear comparison
4. Visual: the chart that makes the result obvious
5. Caveat: what the analysis does not prove
6. Link: GitHub repo or project folder
```

For the GLP-1 notebook, the best angle is not "which drug is safer." The cleaner angle is: "I used Bayesian inference to compare serious-report proportions in openFDA adverse-event data, and the caveats matter as much as the result."

## Repository Structure

```text
.
|-- notebooks/
|   |-- glp1-bayesian-farmacovigilancia/
|   |   |-- README.md
|   |   |-- PROJECT_REVIEW.md
|   |   |-- portfolio_glp1_bayesian.ipynb
|   |   `-- test_fda_api.py
|   |-- remote-work-salary-causal-inference/
|   |   |-- README.md
|   |   |-- remote_work_salary_causal_inference.ipynb
|   |   |-- test_data_source.py
|   |   `-- assets/
|   |-- crypto-market-regime-detection/
|   |   |-- README.md
|   |   |-- crypto_market_regime_detection.ipynb
|   |   |-- test_binance_market_data.py
|   |   `-- assets/
|   `-- brazil-inflation-monetary-regimes/
|       |-- README.md
|       |-- LITERATURE_REVIEW.md
|       |-- brazil_inflation_monetary_regimes.ipynb
|       |-- test_bcb_api.py
|       `-- assets/
|-- scripts/
|   `-- normalize_notebook.py
|-- requirements.txt
`-- .github/workflows/notebook-checks.yml
```

## How to run this repo

Install the Python packages:

```bash
python -m pip install -r requirements.txt
```

Check that the openFDA endpoint still responds with the fields the notebook expects:

```bash
python notebooks/glp1-bayesian-farmacovigilancia/test_fda_api.py
```

Make sure the notebook is clean before committing it:

```bash
python scripts/normalize_notebook.py notebooks/glp1-bayesian-farmacovigilancia/portfolio_glp1_bayesian.ipynb --check
```

Run the notebook end to end:

```bash
jupyter nbconvert --to notebook --execute notebooks/glp1-bayesian-farmacovigilancia/portfolio_glp1_bayesian.ipynb --output portfolio_glp1_bayesian_executed.ipynb
```

## Notebook rules I want to keep

- Commit the readable notebook, not a 5 MB executed copy.
- Put every project in its own folder under `notebooks/`.
- Add a README for the project before the notebook starts growing.
- Test external APIs with a small script. A notebook that silently fails six months later is not useful.
- Keep the conclusion and the caveats near each other, especially for health data.
- Leave generated notebooks out of Git unless there is a good reason to publish the output.

## Next Additions

The next notebook should reuse this same shape. If the structure starts feeling heavy, that is a sign the project probably belongs in its own repo instead.
