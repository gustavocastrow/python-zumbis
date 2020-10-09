# ELIF.

minutos = int(input("Minutos: "))

if minutos < 200:
    preco = 0.2
elif minutos <= 400:
    preco = 0.18
elif minutos <= 800:
    preco = 0.15
else:
    preco = 0.08
print(f'R$ {preco * minutos:.2f}')