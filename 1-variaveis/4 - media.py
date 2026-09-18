import os

# Limpa o terminal.
os.system('cls')

print('= SOLICITANDO DAODS =')
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
primeira_nota = float(input('Digite a primeira nota: '))
segunda_nota = float(input('Digite a segunda nota: '))

media = (primeira_nota + segunda_nota) / 2

print('\n= EXIBINDO DAODS =')
print('Nome: ', nome)
print('Idade: ', idade)
print('Primeira nota: ', primeira_nota)
print('Segunda nota: ', segunda_nota)
print('Medía: ', media)
