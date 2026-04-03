def mover_inicio(lista, posicao):
    elemento = lista.pop(posicao)
    lista.insert(0, elemento)
    return lista