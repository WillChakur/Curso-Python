#Esse arquivo vai armazenar o número favorito do usuário e relembrá-lo a partir de um arquivo json
import json

filename = 'favorite_number.json'

try:
    with open(filename, 'r') as f_object:
        number = json.load(f_object)
        print(f'Seu número favorito é {number}! :)')
except FileNotFoundError:
    number = input('Qual seu número favorito? ')
    with open(filename, 'w') as f_object:
        json.dump(number, f_object)
        print('Nós vamos lembrar seu número favorito! :)')