import os
from datetime import date
os.system('cls')

def idade_atual(ano_nascimento):
    ano_atual = date.today().year
    idade_atual = 2026 - ano_nascimento
    return idade_atual

ano_nascimento = int(input('\nDigite o ano do seu nascimento: '))
idade = idade_atual(ano_nascimento)

print(f'Ano de nascimento: {ano_nascimento}')
print(f'Idade: {idade}')