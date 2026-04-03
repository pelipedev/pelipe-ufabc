def amplitude_termica(temp_array):
    maior = float('-inf')
    menor = float('inf')
    for i in temp_array:
        if i > maior:
            maior = i
    for i in temp_array:
        if i < menor:
            menor = i
    return(maior-menor)