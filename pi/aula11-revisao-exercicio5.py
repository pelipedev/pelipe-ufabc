def higienizar_leituras(lista_leituras, limite_min, limite_max):
    remocoes = 0
    if lista_leituras.count(0.0):
        for i in range(lista_leituras.count(0.0)):
            lista_leituras.remove(0.0)
            remocoes += 1
    for i in lista_leituras:
        if i < limite_min or i > limite_max:
            lista_leituras.remove(i)
            remocoes += 1
    return (lista_leituras, remocoes)