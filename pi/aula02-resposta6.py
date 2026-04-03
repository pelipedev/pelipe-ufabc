altura = float(input(""))

pes = altura//0.3048
polegadas = (altura%0.3048)/0.0254

print(f"{altura:.2f} metros correspondem a {pes:.0f} pés e {polegadas:.0f} polegadas.")