#9. Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo
# usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

km_percorridos = int(input("Digite a quantidade de KMs percorridos: "))
dias_carro = int(input("Informe a quantidade de dias de uso do carro: "))

aluguel_dia = 60.00 * dias_carro
km_rodado = 0.15 * km_percorridos
total = aluguel_dia + km_rodado

print(f'Voce vai pagar {total} por {km_percorridos} km percorridos em {dias_carro} dias de uso')