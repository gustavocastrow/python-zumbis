#1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue
# pedindo até que o usuario informe um valor válido.

nota = float(input("Digite uma nota: "))

while nota < 0 or nota > 10:
    print("Apenas notas entre 0 e 10 serão aceitas")
    nota = float(input("Digite uma nota: "))
