def maior(n_array):
    maximo_n = float('-inf')
    for i in n_array:
        if i > maximo_n:
            maximo_n = i
    return(maximo_n)

#APAGAR PARA EXERCICIO
user_array = []
length = int(input("Quantos numeros ira inserir?"+'\n'))
for n in range(length):
    user_array.append(int(input("Insira numero:")))
print(user_array)
print("O maior numero de sua lista eh:",maior(user_array))