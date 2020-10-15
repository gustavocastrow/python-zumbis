n1 = int(input("Digite um numero: "))
x = 1

while x <= n1:
    print(x)
    x = x + 1

x = 1 # inicalizacao das variaveis
while x <= 3: # condição de parada
    print(x) # bloco de repetição
    x = x + 1

# Imprima os números pares de zero até um número lido

n2 = int(input("Informe o numero max: "))

x = 0

while x <= n2:
    print(x)
    x = x + 2

# Somar 10 inteiros lidos

contador = 1
soma = 0

while contador <= 10:
    x = int(input(f'{contador} número: '))
    soma = soma + x
    contador = contador + 1
print(f'Soma: {soma}')

# Calcule a média dos 10 números

