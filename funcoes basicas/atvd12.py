print ('Qual é maior e qual é menor?')
str1 = str(input('Digite a primeira palavra: '))
str2 = str(input('Digite a segunda palavra: '))
str3 = str(input('Digite a terceira palavra: '))
lista = [str1, str2, str3]  
max= max(lista, key=None)
min= min(lista, key=None)
print ('A menor palavra é ',max, ' e a maior ',min)