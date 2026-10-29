# 4. Para ir além

Você viu o mecanismo, leu o código e rodou experimentos. E agora?

## 4.1 O que este modelo deixa de fora

Todo modelo simplifica. Estas são as simplificações mais importantes deste projeto, e cada uma é uma ideia de projeto:

| Simplificação | Na vida real | Como estender |
|---|---|---|
| O gosto do usuário é fixo | Gostos mudam, e o feed também muda o gosto | Usuário cujas probabilidades se movem com o que ele vê |
| Criadores não reagem | Criadores aprendem o que rende curtida e produzem mais disso | Aumentar a oferta de manchetes do tema premiado |
| Um único tipo de sinal (curtida) | Tempo de tela, compartilhamento, comentário, pausa | Vários sinais com pesos diferentes |
| Um só sistema | Plataformas misturam várias regras e modelos de aprendizado de máquina | Combinar regras, ou usar um modelo simples treinado |
| Sem moderação | Plataformas removem, rotulam e reduzem alcance | Penalizar conteúdo marcado |
| Sem laços entre pessoas | Redes sociais têm grupos e amizades | Simular uma pequena rede de usuários |

## 4.2 Palavras-chave para pesquisar

Se você quiser aprofundar, estes termos abrem muitas portas:

- **Sistemas de recomendação:** filtragem colaborativa, filtragem baseada em conteúdo, *learning to rank*.
- **Exploração × aproveitamento** (*exploration–exploitation*): bandidos multi-braços (*multi-armed bandits*), epsilon-greedy, Thompson sampling. O parâmetro **ε** deste projeto é exatamente o epsilon-greedy.
- **Processos de reforço positivo:** urna de Pólya (*Pólya urn*), *preferential attachment*, "o rico fica mais rico".
- **Teoria da informação:** entropia de Shannon, índice de Gini-Simpson.
- **Lei de Goodhart:** "quando uma medida vira meta, deixa de ser uma boa medida".
- **Responsabilidade algorítmica:** transparência, auditoria de algoritmos, LGPD.

## 4.3 Uma trilha de estudo sugerida

1. **HTML, CSS e JavaScript básicos.** Altere o `index.html` deste projeto. Tente mudar uma cor, uma manchete, um número.
2. **Python.** Rode e modifique `python/simulacao_feedback_loop.py`. Aprenda listas, funções e laços.
3. **Probabilidade e estatística.** O que é uma média, uma variância, um teste de hipótese? Isso responde "a diferença é real ou foi sorte?".
4. **Estruturas de dados e algoritmos.** A roleta de `sorteia` é um algoritmo clássico.
5. **Aprendizado de máquina.** Recomendadores reais aprendem os pesos a partir de dados, em vez de seguirem uma fórmula fixa.
6. **Ética e governança de dados.** Quem decide a métrica? Quem responde pelo resultado?

Os passos 5 e 6 se encontram em uma pergunta que nenhum código resolve sozinho: **o que um sistema deveria otimizar?**

## 4.4 Contribuindo com o projeto

O projeto é aberto. Você pode:

- abrir uma *issue* com uma dúvida, um erro ou uma ideia;
- propor mudanças por *pull request* (por exemplo, novas manchetes, novas regras, tradução);
- usar o material em aulas, rodas de conversa e eventos, citando a fonte.

Boas contribuições para quem está começando: corrigir um texto, adicionar manchetes neutras, criar um perfil de usuário novo no Python.

## 4.5 Estudar essas tecnologias na Mauá

Este projeto nasceu em um contexto acadêmico: um artigo de iniciação científica de estudantes de Ensino Médio sobre economia da desinformação e algoritmos de plataformas. Se você gostou de entender como esses sistemas funcionam e quer **aprender a construí-los e a decidir o que eles devem fazer**, vale conhecer os cursos de computação do Instituto Mauá de Tecnologia:

- [Ciência da Computação](https://www.maua.br/graduacao/ciencia-computacao?utm_source=bolhas-demo&utm_medium=docs&utm_campaign=vestibular)
- [Sistemas de Informação](https://www.maua.br/graduacao/sistemas-informacao?utm_source=bolhas-demo&utm_medium=docs&utm_campaign=vestibular)
- [Vestibular](https://www.maua.br/vestibular?utm_source=bolhas-demo&utm_medium=docs&utm_campaign=vestibular) (datas, valores e inscrição ficam na página oficial)

Na Mauá, estudantes desses cursos aprendem a trabalhar com tecnologias como as deste projeto: dados, algoritmos e sistemas de informação.

---

Voltar ao [índice](../README.md).
