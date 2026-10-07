import os
os.system('cls')

soma_pares = 0
soma_geral = 0
quantidade_pares = 0
quantidade_impares = 0
quantidade_geral = 0
while True:
    numero = int(input('Digite um número: '))
    if numero == 0:
        break
    soma_geral += numero
    quantidade_geral += 1
    if numero % 2 == 0:
        quantidade_pares += 1
        soma_pares += numero
    else:
        quantidade_impares += 1

print(f'Quantidade de pares: {quantidade_pares}')
print(f'Quantidade de ímpares: {quantidade_impares}')

if quantidade_pares > 0:
    media_pares = soma_pares / quantidade_pares
    print(f'Média dos pares: {media_pares:.2f}')

media_geral = soma_geral / quantidade_geral
print(f'Média geral: {media_geral:.2f}')