def maior(n1,n2):
    maximo_n = float('-inf')
    x = [n1,n2]
    for i in x:
        if i > maximo_n:
            maximo_n = i
    return(maximo_n) 
#APAGAR PARA EXERCICIO
num_1 = float(input(""))
num_2 = float(input(""))

print(maior(num_1,num_2))