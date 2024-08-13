def converter():
    metros= float(input('Digite a medida em metros: '))
    cm = metros * 100
    mm = metros * 1000
    km = metros / 1000
    print(f'{metros} metros equivalem a:')
    print(f'{cm:.2f} centímetros')
    print(f'{mm:.2f} milímetros')
    print(f'{km:.2f} quilômetros')
converter()