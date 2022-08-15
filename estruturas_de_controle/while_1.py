#Valor aleatório
from random import randint

numero_informado = -1 #Inicia a variável com uma valor diferente do random
numero_sorteado = randint(0, 9)

while numero_informado != numero_sorteado:
    numero_informado = int(input("Informe um valor entre 0 a 9: "))

print(f'O valor sorteado foi o {numero_sorteado}!!')
