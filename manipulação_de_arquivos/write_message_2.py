#Agora vamos concatenar textos ou dados no arquivo 'programming'

#Para isso devemos abrir o arquivo no modo de concatenação, com "a"
with open('programming_txt', 'a') as file_object:
    file_object.write('\n' + 'I also love games')
#Toda vez que esse algoritmo rodar vamos ver mais uma concatenação