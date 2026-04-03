import math

area = float(input(""))
calculo_lata = math.ceil(area/216)
calculo_galao = math.ceil(area/43.2)
calculo_misto_lata = int(area//216)
calculo_misto_galao = int(math.ceil((area%216)/43.2))
preco_lata = calculo_lata*80
preco_galao = calculo_galao*25
preco_misto = (calculo_misto_galao*25) + (calculo_misto_lata*80)

print(f"Para uma parede de área {area:.2f}, você vai precisar de {calculo_lata} latas de 18 litros, com o custo de R$ {preco_lata:.2f}.")
print(f"Para uma parede de área {area:.2f}, você vai precisar de {calculo_galao} latas de 3,6 litros, com o custo de R$ {preco_galao:.2f}.")
print(f"Para uma parede de área {area:.2f}, você vai precisar de {calculo_misto_lata} latas de 18 litros e {calculo_misto_galao} latas de 3,6, com o custo de R$ {preco_misto:.2f}.")