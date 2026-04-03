def seleciona_multiplos(array_entrada,numero_divisor):
    array_saida = []
    for i in array_entrada:
        if not i % numero_divisor:
            array_saida.append(i)
    return(array_saida)