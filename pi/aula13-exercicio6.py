def quadrado_magico(m):
    
    soma_referencia = 0
    for j in range(len(m[0])):
        soma_referencia += m[0][j]
        
    for i in range(len(m)):
        soma = 0
        for j in range(len(m[i])):
            soma += m[i][j]
        if soma != soma_referencia:
            return False
            
    for j in range(len(m)):
        soma = 0
        for i in range(len(m[j])):
            soma += m[i][j]
        if soma != soma_referencia:
            return False
    
    soma = 0
    for i in range(len(m)):
        soma += m[i][i]
    if soma != soma_referencia:
        return False
            
    soma = 0
    for i in range(len(m)):
        soma += m[i][len(m) - 1 - i]
    if soma != soma_referencia:
        return False
            
    return True