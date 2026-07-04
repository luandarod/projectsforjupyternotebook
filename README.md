# Notebooks Portfolio

Projetos de análise em notebooks, com foco em reprodutibilidade, narrativa executiva e validação automatizada.

## Catalogo

- `notebooks/glp1-bayesian-farmacovigilancia/`: analise Bayesiana de relatos adversos no openFDA/FAERS para Semaglutida vs Tirzepatida.

## Como rodar

```bash
python -m pip install -r requirements.txt
python notebooks/glp1-bayesian-farmacovigilancia/test_fda_api.py
python scripts/normalize_notebook.py notebooks/glp1-bayesian-farmacovigilancia/portfolio_glp1_bayesian.ipynb
```

Para executar um notebook inteiro localmente:

```bash
jupyter nbconvert --to notebook --execute notebooks/glp1-bayesian-farmacovigilancia/portfolio_glp1_bayesian.ipynb --output portfolio_glp1_bayesian_executed.ipynb
```

## Padrao de processo

1. Notebook limpo no Git, sem outputs pesados.
2. README curto com objetivo, fonte de dados, como rodar e limitacoes.
3. Smoke test para dependencias externas.
4. Execucao completa antes de publicar.
5. Conclusoes separadas de limitacoes metodologicas.
