# Project audit

Checked on 2026-07-07.

## GLP-1 Bayesian pharmacovigilance

Academic fit: defensible as pharmacovigilance signal work. The notebook uses FAERS/openFDA reports and a Beta-Binomial model to compare serious-report proportions for Semaglutide and Tirzepatide. The key strength is the framing: the README says clearly that FAERS has no patient denominator and cannot support a clinical causality claim.

Relevance: high. GLP-1 safety is visible in public discussion, and the project shows how to stay careful with public adverse-event data.

Writing check: human enough. The caveat language is direct and avoids inflated claims.

Next improvement: add one small result chart from the notebook into `assets/`, then reference it in the README before posting a second version.

## Remote work salary premium

Academic fit: strong for a portfolio project. It uses an observational causal design with a declared treatment, outcome, adjustment set, overlap checks, covariate balance, cross-fit AIPW, DML, IPW, matching and sensitivity analysis. The conclusion does not overstate causality.

Relevance: high. Remote-work pay is still a live labor-market question, and the result is useful because the raw gap changes after adjustment.

Writing check: human enough. The report has specific numbers and a plain interpretation.

Next improvement: replace the generic source note with a pinned dataset citation, including retrieval date and original Kaggle/GitHub source if available.

## Crypto market regime detection

Academic fit: defensible as unsupervised financial time-series analysis. The notebook uses recent Binance BTC/ETH data, GMM model selection by BIC, a holdout window, baseline comparison and bootstrap stability. It avoids trading claims, which is the right boundary.

Relevance: high, but time-sensitive. The report is strongest when it is rerun before posting because market regimes decay quickly.

Writing check: human enough. The README names the latest regime probability and admits when the label is close to a boundary.

Next improvement: add a short bibliographic note on regime-switching, mixture models and volatility clustering. That would make the method base look less like a notebook choice and more like an academic modeling decision.

## Brazil inflation and monetary regimes

Academic fit: strong for a macro portfolio report. It has a literature review, BCB/SGS data, a declared feature set, train/test model selection, baselines and stability checks. The pass-through section is framed as diagnostic instead of causal.

Relevance: high. It uses public Brazilian macro data through 2026 and connects the result to inflation targeting, exchange-rate pressure and policy rates.

Writing check: human enough. The report is specific, cautious and readable.

Next improvement: add expectations, output gap or a fiscal proxy in a later version. The current caveats already say that.

## Overall read

The four projects are coherent together. They cover Bayesian modeling, causal inference, unsupervised financial regimes and applied macroeconomics. The main academic risk is overclaiming, and the current README files mostly avoid that. I would post them as portfolio reports, not as papers.

The weakest presentation gap is GLP-1 because it has no chart asset committed yet. The weakest methodology gap is crypto because the academic base is implied by diagnostics rather than documented through references. Remote work and Brazil macro are the most complete right now.
