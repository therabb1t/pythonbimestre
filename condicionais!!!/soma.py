def valores(quantidade):
    lista = []
    for i in range(quantidade):
        numero = float(input(f" - Digite o {i + 1}º número: "))
        lista.append(numero) 
    return lista        
def main():
    quantidade = int(input('Vamos somar números com Python?\nDigite a quantidade de números que deseja somar: '))
    lista = valores(quantidade)
    soma = sum(lista) 
    print(f'A soma dos números é igual a {soma}.')
main()