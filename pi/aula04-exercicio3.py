def jokenpo(m1, m2):
    if m1 == m2:
        return 0

    if m1 == "pedra":
        if m2 == "tesoura":
            return 1
        elif m2 == "papel":
            return 2
            
    elif m1 == "papel":
        if m2 == "pedra":
            return 1
        elif m2 == "tesoura":
            return 2
            
    elif m1 == "tesoura":
        if m2 == "papel":
            return 1
        elif m2 == "pedra":
            return 2