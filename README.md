# API de Teste de Autenticação via WinRM

Essa API foi desenvolvida em Python com o framework Flask para testar a autenticação via WinRM em servidores remotos. O objetivo da API é permitir que o usuário teste a conexão remota com um servidor e execute um comando para verificar se a comunicação está funcionando corretamente. A API suporta diferentes tipos de autenticação, incluindo NTLM, Kerberos e CredSSP.

## Instalação

Para executar a API, você precisará ter o Python 3 instalado na sua máquina. Em seguida, execute o seguinte comando para instalar as bibliotecas necessárias:

```bash
pip install -r requirements.txt
```

Além disso, é necessário ter as seguintes dependências instaladas no seu sistema:

`krb5-config`: necessário para a autenticação Kerberos.
Para instalá-las, utilize o gerenciador de pacotes do seu sistema (por exemplo, `apt-get` no Ubuntu ou `brew` no macOS).

## Uso
Para executar a API, execute o seguinte comando:
```bash
python app.py
```
A API estará disponível em http://localhost:5000.

## Testando a API
Você pode testar a API de diferentes formas. A seguir, descrevemos duas maneiras de fazê-lo: usando o Postman e usando o cURL.

Postman
- Instale o Postman em sua máquina.
- Importe a coleção winrm_api.postman_collection.json.
- Abra a requisição desejada e clique em "Send".
- O resultado da requisição será exibido na aba "Body".

cURL
Execute o seguinte comando para testar a API usando cURL:

```bash
curl -H "Content-Type: application/json" \
  --negotiate -u : \
  --data '{"host":"<IP_DO_SERVIDOR>", "user":"<USUARIO>", "password":"<SENHA>", "transport":"<TIPO_DE_TRANSPORTE>", "command":"<COMANDO>"}' \
  http://localhost:5000/winrm
```

Substitua `<IP_DO_SERVIDOR>`, `<USUARIO>`, `<SENHA>`, `<TIPO_DE_TRANSPORTE>` e `<COMANDO>` pelos valores desejados.

## Parâmetros
A API suporta os seguintes parâmetros:

- `host`: o endereço IP do servidor remoto que você deseja testar.
- `user`: o nome de usuário usado para autenticação no servidor remoto no formato `DOMAIN\User`.
- `password`: a senha usada para autenticação no servidor remoto.
- `transport`: o tipo de autenticação usado. Os valores possíveis são `ntlm`, `kerberos` e `credssp`.
- `command`: qualquer comando para realizar o teste remoto. Ex: `ipconfig /all`.

## Contribuição
Contribuições são bem-vindas! Se você tiver sugestões de melhoria ou encontrar algum problema, sinta-se à vontade para abrir uma issue ou um pull request.