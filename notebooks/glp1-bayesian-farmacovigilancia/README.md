# GLP-1 Bayesian pharmacovigilance

This notebook looks at openFDA/FAERS adverse-event reports for Semaglutide and Tirzepatide from January 2024 onward.

The point is not to claim that one drug is clinically safer than the other. FAERS is not built for that. The point is narrower: among the reports available in openFDA, how different is the share of reports marked as serious?

## Question

Using a simple Bayesian Beta-Binomial model, the notebook estimates the probability that Semaglutide has a higher serious-report proportion than Tirzepatide in this reporting window.

## Data

- API: openFDA Drug Adverse Event API
- Date field: `receiptdate`
- Seriousness field: `serious`
- Window: `20240101` through the day the notebook is run

## Files

- `portfolio_glp1_bayesian.ipynb`: the clean notebook, committed without heavy outputs.
- `test_fda_api.py`: a small smoke test for the API response and the fields used by the notebook.

## Run it

```bash
python test_fda_api.py
jupyter nbconvert --to notebook --execute portfolio_glp1_bayesian.ipynb --output portfolio_glp1_bayesian_executed.ipynb
```

## Caveats

FAERS/openFDA contains spontaneous reports. There is no patient denominator here, no exposure adjustment, and no causal design. Treat this as signal work: useful for deciding what deserves a closer look, not for making a clinical claim by itself.
