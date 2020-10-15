#7.
# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
# ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
# em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem
# compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas.

# 1 lata pinta 54m2
# 60 % 54 -> 6 (1 + 1 resto)
# 54 % 54 -> 0 apenas de 1 lata

metros = int(input("Metros: "))
if metros % 54 == 0:
  latas = metros / 54
else:
  latas = int(metros / 54) + 1

valor = latas * 80
print(f'{latas} latas.')
print(f'Total: R$ {valor:.2f}')


#TWP150
