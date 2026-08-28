import os
os.system('cls')

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

# PROCESSO.
if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1

# SAIDA.
print(f'\nPrimeiro número: {n1}')
print(f'Segundo número: {n2}')
print(f'Maior número: {maior}')
print(f'Menor número: {menor}')