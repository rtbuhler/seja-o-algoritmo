"""Simulação didática de feedback loop em um recomendador de feed.

É a mesma ideia do site (index.html), escrita em Python para você ler, rodar e modificar.
Usa o mesmo gerador de números aleatórios do site (mulberry32) e a mesma ordem de sorteios,
então, com as mesmas sementes, os resultados são IGUAIS aos do site.

O sistema só faz uma coisa: dá mais espaço aos temas que já receberam mais curtidas.
Ninguém programou "faça uma bolha". Mesmo assim, o feed se estreita, porque a
recomendação vira dado de treino do próprio sistema.

Uso (só biblioteca padrão; matplotlib é opcional, para o gráfico):

    python simulacao_feedback_loop.py                      # regra A, usuário neutro
    python simulacao_feedback_loop.py --gama 1             # histórico pesa menos
    python simulacao_feedback_loop.py --epsilon 0.1        # 10% de exploração
    python simulacao_feedback_loop.py --teto 0.4           # nenhum tema passa de 40%
    python simulacao_feedback_loop.py --usuario fiel       # usuário que curte Esporte
    python simulacao_feedback_loop.py --csv resultado.csv  # salva a diversidade por rodada
    python simulacao_feedback_loop.py --grafico            # salva simulacao.png (precisa de matplotlib)

Para reproduzir os números do resumo do trabalho, rode reproduzir_resumo.py.
"""
import argparse
import csv
import math

TEMAS = ["Esporte", "Ciência", "Política", "Celebridades", "Polêmica"]
K = len(TEMAS)

# Probabilidade de o usuário clicar em cada tema.
USUARIOS = {
    "neutro": [0.30, 0.30, 0.30, 0.30, 0.30],    # gosta de tudo igualmente
    "fiel": [0.75, 0.15, 0.15, 0.15, 0.15],      # gosta principalmente de Esporte
    "reativo": [0.30, 0.30, 0.30, 0.30, 0.36],   # "Polêmica" rende 20% mais cliques
}

M32 = 0xFFFFFFFF


def mulberry32(semente):
    """Gerador de números aleatórios com semente (o mesmo do site). Devolve uma função sem argumentos."""
    a = semente & M32

    def rnd():
        nonlocal a
        a = (a + 0x6D2B79F5) & M32
        t = ((a ^ (a >> 15)) * (1 | a)) & M32
        t = ((t + (((t ^ (t >> 7)) * (61 | t)) & M32)) & M32) ^ t
        return ((t ^ (t >> 14)) & M32) / 4294967296

    return rnd


def entropia_normalizada(contagem):
    """Diversidade do feed: 1.0 = todos os temas igualmente presentes; 0.0 = um tema só."""
    total = sum(contagem)
    h = 0.0
    for c in contagem:
        if c > 0:
            p = c / total
            h -= p * math.log(p)
    return abs(h / math.log(len(contagem)))


def sorteia(pesos, rnd):
    """Roleta: sorteia um índice com probabilidade proporcional ao peso."""
    total = 0.0
    for p in pesos:
        total += p
    r = rnd() * total
    for i, p in enumerate(pesos):
        r -= p
        if r <= 0:
            return i
    return len(pesos) - 1


def monta_feed(cliques, gama, epsilon, teto, n, rnd):
    """Escolhe o tema de cada vaga do feed.

    cliques: pontuação de cada tema (começa em 1).
    gama:    expoente do peso (peso = pontuação ** gama). Quanto maior, mais "o vencedor leva tudo".
    epsilon: fração do feed sorteada entre todos os temas (exploração).
    teto:    fração máxima do feed que um tema pode ocupar (None = sem teto).
    """
    pesos = [float(c) ** gama for c in cliques]
    limite = max(1, math.floor(teto * n)) if teto else None
    feed, cont = [], [0] * K
    for _ in range(n):
        tema = math.floor(rnd() * K) if rnd() < epsilon else sorteia(pesos, rnd)
        if limite is not None and cont[tema] >= limite:
            livres = [i for i in range(K) if cont[i] < limite]
            tema = livres[sorteia([pesos[i] for i in livres], rnd)]
        feed.append(tema)
        cont[tema] += 1
    return feed


