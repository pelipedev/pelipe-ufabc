def maior(n1,n2,n3):
    maximo_n = float('-inf')
    x = [n1,n2]
    for i in x:
        if i > maximo_n:
            maximo_n = i
    return(maximo_n)