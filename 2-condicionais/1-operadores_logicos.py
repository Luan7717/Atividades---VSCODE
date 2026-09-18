import os
from datetime import date
os.system('cls')

# ENTRADA.
codigo = int(input('Digite seu codigo de matricula: '))
ano_de_nascimento = int(input('Digite seu ano de nascimento: '))
tempo_trabalho = int(input('Digite o tempo de trabalho em anos: '))

idade = date.today().year - ano_de_nascimento

# PROCESSAMENTO.
if idade >= 65 or tempo_trabalho >= 30:
    msg = 'Requerer aposentadoria.'
else:
    msg = 'Não requerer aposentadoria.'

# SAÍDA
print('\nCódigo: ', codigo)
print('Idade: ', idade)
print('Tempo de trabalho: ', tempo_trabalho)
print(msg)
print(f'Data: {date.today()}')