def soma_pontuacao(list1,list2):
    indice = 0
    score = 0
    for i in list1:
        score += pontuacao(i,list2[indice])
        indice += 1
    return score

def pontuacao(gm,gs):
    pontos = 0
    if gm > gs:
        pontos += 3
    elif gm == gs:
        pontos += 1
    return pontos