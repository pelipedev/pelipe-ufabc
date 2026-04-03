def limpar_leitura(leituras, valor_invalido):
    contagem = leituras.count(valor_invalido)
    if contagem > 1:
        leituras.remove(valor_invalido)
    return (leituras, contagem)