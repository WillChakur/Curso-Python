PALAVRAS_PROIBIDAS = {'futebol', 'religião', 'política'}
textos = [
    'João gosta de futebol e política',
    'A praia foi divertida'
]

'''
Nesse exemplo vamos jogar as palavras de cada texto para dentro de um set(conjunto)
Após isso vamos verificar se existe alguma interseção entre o set proibido
'''
for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        #Vazio = False // Não Vazia = True
        print(f'O texto possuí palavras proibidas: {intersecao}')
    else:
        print(f'Texto liberado: {texto}')