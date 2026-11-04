import os
os.system('cls')

lista_jogares = []
contador = 0

while True:
    os.system('cls')
    print('''
=== CADASTRO DE JOGADORES ===
1 - Cadastrar jogador
2 - Listar jogadores
3 - Atualizar jogador
4 - Excluir jogador
0 - Sair''')

    opcao = int(input('Digite uma opção: '))

    match opcao:
        case 1:
            contador += 1
            nome_jogador = input('Digite o nome do jogador: ').strip()
            sobrenome_jogador = input('Digite o sobrenome do jogador: ').strip()
            posicao = input('Digite a posição do jogador: ').strip()
            numero_camisa = int(input('Digite o número da camisa do jogador: '))
            if nome_jogador == '' or sobrenome_jogador == '' or posicao == '' or numero_camisa == '':
                print('Nenhuma das informações podem ser em branco!')
                input('Toque em uma tecla para continuar...')
            else:
                lista_jogares.append((nome_jogador, sobrenome_jogador, posicao, numero_camisa))
                print(f'\nNome: {nome_jogador}')
                print(f'Sobrenome: {sobrenome_jogador}')
                print(f'Posição: {posicao}')
                print(f'Número da camisa: {numero_camisa}')
                input('Toque em uma tecla para continuar...')
        case 2:
            print('\n=== JOGADORES CADASTRADOS ===')
            if len(lista_jogares) == 0:
                print('Não há jogadores cadastrados.')
                input('Toque em uma tecla para continuar...')
            else:
                for contador, (nome_jogador, sobrenome_jogador, posicao, numero_camisa) in enumerate (lista_jogares, start=1):
                    print(f'{contador} - {nome_jogador} {sobrenome_jogador} / {posicao} / Camisa: {numero_camisa}')
                print(f'Quantidade de jogadores cadastrados: {len(lista_jogares)}')
                input('Toque em uma tecla para continuar...')
        case 3:
            print('\n=== ATUALIZAR JOGADOR ===')
            if len(lista_jogares) == 0:
                print('Não há jogadores cadastrados.')
                input('Toque em uma tecla para continuar...')
            else:
                for contador, (nome_jogador, sobrenome_jogador, posicao, numero_camisa) in enumerate (lista_jogares, start=1):
                    print(f'{contador} - {nome_jogador} {sobrenome_jogador} / {posicao} / Camisa: {numero_camisa}')
                numero = int(input('\nDigite o número do paciente que deseja atualizar: '))
                if numero >= 1 and numero <= len(lista_jogares):
                    novo_nome = input('\nNovo nome: ')
                    novo_sobrenome = input('Novo sobrenome: ')
                    nova_posicao = input('Nova posição: ')
                    novo_numero = int(input('Novo número da camisa: '))
                    lista_jogares[numero - 1] = (novo_nome, novo_sobrenome, nova_posicao, novo_numero)
                    print('Dados do jogador atualizados!')
                    input('Toque em uma tecla para continuar...')
                else:
                    print('Jogador não encontrado!')
                    input('Toque em uma tecla para continuar...')
        case 4:
            print('\n=== REMOVER JOGADOR ===')
            for contador, (nome_jogador, sobrenome_jogador, posicao, numero_camisa) in enumerate (lista_jogares, start=1):
                print(f'{contador} - {nome_jogador} {sobrenome_jogador} / {posicao} / Camisa: {numero_camisa}')
            numero = int(input('\nDigite o número do jogador que deseja remover: '))
            if numero >= 1 and numero <= len(lista_jogares):
                lista_jogares.pop(numero - 1)
                print('Jogador removido com sucesso!')
            else:
                print('Jogador não encontrado!')
                input('Toque em uma tecla para continuar...')
        case 0:
            print('Programa finalizado!')
            break