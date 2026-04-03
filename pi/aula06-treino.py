#testes
lista = ["pelipe", "paulo", "abobora"]
for opa in lista:
    print(opa)

x = range(5,0,-1)
for p in x:
    print(p)

for pos in range(len(lista)):
    print(pos)
    
for numeroatual in range(30):
    if not numeroatual % 3:
        print(numeroatual,"divisivel por 3")
    else:
        print(numeroatual)

#soma P.A.
inicio = input("Valor inicial da PA (deixe vazio para 0): ")

if inicio == "":
    inicio = 0

inicio = int(inicio)
fim = int(input("Valor final: "))
razao =(input("Razao (deixe vazio para 1): "))

if razao == "":
    razao = 1
razao = int(razao)

pa = range(inicio,fim+1, razao)
acumulador = 0
for i in pa:
    acumulador += i 
print(acumulador)