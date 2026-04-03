vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

def conta_vogal(matriz):
    count = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if vogais.count(matriz[i][j]):
                count += 1
    return count