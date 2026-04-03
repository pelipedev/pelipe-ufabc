def matriz_identidade(n):
    identidade = []
    for i in range(n):
        linha = []
        for j in range(n):
            if i == j:
                linha.append(1)
            else:
                linha.append(0)
        identidade.append(linha)
    return identidade