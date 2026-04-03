def mover_maior_inicio(array_entrada):
    maior_elemento = maior(array_entrada)
    array_entrada.remove(maior_elemento)
    array_entrada.insert(0, maior_elemento)
    return array_entrada

def maior(n_array):
    maximo_n = float('-inf')
    for i in n_array:
        if i > maximo_n:
            maximo_n = i
    return(maximo_n)