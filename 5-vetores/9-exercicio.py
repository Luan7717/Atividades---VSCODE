import os
os.system('cls')

vetor_notas = []
QUANTIDADE_NOTAS = 5

for i in range(QUANTIDADE_NOTAS):
    nota = int(input(F'Digite o {i+1}º número: '))
    vetor_notas.append(nota)

maior_nota = max(vetor_notas)
menor_nota = min(vetor_notas)

print('\n= EXIBINDO OS NÚMEROS DO VETOR =')
for  posicao, numero in enumerate(vetor_notas, start=1):
    print(f'{posicao} número: {numero}')

print(f'\n= EXIBINDO A MENOR E MAIOR NÚMEROS DO VETOR =')
print(f'Maior número: {maior_nota}')
print(f'Menor número: {menor_nota}')