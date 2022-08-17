#Agora vamos montar uma lista de convidados

print('Digite quit caso queira sair.')
with open('guest_book.txt', 'a') as file_object:
    while True:
        nome = input("Infome seu nome: ")
        if nome == 'quit':
            break
        file_object.write(nome + '\n')
        print(f'Seja bem vindo {nome}!!')