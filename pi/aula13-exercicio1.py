def dobro_matriz(m):
    dobro = []
    for i in range(len(m)):
        linha = []
        for j in range(len(m[i])):
            linha.append( m[i][j] * 2 )
        dobro.append(linha)
    return dobro