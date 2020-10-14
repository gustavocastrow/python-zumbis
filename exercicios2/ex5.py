#5.
# Faça um Programa que leia três números e mostre o maior e o menor deles

n1 = int(input("N1: "))
n2 = int(input("N2: "))
n3 = int(input("N3: "))

if n1 > n2 and n2 > n3:
    print(n1)
elif n2 > n3:
    print(n2)
else:
    print(n3)

if n1 < n2 and n2 < n3:
    print(n1)
elif n2 < n3:
    print(n2)
else:
    print(n3)