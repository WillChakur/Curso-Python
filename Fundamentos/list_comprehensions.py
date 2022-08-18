#Uma list comprehension é um modo mais compacto de criar uma lista
#Nesse metódo temos a junção de um for com a concatenação

quadrado_dos_numeros = [valor**2 for valor in range(1, 11)]
print(quadrado_dos_numeros)

primeiros_cubos = [cubos**3 for cubos in range(1, 11)]
print(primeiros_cubos)

