#Tratando do typerror
print('Insira "q" caso queira sair')
while True:
    primeiro_valor = input('Informe o primeiro valor: ')
    if primeiro_valor == "q":
        break
    segundo_valor = input('Informe o segundo valor: ')
    try:
        resultado = int(primeiro_valor) + int(segundo_valor)
    except ValueError:
        print('Você deve informar valores númericos :)')
    else:
        print(f'O resultado da soma foi: {resultado}')