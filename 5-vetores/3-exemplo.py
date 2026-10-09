import os
os.system('cls')

vetor_nomes = []

for i in range(3):
    nome = input('Digite seu nome: ')
    vetor_nomes.append(nome)

for i in range(3):
    print(f'Nome: {vetor_nomes[i]}')