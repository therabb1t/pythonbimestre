dinheiro = float(input('Qual quantia você deseja converter? '))
def convdolar(dinheiro):
    dolar = dinheiro / 5.97 
    print('Com {} reais voce consegue comprar {} dolares'.format(dinheiro,dolar))
convdolar(dinheiro)
def conveuro (dinheiro):
    euro = dinheiro / 6.12 
    print('Com {} reais voce consegue comprar {} euros'.format(dinheiro,euro))
conveuro(dinheiro)
def convrublo (dinheiro):
    rublo = dinheiro / 0.0066
    print('Com {} reais voce consegue comprar {} rublos'.format(dinheiro,rublo))
convrublo(dinheiro)