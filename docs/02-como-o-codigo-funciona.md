# 2. Como o código funciona

Tempo de leitura: 20 minutos. Ajuda saber um pouco de programação, mas o texto explica cada passo.

O site inteiro está em um único arquivo, `index.html`. Ele tem três partes:

| Parte | O que contém | Tecnologia |
|---|---|---|
| `<style>` | Aparência: cores, tema claro/escuro, animações | CSS |
| `<body>` | A estrutura das telas (5 passos) | HTML |
| `<script>` | A lógica: o sistema, o jogo, as simulações, os gráficos | JavaScript |

Não há bibliotecas, servidor nem banco de dados. Tudo roda no navegador. Quando você abre o arquivo, o navegador executa o JavaScript.

> Dica: com o Modo nerd ligado, o passo 3 mostra o código real da função principal, direto na página.

## 2.1 O mapa do `<script>`

O JavaScript está organizado em blocos, separados por comentários do tipo `/* ===== NOME ===== */`. Na ordem:

1. DADOS: as manchetes (`TEMAS`), as regras (`CFG`) e os perfis de usuário.
2. MOTOR: o sistema que sorteia o feed e mede a diversidade.
3. ESTADO DO JOGO: o que o site "lembra" enquanto você joga.
4. COMPONENTES VISUAIS: barras e blocos coloridos.
5. NAVEGAÇÃO: o fluxo dos 5 passos.
6. PASSO 1 a 4: a lógica de cada tela.
7. ROSCA, MODO NERD, LABORATÓRIO: extras visuais e de exploração.
8. TEMA e COMPARTILHAR: botões utilitários.
9. INÍCIO: a última linha, que liga tudo.

## 2.2 Os dados

```js
const TEMAS = [
  {nome:"Esporte", ico:"▲", cor:"#1b7f74", tit:["Time da cidade vence...", /* 26 manchetes */]},
  {nome:"Ciência", ico:"◆", cor:"#3b5bdb", tit:[ ... ]},
  // Política, Celebridades, Polêmica
];
```

Cada tema tem um nome, um ícone (para quem não distingue cores), uma cor e uma lista de manchetes. Todas as manchetes são fictícias.

As regras ficam em um objeto de configuração:

```js
const CFG = {
  A: {gama:2, eps:0,    teto:null},   // só engajamento
  B: {gama:2, eps:0.10, teto:null},   // com exploração
  C: {gama:2, eps:0,    teto:0.4},    // com teto de diversidade
  X: {gama:2, eps:0,    teto:null}    // a regra que você edita no modo nerd
};
```

Três números descrevem qualquer regra:

- gama (γ): quanto o histórico pesa. Com γ = 0 o histórico é ignorado; com γ = 1 a chance é proporcional às curtidas; com γ ≥ 2 quem lidera tende a levar quase tudo.
- eps (ε): a fração do feed sorteada entre todos os temas, sem olhar o histórico (exploração).
- teto: a fração máxima do feed que um tema pode ocupar.

## 2.3 O motor: onde a "bolha" nasce

São três funções pequenas.

### `sorteia`: escolhe um item com chance proporcional ao peso

```js
function sorteia(pesos, rnd){
  const total = pesos.reduce((a,b)=>a+b,0);
  let r = rnd()*total;
  for(let i=0;i<pesos.length;i++){ r -= pesos[i]; if(r<=0) return i; }
  return pesos.length-1;
}
```

Imagine uma roleta em que cada tema ocupa uma fatia proporcional ao seu peso. `rnd()` gira a roleta. Quanto maior o peso, maior a fatia.

### `montaTemas`: monta um feed inteiro

```js
function montaTemas(cliques, modo, n, rnd){
  const cf = CFG[modo];
  const pesos = cliques.map(c=>Math.pow(c, cf.gama));
  const eps = cf.eps;
  const teto = cf.teto ? Math.max(1, Math.floor(cf.teto*n)) : Infinity;
  const feed = [], cont = Array(K).fill(0);
  for(let j=0;j<n;j++){
    let t = rnd()<eps ? Math.floor(rnd()*K) : sorteia(pesos, rnd);
    if(cont[t]>=teto){
      const livres = [...Array(K).keys()].filter(i=>cont[i]<teto);
      t = livres[sorteia(livres.map(i=>pesos[i]), rnd)];
    }
    feed.push(t); cont[t]++;
  }
  return feed;
}
```

Passo a passo:

1. `pesos`: transforma a pontuação de cada tema em peso, elevando ao expoente γ. É aqui que mora o *rich-get-richer*: com γ = 2, dobrar a pontuação quadruplica o peso.
2. Para cada vaga do feed, `sorteia` escolhe um tema pela roleta.
3. Com probabilidade ε, o tema é sorteado sem olhar o histórico (exploração, regra B).
4. Se o tema já atingiu o teto, a vaga é redistribuída entre os temas que ainda têm espaço (regra C).

`cliques` começa com 1 para todos os temas (todo mundo parte igual). Cada curtida soma à pontuação do tema. É o feedback loop: a pontuação alimenta o peso, o peso decide o feed, o feed gera novas curtidas, que mudam a pontuação.

### `entropia`: mede a diversidade

```js
function entropia(cont){
  const t = cont.reduce((a,b)=>a+b,0); if(!t) return 1;
  let h = 0; for(const c of cont){ if(c>0){ const p=c/t; h -= p*Math.log(p); } }
  return Math.abs(h/Math.log(cont.length));
}
```

