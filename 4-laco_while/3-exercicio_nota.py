import os
os.system('cls')

soma = 0
quantidade_notas = 2

for i in range(quantidade_notas):
    while True:
        nota = float(input(f'Digite a {i+1} nota entre 0 e 10: '))
        if nota >= 0 and nota <= 10:
            soma = soma + nota
            break
        else:
            print()
            print('Nota inválida, tente novamente!')

media = soma / quantidade_notas

print(f'Média: {media}')
print('= FIM =')