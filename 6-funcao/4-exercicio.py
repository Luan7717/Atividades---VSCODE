import os
os.system('cls')

def mostar_dados(nome, telefone, email):
    print(f'''
Nome: {nome}
Telefone: {telefone}
Email: {email}''')

def logo_senai():
    os.system('cls')
    print('\n')
    print('='*15)
    print('SENAI - VITORIA')
    print('='*15)

while True:
    os.system('cls')
    print('''
  === CADASTRO ===
1 - Cadastrar pessoa
2 - Listar pessoa
3 - Sair''')

    opcao = int(input('Digite a opção que deseja: '))

    match opcao:
        case 1:
            logo_senai()
            nome = input('Digite seu nome: ')
            print('Nome cadastrado com sucesso!')
            input('Toque em uma tecla para continuar...')
            logo_senai()
            telefone = input('Digite seu telefone: ')
            print('Telefone cadastrado com sucesso!')
            input('Toque em uma tecla para continuar...')
            logo_senai()
            email = input('Digite seu email: ')
            print('Emai cadastrado com sucesso!')
            print('\nCadastro concluido!')
            input('Toque em uma tecla para continuar...')
        case 2:
            print(f'\n= Exibindo Dados =')
            mostar_dados(nome, telefone, email)
            input('Toque em uma tecla para continuar...')
        case 3:
            print('\nFim do programa')
            break
        case _:
            print('Opção inválida.')
            input('Toque em uma tecla para continuar...')