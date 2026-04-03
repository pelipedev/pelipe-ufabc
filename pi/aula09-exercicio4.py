def mover_elemento2(array_entrada, elemento):
    array_entrada.remove(elemento)
    array_entrada.append(elemento)
    return array_entrada