#4. Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a
# porcentagem do aumento. Exiba o valor do aumento e do novo salário.

salario = float(input("SALARIO: "))
percentual = float(input("AUMENTO: "))

percentual = percentual / 100.0
aumento = percentual * salario
novo_salario = salario + aumento

print(f'Aumento de: R$ {aumento}')
print(f'Novo salario: R$ {novo_salario}')