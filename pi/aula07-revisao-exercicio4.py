def amplitude_termica_fahrenheit(temp_array):
    maior = float('-inf')
    menor = float('inf')
    for i in temp_array:
        if i > maior:
            maior = i
    for i in temp_array:
        if i < menor:
            menor = i
    maior = celsius_fahrenheit(maior)
    menor = celsius_fahrenheit(menor)
    return(maior-menor)

def celsius_fahrenheit(celsius):
    american_temp = (celsius*1.8)+32
    return(american_temp)