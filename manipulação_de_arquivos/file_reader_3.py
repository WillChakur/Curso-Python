#Agora vamos armazenar as linhas em uma lista
with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())

#Agora vamos manipular tirando os espaços em branco
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
    #Vamos concatenando as linhas na string
print(pi_string)
print(len(pi_string))