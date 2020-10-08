#3. Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário.
# Calcule o total em segundos.

dias = int(input("Informa a quantidade de dias: "))
horas = int(input("Informe a quantidade de horas: "))
minutos = int(input("Informe a quantidade de minutos: "))
segundos = int(input("Informe a quantidade de segundos: "))

# 1h = 3600s
# 1dia = 24h * 3600 =
# 1min = 60s
# 1s = 1s

segundos_segundos = segundos
minutos_segundos = minutos * 60
horas_segundos = horas * 3600
dias_segundos = (dias * 24) * 3600

print(f'{dias} dias tem {dias_segundos} segundos')
print(f'{horas} dias tem {horas_segundos} segundos')
print(f'{minutos} dias tem {minutos_segundos} segundos')
print(f'{segundos} dias tem {segundos_segundos} segundos')