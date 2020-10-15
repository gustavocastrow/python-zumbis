#2. Faça um programa que leia um nome de usuário e a sua senha e não aceitei a senha igual ao nome do usuário
# mostrando uma mensagem de erro e voltando a pedir as informaçãoes.

usuario = input('Usuário: ')
senha = input('Senha: ')

while usuario == senha:
  print('Senha deve ser diferente do Usuário')
  usuario = input('Usuário: ')
  senha = input('Senha: ')
  while len(senha) <= 5:
    print("Senha deve ter mais que 5 caracteres:")
    usuario = input('Usuário: ')
    senha = input('Senha: ')
if usuario != senha:
    print("Bem vindo!")