def main():
    n = int(input("Vamos calcular fatoriais? \nDigite o valor de n: "))
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i = i + 1
    print("O valor de %d! é =" %n, fat)
main()