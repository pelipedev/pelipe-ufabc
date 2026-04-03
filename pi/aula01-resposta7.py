import math

area = float(input(""))
calculo = math.ceil(area/216)

print(f"Para uma parede de área {area:.2f}, você vai precisar de {calculo} latas de tinta, com o custo de R$ {(calculo*80):.2f}.")