#5. Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando o algoritmo de Euclides

n1 = int(input("N1: "))
n2 = int(input("N2: "))

while n1 % n2 != 0:
    n1, n2 = n2, n1 % n2
print(f'MDC = {n2}')
