def soma_triangular_superior(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j >= i:
                soma += matriz[i][j]
    return soma