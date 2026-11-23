from dataclasses import dataclass
from tqdm import tqdm
import time
import os
os.system('cls')

@dataclass
class Cliente:
    nome : str
    idade : int
    altura : float
    peso : float
# BALA
    telefone : str
    email : str
    cpf : int
    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Altura: {self.altura:.2f}')
        print(f'Peso: {self.peso:.3f}')
        print(f'Telefone: {self.telefone}')
        print(f'E-mail: {self.email}')
        print(f'CPF: {self.cpf}')
        print(f'=' * 30)
    # Função somente para enviar e-mails.
    def email_marketing(self):
        print(f'Nome: {self.nome}')
        print(f'E-mail: {self.email}')
        print(f'=' * 30)
    # Função somente para enviar mensagens via WhatsApp.
    def whatsapp_marketing(self):
        print(f'Nome: {self.nome}')
        print(f'Telefone: {self.telefone}')
        print(f'=' * 30)

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
    for i in tqdm(range(100), desc= 'Cadastrando dados...'):
        time.sleep(0.02)
    print('\nCliente cadastrado com sucesso!')
    input('Toque para continuar')
    lista_clientes.append(dados_do_cliente)
    os.system('cls')

# EXIBINDO DADOS.
print('\n= EXIBINDO DADOS =')
for cliente in lista_clientes:
    cliente.mostrar_dados()

print('\n= EXIBINDO E-MAIL MARKETING =')
for cliente in lista_clientes:
    cliente.email_marketing()

print('\n= EXIBINDO WHATSAPP MARKETING =')
for cliente in lista_clientes:
    cliente.whatsapp_marketing()
