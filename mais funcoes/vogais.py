def contador(palavra):
    vogais = "aeiouAEIOU"
    contador = 0
    for char in palavra:
        if char in vogais:
            contador += 1
    return contador

palavra = str(input('Vamos contar vogais? \nDigite uma palavra: '))
print('O número de vogais na sua palavra é',contador(palavra))