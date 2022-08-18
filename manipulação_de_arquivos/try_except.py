'''
O bloco try-except é utilizado para que tratemos excessões
, ou seja, quando ocorre algo que o python não sabe o que fazer.

Vamos usar quando prevemos que algum erro pode ocorrer, então mandamos uma mensagem para o usuário
'''

#Vamos tratar o erro de divisão por zero
#O programa vai tentar rodar o try, caso não consiga vai rodar o except, bem parecido com if e else
print("Insira 'q' para sair.")

while True:
    primeiro_valor = input('Informe o primeiro valor: ')
    if primeiro_valor == 'q':
        break
    segundo_valor = input('Informe o segundo valor: ')

    try:
        resultado = int(primeiro_valor) / int(segundo_valor)
    except ZeroDivisionError:
        print('Você não pode dividir por zero')
    else:
        print(f'O resultado da divisão foi: {resultado}')

#Com esse bloco nós podemos continuar executando após a falha, então não temos uma pausa do algoritmo
#Sabendo disso é essencial colocar qualquer comando que dependa do resultado do bloco try em uma bloco else
