import os
os.system('cls')

# ENTRADA.
nome = input('Digite o nome do aluno: ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

# PROCESSAMENTO.
media = (nota1 + nota2) / 2
print(f'Nota final: {media:.1f}')
if media >= 9:
    print('A - Aprovado.')
elif media >= 7.5:
    print('B - Aprovado.')
elif media >= 6:
    print('C - Aprovado.')
elif media >= 4:
    print('D - Reprovado.')
else:
    print('E - Reprovado.')