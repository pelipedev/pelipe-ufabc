def matriz_X(n):
    identidade = []
    for i in range(n):
        linha = []
        for j in range(n):
            if i == j or n - i-1 == j:
                linha.append(1)
            else:
                linha.append(0)
        identidade.append(linha)
    return identidade