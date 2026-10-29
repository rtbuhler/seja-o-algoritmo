"""Reproduz os números citados no resumo do trabalho.

    python reproduzir_resumo.py

Protocolo (o mesmo do site, em Modo nerd > passo 4 > "Resultados do resumo"):
  - 100 rodadas por simulação, feed de 10 posts;
  - média de 40 simulações, com as sementes 0 a 39;
  - regra A: só engajamento (gama = 2, sem exploração, sem teto);
  - teto: nenhum tema ocupa mais de 40% do feed;
  - usuário neutro: 30% de chance de clicar em qualquer tema;
  - usuário fiel: 75% de chance em Esporte e 15% nos outros;
  - prêmio de engajamento: "Polêmica" com 36% de chance, contra 30% dos outros (200 simulações).

Com as mesmas sementes, o site e este script dão os mesmos números.
"""
import simulacao_feedback_loop as s

RODADAS, FEED, SEMENTES = 100, 10, 40


def principal():
    neutro, fiel, reativo = s.USUARIOS["neutro"], s.USUARIOS["fiel"], s.USUARIOS["reativo"]

    n_a = s.media(neutro, 2.0, 0.0, None, RODADAS, FEED, SEMENTES)
    n_c = s.media(neutro, 2.0, 0.0, 0.4, RODADAS, FEED, SEMENTES)
    f_a = s.media(fiel, 2.0, 0.0, None, RODADAS, FEED, SEMENTES)
    f_c = s.media(fiel, 2.0, 0.0, 0.4, RODADAS, FEED, SEMENTES)

    print("1) Diversidade do feed (1 = variado, 0 = um tema só), usuário neutro")
    print(f"   só engajamento: rodada 1 = {n_a[0][0]:.2f}  |  rodada 100 = {n_a[0][RODADAS-1]:.2f}")
    print(f"   teto de 40%:    rodada 100 = {n_c[0][RODADAS-1]:.2f}")
    print()
    print("2) Curtidas por 100 posts (proxy de receita), usuário fiel")
    print(f"   só engajamento: {f_a[1]*100:.0f}  |  teto de 40%: {f_c[1]*100:.0f}")
    print()

    # 3) Prêmio de engajamento: quem domina o feed nas últimas 20 rodadas?
    def dominancia(p):
        vit = [0] * s.K
        parte = 0.0
        n = 200
        for semente in range(n):
            _, _, fim = s.simula(p, 2.0, 0.0, None, RODADAS, FEED, semente)
            vit[fim.index(max(fim))] += 1
            parte += fim[4] / sum(fim) / n
        return [v / n for v in vit], parte

    sem, sem_parte = dominancia(neutro)
    com, com_parte = dominancia(reativo)
    print("3) Prêmio de engajamento para 'Polêmica' (200 simulações)")
    print(f"   'Polêmica' domina o feed em {com[4]:.0%} das simulações (sem prêmio: {sem[4]:.0%})")
    print(f"   parcela média de 'Polêmica' nas últimas 20 rodadas: {com_parte:.0%} (sem prêmio: {sem_parte:.0%})")


if __name__ == "__main__":
    principal()
