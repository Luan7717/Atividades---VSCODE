from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class Fornecedor:
    nome : str
    email : str
    telefone : str
    endereco : str

QUANTIDADE_FORNECEDOR = 3
lista_fornecedores = []

arquivo = 'dados_fornecedores.csv'
with open(arquivo, 'r') as arquivo_de_fornecedores:
    for linha in arquivo_de_fornecedores:
        nome, email, telefone, endereco = linha.strip().split(',')
        lista_fornecedores.append(Fornecedor(
            nome = nome,
            email = email,
            telefone = telefone,
            endereco = endereco
        ))

print('\nExibindo dados dos fornecedores: ')
for fornecedor in lista_fornecedores:
    print(f'Nome: {fornecedor.nome}')
    print(f'E-mail: {fornecedor.email}')
    print(f'Telefone: {fornecedor.telefone}')
    print(f'Endereço: {fornecedor.endereco}')
    print(f'================================')