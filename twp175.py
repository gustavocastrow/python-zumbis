# Break

# E se não soubesse quando terminar?

soma = 0
contador = 0
while True:
    x = int(input("n (zero sai) : "))
    if x == 0:
        break
    else:
        contador = contador + 1
    soma = soma + x
print(f'Soma: {soma/contador:.1f}')