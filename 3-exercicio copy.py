from dataclasses import dataclass
import os
os.system('cls')

class Cliente:
    nome: str
    email: str
    telefone: str

def mostar_dados(nome, telefone, email):
    print(f'''
Nome: {nome}
Telefone: {telefone}
Email: {email}''')

def logo_senai():
    os.system('cls')
    print('\n')
    print('='*15)
    print('     SENAI - VITORIA')
    print('='*15)

logo_senai()
nome = input('Digite seu nome: ')

logo_senai()
telefone = input('Digite seu telefone: ')

logo_senai()
email = input('Digite seu email: ')

print(f'\n= Exibindo Dados =')
mostar_dados(nome, telefone, email)