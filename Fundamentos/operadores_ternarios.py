#Temos dois modos de usar o operador ternário
esta_chovendo = True
print('Hoje estou com as roupas ' + ('secas', 'molhadas')[esta_chovendo])
#Nesse caso quando "esta_chovendo" for True, o operador mais próximo dele sera o escolhido

print('Hoje estou com as roupas ' + ('molhadas' if esta_chovendo else 'secas'))
#Nesse segundo caso usamos o if e else