import os
os.system('cls')

vetor_notas = []
pares = 0
impares = 0
QUANTIDADE_NOTAS = 5

for i in range(QUANTIDADE_NOTAS):
    nota = int(input(F'Digite o {i+1}º número: '))
    vetor_notas.append(nota)

maior_nota = max(vetor_notas)
menor_nota = min(vetor_notas)

print('\n= EXIBINDO OS NÚMEROS DO VETOR E IMPARES E PARES =')
for  posicao, numero in enumerate(vetor_notas, start=1):
    print(f'{posicao} número: {numero}')
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f'\nQuantidade de pares: {pares}.')
print(f'Quantidade de impares: {impares}.')