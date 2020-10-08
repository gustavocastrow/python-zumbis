#6. Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem

distancia_percorrida = float(input("Informe a distancia percorrida em km: "))
velocidade_media = int(input("Informe a velocidade media: "))

tempo = distancia_percorrida / velocidade_media

print(f'O tempo em horas para percorrer {distancia_percorrida}km sera de: {tempo} horas')