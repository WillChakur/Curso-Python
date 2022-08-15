#Dessa vez vamos pegar um argumento via terminal

#!/usr/local/bin/python3
from math import pi
#Agora vamos importar o argumento do sys(terminal)
import sys


def area_do_circulo(raio):
    return pi * float(raio) ** 2


#O sys.argv é a lista de argumentos passados para o terminal
raio = sys.argv[1]
area = area_do_circulo(raio)
print(f'A área do circulo é: {area}')