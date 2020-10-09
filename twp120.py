#Else

# O que fazer quando a condição do IF é falsa?
# Os dois códigos abaixo fazem a mesma coisa:

idade = int(input("Idade do carro: "))

if idade <= 3:
    print("Seu carro é novo!")
if idade > 3:
    print("Seu carro é velho!")

idade_moto = int(input("Idade da moto: "))

if idade_moto <= 3:
    print("Sua moto é nova!")
else:
    print("Sua moto é velha!")

