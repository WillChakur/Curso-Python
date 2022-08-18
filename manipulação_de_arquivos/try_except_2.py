#Agora vamos tratar do erro FileNotFoundError
'''
Vai ocorrer quando um arquivo solicitado não esteja no diretório pesquisado, ou não exista, ou o usuário pode ter colocado
o nome errado
'''

from word_county import word_county_function

filename = 'alice.txt'

try:
    with open(filename) as f_object:
        contents = f_object.read()
except FileNotFoundError:
    msg = 'O arquivo ' + filename + ' não foi encontrado.'
    print(msg)
else:
    print(f'O texto alice possuí {word_county_function(contents)} palavras')

#Caso o objetivo é que ocorra um erro silencioso, devemos usar o comando pass no except

