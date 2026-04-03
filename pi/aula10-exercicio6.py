from scipy.constants import g
from math import sin, radians

def alcance_horizontal(v0,angle):
    alcance = (v0**2*sin(2*radians(angle)))/g
    return alcance