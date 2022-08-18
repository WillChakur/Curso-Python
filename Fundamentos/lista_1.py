#Nesse arquivo vamos copiar uma lista em outra
favorite_foods = ['Pizza', 'Falafel', 'Carrot Cake']

#Usando o parentêses com dois pontos nós estamos dizendo que queremos do começo até o fim da lista
new_favorite_foods = favorite_foods[:]

new_favorite_foods.append('Pasta')

print(favorite_foods)
print(new_favorite_foods)