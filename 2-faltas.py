import os
os.system('cls')

# ENTRADA.
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
faltas = int(input('Digite o numero de faltas: '))
# PROCESSAMENTO.
media = (n1 + n2) / 2

# SAÍDA.
print(f'\nMédia do aluno: {media}')
print(f'Faltas do aluno: {faltas}')
if media >= 7 and faltas <= 40:
    print('Aluno aprovado!')
else:
    print('Aluno reprovado!')