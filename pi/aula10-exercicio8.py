def soma_cumulativa(nums):
    soma_parcial = 0
    lista_soma = []
    for i in nums:
        lista_soma.append( soma_parcial + i )
        soma_parcial += i
    return lista_soma