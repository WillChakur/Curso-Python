import json

filename = 'username.json'
with open(filename, 'r') as f_object:
    username = json.load(f_object)
    print(f'Bem vindo de volta {username}!!')

#Aqui nesse programa, nós conseguimos ler dados que foram gerados em outro programa e armazenados em username.json