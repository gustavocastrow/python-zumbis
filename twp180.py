# While dentro do while

tabuada = 1
while tabuada <= 10:
    print(f'Tabuada do {tabuada}')
    n = 1
    while n <= 10:
        print(f'{tabuada} x {n} = {tabuada*n}')
        n = n + 1
    tabuada = tabuada + 1
    print()