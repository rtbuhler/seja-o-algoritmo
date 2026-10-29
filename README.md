# Seja o algoritmo da sua própria bolha

**Em 5 minutos, veja um feed virar bolha na sua frente, e descubra por que isso acontece.**

[**▶ Experimentar agora**](https://rtbuhler.github.io/seja-o-algoritmo/) · funciona no celular, no projetor e offline · sem cadastro, sem coleta de dados

Uma demonstração interativa e de código aberto sobre algoritmos de recomendação, bolhas informacionais e a pergunta "quem escolhe o que chega até nós?". Você curte manchetes (fictícias), o sistema aprende com as suas curtidas e você acompanha o feed se estreitar. Depois, troca a regra do sistema e compara os resultados.

Feita para aulas, rodas de conversa e eventos de ciência e tecnologia. Se você é estudante do Ensino Médio e curte mexer no código, ligue o Modo nerd dentro do site.

## O que você vai ver

| Passo | O que acontece |
|---|---|
| 1. Prever | Você aposta no que vai acontecer com o seu feed. |
| 2. Jogar | 8 rodadas: você curte, o sistema anota, a "bolha" aparece em uma rosca animada. |
| 3. Ver | O gráfico "o que você curtiu × o que o sistema mostrou" separa a **sua escolha** da **amplificação do sistema**. |
| 4. Regras | Mesmo perfil de curtidas, três regras diferentes. O experimento 2×2: quem escolhe, o sistema ou o usuário? E o enfoque econômico: um pequeno prêmio de engajamento muda o feed? Quanto custa a diversidade em receita? |
| 5. Pensar | Perguntas para discutir, o desafio do auditor ("projetar, auditar e governar"), limites do modelo e glossário. |

Modo plateia: para quem não tem celular, o projetor vira a tela de todos. Conte as mãos levantadas e registre os votos com + e −.

Modo nerd: mostra o sistema por dentro (pontuações, pesos, probabilidades), deixa você mudar os parâmetros (γ, ε, teto), traz o código real da função principal, um laboratório com desafios e exporta seus dados em CSV.

## Comece em 1 minuto

```text
1. Baixe o repositório (botão verde "Code" → "Download ZIP") ou clone:
   git clone https://github.com/rtbuhler/seja-o-algoritmo.git
2. Abra o arquivo index.html no navegador.
   Pronto. Não precisa instalar nada.
```

## Aprenda como funciona

A documentação foi escrita para ser lida em ordem, do mais simples ao mais técnico:

1. [Conceitos](docs/01-conceitos.md): métrica, feedback loop, bolha × câmara de eco, o que a pesquisa diz. Não precisa programar.
2. [Como o código funciona](docs/02-como-o-codigo-funciona.md): o arquivo, as funções, a simulação, passo a passo.
3. [Experimentos e desafios](docs/03-experimentos-e-desafios.md): perguntas para testar, no site ou em Python, e desafios de código em três níveis.
4. [Para ir além](docs/04-para-ir-alem.md): limites do modelo, palavras-chave para pesquisar e uma trilha de estudo.
5. [Resultados do resumo](docs/05-resultados-do-resumo.md): os números citados no trabalho, com o protocolo para reproduzi-los.
6. [Referências](docs/06-referencias.md): artigos com DOI conferido, livros e a origem de cada conceito.

## Versão em Python

```bash
python python/simulacao_feedback_loop.py                    # regra A, usuário neutro
python python/simulacao_feedback_loop.py --gama 1           # o histórico pesa menos
python python/simulacao_feedback_loop.py --teto 0.4 --usuario fiel
python python/simulacao_feedback_loop.py --epsilon 0.1 --csv resultado.csv --grafico
```

Só usa a biblioteca padrão (o gráfico é opcional e precisa de `matplotlib`). Mostra a diversidade do feed por rodada e compara com a regra A.

## Estrutura do repositório

```text
index.html                        o site inteiro (HTML + CSS + JavaScript, arquivo único)
python/simulacao_feedback_loop.py a mesma ideia em Python
python/reproduzir_resumo.py       reproduz os números citados no resumo
docs/                             documentação didática (6 documentos)
CITATION.cff                      como citar este projeto
logo-maua.png                     cópia do logo usado no site
LICENSE                           licença MIT do código (veja a nota sobre a marca)
```

## Limites

É um modelo de brinquedo para ilustrar um mecanismo. Não mede nenhuma plataforma real. Os gostos do usuário são fixos, os criadores de conteúdo não reagem, e a pesquisa real sobre bolhas é mais complexa e disputada. O site e a documentação dizem isso com todas as letras.

## Sobre o projeto

A atividade se apoia no artigo de iniciação científica *Economia da desinformação e sistemas algorítmicos* (Angelo e Nogueira, RICEM, Revista de Iniciação Científica do Ensino Médio, 2026), que usa o modelo de três fases (criação, disseminação e recirculação) de Jesus-Silva (2026).

Desenvolvido por Rudolf Theoderich Buhler, coordenador dos cursos de Ciência da Computação e de Sistemas de Informação do Instituto Mauá de Tecnologia (Campus de São Caetano do Sul), com o apoio do Claude (Anthropic).

Quer aprender a construir sistemas como este e a decidir o que eles devem fazer? Conheça [Ciência da Computação](https://www.maua.br/graduacao/ciencia-computacao?utm_source=bolhas-demo&utm_medium=github&utm_campaign=vestibular) e [Sistemas de Informação](https://www.maua.br/graduacao/sistemas-informacao?utm_source=bolhas-demo&utm_medium=github&utm_campaign=vestibular) na Mauá. Datas, valores e inscrição ficam na página do [vestibular](https://www.maua.br/vestibular?utm_source=bolhas-demo&utm_medium=github&utm_campaign=vestibular).

## Como citar

O GitHub mostra o botão "Cite this repository" (a partir do arquivo `CITATION.cff`), com a citação pronta em APA e BibTeX. Os números do trabalho podem ser conferidos com `python python/reproduzir_resumo.py`, e os detalhes estão em [`docs/05-resultados-do-resumo.md`](docs/05-resultados-do-resumo.md).

## Contribuir

Ideias, dúvidas e correções são bem-vindas: abra uma *issue* ou um *pull request*. Boas primeiras contribuições: novas manchetes neutras, tradução, um novo perfil de usuário no Python. Detalhes em [`docs/04-para-ir-alem.md`](docs/04-para-ir-alem.md).

## Licença e marca

O código e a documentação estão sob a licença [MIT](LICENSE): você pode usar, copiar, modificar e redistribuir, mantendo o aviso de autoria.

O nome e o logotipo do Instituto Mauá de Tecnologia são marcas do Instituto e não estão cobertos pela licença MIT. Ao reutilizar o projeto, troque a identidade visual pela sua.
