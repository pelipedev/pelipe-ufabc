def verifica_identidade(m):
    validacao = True
    for i in range(len(m)):
        for j in range(len(m[i])):
            if i == j:
                if not m[i][j] == 1:
                    validacao = False
            else:
                if m[i][j]:
                    validacao = False
    return validacao