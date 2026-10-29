# 5. Resultados citados no resumo do trabalho

Este documento existe para que qualquer pessoa confira os números do resumo. Tudo é determinístico: com as mesmas sementes, o site e o script em Python dão exatamente os mesmos resultados.

## 5.1 Protocolo

| Item | Valor |
|---|---|
| Rodadas por simulação | 100 |
| Posts por rodada (tamanho do feed) | 10 |
| Simulações por média | 40, com as sementes 0 a 39 |
| Regra A (só engajamento) | γ = 2, sem exploração, sem teto |
| Teto | nenhum tema ocupa mais de 40% do feed |
| Usuário neutro | 30% de chance de clicar em qualquer tema |
| Usuário fiel | 75% de chance em Esporte, 15% nos outros quatro |
| Usuário reativo | 36% de chance em "Polêmica", 30% nos outros (prêmio de 20%) |
| Gerador de números aleatórios | mulberry32 (o mesmo no site e no Python) |

Medidas:

- Diversidade do feed: entropia de Shannon normalizada, de 0 (um tema só) a 1 (todos os temas igualmente presentes).
- Curtidas por 100 posts: fração de posts que receberam clique, vezes 100. É um proxy de receita, porque numa plataforma de anúncios a receita cresce com os cliques.
- Tema dominante: o tema com mais posts nas últimas 20 rodadas.

## 5.2 Resultados

| Resultado | Valor |
|---|---|
| Diversidade do usuário neutro, só engajamento | 0,86 na rodada 1, 0,05 na rodada 100 |
| Diversidade do usuário neutro, teto de 40% | 0,66 na rodada 100 |
| Curtidas por 100 posts do usuário fiel, só engajamento | 73 |
| Curtidas por 100 posts do usuário fiel, teto de 40% | 39 |
| "Polêmica" domina o feed (200 simulações) | 28% com o prêmio de 20%, contra 20% sem prêmio |
| Parcela média de "Polêmica" nas últimas 20 rodadas | 28% com o prêmio, contra 19% sem prêmio |

Leitura:

- Sem nenhuma preferência do usuário, a regra de só engajamento leva o feed de bem variado a quase um tema só.
- O teto de 40% mantém a diversidade em torno de dois terços, e para o usuário neutro isso não custa curtidas.
- Para o usuário de gosto concentrado, o mesmo teto reduz as curtidas em cerca de 47% (de 73 para 39). Esse é o custo econômico da regra alternativa.
- Um prêmio de 20% no engajamento do conteúdo caça-clique eleva a chance de ele dominar o feed de 20% para 28%. É uma tendência, não uma regra: o resultado ainda depende muito do acaso do início.

## 5.3 Como reproduzir

No site, ligue o Modo nerd, vá ao passo 4 e use o bloco Resultados do resumo (reprodutível).

Em Python (só biblioteca padrão):

```bash
python python/reproduzir_resumo.py
```

A saída deve ser:

```text
1) Diversidade do feed (1 = variado, 0 = um tema só), usuário neutro
   só engajamento: rodada 1 = 0.86  |  rodada 100 = 0.05
   teto de 40%:    rodada 100 = 0.66

2) Curtidas por 100 posts (proxy de receita), usuário fiel
   só engajamento: 73  |  teto de 40%: 39

3) Prêmio de engajamento para 'Polêmica' (200 simulações)
   'Polêmica' domina o feed em 28% das simulações (sem prêmio: 20%)
   parcela média de 'Polêmica' nas últimas 20 rodadas: 28% (sem prêmio: 19%)
```

## 5.4 Por que os números podem variar um pouco

- Com outras sementes, o resultado muda na segunda casa decimal. Por exemplo, com sementes diferentes a diversidade inicial do usuário neutro fica entre 0,85 e 0,88. Por isso o resumo diz "cerca de".
- Mudar qualquer item do protocolo (rodadas, tamanho do feed, γ, usuários) muda os resultados. Os arquivos `python/simulacao_feedback_loop.py` e `python/reproduzir_resumo.py` mostram onde mexer.
- O modelo é didático: ilustra um mecanismo e não mede nenhuma plataforma real.

## 5.5 O painel do negócio (passo 4)

O painel testa 64 regras (γ de 0 a 3, ε de 0% a 30%, teto de 30%, 40%, 60% ou sem teto) e mostra, para cada uma, a receita fictícia por 1.000 posts e a diversidade final. Os círculos vazios formam a fronteira: nenhuma outra regra dá, ao mesmo tempo, mais receita e mais diversidade.

Exemplo com o usuário fiel e R$ 0,20 por clique (médias de 20 simulações por regra):

| Regra | Receita por 1.000 posts | Diversidade final |
|---|---|---|
| A, só engajamento | R$ 146,80 | 0,00 |
| C, teto de 40% | R$ 78,12 (queda de 47%) | 0,67 |
| Melhor regra que mantém 90% da receita de A (γ = 2, ε = 10%) | R$ 137,32 | 0,10 |

A lição econômica: para um usuário de gosto concentrado, a diversidade é cara, e pouca receita sacrificada compra pouca diversidade. Para o usuário neutro, ela quase não custa nada. O custo aparece quando o interesse do usuário é estreito.

Próximo documento: [`06-referencias.md`](06-referencias.md).
