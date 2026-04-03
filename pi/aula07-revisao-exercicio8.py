def conta_sobrepeso(peso_array,altura_array):
    count = 0
    indice = 0
    for i in peso_array:
        if calcula_imc(peso_array[indice], altura_array[indice]) > 25:
            count += 1
        indice += 1
    return (count)

def calcula_imc(peso,altura):
    return(peso/altura**2)