#É uma estrutura de dados onde temo um par de chave e valor
pessoa = {'nome': 'William de Morais Chakur', 'idade': 21, 'cursos': ['Engenharia da computação']}

print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['cursos'])
#Para pegar as chaves
print(pessoa.keys())
#Para pegar os valores
print(pessoa.values())
#Para pegar as chaves e os valores
print(pessoa.items())
print(pessoa.get('idade'))
#Podemos fazer adições e remoções dentro do dicionário
pessoa['idade'] = 20
pessoa['cursos'].append('Python')
print(pessoa.items())
#Para ler um valor e logo depois remover, usamos a função pop()
print(pessoa.pop('idade'))
pessoa.update({'idade': 21, 'sexo': 'Masculino'})
print(pessoa.items())
#Para deletar um par usamos o del
del pessoa['idade']
#Para limpar um dicionário usamos a função clear
pessoa.clear()




