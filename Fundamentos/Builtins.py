#O builtinn é um módulo muito importante, nele temos várias funções importantes
__builtins__.type('Fala Galera!')
__builtins__.print(10/3)
#A maioria das função vão estar dentro do builtins

#O __builtins__ é um alias que aponta para o módulo builtins

#Um pouco de escopo global
#Usamos a função dir() para visualizar o escopo
print(dir(__builtins__))