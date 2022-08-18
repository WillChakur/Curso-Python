#Nesse arquivo vamos salvar os dados que o usuário inseriu, usando json
import json

filename = 'username.json'

try:
    with open(filename, 'r') as f_object:
        username = json.load(f_object)
        input_username = input('Username: ')
        if input_username == username:
            print(f'Bem vindo de volta {username}!!')
        else:
            print('Username incorreto')
except FileNotFoundError:
    username = input('Informe seu nome: ')
    with open(filename, 'w') as f_object:
        json.dump(username, f_object)
        print(f'{username} você será lembrado quando retornar')

#Caso o arquivo não seja encontrado, o programa vai criar um arquivo nome e armazenar os dados nele