A entropia de Shannon mede o quanto algo está "espalhado". Normalizada pelo logaritmo do número de temas, ela vale:

- 1,0 quando todos os temas aparecem igualmente;
- 0,0 quando só um tema aparece.

Exemplo com 5 temas e 6 posts: um feed `[2,1,1,1,1]` tem entropia próxima de 0,97; um feed `[6,0,0,0,0]` tem 0.

## 2.4 O gerador de números aleatórios com semente

```js
function mulberry32(a){ return function(){ a|=0; a=a+0x6D2B79F5|0; let t=Math.imul(a^a>>>15,1|a); t=t+Math.imul(t^t>>>7,61|t)^t; return ((t^t>>>14)>>>0)/4294967296; }; }
```

`Math.random()` dá resultados diferentes a cada vez. Para comparar regras de forma justa, as simulações usam `mulberry32(semente)`: com a mesma semente, a sequência de números aleatórios se repete. Por isso o passo 4 sempre dá os mesmos resultados, e os desafios do laboratório são reproduzíveis.

## 2.5 A simulação

```js
function simula(p, modo, rodadas, n, seed){
  const rnd = mulberry32(seed), c = Array(K).fill(1);
  const div = [], fim = Array(K).fill(0);
  let cliq = 0, posts = 0;
  for(let r=0;r<rodadas;r++){
    const feed = montaTemas(c, modo, n, rnd), cont = contagem(feed);
    div.push(entropia(cont));
    if(r>=rodadas-20) cont.forEach((v,i)=>fim[i]+=v);
    feed.forEach(t=>{ posts++; if(rnd()<p[t]){ c[t]++; cliq++; } });
  }
  return {div, eng:cliq/posts, fim};
}
```

Um usuário simulado é só uma lista de probabilidades `p[t]`: a chance de clicar em cada tema. Em cada rodada:

1. o sistema monta o feed (`montaTemas`);
2. mede-se a diversidade (`entropia`);
3. o usuário "clica" com a probabilidade do tema; cada clique soma à pontuação (`c[t]++`).

Duas funções ajudam:

- `mediaSims` repete a simulação 40 vezes com sementes diferentes e tira a média, para a curva não depender do acaso.
- `eng` (engajamento) é a fração de posts que receberam clique. É o "custo" da regra C: mostrar mais variedade pode reduzir os cliques.

Os perfis de usuário:

```js
const USU_NEUTRO = [0.30,0.30,0.30,0.30,0.30];   // gosta de tudo igual
const USU_FIEL   = [0.75,0.15,0.15,0.15,0.15];   // gosta principalmente de Esporte
```

## 2.6 O estado do jogo

```js
st = {
  pred, cliq, curt, vistos,   // previsão, pontuações, curtidas, posts vistos por tema
  rodada, feed, votos, hist,  // rodada atual, feed atual, votos da rodada, histórico
  part, vistosTit, plateia    // pessoas votando, manchetes já vistas, modo plateia
};
```

`st` é o único objeto que guarda o que aconteceu. Tudo o que você vê na tela é desenhado a partir de `st`. Essa regra simples (um estado, várias telas) evita muitos erros.

Por que `cliq` e `curt` são separados? `cliq` é a pontuação que o sistema usa (começa em 1); `curt` é a contagem das suas curtidas (começa em 0). O gráfico do passo 3 usa `curt` e `vistos`.

## 2.7 A interface

- `ir(n)` mostra o passo `n` e esconde os outros.
- `desenhaJogo()` redesenha o passo 2: os cartões, o histórico, a tabela de chances e a rosca.
- `concluirRodada()` registra os votos, atualiza as pontuações, escreve a mensagem "o sistema anotou" e gera o próximo feed.
- `revela()` monta o passo 3.
- `rodaReplay()` e `rodaDoisPorDois()` montam o passo 4.
- A rosca e os gráficos usam o elemento `<canvas>` e a API de desenho 2D do navegador.

Acessibilidade: os cartões são navegáveis por teclado (`Enter` e `Espaço`), usam `aria-pressed`, o tema respeita `prefers-color-scheme` e as animações respeitam `prefers-reduced-motion`. Cada tema tem cor e ícone.

## 2.8 Como o modo nerd funciona

Ligar o modo nerd só faz `document.body.classList.toggle("nerd")`. Elementos com a classe `only-nerd` ficam escondidos por padrão e aparecem com `body.nerd .only-nerd {display:block}`. Os controles deslizantes alteram o objeto `CFG.X`, e o jogo passa a usar a regra `X` em vez da `A`.

O código mostrado em "Sob o capô" é gerado com `montaTemas.toString()`: o JavaScript consegue devolver o texto da própria função. Assim, o que você lê é, de fato, o que está rodando.

## 2.9 Para explorar o código

1. Abra o `index.html` em um editor de texto (Bloco de Notas, VS Code).
2. Procure por `CFG` e mude `A: {gama:2, ...}` para `gama:3`. Salve e recarregue a página.
3. Abra o navegador e aperte `F12` para ver o console. Digite `CFG` e aperte Enter.
4. Digite `montaTemas([1,1,1,1,1], "A", 6, Math.random)` e veja um feed sair, como lista de números de 0 a 4.

Próximo documento: [`03-experimentos-e-desafios.md`](03-experimentos-e-desafios.md).
