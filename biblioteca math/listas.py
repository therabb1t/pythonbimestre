# Criando uma lista de valores de 0-9
valores = list(range(10))
print(valores)
print('\n')

# enumerate
valores = list (range(10,20))
for indice, valor in enumerate (valores):
    print('O indice:{} tem o valor {}'.format(indice,valor))