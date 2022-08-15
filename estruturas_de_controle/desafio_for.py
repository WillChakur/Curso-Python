from random import randint


def sortear_dado():
    return randint(1, 6)


numero_sorteado = sortear_dado()

for numero in range(1, 7):
    if numero % 2 != 0:
        continue
        #O continue ter papel de filtrar os ímpares

    if numero == numero_sorteado:
        print('Acertou!!!', numero)
        break
else:
    print('Não acertou o número!')


