'''
O arquivo json é de suma importância devido a sua utilidade em armazenar dados, esses dados armazenados por json
são utilizados ao reabrir o programa, os dados vão ser recarregados a partir de um arquivo json.

Exemplo: O usuário pode fornecer vários tipos de informações e logo após fechar o programa, ao reabrir o programa
o arquivo json vai ser o responsável por armazenar esses dados e carregar eles na reabertura do programa.
'''

#Para armazenar um conjunto de dados vamos usar o json.dump
import json

numbers = [1, 2, 3, 4, 5, 6]

filename = 'numbers.json'

with open(filename, 'w') as f_object:
    #O json.dump vai armazenar a lista de números em um objeto
    json.dump(numbers, f_object)
#Podemos ver que foi criado um arquivo json com a lista inserida nele
