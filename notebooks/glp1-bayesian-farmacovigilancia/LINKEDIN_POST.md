# LinkedIn post draft

Visual: `assets/linkedin_glp1_bayesian_quiet.png`

Project link: https://github.com/luandarodrigues/projectsforjupyternotebook/tree/main/notebooks/glp1-bayesian-farmacovigilancia

## Post

Nos últimos dias eu peguei um tema que aparece muito em conversa pública, mas que pede bastante cuidado estatístico: os relatos de segurança em medicamentos GLP-1.

O projeto não tenta responder "qual medicamento é mais seguro". Essa pergunta exigiria desenho clínico, denominador de exposição e controle de muita coisa que o FAERS não traz. O recorte aqui é mais honesto: usando dados públicos do openFDA/FAERS, comparei Semaglutide e Tirzepatide pela proporção de relatos marcados como serious reports.

Usei um modelo Beta-Binomial porque queria tratar a incerteza como parte do resultado, não como rodapé. Em vez de olhar só para uma diferença bruta, o notebook estima distribuições posteriores e intervalos críveis para a comparação.

A parte mais importante do trabalho foi manter o limite perto do resultado. FAERS é uma base de relatos espontâneos. Ela sofre com subnotificação, viés de atenção, possíveis duplicidades e ausência de denominador de pacientes expostos. Então o resultado entra como sinal de farmacovigilância. Não como conclusão causal.

Stack do projeto:
Python, pandas, openFDA API, inferência bayesiana, modelo Beta-Binomial, teste de API e notebook reprodutível.

Repo do projeto:
https://github.com/luandarodrigues/projectsforjupyternotebook/tree/main/notebooks/glp1-bayesian-farmacovigilancia

#DataScience #BayesianStatistics #Pharmacovigilance #Python #OpenFDA

## Visual plan

Use `assets/linkedin_glp1_bayesian_quiet.png` como imagem única no primeiro post.

Para um carrossel depois, eu faria quatro telas:

1. Pergunta: o que dá para aprender com FAERS sem transformar relato espontâneo em causalidade.
2. Método: Beta-Binomial e intervalos posteriores.
3. Resultado: comparação das proporções e incerteza.
4. Limite: sinal de farmacovigilância, não conclusão clínica.
