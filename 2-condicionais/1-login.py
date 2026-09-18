import os
os.system('cls')

# ENTRADA.
login = input('Digite o login: ')
senha = input('Digite a senha: ')

# PROCESSAMENTO.
login_cadastrado = "senai"
senha_cadastrada = "1234"

# SAÍDA.
if login == login_cadastrado and senha == senha_cadastrada:
    print('Bem-vindo!')
else:
    print('Login ou senha inválidos.')