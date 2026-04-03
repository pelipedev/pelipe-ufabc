def verifica_primo(n):
    d = 2
    if (n <= 1):
        return False
    while(d <= n-1):
        if (n%d == 0):
            return False
        d += 1
    else:
        return True