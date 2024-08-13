import math
oposto=int(input('Cateto oposto: '))
adjacente=int(input('Cateto adjacente: '))
hipotenusa=math.sqrt(math.pow(oposto, 2)+math.pow(adjacente, 2))
print('A hipotenusa vale:', hipotenusa)