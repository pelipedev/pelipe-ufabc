def mover_elemento(array_entrada,posicao):
    stored = None
    stored = array_entrada.pop(posicao)
    array_entrada.append(stored)
    return array_entrada