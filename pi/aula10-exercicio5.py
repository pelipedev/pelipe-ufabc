def media_ponderada(notas,pesos):
    media_parcial = 0
    peso_total = 0
    for i in notas:
        media_parcial += i * pesos [ notas.index(i) ]
        peso_total += pesos [ notas.index(i) ]
    return media_parcial/peso_total