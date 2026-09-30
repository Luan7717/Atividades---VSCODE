import os
import time
os.system('cls')

tentativas = 0

while True:
    tentativas += 1
    print(f'Tentativa {tentativas}/3')
    login = input('Digite o seu usuario de login: ')
    senha = input('Digite sua senha: ')

    if login == 'luan' and senha == '2531':
        print('Bem vindo!')
        break
    else:
        print('\nUsuario ou senha inválidos, tente novamente!')
        input('Pressione qualquer tecla para continuar...')
        os.system('cls')

        if tentativas == 3:
            print('Você atingiu o maximo de tentativas, tente novamente mais tarde.')
            tentativas = 0
            print('=== FIM ===')
            break