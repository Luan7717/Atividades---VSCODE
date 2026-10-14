import os
os.system('cls')

print('= INSERINDO NOTAS =')
vetor_notas = []
QUANTIDADE_NOTAS = 4

for i in range(QUANTIDADE_NOTAS):
    nota = float(input(f'Digite a {i+1}° nota: '))
    vetor_notas.append(nota)
os.system('cls')

print('\n= EXIBINDO NOTAS =')
for lugar, nota in enumerate (vetor_notas, start=1):
    print(f'{lugar}° Nota do aluno: {nota}')
    media = sum(vetor_notas) / QUANTIDADE_NOTAS
if media >= 7:
    r = 'Aprovado'
elif media >= 5:
    r = 'Recuperação'
else:
    r = 'Reprovado'

print(f'\nMédia: {media:.2f}')
print(f'Situação: {r}')