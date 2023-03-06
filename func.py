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
    final = np.array([0 for i in range(27)])
    hotMsg = para_one_hot(msg)
    size = hotMsg.shape
    for i in range(size[1]):
        if i > 1:
            x = E
            for _ in range(i-1):
                x = E @ x
            x = x @ P @ hotMsg
        elif i == 1:
            x = E @ P @ hotMsg
        elif i == 0:
            x = P @ hotMsg

        if i != 0:
            final = np.vstack((final,x.T[i]))
        else:
            final = x.T[i]
    return para_string(final.T)

def de_enigma(msg, P, E):
    msg = para_one_hot(msg).T
    size = msg.shape
    final = np.array([0 for i in range(27)])
    for i in range(size[0]):
        x = msg[i] 
        if i == 0: 
            final = np.linalg.inv(P) @ x
        else:
            for _ in range(i):
                x = np.linalg.inv(E) @ x 
            final = np.vstack((final, np.linalg.inv(P) @ x))
    return para_string(final.T)

alfabeto_cifrado = para_one_hot("bcdefghijkl mnopqrstuvwxyza")
cifrador_auxiliar = para_one_hot("ijkl mnopqrstuvwxyzabcdefgh")
mensagem_entrada = "o bolo de chocolate fica pronto quatro horas da tarde"
mensagem_entrada = "alemagno"
x = enigma(mensagem_entrada, alfabeto_cifrado, cifrador_auxiliar)
y = de_enigma(x, alfabeto_cifrado, cifrador_auxiliar)
print(x,y)

