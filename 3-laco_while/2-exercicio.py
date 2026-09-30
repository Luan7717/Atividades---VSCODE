import os
os.system('cls')

while True:
    nota = float(input('Digite a nota do aluno: '))
    if nota < 0 or nota > 10:
        print('\nNota inválida.')
    else:
        print('\nA nota está entre 0 e 10.')
        print(f'A nota é {nota}')
        break

print('= FIM =')