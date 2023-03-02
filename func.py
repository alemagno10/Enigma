import numpy as np
def para_one_hot(msg : str):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz '
    posicoes = {letra: indice for indice, letra in enumerate(alfabeto)}
    return np.array([[1 if posicoes[j] == i else 0 for i in range(27)] for j in msg]).T


def para_string(M):
    M = M.T
    alfabeto = 'abcdefghijklmnopqrstuvwxyz '
    resultado = ''
    row,cols = M.shape
    for i in range(row):
        resultado += alfabeto[np.where(M[i] ==  1)[0][0]]
    return resultado

print(para_string(para_one_hot('joao oiiiiiiiiiiii')))