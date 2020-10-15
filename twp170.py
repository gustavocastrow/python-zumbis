# Acumulador pode ser produto..
# Fatorial de 10 ->  1*2*3*4*5*6*7*8*9*10
k = 1
fat = 1
while k <= 10:
    fat = fat * k
    k = k + 1
print(f'fat(10) = {fat}')


# Altere esse código para calcular o fatorial de um numero lido.
x = 1
fatorial = 1
numero = int(input("Informe um numnero: "))
while x <= numero:
    fatorial = fatorial * x
    x = x + 1
print(f' fat({numero}) = {fatorial}')