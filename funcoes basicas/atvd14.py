p1 = str(input('Digite a primeira palavra: '))
p2 = str(input('Mais uma: '))
p3= str(input('E mais uma: '))
lista = [p1,p2,p3]
for indice, valor in enumerate(lista, start=1):
    print(indice, valor)