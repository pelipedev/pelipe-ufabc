def soma_linhas(m):
    lista = []
    for i in range(len(m)):
        soma = 0
        for j in range(len(m[i])):
            soma += m[i][j]
        lista.append(soma)
    return lista