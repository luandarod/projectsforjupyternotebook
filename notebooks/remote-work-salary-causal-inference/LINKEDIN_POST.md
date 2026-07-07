# LinkedIn post draft

Visual: `assets/linkedin_remote_salary_causal_quiet.png`

Project link: https://github.com/luandarodrigues/projectsforjupyternotebook/tree/main/notebooks/remote-work-salary-causal-inference

## Post

Trabalho remoto aparece melhor pago no dado bruto. Neste dataset, vagas de dados 100% remotas mostram um gap salarial de cerca de 12.1% em relação às vagas presenciais.

Esse é exatamente o tipo de número que eu não queria postar sem mexer na estrutura por trás.

No projeto, tratei trabalho remoto como exposição e salário como desfecho. Depois ajustei a comparação por ano, senioridade, família de cargo, mercado do funcionário, mercado da empresa e porte da empresa.

O modelo principal usa AIPW com cross-fitting. Também deixei no notebook checagens de overlap, balanceamento, DML, IPW, matching e um teste simples de sensibilidade para confundimento omitido.

Depois do ajuste, o prêmio remoto cai para cerca de 2.4%. O intervalo de 95% vai de -8.2% a +14.2%, então eu não venderia isso como evidência forte de um grande prêmio causal.

Minha leitura: vagas remotas parecem mais bem pagas no arquivo bruto porque os grupos não são comparáveis o bastante no primeiro olhar. Quando as diferenças visíveis de cargo e mercado entram no modelo, a história fica menor e mais incerta.

Foi isso que eu mais gostei nesse notebook. O resultado interessante não foi encontrar um prêmio enorme. Foi ver o primeiro número perder confiança.

Repo:
https://github.com/luandarodrigues/projectsforjupyternotebook/tree/main/notebooks/remote-work-salary-causal-inference

#DataScience #CausalInference #Statistics #Python #RemoteWork

## Visual plan

Use `assets/linkedin_remote_salary_causal_quiet.png` as the single image for the post.

For a later carousel, I would use four pages:

1. Raw gap: fully remote roles look better paid.
2. Adjustment: year, seniority, market, job family and company size.
3. Estimate: AIPW premium around 2.4% with a wide interval.
4. Caveat: observational data, not a labor-market law.
