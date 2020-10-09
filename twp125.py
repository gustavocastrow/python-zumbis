minutos = int(input("Informe o número de minutos falados: "))

if minutos < 200:
    preco = 0.2
else:
    if minutos <= 400:
        preco = 0.18
    if minutos <= 800:
        preco = 0.15
    else:
        preco = 0.08

print(f'R$ {preco * minutos:.2f}')