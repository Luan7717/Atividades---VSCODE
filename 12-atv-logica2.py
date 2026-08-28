import os
os.system('cls')

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

maior = max(n1, n2, n3)
menor = min(n1, n2, n3)

print(f'\nPrimeiro número: {n1}')
print(f'Segundo número: {n2}')
print(f'Terceiro número: {n3}')
print(f'Maior número: {maior}')
print(f'Menor número: {menor}')
