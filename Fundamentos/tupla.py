#Uma dupla é uma estrutura de dados imutável
tupla = ('verde', 'amarelo', 'azul', 'branco')
#Se a tupla possuír um único elemento devemos utilizar a vírgula depois dele
tupla_unitaria = ('unico_item',)
print(tupla)
print(tupla_unitaria)

#Podemos contar a quantidade de um tipo de elemento dentro da tupla, utilizando a função count
print(tupla.count('verde'))