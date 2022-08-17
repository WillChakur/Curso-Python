'''
O bloco try-except é utilizado para que tratemos excessões
, ou seja, quando ocorre algo que o python não sabe o que fazer.

Vamos usar quando prevemos que algum erro pode ocorrer, então mandamos uma mensagem para o usuário
'''

#Vamos tratar o erro de divisão por zero
#O programa vai tentar rodar o try, caso não consiga vai rodar o except, bem parecido com if e else
try:
    print(5/0)
except ZeroDivisionError:
    print('Você não pode dividir por zero')

print('Executando após a falha!!')

#Com esse bloco nós podemos continuar executando após a falha, então não temos uma pausa do algoritmo
