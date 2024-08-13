string = str(input('Vamos descobrir palindromos? \nDigite a palavra: '))
semespaço = string.replace(' ', '')
minuscula = semespaço.lower()
inv = minuscula[::-1]
if inv == minuscula:
    print ('É um palindromo!')
else:
    print ('Não é um palindromo! :(')