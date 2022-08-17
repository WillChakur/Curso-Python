#Dessa vez vamos perguntar o nome de um convidado e concatenar e escrever o nome dele em um arquivo texto
nome = input('Digite seu nome: ')

with open('guest.txt', 'w') as file_object:
    file_object.write(nome)