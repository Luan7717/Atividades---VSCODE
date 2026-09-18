import os
os.system('cls')

print('= TABUADA =')
numero = int(input('Digite um número: '))

print('\nAdição:')
for i in range(1, 11):
    print(f'{numero} + {i} = {numero + i}')

print('\nSubtração')
for i in range(1, 11):
    print(f'{numero} - {i} = {numero - i}')

print('\nMultiplição')
for i in range(1, 11):
    print(f'{numero} * {i} = {numero * i}')

print('\nDivisão:')
for i in range(1, 11):
    print(f'{numero} / {i} = {numero / i:.2f}')