#A lista é o equivalente ao array
#Ela é mutável, ou seja, podemos adicionar e remover itens dela
#Diferente do C, em python podemos juntar mais de um tipo de dado dentro de uma lista
#Mas utilizar listas heterogêneas não são boas práticas

lista = []

#Para adicionar um número na lista, usamos a função append
lista.append(1)
lista.append('William')
#Podemos adicionar uma nova lista dentro de uma lista
lista.append([1, 2, 3])

#E usamos o remove para remover um item da lista
lista.remove('William')
print(lista)

#A função reverse() pode inverter a ordem de uma lista
lista.reverse()
print(lista)

#Para descobrir o index de um item usamos a função index()
print(lista.index(1))