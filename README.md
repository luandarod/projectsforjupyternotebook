# Jupyter notebook projects

This repo is where I keep notebook-first data projects that are worth showing, rerunning, and improving later.

The rule is simple: a notebook should not be a loose dump of cells. Each project needs a short README, a way to test the outside data source, and a clean notebook committed without bulky outputs.

[![Notebook checks](https://github.com/luandarodrigues/projectsforjupyternotebook/actions/workflows/notebook-checks.yml/badge.svg)](https://github.com/luandarodrigues/projectsforjupyternotebook/actions/workflows/notebook-checks.yml)

## Projects

| Project | Theme | Status |
| --- | --- | --- |
| [GLP-1 Bayesian pharmacovigilance](notebooks/glp1-bayesian-farmacovigilancia/) | Semaglutide vs Tirzepatide adverse-event reports from openFDA/FAERS, modeled with a Beta-Binomial approach | Published |

## Repository Structure

```text
.
|-- notebooks/
|   `-- glp1-bayesian-farmacovigilancia/
|       |-- README.md
|       |-- PROJECT_REVIEW.md
|       |-- portfolio_glp1_bayesian.ipynb
|       `-- test_fda_api.py
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
