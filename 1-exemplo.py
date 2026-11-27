from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class Clientes:
    nome : str
    idade : int
    altura : float

QUANTIDADE_CLIENTES = 2

# Ladrão

lista_clientes = []

for i in range(QUANTIDADE_CLIENTES):
    novo_cliente = Clientes(
        nome = input('Digite seu nome: '),
        idade = int(input('Digite sua idade: ')),
        altura = float(input('Digite sua altura: '))
    )
    lista_clientes.append(novo_cliente)
    print(f'Cliente cadastrado com sucesso!')
    input('Toque "Enter" para continuar')
    os.system('cls')

# Salvando em um arquivo.
arquivo = 'dados_clientes.csv'
with open(arquivo, 'a') as arquivo_de_clientes:
    for cliente in lista_clientes:
        arquivo_de_clientes.write(f'{cliente.nome}, {cliente.idade}, {cliente.altura}\n')

print('Cliente salvo com sucesso!')