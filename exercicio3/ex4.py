#4. A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra deformação é simples: os dois
# primeiros elementos são 1; a partir de então, cada elemento é asoma dos dois anteriores. Faça um algoritmo que leia um
# número inteiro calcule o seu número de Fibonacci. F1= 1, F2= 1, F3= 2, etc

numero = int(input("Digite o valor de N: "))

a, b = 1, 1
contador = 1

while contador <= numero - 2:
    a, b = b, a + b
    contador = contador + 1
print(b)