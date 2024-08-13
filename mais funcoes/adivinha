from random import randint
random = randint(0, 20)
palpite = 0;
tentativas = 5;
print ('Vamos jogar adivinha? Você possui 5 tentativas.')
while palpite!= random:
    palpite = input('Insira seu palpite de 0 á 20: ')
    if palpite.isnumeric():
        palpite = int(palpite)
        tentativas = tentativas - 1
        if palpite == random:
            print('Você acertou o número {} !'.format(random))
            break;
        else:
            if palpite > random:
                print('Tente novamente. Dica: É um número menor.')
            else:
                print('Tente novamente. Dica: É um número maior.')
            print('Você ainda possui {} chances.'.format(tentativas))
        if tentativas == 0:
            print('Você perdeu!')
            break;
