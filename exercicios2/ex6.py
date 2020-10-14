#6.Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule
# e mostre o total do seu salário no referido mês, sabendo se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS,quanto pagou ao sindicato
# e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os descontos e o salário líquido, conforme a tabela abaixo:/

# A. + Salario Bruto: R$
# B. IR (11%): R$
# C. - INSS (8%): R$
# D. - Sindicato (5%): R$
# E. = Salario Liquido: R$

salario_hora = int(input("Informe quantos R$ você ganha por hora: "))
horas_trabalhadas = int(input("Informe o número de horas trabalhadas no mes: "))
salario_bruto = horas_trabalhadas * salario_hora

imposto_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

descontos = imposto_renda + inss + sindicato

salario_liquido = salario_bruto - descontos

print(f'+ SALARIO BRUTO: R$ {salario_bruto:.2f}')
print(f'- DESCONTOS: IR: R$ {imposto_renda:.2f}, INSS: R$ {inss:.2f}, R$ SINDICATO: {sindicato:.2f}, R$ totalizando - {descontos:.2f}')
print(f'+ SALARIO LIQUIDO: R$ {salario_liquido:.2f}')
