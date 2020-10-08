#5. Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e opreço a pagar.

preco_mercadoria = float(input("Valor da mercadoria: R$ "))
desconto_mercadoria = float(input("Percentual do desconto:  "))

novo_preco = preco_mercadoria - ((preco_mercadoria*desconto_mercadoria)/100)
desconto = preco_mercadoria - novo_preco

print(f'Valor do desconto: R$ {desconto}')
print(f'Total a pagar: R$ {novo_preco}')