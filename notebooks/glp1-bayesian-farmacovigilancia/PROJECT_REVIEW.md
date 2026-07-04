# Revisao do Projeto: GLP-1 Bayesian Pharmacovigilance

## O que esta bom

- Tema forte para portfolio: combina saude, dados publicos, estatistica Bayesiana e comunicacao executiva.
- Notebook agora roda de ponta a ponta com dados reais do openFDA.
- O resultado estatistico e apresentado como probabilidade direta, o que facilita decisao executiva.
- O notebook inclui limitacoes metodologicas importantes sobre FAERS/openFDA.

## Melhorias feitas

- Adicionado tratamento de erro e timeout nas chamadas da API.
- Janela de coleta atualizada dinamicamente ate a data de execucao.
- Incluido `last_updated` retornado pela openFDA.
- Adicionados intervalos crediveis e simulacao Monte Carlo reproduzivel.
- Criado smoke test da API com asserts.
- Corrigido o gerador/normalizador para evitar sobrescrever o notebook com texto corrompido.
- Notebook limpo para versionamento, sem outputs pesados.

## Melhorias recomendadas para uma proxima iteracao

- Separar codigo reutilizavel em um modulo Python quando houver mais notebooks no repo.
- Adicionar `Makefile` ou `noxfile.py` para comandos padronizados: instalar, testar, executar notebook, limpar outputs.
- Criar um template unico de README para cada notebook: problema, dados, metodologia, resultado, limitacoes, como rodar.
- Salvar imagens estaticas leves dos graficos principais em `assets/` para preview no GitHub.
- Usar `nbstripout` ou um check simples de CI para impedir outputs grandes em notebooks versionados.
- Adicionar GitHub Actions para rodar smoke tests e validar notebooks a cada push.

## Riscos metodologicos que devem continuar explicitos

- FAERS/openFDA nao mede incidencia populacional.
- Nao ha denominador de pacientes expostos.
- Relatos espontaneos sofrem vies de notoriedade, subnotificacao, duplicidade e severidade percebida.
- O resultado e sinal de farmacovigilancia, nao conclusao causal clinica.
