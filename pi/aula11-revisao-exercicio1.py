def gerenciar_fila(fila, nome, prioridade):
    if not prioridade:
        fila.insert(0, nome)
    elif prioridade == 1:
        fila.insert(len(fila)//2, nome)
    else:
        fila.append(nome)
    return fila