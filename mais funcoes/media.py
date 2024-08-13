import random
lista = list(range(3))
print('Os valores da sua lista são:', lista)
def media():
    soma=sum(lista)
    qnt=len(lista)
    media = soma/qnt
    return media 
print('A média dos números da sua  lista é igual a:', media())