import os
import time
os.system('cls')

tentativas = 0

print('        === CADASTRO ===')
cadastro_login = input('Digite o login para cadastro: ')
cadastro_senha = input('Digite o senha para cadastro: ')
print('Cadastro realizado!')
time.sleep(4)
os.system('cls')

while True:
    tentativas += 1
    print(f'Tentativa: {tentativas}/3')
    login = input('Digite o login: ')
    senha = input('Digite a senha: ')
    if login == cadastro_login and senha == cadastro_senha:
        print('Bem vindo!')
        break
    else:
        print('Login ou senha inválidos, tente novamente!')
        time.sleep(3)
        os.system('cls')
        if tentativas == 3:
            os.system('cls')
            print('Você atingiu o limite de tentativas, tente novamente mais tarde!')
            print('=== FIM ===')
            break