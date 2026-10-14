import os
os.system('cls')

print('= INSERINDO NOTAS =')
vetor_notas = []
soma = 0

for i in range(3):
    nota = float(input(f'Digite a {i+1}° nota: '))
    vetor_notas.append(nota)
os.system('cls')

print('\n= EXIBINDO NOTAS =')
for lugar, nota in enumerate (vetor_notas, start=1):
    print(f'{lugar}° Nota do aluno: {nota}')
    soma += nota

media = soma / 3
print(f'\nMédia: {media:.2f}')