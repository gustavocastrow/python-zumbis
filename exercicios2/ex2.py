#2. Determine se um ano é bissesexto

ano = int(input("Informe o ano: "))

if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} NÃO é bissexto!')