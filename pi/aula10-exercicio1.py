def cria_lista_quadrado(n):
    counter = 0
    lista_quadrado = []
    while (n-counter) > 0:
        lista_quadrado.append((n-counter)**2)
        counter += 1
    return lista_quadrado