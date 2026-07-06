# Remote work salary premium: causal inference

Remote jobs look richer in this dataset. The first pass says fully remote data roles pay about **12.1%** more than onsite roles.

That number is tempting. I do not trust it on its own.

The notebook treats remote work as the exposure and salary as the outcome, then asks a narrower question: after matching roles on year, seniority, job family, company market, employee market, and company size, is there still much of a salary premium left?

![Estimated remote salary effects](assets/01_effect_estimates.png)

## Result

- Raw salary gap: **+12.1%** for fully remote roles.
- Cross-fit AIPW estimate: **+2.4%** after adjustment.
- 95% influence-function interval: **-8.2% to +14.2%**.
- Trimmed AIPW estimate, after overlap filtering: **+2.5%**.
- Rows removed by common-support and propensity trimming: **6**.

My read: the raw premium mostly comes from who gets counted in each group. Remote roles in this file are not a clean random slice of the market. Once the comparison adjusts for visible job and market differences, the estimate gets small and noisy.

## Causal Setup

The target estimand is the average treatment effect of fully remote work on log salary.

`E[Y(1) - Y(0)]`

Here, `Y(1)` is salary if the role is fully remote and `Y(0)` is salary if the same kind of role were onsite. The hard assumption is conditional exchangeability: after the observed controls, remote and onsite rows are comparable enough to line up.

That assumption can be wrong. So the notebook checks overlap, balance, effective sample size, and a simple omitted-confounder tipping point.

![Causal DAG](assets/00_causal_dag.png)

## Data

- Source file: public `ds_salaries.csv` mirror on GitHub
- Raw rows: `607`
- Analysis rows: `498`
- Fully remote rows: `376`
- Onsite rows: `122`
- Treatment: `remote_ratio == 100`
- Control: `remote_ratio == 0`
- Dropped from the causal contrast: hybrid rows and salary records outside the project filter

The outcome is log salary in USD. The adjustment set stays small on purpose:

- work year
- experience level
- job family
- employee market: US vs non-US
- company market: US vs non-US
- company size

## Method

The main estimate is cross-fitted AIPW. Each row gets out-of-sample estimates for its propensity score, expected salary if remote, and expected salary if onsite.

Cross-fitting matters here because the dataset is small. If the same rows train and evaluate every nuisance model, the treatment effect can look cleaner than it is.

I also report regression adjustment, Hajek IPW, nearest-neighbor propensity matching, partial-linear DML, and a trimmed AIPW estimate inside common support. They tell the same story: the big raw gap shrinks fast.

## Diagnostics

![Propensity overlap](assets/02_propensity_overlap.png)

The overlap is usable. The cross-fitted propensity AUC is **0.58**, so the model does not cleanly separate remote from onsite roles. That is good for this comparison. After weighting, the effective sample size is about **370 remote** and **106 onsite** rows.

![Covariate balance](assets/03_covariate_balance.png)

Weighting pulls down the biggest observed imbalances, especially market and seniority differences. It does not solve company brand, negotiation skill, equity, or applicant quality. Those are still missing.

![Effect by seniority](assets/04_effect_by_seniority.png)

The seniority slices move around. Some cells are thin, so I treat this as a heterogeneity check rather than a firm subgroup claim.

![Raw salary distribution](assets/05_raw_salary_distribution.png)

The raw distribution explains why the question is worth asking. Remote rows sit higher. The causal estimates explain why the plot is not enough.

![Sensitivity to omitted confounding](assets/06_sensitivity_tipping_point.png)

The adjusted estimate is small. A hidden factor with a combined log-salary effect times prevalence gap of about **0.024** would push the AIPW estimate to zero. That is not a huge amount of missing structure.

## Interpretation

This does not mean remote work has no value. It means this dataset does not support a large causal salary premium after adjustment.

The cleanest sentence I can defend is this: fully remote data-science roles look better paid in the raw file, but the adjusted estimate points to a small, uncertain premium.

## Method Notes

The workflow is the usual observational causal path: define treatment and outcome, choose pre-treatment controls, estimate propensity and outcome models, check balance and overlap, then report an AIPW effect with uncertainty.

The result also lines up with recent work-from-home wage research, where raw premiums shrink once worker selection, role quality, and job composition enter the model.

References I had in mind while building this:

- Chernozhukov et al. on double/debiased machine learning
- Robins, Rotnitzky, and Zhao on augmented inverse probability weighting
- Recent Federal Reserve work on work-from-home wage premiums

## Caveats

This is observational salary data. The file does not know company brand, exact city, equity, benefits, negotiation strength, team scope, applicant quality, or whether remote work was chosen by the worker.

I read this as a causal-analysis portfolio report, not a labor-market rule.

## Files

- `remote_work_salary_causal_inference.ipynb`: clean notebook
- `test_data_source.py`: smoke test for the public CSV
- `assets/`: charts used in this report
- `results_summary.json`: machine-readable output from the latest notebook run
