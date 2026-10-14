import os
os.system('cls')

print('= REGISTRANDO LIVROS =')
vetor_nomes = []

for i in range(5):
    nome_livro = input(f'Digite o nome do {i+1}° livro: ')
    vetor_nomes.append(nome_livro)
os.system('cls')

print('\n= EXIBINDO LIVROS =')
for lugar, nome in enumerate (vetor_nomes, start=1):
    print(f'Nome do {lugar}° livro: {nome}')