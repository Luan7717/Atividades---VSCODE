import os
os.system('cls')

#print('ACUMULANDO VALORES EM UMA VARIÁVEL.')
#soma = 0

#print(f'Valor inicial da variável soma: {soma}')

#for i in range(3):
#    numero = int(input('Digite um número para somar: '))
#    soma = soma + numero
#    print(f'\nvalor temporário da variável soma: {soma}')

#print(f'\nValor final da variável soma: {soma}')

print('ACUMULANDO VALORES EM UMA VARIÁVEL.')
soma = 0

for i in range(3):
    soma += int(input('Digite um número para somar: '))

print(f'\nValor final da variável soma: {soma}')