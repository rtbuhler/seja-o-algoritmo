# 1. Conceitos: o que acontece dentro de um feed

Tempo de leitura: 10 minutos. Não precisa saber programar.

## 1.1 A pergunta

Quando você abre uma rede social, quem decidiu o que aparece primeiro? Existem quatro candidatos:

| Quem | O que faz |
|---|---|
| **O sistema** (o algoritmo) | Ordena o que mostrar, seguindo uma regra. |
| **A plataforma** (a empresa) | Escolhe qual número o sistema deve aumentar: cliques, tempo de tela, curtidas. |
| **Você** | Escolhe o que clicar, o que curtir, a quem seguir. |
| **Os criadores de conteúdo** | Produzem o que acham que vai render. |

Este projeto deixa você mexer em três deles e ver o resultado. O quarto, os criadores, aparece só como ideia para estender o modelo (veja `docs/04-para-ir-alem.md`).

## 1.2 Sistema de recomendação em uma frase

> Um sistema de recomendação é um programa que prevê o que você vai querer ver e ordena o feed com base nessa previsão.

Ele não "entende" o conteúdo como uma pessoa. Em geral, ele só conta e calcula: quantas pessoas curtiram, quanto tempo você ficou, o que pessoas parecidas com você fizeram.

## 1.3 Função objetivo (a "métrica")

Todo sistema de recomendação tenta aumentar um número. Esse número se chama função objetivo ou métrica.

- Se a métrica é "tempo de tela", o sistema aprende a mostrar o que prende você.
- Se a métrica é "curtidas", ele aprende a mostrar o que rende curtidas.

O sistema não precisa querer espalhar desinformação. Basta que conteúdo emocional e polêmico renda mais curtidas que conteúdo neutro. Aí a métrica faz o resto.

Resumo: o algoritmo faz o que a métrica pede.

## 1.4 Feedback loop (ciclo de realimentação)

Este é o mecanismo central do projeto.

```
Você curte  →  o sistema conta  →  recalcula o ranking  →  novo feed  →  você curte...
```

O sistema usa o resultado das próprias recomendações para decidir as próximas. Pequenas vantagens do começo crescem sozinhas, como uma bola de neve. É um *rich-get-richer*: quem tem mais, ganha mais.

No site, você vê isso em três lugares: na mensagem "o sistema anotou as curtidas", na tabela de chances do passo 2 e na rosca "Sua bolha agora".

## 1.5 Bolha e câmara de eco

São duas coisas diferentes, e a diferença responde à pergunta "quem escolheu?".

| Conceito | Quem causa | Exemplo |
|---|---|---|
| **Filtro-bolha** | A filtragem técnica da plataforma | O sistema só mostra o que combina com seu histórico. |
| **Câmara de eco** | A escolha das pessoas e dos grupos | Você segue só quem pensa como você e o grupo repete as mesmas ideias. |

Na vida real as duas se somam. No passo 3 do site, o gráfico "o que você curtiu × o que o sistema mostrou" separa uma da outra:

- "Você curtiu" é a sua escolha (se aproxima da câmara de eco).
- "Você viu" é o que o sistema entregou. Quando passa muito do que você curtiu, o sistema amplificou sua escolha (se aproxima do filtro-bolha).

Um cuidado: você só pode curtir o que aparece. Então preferência e exposição se influenciam. É por isso que o passo 4 usa usuários simulados com gosto fixo, para separar as duas coisas de verdade.

## 1.6 O ciclo da desinformação em três fases

O site se apoia no artigo *Economia da desinformação e sistemas algorítmicos* (Angelo e Nogueira, RICEM 2026, Revista de Iniciação Científica do Ensino Médio), que usa o modelo de três fases de Jesus-Silva (2026):

1. Criação: conteúdo feito para gerar engajamento, às vezes imitando a aparência de jornal. No site: as manchetes, algumas em estilo caça-clique.
2. Disseminação: a plataforma coleta dados e ordena o feed. No site: o sorteio por curtidas.
3. Recirculação: o que engajou volta a circular e realimenta o sistema. No site: suas curtidas virando dado.

Há ainda o efeito de verdade ilusória: ver algo repetidas vezes aumenta a sensação de que é verdade. É um dos motivos de a recirculação ser tão eficaz.

## 1.7 O que a pesquisa diz (e o que ela não diz)

O efeito real das bolhas é disputado. Pesquisadores sérios discordam. O resumo a seguir precisa ser confirmado nas fontes antes de citar:

- Há estudos em que a escolha individual limitou a exposição a ideias diferentes mais do que o ranking do algoritmo (por exemplo, Bakshy, Messing e Adamic, 2015, na revista *Science*).
- Há estudos em que trocar o feed por ordem cronológica mudou o que as pessoas viam, mas quase não mudou a polarização no curto prazo (pesquisas sobre a eleição dos EUA em 2020 com a Meta, 2023).
- Notícias falsas se espalharam mais que verdadeiras em um estudo no Twitter (Vosoughi, Roy e Aral, 2018), e os autores atribuíram a diferença principalmente a pessoas, não a robôs.
- No Brasil, boa parte da circulação acontece em grupos de mensagens, que não funcionam como um feed ordenado por algoritmo.

Por isso o site é um modelo de brinquedo: mostra um mecanismo possível, não mede nenhuma plataforma real.

## 1.8 Para checar se você entendeu

1. Por que o sistema pode criar uma bolha sem que ninguém tenha programado isso?
2. Qual é a diferença entre "o que você curtiu" e "o que você viu"?
3. Por que só olhar para o código não basta para resolver o problema?
4. Cite uma limitação deste modelo.

Respostas esperadas, em resumo: (1) basta a regra "mais curtidas, mais espaço" e o feedback loop; (2) a primeira é a sua escolha, a segunda é o que o sistema entregou; (3) a métrica e o modelo de negócio definem o objetivo do sistema; (4) criadores não reagem, a pesquisa real é mais complexa, o gosto do usuário não muda.

Próximo documento: [`02-como-o-codigo-funciona.md`](02-como-o-codigo-funciona.md).
