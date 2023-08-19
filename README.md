# Calculadora Simples Cliente-Servidor

Este é um aplicativo básico cliente-servidor construído em Python que simula uma calculadora simples. O cliente envia solicitações para o servidor para realizar várias operações matemáticas, incluindo adição, subtração, multiplicação e divisão. O servidor processa as solicitações e envia os resultados de volta para o cliente.

## Como Funciona

1. O cliente e o servidor se comunicam por meio de sockets, usando um protocolo predefinido.
2. O cliente envia uma solicitação contendo a operação desejada e os operandos para o servidor.
3. O servidor recebe a solicitação, realiza a operação solicitada e envia o resultado de volta para o cliente.
4. O cliente exibe o resultado.

## Operações Suportadas

A calculadora suporta as seguintes operações:

- Adição (+)
- Subtração (-)
- Multiplicação (*)
- Divisão (/)

## Uso

1. Inicie o servidor executando `server.py`. e em outro terminal execute `client.py`
   python server.py
   python client.py
2. O cliente solicita que você escolha uma operação e insira dois números.
3. O cliente envia a solicitação para o servidor, que a processa e envia o resultado de volta.
4. O cliente exibe o resultado.

## Exemplo
  Suponha que você queira realizar o seguinte cálculo:

  Operação: Adição
  Primeiro número: 10
  Segundo número: 5
  Resultado esperado: 10 + 5 = 15

  1. Execute o cliente e escolha "ADD" como operação.
  2. Insira "10" como o primeiro número e "5" como o segundo número.
  3. O cliente exibe o resultado "Resultado: 15".

## Notas 

  1. O servidor lida com solicitações inválidas de forma adequada e envia uma resposta apropriada.
  2. A divisão por zero não é permitida, e o servidor responde com uma mensagem de erro se isso for tentado.
  3. Este projeto é uma ilustração básica e não possui recursos como tratamento de erros, validação de entrada e considerações de segurança. É recomendado para fins educacionais e como ponto de partida para aplicativos mais complexos.
