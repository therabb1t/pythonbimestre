import math
angulo = int(input('Vamos decobrir o seno, cosseno e tangente? \nDigite seu ângulo: '))
rad = math.radians(angulo)
seno = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
print('Seus valores são: ')
print('Seno:', seno, '\nCosseno:',cos, '\nTangente:',tan)