#Percorrendo estruturas de dados

#String
palavra = 'paralelepípedo'
for letra in palavra:
    print(letra, end=' ') #Como padrão o fim do print vem com o 'barra n', mas podemos mudar usando o 'end'

print('Fim')

#Lista
aprovados = ['William', 'Pedro', 'Felipe', 'Jackieline']
for nome in aprovados:
    print(nome, end=' ')

print('Fim')

#Tupla
dias_da_semana = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta')
for dia in dias_da_semana:
    print(f'Hoje é {dia}')

#Conjunto // Set
for numero in {1, 2, 3, 4, 5, 6}:
    print(numero)


#Dicionário
pessoa = {'nome': 'William', 'idade': 21, 'faculdade': 'UTFPR'}
for chave in pessoa:
    print(chave)

for valor in pessoa.values():
    print(valor)

for chave, valor in pessoa.items():
    print(f'{chave} : {valor}')