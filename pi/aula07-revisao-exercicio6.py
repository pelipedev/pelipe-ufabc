def diferenca_quadrados(n):
    soma_quad = 0
    quad_soma = 0
    for i in range(n+1):
        soma_quad += i**2
    for i in range(n+1):
        quad_soma += i
    quad_soma = quad_soma**2
    return(quad_soma - soma_quad)