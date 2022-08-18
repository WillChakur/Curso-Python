#Uma lista de números pode ser formada juntando a funçaõ range() com a função list()

#Aqui estamos montando uma lista de números de 1 a 5 sem contar o 5
numbers = list(range(1, 5))
print(numbers)

#Para montar uma lista de números pares vamos usar um terceiro parâmetro na função rand()
numeros_pares = list(range(2, 11, 2))
#O dois no final está pedindo para somar dois a cada passada do range
print(numeros_pares)