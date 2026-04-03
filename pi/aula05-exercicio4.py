def soma_harmonico(epsilon):
    n = 1
    soma = 0
    while (1/n > epsilon):
        soma += 1/n
        n += 1
        
    return soma