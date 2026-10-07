import os
os.system('cls')

soma = 0
contador = 0

while True:
    nota = float(input('Digite a nota do aluno: '))
    soma += nota
    contador += 1
    adicionar = input('Deseja inserir mais uma nota?: ').upper()
    if adicionar == 'N':
        break

media = soma / contador
print(f'Média: {media:.2f}')