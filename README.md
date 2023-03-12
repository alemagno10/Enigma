<h1>Enigma</h1>
<h2>Descrição</h2>
<p>Biblioteca com funcionalidades de criptografia e descriptografia de mensagens por meio de transformações matriciais.</p>
<h2>Como utilizar</h2>
1. Para utilizar localmente execute o comando: <br>
- `pip install git+https://github.com/alemagno10/Enigma` para baixar os módulos. <br>
2. Caso queira utilizar na forma de API, clone o repositório, baixe as dependências: <br>
- `git clone https://github.com/alemagno10/Enigma`;
- `pip install -r requirements.txt`;
- Execute o arquivo setup.py para iniciar o servidor;
- Como opcional, utilize o Postman para testar a rotas importanto o arquivo `APS2.postman_collection.json`. (Como importar)[https://testfully.io/blog/import-from-postman/#import-postman-collections]
<h2> Rotas da API </h2>
|Funcionalidade|Url path|
|Cifra|/encrypt/cifra|
|De_Cifra| /decrypt/de_cifra|
|Enigma|/encrypt/enigma|
|De_Enigma|/decrypt/de_enigma|
|Para_OneHot|/encrypt/one_hot| 
|Para_String|/decrypt/string|
