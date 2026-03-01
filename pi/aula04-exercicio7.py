import math

def area_triangulo(l1,l2,l3):
    p = (l1+l2+l3)/2
    return math.sqrt(p*(p-l1)*(p-l2)*(p-l3))

def verifica_triangulo(a,b,c):
    if (a + b > c) and (b + c > a) and (a + c > b):
        return True
    else:
        return False
    
def tipo_triangulo(l1,l2,l3):
    if (l1 == l2) and (l2 == l3):
        return "equilátero"
    elif (l1 != l2) and (l2 != l3) and (l1 != l3):
        return "escaleno"
    else:
        return "isóceles"
    
def info_triangulo(l1,l2,l3):
    if verifica_triangulo(l1,l2,l3) == True:
        return tipo_triangulo(l1,l2,l3), area_triangulo(l1,l2,l3)
    else:
        return None