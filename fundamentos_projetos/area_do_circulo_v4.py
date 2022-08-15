#Nessa versão vamos utilizar uma função sem retorno
from math import pi

#O bloco da função é delimitada pela identação


def area_do_circulo(raio):
    print(f'Área do circulo: {pi * float(raio) ** 2}')


raio = input('Informe o raio: ')
area_do_circulo(raio)


