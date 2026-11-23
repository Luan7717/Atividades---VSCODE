from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class Cliente:
    # Nome da variável : tipo da variável
    nome: str
    idade: int
    altura: float
    peso: float

lista_clientes = []

# SOLICITANDO DADOS DE DOIS CLIENTES.
for i in range(2):
    dados_do_cliente = Cliente(
        nome = input('Digite seu nome: '),
        idade = int(input('Digite sua idade: ')),
        altura = float(input('Digite sua altura: ')),
        peso = float(input('Digite seu peso: '))
    )
    print('Cliente cadastrado com sucesso!')
    input('Toque para continuar...')
    lista_clientes.append(dados_do_cliente)
    os.system('cls')

print('\n= EXIBINDO DADOS =')
for cliente in lista_clientes:
    print(f'Nome: {cliente.nome}')
    print(f'Idade: {cliente.idade}')
    print(f'Altura: {cliente.altura:.2f}')
    print(f'Peso: {cliente.peso:.3f}')
    print(f'=' * 10)