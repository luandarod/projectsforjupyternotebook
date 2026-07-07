# LinkedIn post draft

Visuals:

- `assets/linkedin_brazil_macro_carousel_01.png`
- `assets/linkedin_brazil_macro_carousel_02.png`
- `assets/linkedin_brazil_macro_carousel_03.png`
- `assets/linkedin_brazil_macro_carousel_04.png`
- `assets/linkedin_brazil_macro_carousel_05.png`

Project link: https://github.com/luandarodrigues/projectsforjupyternotebook/tree/main/notebooks/brazil-inflation-monetary-regimes

## Post

Brasil é um caso macro bagunçado do jeito útil.

IPCA, dólar, Selic, juros reais e credibilidade passam pela mesma história, mas raramente se movem com a educação que a gente gostaria de ver em um gráfico limpo.

Nesse projeto eu puxei dados públicos do Banco Central do Brasil, via SGS/BCB, e montei um painel mensal de 2002-11 a 2026-02. A base final ficou com 280 meses de IPCA, USD/BRL e Selic.

A pergunta era direta: dá para separar fases de pressão inflacionária usando só séries públicas e um modelo que qualquer pessoa consiga reproduzir?

Usei um Gaussian Mixture Model com seleção por BIC na janela de treino. O modelo escolheu 4 regimes. Depois eu comparei com KMeans, uma baseline por quantis de inflação, matriz de transição e bootstrap de estabilidade.

A leitura mais recente caiu em `Inflation/fx pressure`. Em fevereiro de 2026, o IPCA 12m estava em 3.81%, a Selic anualizada em 14.90% e o juro real ex-post em 11.09%.

Eu não leria esse rótulo como manchete de crise. Ele vem do comportamento médio do cluster, não de um mês isolado. O ponto é mapear fases longas de pressão, câmbio e resposta monetária.

Também incluí uma base bibliográfica curta. Usei trabalhos sobre metas de inflação no Brasil, pass-through cambial, regras de política monetária e regime switching. Isso não valida o GMM. Ajuda a justificar por que IPCA, USD/BRL, Selic e juros reais pertencem ao mesmo notebook.

O relatório ainda é um projeto de portfólio. Não tem expectativas de inflação, hiato do produto, fiscal, preços administrados ou commodities. Mesmo assim, gostei do resultado porque ele junta dados públicos, estatística e literatura em uma análise que dá para abrir, rodar e criticar.

Repo:
https://github.com/luandarodrigues/projectsforjupyternotebook/tree/main/notebooks/brazil-inflation-monetary-regimes

#DataScience #Macroeconomics #TimeSeries #Python #Brazil

## Carousel story

1. Brazil macro pressure is messy, and that is the point.
2. The data comes from BCB/SGS.
3. The model separates 4 long regimes.
4. Latest state: inflation/fx pressure.
5. Useful map, not a central-bank model.
