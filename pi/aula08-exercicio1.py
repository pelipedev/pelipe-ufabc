def seleciona_pares(array_entrada):
    array_saida = []
    for i in array_entrada:
        if not i % 2:
            array_saida.append(i)
    return(array_saida)