def conta_igual(array1,array2):
    counter = 0
    for i in range(len(array1)):
        if array1[i] == array2[i]:
            counter += 1
    return(counter)

#APAGAR PARA EXERCICIO
user_array1 = []
length = int(input("Quantos numeros ira inserir na lista 1?"+'\n'))
for n in range(length):
    user_array1.append(int(input("Insira numero:")))
user_array2 = []
length = int(input("Quantos numeros ira inserir na lista 1?"+'\n'))
for n in range(length):
    user_array2.append(int(input("Insira numero:")))

print(user_array1, user_array2)
print("A qntd de elementos iguais em ambas as listas eh:",conta_igual(user_array1,user_array2))








#CODIGO ANTIGO, CASO TIVESSEM TAMANHOS DIFERENTES
#def conta_igual(array1,array2):
#    if len(array1) >= len(array2):
#        selecionado = array1
#    else:
#        selecionado = array2    