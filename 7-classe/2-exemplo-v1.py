from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class Cliente:
    nome : str
    idade : int
    altura : float
    peso : float
    telefone : str
    email : str
    cpf : int

lista_clientes = []

# SOLICITANDO DADOS DO CLIENTE.
for i in range(2):
    dados_do_cliente = Cliente(
        nome = input('Digite seu nome: '),
        idade = int(input('Digite sua idade: ')),
        altura = float(input('Digite sua altura: ')),
        peso = float(input('Digite seu peso: ')),
        telefone = input('Digite seu telefone: '),
        email = input('Digite seu email: '),
        cpf = int(input('Digite seu CPF: '))
    )
    print('Cliente cadastrado com sucesso!')
    input('Toque para continuar')
    lista_clientes.append(dados_do_cliente)
    os.system('cls')

# EXIBINDO DADOS.
print('\n= EXIBINDO DADOS =')
for cliente in lista_clientes:
    print(f'Nome: {cliente.nome}')
    print(f'Idade: {cliente.idade}')
    print(f'Altura: {cliente.altura:.2f}')
    print(f'Peso: {cliente.peso:.3f}')
    print(f'Telefone: {cliente.telefone}')
    print(f'E-mail: {cliente.email}')
    print(f'CPF: {cliente.cpf}')
    print('bahia')
    print(f'=' * 15)