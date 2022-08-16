PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'política')
#Temos uma convenção de colocar as constantes em letra maiúscula no python
textos = [
    'João gosta de futebol e política',
    'A praia foi divertida'
]

for texto in textos:
    found = False
    for palavra in texto.lower().split(): #O split vai separar cada substring
        if palavra in PALAVRAS_PROIBIDAS: #Aqui podemos relacionar uma string a lista
            print(f'O texto possui pelo menos uma palavra proibida: {palavra}')
            found = True
            break
    if not found:
        print('Texto autorizado:', texto)