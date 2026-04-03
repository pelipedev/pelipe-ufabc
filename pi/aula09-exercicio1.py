def remover_todos(array_entrada,elemento):
    counter = array_entrada.count(elemento)
    for i in range(counter):
        array_entrada.remove(elemento)
    return(array_entrada)