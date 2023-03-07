from __future__ import annotations
import numpy as np


def para_one_hot(msg : str):
    posicoes = {letra: indice for indice, letra in enumerate('abcdefghijklmnopqrstuvwxyz ')}
    return np.array([[1 if posicoes[j] == i else 0 for i in range(27)] for j in msg.lower()]).T

def para_string(M):
    M = M.T
    alfabeto, resultado = 'abcdefghijklmnopqrstuvwxyz ', ""
    for i in range(M.shape[0]):
        resultado += alfabeto[np.where(M[i] ==  1)[0][0]]
    return resultado

def cifra(msg,M):
    return para_string(M @ para_one_hot(msg))

def de_cifra(msg, M):
    return para_string(np.linalg.inv(M) @ para_one_hot(msg))

def enigma(msg, P, E):
    hotMsg = para_one_hot(msg).T
    final = P @ hotMsg[0]
    for i in range(1,hotMsg.shape[0]):
        x = P @ hotMsg[i]
        for _ in range(i):
            x = E @ x
        final = np.vstack((final,x.T))
    return para_string(final.T)

def de_enigma(msg, P, E):
    msg = para_one_hot(msg).T
    final = np.linalg.inv(P) @ msg[0]
    for i in range(1,msg.shape[0]):
        x = msg[i] 
        for _ in range(i):
            x = np.linalg.inv(E) @ x 
        final = np.vstack((final, np.linalg.inv(P) @ x))
    return para_string(final.T)
