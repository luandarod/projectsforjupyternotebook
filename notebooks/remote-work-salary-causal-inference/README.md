# Remote work salary premium: causal inference

Remote jobs look better paid in raw salary data. The question is whether that premium survives after adjusting for seniority, job family, company market, employee market, company size, and year.

This notebook treats fully remote work as a treatment and compares remote vs onsite data-science salaries using matching, inverse probability weighting, and a doubly robust estimator.

![Estimated remote salary effects](assets/01_effect_estimates.png)

## Result

- Raw comparison: fully remote roles show a **+12.6%** salary difference.
- Doubly robust estimate: the adjusted effect drops to **+3.0%**.
- Bootstrap 95% interval: **-7.4% to +13.3%**.

The read is pretty simple: the naive chart makes remote work look like a clear salary premium. Once the comparison accounts for observable composition, the effect becomes smaller and uncertain.

## Data

- Source file: public `ds_salaries.csv` mirror on GitHub
- Original context: data-science salary records with salary, year, seniority, job title, company size, company location, employee residence, and remote ratio
- Raw rows: `607`
- Analysis rows: `486`
- Treatment: `remote_ratio == 100`
- Control: `remote_ratio == 0`
- Excluded: hybrid roles and extreme/implausible salary records outside the project filter

## Method

The outcome is log salary in USD. The adjustment set is intentionally readable:

- work year
- experience level
- job family
- employee market: US vs non-US
- company market: US vs non-US
- company size

Estimators used:

- naive difference in mean log salary
- regression adjustment
- inverse probability weighting
- doubly robust / AIPW estimate
- nearest-neighbor matching on propensity score

The confidence interval comes from a row bootstrap that refits the propensity and outcome models on each sample.

## Diagnostics

![Propensity overlap](assets/02_propensity_overlap.png)

The overlap is usable, though not perfect. Remote roles are common in this sample, so the analysis leans on a relatively small onsite control group.

![Covariate balance](assets/03_covariate_balance.png)

Weighting improves the largest observed imbalances. It does not solve unobserved confounding.

![Effect by seniority](assets/04_effect_by_seniority.png)

The adjusted effect is not stable across seniority levels. Entry-level rows are sparse, so that slice should be read carefully.

![Raw salary distribution](assets/05_raw_salary_distribution.png)

The raw distribution explains why this question is tempting. It also shows why a direct comparison is too quick.

## Caveats

This is observational salary data, not an experiment. The estimate does not adjust for company brand, exact city, negotiation strength, equity, benefits, team scope, or applicant quality. The result is best read as: **the visible remote salary premium is mostly a composition story in this dataset.**

## Files

- `remote_work_salary_causal_inference.ipynb`: clean notebook
- `test_data_source.py`: smoke test for the public CSV
- `assets/`: charts used in this report
- `results_summary.json`: small machine-readable output from the notebook run
