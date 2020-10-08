#10. Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a
#    quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10
#   minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias.

cigarros_dia = int(input("Informe a quantidade de cigarros fumados por dia: "))
anos_fumando = int(input("Informe a quantidade de anos como fumante: "))

total_cigarros = (anos_fumando * 365) * cigarros_dia
dias_perdidos = (total_cigarros * 10)/24

print(f'Voce perdera um total de {dias_perdidos:.2f} dias')
