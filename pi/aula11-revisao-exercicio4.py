def posicao_candidato(lista, nome):
    if lista.count(nome):
        return lista.index(nome)
    lista.append(nome)
    return lista.index(nome)