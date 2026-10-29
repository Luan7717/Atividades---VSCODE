import os
import time
os.system('cls')

lista_produtos = []

while True:
    print('''
=== MERCADO DENDEZEIROS ===
1 - Cadastrar produtos
2 - Listar produtos
0 - Sair''')
    opcao = int(input('Escolha uma opção: '))
    match opcao:
        case 1:
            print('\n== CADASTRAR UM PRODUTO ==')
            nome = input('Nome do novo produto: ').strip().upper()
            if nome == '':
                print('O nome não pode ficar vazio.')
            elif nome in lista_produtos:
                print(f'{nome} já está cadastrado.')
            else:
                lista_produtos.append(nome)
                print('Produto cadastrado com sucesso!')
                time.sleep(2)
                os.system('cls')

        case 2:
            print('\n== LISTANDO TODOS OS PRODUTOS ==')
            if len(lista_produtos) == 0:
                print('O estoque está vazio.')
            else:
                for i, produto in enumerate(lista_produtos):
                    print(f'{i+1}. {produto}')
                # len(lista_produtos) mostra a quantidade de produtos na lista.
                print(f'Total de produtos: {len(lista_produtos)}')
            input('Pressione uma tecla para continuar...')
            os.system('cls')

        case 0:
            print('\nFim do programa.')
            break

        case _:
            print('Opção inválida')
            input('Pressione uma tecla para continuar...')