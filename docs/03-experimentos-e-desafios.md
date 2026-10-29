# 3. Experimentos e desafios

Aqui você sai de "entender" para "testar". Cada experimento tem uma pergunta, um jeito de fazer e o que observar. Tente prever antes de rodar: é assim que se aprende mais.

Você pode fazer tudo no site (com o Modo nerd ligado) ou em Python (`python/simulacao_feedback_loop.py`).

## Experimento 1: o histórico pesa demais?

*Pergunta:* o que acontece com a diversidade se o histórico pesar menos?

*Como fazer (site):* Modo nerd → passo 2 → controle γ em 1 → passo 4 → *Rodar laboratório*.
*Como fazer (Python):* `python python/simulacao_feedback_loop.py --gama 1`

*O que observar:* com γ = 2 e usuário neutro, a diversidade final cai para perto de 0 (um tema domina). Com γ = 1, ela se mantém bem mais alta (no site, em torno de 0,7; no Python, parecido).

*Para pensar:* γ = 1 significa "chance proporcional às curtidas". γ = 2 significa "quem tem mais, ganha desproporcionalmente". Qual dos dois se parece mais com um sistema que otimiza só engajamento? Por quê?

## Experimento 2: um pouco de sorte ajuda?

*Pergunta:* reservar uma parte do feed para temas aleatórios resolve?

*Como fazer:* `--epsilon 0.1`, depois `0.2`, depois `0.3`.

*O que observar:* a diversidade sobe, mas o tema dominante continua ocupando boa parte do feed. A exploração ajuda, mas sozinha não elimina o efeito.

*Para pensar:* por que uma plataforma real usaria exploração? (Dica: ela também precisa descobrir do que você gosta.)

## Experimento 3: o custo do teto

*Pergunta:* limitar cada tema a 40% do feed custa engajamento?

**Como fazer:**

```
python python/simulacao_feedback_loop.py --usuario neutro --teto 0.4
python python/simulacao_feedback_loop.py --usuario fiel   --teto 0.4
```

*O que observar:* para o usuário neutro, o teto quase não custa engajamento. Para o usuário fiel (que gosta de Esporte), o engajamento cai bastante (nas rodadas de teste, de cerca de 73 para cerca de 39 curtidas a cada 100 posts), porque o sistema passa a mostrar coisas que ele gosta menos.

*Para pensar:* isto explica por que uma empresa que ganha com atenção pode hesitar em adotar um teto de diversidade. Quem deveria decidir isso: a empresa, o usuário ou a lei?

## Experimento 4: o gosto do usuário importa?

*Pergunta:* o que é culpa do sistema e o que é escolha do usuário?

*Como fazer:* rode as quatro combinações e compare o "tema dominante":

```
--usuario neutro            # sem preferência
--usuario fiel              # com preferência forte
--usuario neutro --teto 0.4
--usuario fiel   --teto 0.4
```

**O que observar:**

- *Neutro sem teto:* o feed concentra mesmo sem preferência do usuário. A bolha vem do sistema.
- *Fiel sem teto:* escolha do usuário e amplificação do sistema se somam.
- *Fiel com teto:* o teto limita o que o sistema entrega, mas não muda o que o usuário quer.

Este é o experimento 2×2 do passo 4 do site.

## Desafios do laboratório (modo nerd)

O laboratório do passo 4 tem três desafios, com verificação automática (✔ concluído):

1. Sem teto, mantenha a diversidade final do usuário neutro em 0,5 ou mais. Dica: pense no γ.
2. Deixe o tema dominante do usuário fiel abaixo de 60% do feed, mantendo pelo menos 90% do engajamento da regra A. Este é difícil: tente combinar parâmetros. Existe solução? Se achar que não, explique por que o objetivo é contraditório.
3. Faça o feed do usuário neutro colapsar mais rápido que na regra A (compare a rodada 20).

## Desafios de código (para quem quer programar)

Nível 1, mexer:

- Troque os nomes e as cores dos temas em `TEMAS`.
- Aumente `TOTAL_R` de 8 para 12 rodadas.
- Mude o tamanho do feed (`TAM`) de 6 para 8.

Nível 2, acrescentar:

- Crie uma regra D em `CFG` que combine ε e teto. Descubra a melhor combinação.
- No Python, adicione um novo perfil em `USUARIOS` (por exemplo, "curioso": clica mais em temas que viu pouco).
- Exporte a diversidade média para CSV e abra em uma planilha para fazer o gráfico.

Nível 3, criar:

- Usuário que muda de gosto: a cada 20 rodadas, o tema favorito muda. A bolha "desgruda"? Quanto tempo leva?
- Criadores que reagem: a cada rodada, aumente o número de manchetes do tema que recebeu mais curtidas. Isso acelera a bolha?
- Teste estatístico: rode 200 sementes por regra e use um teste (por exemplo, t de Welch) para dizer se a diferença entre A e C é estatisticamente significativa.
- Outra métrica de diversidade: troque a entropia pelo índice de Gini-Simpson e compare.

## Como registrar o que você descobriu

Anote em uma tabela: regra, parâmetros, usuário, diversidade final, tema dominante, engajamento. Compartilhe com sua turma e compare: os resultados batem? Se não, o que mudou (semente, parâmetros, número de rodadas)?

Uma boa pergunta científica diz o que você mudou, o que mediu e o que esperava. Escreva isso antes de rodar.

Próximo documento: [`04-para-ir-alem.md`](04-para-ir-alem.md).
