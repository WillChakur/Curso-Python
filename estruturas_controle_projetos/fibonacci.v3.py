#Usando a função soma: sum()

def fibonacci():
    lista = [0, 1]
    while lista[-1] < 1000:
        lista.append(sum(lista[-2:]))
        #Usando o [-2:] podemos usar o sum para somar apenas os dois últimos elementos
        #Esse comando vai limitar a lista aos dois últimos elementos
    return lista


for fib in fibonacci():
    print(fib)