from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class Paciente:
    nome : str
    idade : int
    telefone : str
    endereco : str
# MOSTRANDO DADOS.
    def mostrar_dados(self):
        print(f'\nNome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Telefone: {self.telefone}')
        print(f'Endereço: {self.endereco}')
        print(f'=' * 20)
# NOME E IDADE.
    def nome_idade(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'=' * 20)
# NOME E TELEFONE.
    def nome_telefone(self):
        print(f'Nome: {self.nome}')
        print(f'Telefone: {self.telefone}')
        print(f'=' * 20)
dados_cliente = Paciente(
    nome = input('Digite seu nome: '),
    idade = int(input('Digite sua idade: ')),
    telefone = input('Digite seu telefone: '),
    endereco = input('Digite seu endereço: ')
)

print(f'\n= EXIBINDO DADOS =')
dados_cliente.mostrar_dados()
print(f'= NOME E IDADE')
dados_cliente.nome_idade()
print(f'NOME E TELEFONE')
dados_cliente.nome_telefone()