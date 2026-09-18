import os
os.system('cls')

# ENTRADA.
nota = int(input('Digite sua nota: '))

# PROCESSAMENTO.
if nota >= 0 and nota <= 10:
    print(f'Sua nota é: {nota}')
else:
    print('A nota deve ser entre 0 e 10!')