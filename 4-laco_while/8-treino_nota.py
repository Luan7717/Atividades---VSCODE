import os
import time
os.system('cls')

soma = 0

for i in range(2):
    while True:
        nota = float(input(f'Digite a {i+1} nota do aluno (0 a 10): '))
        if nota < 0 or nota > 10:
            print('Nota inválida, tente novamente')
            time.sleep(4)
            os.system('cls')
        else:
            soma += nota
            break
media = soma / 2
print(f'\nA nota do aluno é: {media}')
print(f'= FIM =')