def simula(p_clique, gama, epsilon, teto, rodadas, n, semente):
    """Uma simulação. Devolve (diversidade por rodada, engajamento, contagem final por tema).

    A contagem final soma os feeds das últimas 20 rodadas.
    """
    rnd = mulberry32(semente)
    cliques = [1] * K
    diversidade, finais = [], [0] * K
    cliques_total = posts = 0
    for r in range(rodadas):
        feed = monta_feed(cliques, gama, epsilon, teto, n, rnd)
        cont = [feed.count(i) for i in range(K)]
        diversidade.append(entropia_normalizada(cont))
        if r >= rodadas - 20:
            finais = [a + b for a, b in zip(finais, cont)]
        for tema in feed:                       # o usuário reage ao que viu...
            posts += 1
            if rnd() < p_clique[tema]:
                cliques[tema] += 1              # ...e a reação vira dado de treino (feedback loop)
                cliques_total += 1
    return diversidade, cliques_total / posts, finais


def media(p_clique, gama, epsilon, teto, rodadas, n, sementes, semente_base=0):
    """Média de várias simulações (sementes semente_base, semente_base+1, ...).

    Devolve (diversidade média por rodada, engajamento médio, parcela média do tema dominante).
    """
    div = [0.0] * rodadas
    eng = dom = 0.0
    for s in range(sementes):
        d, e, fim = simula(p_clique, gama, epsilon, teto, rodadas, n, semente_base + s)
        for i, v in enumerate(d):
            div[i] += v / sementes
        eng += e / sementes
        dom += max(fim) / sum(fim) / sementes
    return div, eng, dom


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--gama", type=float, default=2.0, help="expoente do peso (padrão 2)")
    ap.add_argument("--epsilon", type=float, default=0.0, help="fração de exploração, de 0 a 1 (padrão 0)")
    ap.add_argument("--teto", type=float, default=0.0, help="teto por tema, de 0 a 1; 0 = sem teto (padrão 0)")
    ap.add_argument("--usuario", choices=USUARIOS, default="neutro")
    ap.add_argument("--rodadas", type=int, default=100)
    ap.add_argument("--feed", type=int, default=10, help="posts por rodada (padrão 10)")
    ap.add_argument("--sementes", type=int, default=40, help="quantas simulações para tirar a média")
    ap.add_argument("--csv", help="salva a diversidade média por rodada neste arquivo")
    ap.add_argument("--grafico", action="store_true", help="salva simulacao.png (precisa de matplotlib)")
    a = ap.parse_args()

    p = USUARIOS[a.usuario]
    teto = a.teto or None
    seus = media(p, a.gama, a.epsilon, teto, a.rodadas, a.feed, a.sementes)
    ref = media(p, 2.0, 0.0, None, a.rodadas, a.feed, a.sementes)   # regra A, de referência

    print(f"Usuário: {a.usuario} | seus parâmetros: gama={a.gama}, epsilon={a.epsilon}, teto={teto or 'sem teto'}")
    print(f"{'rodada':>7} | {'regra A':>8} | {'seus parâmetros':>15}")
    for r in [1, 5, 10, 20, 50, 100]:
        if r <= a.rodadas:
            print(f"{r:>7} | {ref[0][r-1]:>8.2f} | {seus[0][r-1]:>15.2f}")
    print()
    print(f"Tema dominante nas últimas 20 rodadas: A = {ref[2]:.0%} | seus parâmetros = {seus[2]:.0%}")
    print(f"Curtidas por 100 posts (engajamento):  A = {ref[1]*100:.0f}  | seus parâmetros = {seus[1]*100:.0f}")

    if a.csv:
        with open(a.csv, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["rodada", "diversidade_regra_A", "diversidade_seus_parametros"])
            for i in range(a.rodadas):
                w.writerow([i + 1, f"{ref[0][i]:.4f}", f"{seus[0][i]:.4f}"])
        print(f"CSV salvo em {a.csv}")

    if a.grafico:
        try:
            import matplotlib
            matplotlib.use("Agg")
            import matplotlib.pyplot as plt
        except ImportError:
            print("matplotlib não está instalado: rode 'pip install matplotlib' para gerar o gráfico.")
            return
        plt.plot(range(1, a.rodadas + 1), ref[0], label="regra A")
        plt.plot(range(1, a.rodadas + 1), seus[0], label="seus parâmetros")
        plt.xlabel("rodadas"); plt.ylabel("diversidade do feed"); plt.ylim(0, 1.05); plt.legend()
        plt.title("Feedback loop: o feed se estreita sozinho")
        plt.tight_layout(); plt.savefig("simulacao.png", dpi=150)
        print("Gráfico salvo em simulacao.png")


if __name__ == "__main__":
    main()
