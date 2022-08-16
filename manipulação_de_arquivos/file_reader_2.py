#Agora vamos ler linha por linha
#O "as" vai dizer a variável em que vamos armazenar o arquivo
with open('pi_digits.txt') as file_object:
    #Para ler cada linha vamos usar um for
    for line in file_object:
        print(line.rstrip())
        #rstrip novamente para tirar os caracteres de quebra de linha