import math

def area_triangulo(l1,l2,l3):
    p = (l1+l2+l3)/2
    return math.sqrt(p*(p-l1)*(p-l2)*(p-l3))