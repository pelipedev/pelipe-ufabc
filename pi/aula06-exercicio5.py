def conta_par(n_array):
    acumulador = 0
    for i in n_array:
        if not (i % 2):
            acumulador += 1
    return(acumulador)

#APAGAR PARA EXERCICIO
user_array = []
length = int(input("Quantos numeros ira inserir?"+'\n'))
for n in range(length):
    user_array.append(int(input("Insira numero:")))
print(user_array)
print("A qntd de numeros pares na sua lista eh:",conta_par(user_array))