'''Execute esse arquivo para ver as funcionalidades de Enigma'''
from enigma.functions import *
placeholder = "algebra"
print("\nBem vindo a demo do programa Enigma, por Alexandre Magno e Pedro Pertusi!\n")

print("A base dessa aplicação consiste em converter mensagens para matrizes e vice-versa,")
print("por meio das funções para_one_hot e para_string.\n")
m = para_one_hot(placeholder)
print(f"m = para_one_hot('{placeholder}')")
print(para_one_hot(placeholder))
print(f"s = para_string(m)")
print(para_string(m)+"\n")

print("É possível também utilizar uma matriz auxiliar de um alfabeto embaralhado\npara criptografar uma mensagem por meio de uma cifra simples.\n")
aux = para_one_hot("qwertyuiopasdfghjklzxc vbnm")
c = cifra(placeholder, aux)
print(f"c = cifra('{placeholder}', aux)")
print(cifra(placeholder, aux))
print(f"dc = de_cifra('{placeholder}', aux)")
print(de_cifra(c, aux)+"\n")

print("Por fim a principal funcionalidade do programa: ")
print("A criptografia de mensagens por meio da cifra básica junto de uma cifragem adicional única para cada caracter.\n")
aux2 = para_one_hot("zxcvbnm asdfghjklpoiuytrewq")
e = enigma(placeholder,aux,aux2)
print(f"e = enigma('{placeholder}',aux,aux2)")
print(e)
print("de = de_enigma(e,aux,aux2)")
print(de_enigma(e,aux,aux2)+"\n")

print("Obrigado pela atenção.\nPara testar a API, consulte o readme.me")