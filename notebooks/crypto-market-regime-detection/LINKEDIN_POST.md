# LinkedIn post draft

Visuals:

- `assets/linkedin_crypto_regime_carousel_01.png`
- `assets/linkedin_crypto_regime_carousel_02.png`
- `assets/linkedin_crypto_regime_carousel_03.png`
- `assets/linkedin_crypto_regime_carousel_04.png`
- `assets/linkedin_crypto_regime_carousel_05.png`

Project link: https://github.com/luandarodrigues/projectsforjupyternotebook/tree/main/notebooks/crypto-market-regime-detection

## Post

BTC muda de humor rápido.

Tem períodos em que o mercado parece calmo e direcional. Em outros, o preço sobe com volatilidade demais por trás. E tem os trechos em que a queda ainda não parece totalmente resolvida.

Eu queria testar uma pergunta bem prática para análise de dados: dá para separar esses períodos sem fingir que o modelo está prevendo preço?

Montei um notebook com candles diários de BTC/USDT e ETH/USDT da Binance, usando dados de 2023-03-31 a 2026-07-06. A partir disso, construí features de retorno, tendência, volatilidade, drawdown, volume e força relativa ETH/BTC.

O modelo principal é um Gaussian Mixture Model. Ele selecionou 4 regimes por BIC na janela de treino, com 20% da série deixada para uma checagem fora da amostra.

A leitura mais recente caiu em `Stress / drawdown`, com probabilidade de 66.1%. Esse número é importante porque não soa como certeza. Ele sugere que o BTC estava perto de uma fronteira de regime, não cravado no centro de um estado limpo.

Também rodei checks para não deixar o notebook bonito demais: comparação com KMeans e buckets de volatilidade, matriz de transição, métricas de risco e bootstrap de estabilidade. O bootstrap deu ARI mediano de 0.42, então eu leio os regimes como estrutura útil, não como taxonomia fixa.

Esse projeto não é recomendação de trade. É um relatório estatístico para olhar contexto de mercado com um pouco mais de disciplina.

Repo:
https://github.com/luandarodrigues/projectsforjupyternotebook/tree/main/notebooks/crypto-market-regime-detection

#DataScience #TimeSeries #Crypto #MachineLearning #Python

## Carousel story

1. BTC changes state fast.
2. The model reads market structure, not headlines.
3. GMM selected 4 regimes.
4. Latest state: stress/drawdown, 66.1%.
5. Useful context, not a trading signal.
