import math

def calcular_media(n1,n2,letra):
    if letra == "A":
        return ((n1+n2)/2)
    elif letra == "G":
        return (math.sqrt(n1*n2))
    elif letra == "H":
        return ( 2 /  ( (1/n1) + (1/n2)  ) )
    else:
        return 0