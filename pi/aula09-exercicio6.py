def mover_maior_fim(array_entrada):
    maior_elemento = maior(array_entrada)
    array_entrada.remove(maior_elemento)
    array_entrada.append(maior_elemento)
    return array_entrada

def maior(n_array):
    maximo_n = float('-inf')
    for i in n_array:
        if i > maximo_n:
            maximo_n = i
    return(maximo_n)