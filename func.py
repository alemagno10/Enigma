import numpy as np
def para_one_hot(msg : str):
    posicoes = {letra: indice for indice, letra in enumerate('abcdefghijklmnopqrstuvwxyz ')}
    return np.array([[1 if posicoes[j] == i else 0 for i in range(27)] for j in msg]).T

def para_string(M):
    M = M.T
    alfabeto = 'abcdefghijklmnopqrstuvwxyz '
    resultado = ''
    row,col = M.shape
    for i in range(row):
        resultado += alfabeto[np.where(M[i] ==  1)[0][0]]
    return resultado

def cifra(msg,M):
    return para_string(M @ para_one_hot(msg))

def de_cifra(msg, M):
    return para_string(np.linalg.inv(M) @ para_one_hot(msg))

def enigma(msg, P, E):
    final = np.array([])
    hotMsg = para_one_hot(msg)
    row,col = hotMsg.shape
    for i in range(row):
        x = E
        for _ in range(i):
            x = E @ x
        x = x @ P @ hotMsg
        final = np.vstack((final,x[i])) #x[i]
    print(final)
        
    return  para_string(final)

# def enigma(msg, P, E):
#     hotMsg = para_one_hot(msg)
#     for i in hotMsg.shape:
#         X = P
#         for _ in range(i):
#             X = E @ X


alfabeto_cifrado = para_one_hot("bcdefghijkl mnopqrstuvwxyza")
cifrador_auxiliar = para_one_hot("ijkl mnopqrstuvwxyzabcdefgh")
mensagem_entrada = "o bolo de chocolate fica pronto quatro horas da tarde"
enigma(mensagem_entrada, alfabeto_cifrado, cifrador_auxiliar)

