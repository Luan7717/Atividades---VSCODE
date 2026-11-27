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

print('= Solicitando Dados - Fornecedores=')
for i in range(QUANTIDADE_FORNECEDOR):
    novo_fonecedor = Fornecedor(
        nome = input('Digite o nome: '),
        email = input('Digite o email: '),
        telefone = input('Digite o telefone: '),
        endereco = input('Digite o endereço: ')
    )
    lista_fornecedores.append(novo_fonecedor)
    print(f'Fornecedor cadastrado com sucesso!')
    input('Toque "Enter" para continuar...')
    os.system('cls')

arquivo = 'dados_fornecedores.csv'
with open(arquivo, 'a') as arquivo_de_fornecedores:
    for fornecedor in lista_fornecedores:
        arquivo_de_fornecedores.write(f'{fornecedor.nome}, {fornecedor.email}, {fornecedor.telefone}, {fornecedor.endereco}\n')
    print('Fornecedor salvo com sucesso!')