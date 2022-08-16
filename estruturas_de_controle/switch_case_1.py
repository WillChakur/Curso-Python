#No python nós não temos o switch case, mas podemos simula-lo

'''
Para simular vamos usar uma função get em um dicionário
Essa função vai ligar a chave a um valor
POR EXEMPLO:
'''


def get_dias_semana(dia):
    dias = {
        1: 'Segunda',
        2: 'Terça',
        3: 'Quarta',
        4: 'Quinta',
        5: 'Sexta'
    }
    return dias.get(dia, '*** invalido ***')


if __name__ == '__main__':
    for dia in range(1, 7):
        print(f'{dia} : {get_dias_semana(dia)}')