import math

def equacao(a, b, c):
    discriminante = math.pow(b,2) - 4*a*c
    
    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return 'Duas soluções para sua equação: \nx1 {}, \nx2{}'. format(x1,x2)
    elif discriminante == 0:
        x = -b/(2*a)
        return 'Uma solução para sua equação: x = {}'.format(x) 
    else: 
        return 'Não há solução para sua equação'
    
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

if a == 0:
    print('O valor de ',a,' deve ser diferente de zero para realizarmos a equação.')
else:
    resultado = equacao(a, b, c)
    print(resultado)