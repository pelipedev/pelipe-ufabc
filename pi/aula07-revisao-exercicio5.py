def fizzbuzz(n):
    texto_saida = ""
    if not n % 3:
        texto_saida += "fizz"
    if not n % 5:
        texto_saida += "buzz"
    if texto_saida == "":
        texto_saida = n
    return(texto_saida)