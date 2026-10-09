import os
import time
os.system('cls')

soma = 0
contador = 0

while True:
    print('S - Inserir uma nota')
    print('N - Calcular média aritmética')
    resposta = input('Digite a opção desejada: ').upper()
    if resposta == 'S':
        nota = float(input('\nDigite a nota do aluno: '))
        print('Nota registrada!')
        time.sleep(3)
        os.system('cls')
    else:
        resposta == 'N'
        os.system('cls')
        break

soma += nota
contador += 1
media = soma / contador
print(f'Média: {media:.2f}')