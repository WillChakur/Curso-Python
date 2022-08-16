#Nesse módulo vamos fazer um desafio

def get_desafio(dia):
    dias = {
        'Segunda': 'Dia de Semana',
        'Terça': 'Dia de Semana',
        'Quarta': 'Dia de Semana',
        'Quinta': 'Dia de Semana',
        'Sexta': 'Dia de Semana',
        'Sábado': 'Dia de Final de Semana',
        'Domingo': 'Dia de Final de Semana',
    }
    return dias.get(dia, '*** inválido ***')


dia = input("Informe o dia: ")

print(f'{get_desafio(dia)}')

