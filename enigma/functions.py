import numpy as np
from unidecode import unidecode

def para_one_hot(msg : str):
    '''Recebe uma mensagem. Retorna uma matriz binária(27xN), sendo N a quantidade de caracteres da string.'''
    posicoes, msg = {letra: indice for indice, letra in enumerate('abcdefghijklmnopqrstuvwxyz ')}, unidecode(msg.lower())
    return np.array([[1 if posicoes[j] == i else 0 for i in range(27)] for j in msg if j in posicoes]).T

def para_string(M):
    '''Recebe uma matriz binária(27xN). Retorna a string correspondente.'''
    M = M.T
    alfabeto, resultado = 'abcdefghijklmnopqrstuvwxyz ', ""
    for i in range(M.shape[0]):
        resultado += alfabeto[np.where(M[i] ==  1)[0][0]]
    return resultado

def cifra(msg, M):
    '''Recebe uma mensagem e uma matriz de permutação. Converte esta string para uma matriz e 
    multiplica-a pela matriz de permutação. Retorna uma string reconvertida.'''
    return para_string(M @ para_one_hot(msg))

def de_cifra(msg, M):
    '''Recebe uma mensagem cifrada e uma matriz de permutação. Converte esta string para uma matriz e 
    multiplica-a pelo o inverso da matriz de permutação. Retorna a string original.'''
    return para_string(np.linalg.inv(M) @ para_one_hot(msg))

def enigma(msg, P, E):
    '''Recebe uma mensagem e duas matrizes de permutação. Faz uma cifragem única para cada carácter, de 
    acordo com a posição de cada um deles, aos moldes da máquina Enigma. Retorna uma string cifrada.'''
    hotMsg = para_one_hot(msg).T
    final = np.array([P @ hotMsg[0]])
    for i in range(1,hotMsg.shape[0]):
        x = P @ hotMsg[i]
        for _ in range(i):
            x = E @ x
        final = np.vstack((final,x.T))
    return para_string(final.T)

def de_enigma(msg, P, E):
    '''Recebe uma mensagem cifrada e duas matrizes de alfabetos de permutação. Descriptografa por carácter, 
    por meio de multiplicações por matrizes inversas, ao longo da mensagem. Retorna a string original'''
    msg = para_one_hot(msg).T
    final = np.array([np.linalg.inv(P) @ msg[0]])
    for i in range(1,msg.shape[0]):
        x = msg[i] 
        for _ in range(i):
            x = np.linalg.inv(E) @ x 
        final = np.vstack((final, np.linalg.inv(P) @ x))
    return para_string(final.T)
