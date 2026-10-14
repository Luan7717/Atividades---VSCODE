import os
os.system('cls')

print('= INSERINDO NOTAS =')
vetor_notas = []

for i in range(3):
    nota = float(input(f'Digite a {i+1}º nota: '))
    vetor_notas.append(nota)
os.system('cls')

print('\n= EXIBINDO NOTAS =')
for lugar, nota in enumerate (vetor_notas, start=1):
    print(f'{lugar}º Nota do aluno: {nota}')

media = sum(vetor_notas) / 3
print(f'Média: {media:.2f}')