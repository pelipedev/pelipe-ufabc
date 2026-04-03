def acima_media(array_entrada):
    total = 0
    media = 0
    array_excepcional = []
    for i in array_entrada:
        total += i
    media = total/len(array_entrada)
    for i in array_entrada:
        if i > media:
            array_excepcional.append(i)
    return(array_excepcional)