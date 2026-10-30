import os

lista_produtos = []

while True:
    os.system('cls')
    print('''
=== MERCADO SENAI ===
1 - Cadastrar produto
2 - Listar todos os produtos
3 - Atualizar produto
4 - Remover produto
5 - Buscar produto
6 - Sair''')

    opcao = int(input('Escolha uma opção: '))

    match opcao:
        case 1:
            print('\n== CADASTRAR PRODUTO ==')
            nome_produto = input('Digite o nome do novo produto: ')
            if nome_produto in lista_produtos:
                print('Produto ja cadastrado.')
            else:
                lista_produtos.append(nome_produto)
                print('Produto cadastrado com sucesso!')
        case 2:
            print('\n== PRODUTOS NO ESTOQUE ==')
            for produto in lista_produtos:
                print(f'- {produto}')
            print(f'Total: {len(lista_produtos)}')
        case 3:
            print('\n== ATUALIZAR PRODUTO ==')
            nome = input('Qual produto deseja atualizar?: ')
            if nome in lista_produtos:
                posicao = lista_produtos.index(nome)
                novo = input('Novo nome: ')
                lista_produtos[posicao] = novo
                print('Produto alterado com sucesso!')
            else:
                print('Produto não encontrado.')
        case 4:
            print('\n== REMOVER PRODUTO ==')
            nome = input('Qual produto deseja remover?: ')
            if nome in lista_produtos:
                lista_produtos.remove(nome)
                print('Produto excluido com sucesso!')
            else:
                print('Produto não encontrado.')
        case 5:
            print('== ENCONTRAR PRODUTO ==')
            nome = input('Qual produto deseja buscar?: ')
            if nome in lista_produtos:
                print('Produto encontrado!')
            else:
                print('Este produto não está no estoque.')
        case 0:
            print('Saido do programa...')
            break
        case _:
            print('Opção inválida! \nTente novamente...')
    input('Pressione uma tecla para continuar...')