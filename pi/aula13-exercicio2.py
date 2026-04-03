def escala_matriz(m,n):
    matriz_escalada = []
    for i in range(len(m)):
        linha = []
        for j in range(len(m[i])):
            linha.append( m[i][j] * n )
        matriz_escalada.append(linha)
    return matriz_escalada