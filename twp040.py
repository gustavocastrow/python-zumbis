nome = "Gustavo"
print(f'Ola {nome}')

preco = 99.123232
print(f'Preço é R$ {preco:.2f}')
# ":.2f" duas casas decimais

# Operadores Relacionais: > , < , ==, >= , <=, !=(diferente)
# and
# or
# not

nota = 5
faltas = 20

if (nota >= 6 and faltas <= 20):
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")