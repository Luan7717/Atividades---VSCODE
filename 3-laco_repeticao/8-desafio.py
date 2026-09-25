import os
os.system('cls')

pares = 0
impares = 0

for i in range(5):
    numero = int(input('Digite um valor inteiro: '))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f'Quantidade de pares: {pares}.')
print(f'Quantidade de impares: {impares}.')
