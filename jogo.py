"""Jogo dos Ingressos: valide o evento e movimente o personagem pelo mapa."""

ALTURA = 5
LARGURA = 7
MAX_INGRESSOS = 100
MAX_CONVIDADOS = 20


def ler_inteiro(mensagem):
    """Le um numero inteiro nao negativo."""
    while True:
        try:
            valor = int(input(mensagem))
            if valor >= 0:
                return valor
            print("Digite um numero maior ou igual a zero.")
        except ValueError:
            print("Digite apenas um numero inteiro.")


def evento_pode_acontecer(alunos, monitores, convidados):
    """Verifica as regras de ocupacao do evento."""
    total_pessoas = alunos + monitores + convidados
    ingressos_disponiveis = total_pessoas <= MAX_INGRESSOS
    convidados_permitidos = convidados <= MAX_CONVIDADOS

    if ingressos_disponiveis and convidados_permitidos:
        print(f"Evento confirmado! Total de pessoas: {total_pessoas}.")
        return True

    if not ingressos_disponiveis:
        print(
            f"Nao ha ingressos suficientes: {total_pessoas} pessoas para "
            f"{MAX_INGRESSOS} ingressos."
        )
    if not convidados_permitidos:
        print(
            f"Limite de convidados ultrapassado: sao permitidos no maximo "
            f"{MAX_CONVIDADOS}."
        )
    return False


def mostrar_mapa(posicao, itens):
    """Mostra o personagem, os itens e as casas livres do mapa."""
    for linha in range(ALTURA):
        casas = []
        for coluna in range(LARGURA):
            casa = (linha, coluna)
            if casa == posicao:
                casas.append("P")
            elif casa in itens:
                casas.append("*")
            else:
                casas.append(".")
        print(" ".join(casas))


def jogar():
    """Executa a partida e retorna a pontuacao final."""
    posicao = (0, 0)
    itens = {(0, 3), (2, 5), (4, 1), (4, 6)}
    pontos = 0

    print("\n=== Jogo dos Ingressos ===")
    print("Pegue todos os ingressos (*) e marque pontos!")
    print("Movimentos: w = cima, s = baixo, a = esquerda, d = direita.")
    print("Digite q para sair.\n")

    while True:
        mostrar_mapa(posicao, itens)
        print(f"Pontos: {pontos} | Itens restantes: {len(itens)}")
        comando = input("Seu movimento: ").strip().lower()

        if comando == "q":
            print("Voce saiu do jogo.")
            break

        movimentos = {"w": (-1, 0), "s": (1, 0), "a": (0, -1), "d": (0, 1)}
        if comando not in movimentos:
            print("Comando invalido. Use w, a, s, d ou q.\n")
            continue

        deslocamento_linha, deslocamento_coluna = movimentos[comando]
        nova_linha = posicao[0] + deslocamento_linha
        nova_coluna = posicao[1] + deslocamento_coluna

        dentro_do_mapa = (
            0 <= nova_linha < ALTURA and 0 <= nova_coluna < LARGURA
        )
        if not dentro_do_mapa:
            print("Voce nao pode sair do mapa.\n")
            continue

        posicao = (nova_linha, nova_coluna)
        if posicao in itens:
            itens.remove(posicao)
            pontos += 10
            print("Ingresso encontrado! +10 pontos.\n")
        else:
            print()

        if not itens:
            print(f"Parabens! Voce encontrou todos os ingressos e fez {pontos} pontos.")
            break

    return pontos


def main():
    """Le os participantes e inicia o jogo quando as regras sao atendidas."""
    print("=== Organizacao do evento escolar ===")
    alunos = ler_inteiro("Quantidade de alunos: ")
    monitores = ler_inteiro("Quantidade de monitores: ")
    convidados = ler_inteiro("Quantidade de convidados: ")

    if evento_pode_acontecer(alunos, monitores, convidados):
        jogar()
    else:
        print("O jogo nao sera iniciado porque o evento nao foi aprovado.")


if __name__ == "__main__":
    main()
