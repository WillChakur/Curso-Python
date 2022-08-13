#Operador de Membro
lista = [1, 2, 3, 'Ana', 'Carla']
2 in lista #True
'Ana' not in lista #False
#Esse operador é utilizado para analise se algum item está dentro de algo, ou não

#Operador Identidade
x = 3
y = x
z = 3
x is y #True
x is z #True
y is not z #False
#Nesse caso teremos True caso o valor armazenado pelas variáveis sejam iguais

#Um caso diferente é em listas, veja:
lista_a = [1, 2, 3]
lista_b = lista_a
lista_c = [1, 2, 3]

lista_a is lista_b #True
lista_a is lista_c #False
lista_c is not lista_c #True
#Diferente de váriaveis, as listas apontam para um local e não armazenam, ou seja mesmo tendo valores iguas a lista_a
#é diferente da lista_c