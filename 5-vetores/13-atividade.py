import os
os.system('cls')

vetor_numero = []

for i in range(5):
    numero = int(input(f'Digite o {i+1}º número: '))
    if numero < 0:
        numero = 0
    vetor_numero.append(numero)

print('\nNúmeros digitados:')
for numero1 in (vetor_numero):
    print(numero1)