#Nesse arquivo vamos aprender a escrever em um arquivo
#Escrever em um arquivo é a melhor forma de salvar algo para se utilizar depois

#Para escrever devemos chamar o open() com um segundo argumento
with open('programming_txt', 'w') as file_object:
    file_object.write('Escrevendo utilizando a função write' + '\n' + 'I love programming!!!')