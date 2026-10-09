import os
os.system('cls')

soma = 0
contador = 0

while True:
    numero = int(input('Digite um número: '))
    if numero < 0:
        break
    soma += numero
    contador += 1

media = soma / contador
print(f'Média: {media:.2f}')