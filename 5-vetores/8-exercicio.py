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
maior_nota = max(vetor_notas)
menor_nota = min(vetor_notas)

if media >= 7:
    r = 'Aprovado'
elif media >= 5:
    r = 'Recuperação'
else:
    r = 'Reprovado'

print('\n= EXIBINDO A MÉDIA DAS NOTAS DO VETOR =')
print(f'Média: {media:.2f}')
print(f'Situação: {r}')

print('\n= EXIBINDO A MENOR E MAIOR NOTAS DO VETOR =')
print(f'Maior nota: {maior_nota}')
print(f'Menor nota: {menor_nota}')