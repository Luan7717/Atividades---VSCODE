import os
os.system('cls')

# Função sem retorno e com parâmetros
def logo_senai():
    print('===========')
    print('   SENAI')
    print('===========')

# Função sem retorno e com parâmetros
def mostar_dados(nome, idade):
    print(f'{nome} tem {idade} anos')

print(f'\n= SOLICITANDO DADOS =')
# Função sem retorno e com parâmetros
logo_senai()
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

logo_senai()
print(f'\n= EXIBINDO DADOS =')
# Função sem retorno e com parâmetros
mostar_dados(nome, idade)