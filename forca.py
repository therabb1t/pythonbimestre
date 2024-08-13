import random

def escolher():
    palavras=['python', 'developing', 'game', 'jogo', 'programacao', 'algoritimo']
    return random.choice(palavras).upper() 

def jogo():
    palavra = escolher()
    palpites = []
    tentativas = 6
    
    print ('Vamos jogar forca?')
    print ('_ ' * len(palavra))
    while tentativas > 0:
        tentativa = input('Insira seu palpite: ').upper()
        if tentativa in palpites:
            print('Você já fez esse palpite. Tente Novamente.')
            continue

    
        palpites.append(tentativa) #append = anexar
        if tentativa in palavra:
            print('Você Acertou! Continue.')
        else:
            tentativas -= 1
            print ('Tente novamente, você ainda possui {} tentativas.'.format(tentativas))
    
    #sub-função
        oculto = "".join ([letra if letra in palpites else "_" for letra in palavra]) #.join = combinador
        print(" ".join(oculto))
    
        if "_" not in oculto:
            print('Você Adivinhou a palavra!')
            break

    if tentativas == 0:
        print('Você Perdeu! Sua palavra era: {}'.format(palavra))

jogo()
    