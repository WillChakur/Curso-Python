#Usando uma validação

#!/usr/local/bin/python3
from math import pi
import sys


def area_do_circulo(raio):
    return pi * float(raio) ** 2


def funcao_help():
    print("É necessario informar o raio do círculo.")
    print(f'Sintaxe {__file__} <raio>')


#Vamos ter uma lista com tamanho menor que 2 caso não seja informado o tamanho do raio
if len(sys.argv) < 2:
    funcao_help()
else:
    raio = sys.argv[1]
    area = area_do_circulo(raio)
    print(f'A área do circulo é: {area}')


