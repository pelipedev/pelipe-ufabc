def media_colunas(m):
    if m:
        lista = []
        n_col = len(m[0])
        for j in range(n_col):
            soma = 0
            for i in range(len(m)):
                soma += m[i][j]
            lista.append(soma/len(m))
        return lista
    else:
        return m