#Vamos colocar mais validações e mensagem de erro

#!/usr/local/bin/python3
from math import pi
import sys
import errno

#Vamos adicionar cores para o erro
ERRO = '\033[91m' #Para cor vermelha
NORMAL = '\033[0m' #Para voltar para a cor normal


def area_do_circulo(raio):
    return pi * float(raio) ** 2


def funcao_help():
    print(ERRO + "É necessario informar o raio do círculo." + NORMAL)
    print(f'Sintaxe {__file__} <raio>')


if len(sys.argv) < 2:
    funcao_help()
    sys.exit(errno.EPERM) #Mensagem de erro: operação não permitida
    #O sys.exit vai fazer com que a operação finalize com uma mensagem

if not sys.argv[1].isnumeric(): #O is.numeric vai validar se o valor é númerico
    print(ERRO + 'O valor informado deve ser númerico' + NORMAL)
    sys.exit(errno.EINVAL)

    raio = sys.argv[1]
    area = area_do_circulo(raio)
    print(f'A área do circulo é: {area}')