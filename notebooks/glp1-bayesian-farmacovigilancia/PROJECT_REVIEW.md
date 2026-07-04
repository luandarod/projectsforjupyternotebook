# Project review: GLP-1 Bayesian pharmacovigilance

## What works

- The topic has a real hook: GLP-1 drugs, public safety reports, and Bayesian uncertainty in one notebook.
- The notebook runs against live openFDA data instead of a frozen sample.
- The result is easy to read because it answers a probability question instead of stopping at a p-value.
- The caveats are now visible. That matters here because FAERS data is easy to overread.

## What changed

- API calls now use a timeout and fail loudly when the response is not usable.
- The end date follows the day the notebook runs.
- The notebook prints the `last_updated` value returned by openFDA.
- Posterior summaries include 95% credible intervals.
- The Monte Carlo step uses a fixed random seed.
- `test_fda_api.py` checks that the endpoint still returns serious and non-serious counts.
- The committed notebook is clean, so Git diffs stay readable.

## Next pass

- Move repeated notebook code into a small Python module once there is a second project using the same pattern.
- Add a `Makefile` if the command list grows past three or four lines.
- Save one lightweight chart image in `assets/` so the GitHub page has a quick visual preview.
- Consider `nbstripout` later. The current `normalize_notebook.py` is enough for now.
- Keep the GitHub Action small. It should catch broken notebooks, not become a second project.

## Caveats to keep

- FAERS/openFDA does not measure population incidence.
- There is no denominator for exposed patients.
- Spontaneous reports are shaped by notoriety, underreporting, duplicates, and perceived severity.
- The result is a pharmacovigilance signal. It is not a clinical causal conclusion.
