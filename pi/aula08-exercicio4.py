def soma_lista(array_a,array_b):
    array_c = []
    for i in array_a:
        array_c.append(i+array_b[array_a.index(i)])
    return(array_c)