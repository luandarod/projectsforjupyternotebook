# Literature review: Brazil inflation pressure and monetary policy regimes

Generated: 2026-07-06  
Review type: scoping review  
Scope: inflation targeting, exchange-rate pass-through, monetary policy rules, and regime methods  

## Research Question

How can public Brazilian macro series be used to identify inflation-pressure regimes after the adoption of inflation targeting, and how should those regimes be interpreted given the literature on credibility, exchange-rate pass-through, and monetary policy reaction functions?

## Search Strategy

The search focused on peer-reviewed papers, central-bank working papers, NBER material, and official data documentation.

| Source | Date searched | Query | Screened use |
| --- | --- | --- | --- |
| Banco Central do Brasil / RePEc | 2026-07-06 | `Implementing Inflation Targeting in Brazil Bogdanski Tombini Werlang` | inflation-targeting institutional setup |
| Journal of International Money and Finance / BCB | 2026-07-06 | `Inflation Targeting in Brazil constructing credibility exchange rate volatility Minella Freitas Goldfajn Muinhos` | credibility, expectations, pass-through |
| NBER / IDEAS | 2026-07-06 | `exchange rate pass-through inflation targeting emerging markets Edwards` | exchange-rate pass-through under inflation targeting |
| Econometrica / JSTOR | 2026-07-06 | `Hamilton 1989 regime switching nonstationary time series` | regime-switching motivation |
| Carnegie-Rochester / Stanford | 2026-07-06 | `Taylor 1993 Discretion versus policy rules in practice` | policy-rule framing |
| AEA / NBER | 2026-07-06 | `Clarida Gali Gertler 1999 science of monetary policy` | inflation targeting and policy-rule background |
| BCB Open Data | 2026-07-06 | `BCData SGS API formato json dataInicial dataFinal` | data access and reproducibility |

## Inclusion Criteria

- Brazil-specific inflation targeting or monetary policy papers
- exchange-rate pass-through papers relevant to inflation-targeting economies
- core regime-switching or policy-rule references
- official documentation for the BCB/SGS data source

## Exclusion Criteria

- market commentary without methodology
- sources without identifiable author, institution, or publication venue
- papers focused only on fiscal policy, credit, or labor markets without an inflation-policy link

## Evidence Summary

| Study | Design | Data / Scope | Method | What I used it for | Limitation |
| --- | --- | --- | --- | --- | --- |
| Bogdanski, Tombini & Werlang (2000) | central-bank working paper | early Brazilian inflation targeting | institutional and policy framework | why IPCA and Selic belong at the center of the project | early regime period |
| Minella, Freitas, Goldfajn & Muinhos (2003) | academic / central-bank empirical paper | Brazil after 1999 inflation targeting | empirical assessment of credibility, expectations, persistence, pass-through | why exchange-rate volatility and credibility matter in Brazil | focuses on early years of inflation targeting |
| Edwards (2006) | NBER working paper | inflation-targeting countries | exchange-rate pass-through analysis | why pass-through is a natural diagnostic in open economies | cross-country scope, not Brazil-only |
| Hamilton (1989) | econometric theory paper | macro time series | Markov regime-switching model | motivation for thinking in regimes rather than one constant macro state | the notebook uses GMM, not a Hamilton Markov model |
| Taylor (1993) | monetary policy paper | policy-rule framework | simple policy-rule reasoning | why inflation and interest-rate reaction belong together | not Brazil-specific |
| Clarida, Gali & Gertler (1999) | literature review / theory | New Keynesian monetary policy | policy-rule and credibility framework | macro background for inflation targeting | theoretical, not an applied Brazil notebook |
| BCB SGS documentation | official data documentation | Brazilian time series | public JSON API | data source and reproducibility | API limits require chunked calls for long daily series |

## Synthesis

Brazil's inflation-targeting literature treats credibility, exchange-rate volatility, and monetary-policy reaction as connected. That shaped the feature set. IPCA measures the target variable, Selic is the policy instrument, USD/BRL captures an open-economy shock channel, and the ex-post real rate gives a rough measure of policy tightness.

The pass-through literature argues against reading FX moves mechanically. Exchange-rate depreciation can matter for inflation, but the coefficient changes with credibility, policy reaction, administered prices, and the state of the economy. For that reason, the notebook uses a rolling pass-through regression as a diagnostic signal, not a causal estimate.

The regime literature gives the project its modeling frame. A single average relationship is a poor summary of Brazil's macro history since 2002. The notebook uses GMM instead of a full Markov-switching model because it keeps the project transparent and dependency-light, but the interpretation borrows the same caution: regimes are latent labels, not observed truth.

## Gaps and Limitations

- The notebook does not include inflation expectations, output gap, fiscal variables, commodity prices, administered prices, credit, or survey data.
- The pass-through regression is reduced-form and rolling. It should not be read as structural causality.
- GMM assigns regimes by feature distribution but does not model transition probabilities the way a hidden Markov model would.
- The latest IPCA observation limits the data end date. Daily BCB series may be newer than monthly inflation.

## References

- Bogdanski, J., Tombini, A. A., & Werlang, S. R. C. (2000). *Implementing Inflation Targeting in Brazil*. Banco Central do Brasil Working Paper No. 1. https://ideas.repec.org/p/bcb/wpaper/1.html
- Minella, A., Freitas, P. S., Goldfajn, I., & Muinhos, M. K. (2003). *Inflation Targeting in Brazil: Constructing Credibility under Exchange Rate Volatility*. Journal of International Money and Finance, 22(7), 1015-1040. https://ideas.repec.org/a/eee/jimfin/v22y2003i7p1015-1040.html
- Edwards, S. (2006). *The Relationship Between Exchange Rates and Inflation Targeting Revisited*. NBER Working Paper No. 12163. https://www.nber.org/system/files/working_papers/w12163/w12163.pdf
- Hamilton, J. D. (1989). *A New Approach to the Economic Analysis of Nonstationary Time Series and the Business Cycle*. Econometrica, 57(2), 357-384. https://www.jstor.org/stable/1912559
- Taylor, J. B. (1993). *Discretion versus Policy Rules in Practice*. Carnegie-Rochester Conference Series on Public Policy, 39, 195-214. https://web.stanford.edu/~johntayl/Onlinepaperscombinedbyyear/1993/Discretion_versus_Policy_Rules_in_Practice.pdf
- Clarida, R., Gali, J., & Gertler, M. (1999). *The Science of Monetary Policy: A New Keynesian Perspective*. Journal of Economic Literature, 37(4), 1661-1707. https://www.aeaweb.org/articles?id=10.1257%2Fjel.37.4.1661
- Banco Central do Brasil. *Sistema Gerenciador de Series Temporais / BCData SGS API*. https://dadosabertos.bcb.gov.br/dataset/20542-saldo-da-carteira-de-credito-com-recursos-livres---total/resource/6e2b0c97-afab-4790-b8aa-b9542923cf88
