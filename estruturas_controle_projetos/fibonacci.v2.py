#Utilizando uma lista
#Neste exemplo só precisamos adicionar a soma na lista
#-1 é o último, e -2 é o penúltimo
def fibonacci():
    lista = [0, 1]
    while lista[-1] < 1000:
        lista.append(lista[-2] + lista[-1])
    return lista


for fib in fibonacci():
    print(fib)