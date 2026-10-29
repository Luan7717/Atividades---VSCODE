import os
import time
os.system('cls')

lista_series = []

while True:
    print('''
=== NETFLIX DENDEZEIROS ===
1 - Cadastrar series
2 - Listar series
0 - Sair''')
    opcao = int(input('Escolha uma opção: '))
    match opcao:
        case 1:
            print('\n== CADASTRAR UMA SERIE ==')
            nome_series = input('Nome da serie: ').strip().upper()
            if nome_series == '':
                print('O nome não pode ficar vazio.')
            elif nome_series in lista_series:
                print(f'{nome_series} já está cadastrada.')
            else:
                lista_series.append(nome_series)
                print('Serie cadastrada com sucesso!')
                time.sleep(2)
                os.system('cls')

        case 2:
            print('\n== LISTANDO TODOS OS PRODUTOS ==')
            if len(lista_series) == 0:
                print('Nenhuma serie cadastrada.')
            else:
                for i, series in enumerate(lista_series):
                    print(f'{i+1}. {series}')
                # len(lista_produtos) mostra a quantidade de produtos na lista.
                print(f'Total de series: {len(lista_series)}')
            input('Pressione uma tecla para continuar...')
            os.system('cls')

        case 0:
            print('\nFim do programa.')
            break

        case _:
            print('Opção inválida')
            input('Pressione uma tecla para continuar...')