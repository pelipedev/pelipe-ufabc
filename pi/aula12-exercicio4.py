def maximo_matriz(matriz):
    maximo_n = float('-inf')
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > maximo_n:
                maximo_n = matriz[i][j]
    return maximo_n
    
def minimo_matriz(matriz):
    minimo_n = float('inf')
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] < minimo_n:
                minimo_n = matriz[i][j]
    return minimo_n