# GLP-1 Bayesian Pharmacovigilance

Analise Bayesiana de relatos adversos do openFDA/FAERS comparando Semaglutida e Tirzepatida desde janeiro de 2024.

## Objetivo

Estimar, entre os relatos espontaneos disponiveis, a probabilidade de a proporcao de notificacoes graves ser maior para Semaglutida do que para Tirzepatida.

## Fonte de dados

- API: openFDA Drug Adverse Event API
- Campo temporal: `receiptdate`
- Campo de gravidade: `serious`
- Janela: de `20240101` ate a data de execucao

## Arquivos

- `portfolio_glp1_bayesian.ipynb`: notebook principal limpo, sem outputs pesados.
- `test_fda_api.py`: smoke test da API e dos campos essenciais.

## Como validar

```bash
python test_fda_api.py
jupyter nbconvert --to notebook --execute portfolio_glp1_bayesian.ipynb --output portfolio_glp1_bayesian_executed.ipynb
```

## Limitacoes

FAERS/openFDA contem notificacoes espontaneas. A analise e adequada para sinalizacao e priorizacao de investigacao, mas nao estima incidencia populacional, nao controla exposicao e nao prova causalidade clinica.
