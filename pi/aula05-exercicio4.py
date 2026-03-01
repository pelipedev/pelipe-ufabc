soma_parcial = 0
def soma(n_array):
    for i in n_array:
        soma_parcial += i**2
    return(soma_parcial)