# Literature review: Brazil inflation pressure and monetary policy regimes

Generated: 2026-07-06  
Review type: scoping review  
Scope: inflation targeting, exchange-rate pass-through, policy rules and regime methods  

## Research Question

Can public Brazilian macro series be used to map inflation-pressure regimes after the adoption of inflation targeting? And once the regimes are estimated, how much caution should we bring from the literature on credibility, exchange-rate pass-through and monetary-policy reaction functions?

## Search Strategy

I kept the search narrow. The notebook is not trying to review all Brazilian macroeconomics. It needs enough literature to justify the variables and the interpretation.

| Source | Date searched | Query | Why it stayed in |
| --- | --- | --- | --- |
| Banco Central do Brasil / RePEc | 2026-07-06 | `Implementing Inflation Targeting in Brazil Bogdanski Tombini Werlang` | institutional setup of the inflation-targeting regime |
| Journal of International Money and Finance / BCB | 2026-07-06 | `Inflation Targeting in Brazil constructing credibility exchange rate volatility Minella Freitas Goldfajn Muinhos` | Brazil-specific credibility, expectations and pass-through |
| NBER / IDEAS | 2026-07-06 | `exchange rate pass-through inflation targeting emerging markets Edwards` | cross-country pass-through under inflation targeting |
| Econometrica / JSTOR | 2026-07-06 | `Hamilton 1989 regime switching nonstationary time series` | the original regime-switching frame |
| Carnegie-Rochester / Stanford | 2026-07-06 | `Taylor 1993 Discretion versus policy rules in practice` | simple policy-rule logic |
| AEA / NBER | 2026-07-06 | `Clarida Gali Gertler 1999 science of monetary policy` | inflation targeting, commitment and policy reaction |
| BCB Open Data | 2026-07-06 | `BCData SGS API formato json dataInicial dataFinal` | data access and reproducibility |

## What I Included

- Brazil-specific work on inflation targeting or monetary policy
- papers on exchange-rate pass-through in inflation-targeting economies
- core references on regime-switching and policy rules
- official documentation for the BCB/SGS data source

I left out market commentary, unnamed sources, and papers that were only about fiscal policy, labor markets or credit without a clear inflation-policy link.

## Evidence Notes

| Study | Design | Data / Scope | Method | How it shaped the notebook | Main limit |
| --- | --- | --- | --- | --- | --- |
| Bogdanski, Tombini & Werlang (2000) | central-bank working paper | early Brazilian inflation targeting | institutional and policy description | anchors IPCA and Selic as the core variables | early regime period |
| Minella, Freitas, Goldfajn & Muinhos (2003) | empirical paper | Brazil after 1999 | credibility, expectations, persistence, pass-through | motivates exchange-rate volatility and credibility as part of the feature set | mostly early inflation-targeting years |
| Edwards (2006) | NBER working paper | inflation-targeting countries | pass-through comparison | keeps the FX coefficient from being read mechanically | cross-country, not Brazil-only |
| Hamilton (1989) | econometric theory paper | macro time series | Markov regime-switching | motivates looking for states instead of one average relationship | the notebook uses GMM, not a Hamilton model |
| Taylor (1993) | monetary policy paper | policy-rule framework | rule-based policy reasoning | links inflation and interest-rate reaction | not Brazil-specific |
| Clarida, Gali & Gertler (1999) | theory / review | New Keynesian monetary policy | policy-rule and credibility framework | background for inflation targeting and commitment | theoretical |
| BCB SGS documentation | official documentation | Brazilian time series | public JSON API | source for the data pipeline | long daily series need chunked calls |

## Synthesis

The Brazil papers treat inflation targeting as a credibility problem as much as a price-index problem. That is why the notebook does not stop at IPCA. It brings in Selic, USD/BRL and an ex-post real policy rate. Those are rough variables, but they map cleanly to the questions in Bogdanski et al. and Minella et al.

The pass-through papers are the main warning label. A weaker exchange rate can feed inflation, but the coefficient is not stable across time or policy environments. In the notebook, the 60-month rolling regression is deliberately modest. It is a moving diagnostic, not a causal claim.

Hamilton gives the modeling intuition: macro relationships can switch states. I did not implement a full Markov-switching model here because the portfolio version needs to stay light and readable. GMM is easier to inspect, easier to rerun, and honest enough for a first regime map.

## Gaps

- No inflation expectations.
- No output gap.
- No fiscal series.
- No administered-price split.
- No commodity shocks, credit cycle or survey data.
- No full hidden Markov model.

Those omissions matter. The report still works as a compact macro notebook, but a central-bank-style model would need a much wider panel.

## References

- Bogdanski, J., Tombini, A. A., & Werlang, S. R. C. (2000). *Implementing Inflation Targeting in Brazil*. Banco Central do Brasil Working Paper No. 1. https://ideas.repec.org/p/bcb/wpaper/1.html
- Minella, A., Freitas, P. S., Goldfajn, I., & Muinhos, M. K. (2003). *Inflation Targeting in Brazil: Constructing Credibility under Exchange Rate Volatility*. Journal of International Money and Finance, 22(7), 1015-1040. https://ideas.repec.org/a/eee/jimfin/v22y2003i7p1015-1040.html
- Edwards, S. (2006). *The Relationship Between Exchange Rates and Inflation Targeting Revisited*. NBER Working Paper No. 12163. https://www.nber.org/system/files/working_papers/w12163/w12163.pdf
- Hamilton, J. D. (1989). *A New Approach to the Economic Analysis of Nonstationary Time Series and the Business Cycle*. Econometrica, 57(2), 357-384. https://www.jstor.org/stable/1912559
- Taylor, J. B. (1993). *Discretion versus Policy Rules in Practice*. Carnegie-Rochester Conference Series on Public Policy, 39, 195-214. https://web.stanford.edu/~johntayl/Onlinepaperscombinedbyyear/1993/Discretion_versus_Policy_Rules_in_Practice.pdf
- Clarida, R., Gali, J., & Gertler, M. (1999). *The Science of Monetary Policy: A New Keynesian Perspective*. Journal of Economic Literature, 37(4), 1661-1707. https://www.aeaweb.org/articles?id=10.1257%2Fjel.37.4.1661
- Banco Central do Brasil. *Sistema Gerenciador de Series Temporais / BCData SGS API*. https://dadosabertos.bcb.gov.br/dataset/20542-saldo-da-carteira-de-credito-com-recursos-livres---total/resource/6e2b0c97-afab-4790-b8aa-b9542923cf88
