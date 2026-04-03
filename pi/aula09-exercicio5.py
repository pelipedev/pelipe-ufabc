def mover_inicio2(array_entrada,elemento):
    array_entrada.remove(elemento)
    array_entrada.insert(0, elemento)
    return array_entrada