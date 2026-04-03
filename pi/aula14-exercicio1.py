def indicadora(m,a):
    m_ind = []
    for i in range(len(m)):
        linha = []
        for j in range(len(m[i])):
            if m[i][j] == a:
                linha.append(1)
            else:
                linha.append(0)
        m_ind.append(linha)
    return m_ind