

# Calcule a média dos 10 números
n = 1
soma = 0
while n <= 10:
    x = int(input(f'{n} numero: '))
    soma = soma + x# Acumuladores
    n = n + 1 # Contadores
print(f'Média: {soma/10:.1f}')

