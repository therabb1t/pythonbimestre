#Faça um programa que leia o comprimento do cateto oposto, cateto adjacente, retornando o valor da hipotenusa.

import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = math.sqrt(ca ** 2 + co** 2) ** (1/2)
print("O valor da hipotenusa é: {}".format(hipotenusa))
