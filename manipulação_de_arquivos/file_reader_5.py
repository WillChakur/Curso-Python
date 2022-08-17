#Nesse arquivo vamos manipular o texto de 'learning_python'

#Lendo o arquivo de maneira simples
with open('learning_python.txt') as file_object:
    content = file_object.read()
    print(content.rstrip())

#Usando um laço para percorrer o arquivo
with open('learning_python.txt') as file_object:
    for texto in file_object:
        print(texto.rstrip())

string_texto = ''

#Dessa maneira podemos utilizar os dados fora do bloco with
with open('learning_python.txt') as file_object:
    for texto in file_object:
        string_texto += texto

print(string_texto)

#Trocando Python por C
print(string_texto.replace('Python', 'C'))

