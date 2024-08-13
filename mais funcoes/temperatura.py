C = float(input('Digite a temperatura inicial em graus Celsius: '))

def convF(C):
    F = C * (9 / 5) + 32
    print('Valor em Fahrenheit: {}°F'.format(F))
convF(C)

def convK(C):
    K = C + 273
    print('Valor em Kelvin: {}°K'.format(K))
convK(C)
