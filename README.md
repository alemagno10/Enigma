# Enigma
Por Alexandre Magno e Pedro Pertusi
## Descrição
Biblioteca com funcionalidades de criptografia e descriptografia de mensagens por meio de transformações matriciais + clone digital da máquina Enigma.
## Como utilizar
* Para utilizar localmente execute o comando: 
  - Instale o package: `pip install git+https://github.com/alemagno10/Enigma`;
  - Importe a biblioteca em seu arquivo python: `Import enigma`. 
* Caso queira utilizar na forma de API: 
  - Clone o repositório: `git clone https://github.com/alemagno10/Enigma`;
  - Baixe as dependências: `pip install -r requirements.txt`;
  - Execute o arquivo setup.py para iniciar o servidor;
  - Como opcional, utilize o Postman para testar a rotas importando o arquivo `APS2.postman_collection.json`. [(como importar)](https://testfully.io/blog/import-from-postman/#import-postman-collections)

## Módulos e Funcionamento

* A função `para_one_hot(msg : str)` pode ser usada para codificar mensagens como uma matriz usando one-hot encoding. Ela funciona criando uma matriz binária com 27 linhas, representando cada letra no alfabeto + espaço e com uma quantidade de colunas correspondente ao tamanho da mensagem.
* A função `para_string(M : np.array)` pode ser usada para converter mensagens da representação one-hot encoding para uma string legível. Este módulo tem um funcionamento oposto ao anterior, re-converte matriz para uma mensagem. 
* A função `cifrar(msg : str, P : np.array)` aplica uma cifra simples em uma mensagem recebida como entrada e retorna a mensagem cifrada. `P` é a matriz de permutação que realiza a cifra. Essa matriz representa um alfabeto embaralhado que é multiplicado pela matriz da mensagem, gerando um texto criptografado. `para_string(P @ para_one_hot(msg))`.
* A função `de_cifrar(msg : str, P : np.array)` recupera uma mensagem cifrada, recebida como entrada, e retorna a mensagem original. `P` é a matriz de permutação que realiza a cifra. Esse módulo segue os passos do anterior, entretanto a multiplicação matricial ocorre entre a matriz da mensagem e a matriz inversa de P. `para_string(P^-1 @ para_one_hot(msg))`.
* A função `enigma(msg : str, P : np.array, E : np.array)` faz a cifra enigma na mensagem de entrada usando o cifrador `P` e o cifrador auxiliar `E`, ambos representados como matrizes de permutação. Neste tipo de criptografia, a cifra é feita de forma única para cada caracter, seguindo a seguinte fórmula: `para_string((E)^N @ P @ para_one_hot(msg))`, sendo N a posição do carácter no texto. Como exemplo em "algebra" a letra "E" receberia a seguinte cifra: `(E)^3 @ P @ para_one_hot(msg)`.
* A função `de_enigma(msg : str, P : np.array, E : np.array)` recupera uma mensagem cifrada como enigma assumindo que ela foi cifrada com o usando o cifrador `P` e o cifrador auxiliar `E`, ambos representados como matrizes de permutação. Para descriptografar esse tipo de enigma, utiliza-se a seguinte fórmula para cada uma das letras da mensagem: `para_string((E^-1)^N @ P^-1 @ para_one_hot(msg))`.

## Rotas da API 

`https://localhost:5000`

| Funcionalidade | Url path |
| --- | --- |
| Cifra| /encrypt/cifra |
| De_Cifra | /decrypt/de_cifra |
| Enigma | /encrypt/enigma |
| De_Enigma | /decrypt/de_enigma |
| Para_OneHot | /encrypt/one_hot | 
| Para_String | /decrypt/string |

Para as rotas é necessário apenas passar a mensagem no body da requisição no formato JSON a seguir: {
    "mensagem":"o bolo de chocolate"
}. Com exceção do método para_string, que recebe uma matriz(27xN). N: quantidade de caracteres do texto.
