def processar_evento(lista_eventos, prioridade):
    if prioridade:
        return lista_eventos.pop(0)
    return lista_eventos.pop(len(lista_eventos)-1)