#Nessa versão vamos pegar dados do usuário
from math import pi # Usando from podemos pegar apenas o pi do módulo math

raio = input('Informe o raio: ')
print('Área do círculo', pi * float(raio) ** 2)

'''
O input vai ter como entrada um valor string, ou seja, temos
que forçar a mudança de tipo de dados para float ou int

float(raio)
'''