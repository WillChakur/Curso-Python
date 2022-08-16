#Esse programa vai abrir, ler e imprimir algum arquivo na tela

#Para começar devemos abrir o arquivo com a função open()
#O open vai procurar o arquivo no mesmo diretório da file.py
#Caso não esteja no mesmo diretório, devemos passar o path do arquivo
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
#A função open vai devolver um objeto que vai representar o arquivo
#O objeto vai ser armazenado em file_object

#A palavra reservada with vai ser a responsável pelo fechamento do arquivo quando não for mais necessário seu uso

'''
A função read() vai devolver uma string em branco quando chegar no final do arquivo,
com isso vamos ter uma linha em branco

Para fugir dessa linha em branco usamos a função rstrip()
'''