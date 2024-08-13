def primos(n):
    if n < 2:
        return False
    for i in range(2, int(n/2)+1):
        if n % i == 0:
            return False
    return True

if __name__=='__main__':
    n1 = int(input('Vamos achar os números primos? \nDigite o primeiro valor: '))
    n2 = int(input('Agora digite o até aonde vamos gerar números primos: '))

    print('Os primos no intervalo de {} a {} são:'.format(n1, n2))

    for i in range(n1, n2 + 1):
        if primos(i):
            print(i, end=' ')