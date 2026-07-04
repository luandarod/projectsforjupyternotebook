# Jupyter Notebook Projects

Portfolio repository for data analysis notebooks, with a focus on reproducibility, clear executive storytelling, and lightweight validation.

[![Notebook checks](https://github.com/luandarodrigues/projectsforjupyternotebook/actions/workflows/notebook-checks.yml/badge.svg)](https://github.com/luandarodrigues/projectsforjupyternotebook/actions/workflows/notebook-checks.yml)

## Projects

| Project | Theme | Status |
| --- | --- | --- |
| [GLP-1 Bayesian Pharmacovigilance](notebooks/glp1-bayesian-farmacovigilancia/) | Bayesian analysis of openFDA/FAERS adverse-event reports for Semaglutide vs Tirzepatide | Published |

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

## How To Run

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the project smoke test:

```bash
python notebooks/glp1-bayesian-farmacovigilancia/test_fda_api.py
```

Validate that the notebook is clean for version control:

```bash
python scripts/normalize_notebook.py notebooks/glp1-bayesian-farmacovigilancia/portfolio_glp1_bayesian.ipynb --check
```

Execute the notebook locally:

```bash
jupyter nbconvert --to notebook --execute notebooks/glp1-bayesian-farmacovigilancia/portfolio_glp1_bayesian.ipynb --output portfolio_glp1_bayesian_executed.ipynb
```

## Notebook Standards

- Keep committed notebooks clean, without heavy outputs or execution counts.
- Each project gets its own folder under `notebooks/`.
- Each project includes a short README with objective, data source, methodology, validation steps, and limitations.
- External data/API dependencies should have a smoke test.
- Conclusions should be separated from methodological limitations.
- Generated or executed notebooks should stay out of Git unless there is a clear reason to publish them.

## Next Additions

Planned future notebooks will follow the same structure so the repository remains easy to scan, test, and extend.
