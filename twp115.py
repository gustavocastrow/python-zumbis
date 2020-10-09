#if

# Pergunte a velocidade de um carro, supondo um valor inteiro. Caso ultrapasse 110km/h, exiba uma mensagem dizendo
# que o usuario foi multado. Neste caso, exiba o valor da multa cobrando R$ 5,00 por km acima de 110.

velocidade = int(input("Informe sua velocidade (km/h): "))
multa = (velocidade - 110) * 5
if velocidade > 110:
    print(f"Velocidade acima da média, você foi multado em R$ {multa:.2f} ")
else:
    print("Velocidade dentro das normas, seguir viagem")