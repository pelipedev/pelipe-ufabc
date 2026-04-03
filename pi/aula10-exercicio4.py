def verifica_ordem_crescente(vetor):
    crescente = True
    for i in range(len(vetor)-1):
        if vetor[i] > vetor[i+1]:
            crescente = False
    return crescente