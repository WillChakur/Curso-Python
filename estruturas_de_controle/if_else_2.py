def faixa_etaria(idade):
    if 0 <= idade < 18:
        return 'Menor de idade'
    elif idade in range(18, 65): #O in range vai abrangir um intervalo de 18 até 65, sem o 65
        return 'Adulto'
    elif idade in range(65, 100):
        return 'Melhor idade'
    elif idade >= 100:
        return 'Centenário'
    else:
        return 'idade inválida'