import os
os.system('cls')

# SOLICITANDO DADOS.
primeira_nota = float(input('Digite a primeira nota: '))
segunda_nota = float(input('Digite a segunda nota: '))
terceira_nota = float(input('Digite a terceira nota: '))

# CALCULANDO.
media = (primeira_nota + segunda_nota + terceira_nota) / 3

# SAÍDA
print('\n= EXIBINDO RESULTADO =')
print(f'Média do aluno: {media:.2f}')

# VERIFICANDO SITUAÇÃO DO ALUNO.
if media < 7:
    print('Aluno está REPROVADO.')
else:
    print('Aluno está APROVADO.')