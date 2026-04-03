from scipy.constants import g
from math import sin, radians

def maior_alcance(velocidades,angulos):
    indice_final = 0
    maximo_n = 0
    for i in range(len(velocidades)):
        alcance_parcial = alcance_horizontal(velocidades[i],angulos[i])
        if alcance_parcial > maximo_n:
            maximo_n = alcance_parcial
            indice_final = i
    return (velocidades[indice_final],angulos[indice_final])

def alcance_horizontal(v0,angle):
    alcance = (v0**2*sin(2*radians(angle)))/g
    return alcance