#Agoras vamos carregar um arquivo json com a função json.load()
import json

filename = 'numbers.json'

with open(filename, 'r') as f_object:
    #json.load vai retornar o conteúdo do arquivo json
    numbers = json.load(f_object)
    print(numbers)

#Essa é uma maneira simples de compartilhar dados entre dois programas

