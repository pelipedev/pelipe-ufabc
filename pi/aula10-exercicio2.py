def pontuacao(gm,gs):
    pontos = 0
    if gm > gs:
        pontos += 3
    elif gm == gs:
        pontos += 1
    return pontos