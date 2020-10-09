#IF.
# Verificar se um carro e novo ou velho
# Se o carro tiver pelo menos tres anos e novo.

idade = int(input("Informe a idade do seu carro: "))

if idade <= 3:
    print("Seu carro é novo")
if idade > 3:
    print("Seu carro é velho!")