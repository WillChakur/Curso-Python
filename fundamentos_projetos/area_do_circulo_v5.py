#Nessa versão vamos utilizar uma função com retorno
from math import pi


def area_do_circulo(raio):
    return pi * float(raio) ** 2


raio = input("Informe o raio: ")
area = area_do_circulo(raio)
print(f'A área do circulo é: {area}')