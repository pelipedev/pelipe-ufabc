def calcula_mdc(a,b): #nao era mmc?
    r = 0
    while (b != 0):
        r = a%b
        a = b
        b = r
    return a