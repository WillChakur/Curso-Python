#Dessa vez vamos procurar pela minha data de aniversário dentro do arquivo de texto pi_million_digits

pi_million = ''
#Primeiro criamos uma string referente a data de aniversário
aniversário = '1909'

with open('pi_million_digits.txt') as file_object:
    for texto in file_object:
        pi_million += texto


#Usando a função find podemos encontrar uma sequência de caracteres dentro de uma string
if pi_million.find(aniversário):
    print('Sua data de aniversário está dentro do PI!!!')
else:
    print('Não está :(')

