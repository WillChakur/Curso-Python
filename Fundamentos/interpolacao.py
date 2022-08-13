nome, idade = 'Ana', 30 # Podemos fazer uma atribuição dupla

# Primeiro tipo de interpolação, bem parecido com linguagem
print('Nome: %s Idade: %d' % (nome, idade))

#Segundo método usando format
print('Nome: {0} Idade: {1}' .format(nome, idade))

#Terceiro método e melhor
print(f'Nome: {nome} Idade: {idade}')
print(f'Conta em string {1*2*3*4*5}')

#Podemos usar o Templeta do módulo string