import os

lista_pratos = []
lista_valores = []
contador = 0
valor_total = 0
cardapio_exibido = False
contar = False


while True:
    os.system('cls')
    print(''' === BOM PRATO ===
1 - Exibir cardapio
2 - Listar pratos
3 - Adicionar prato
4 - Remover prato
5 - Total da conta
0 - Sair
''')
    
    opcao = int(input('Digite a opção que deseja: '))

    match opcao:
        case 1:
            if cardapio_exibido == False:
                print('''=== MENU ===
1 - Picanha - R$25.00
2 - Lasanha - R$20.00
3 - Strogonoff - R$18.00
4 - Bife Acebolado - R$15.00
5 - Pão com ovo - R$5.00''')
                
                prato = int(input('Escolha o prato que deseja: '))

                match prato:
                   case 1 | 2 | 3 | 4 | 5:
                        comida = ['Picanha', 'Lasanha', 'Strogonoff', 'Bife Acebolado', 'Pão com ovo']
                        valor = [25.00, 20.00, 18.00, 15.00, 5.00]
                        comida = comida [prato - 1]
                        valor = valor [prato - 1]

                if prato == '':
                    print('O espaço não pode ser vazio.')
                    continue
                elif prato >= 6 or prato <= 0:
                    print(f'{prato} não é um número valido, escolha um número referente a um prato selecionavel!')
                else:
                    lista_pratos.append(comida)
                    lista_valores.append(valor)
                    contador += 1
                    valor_total += valor
                    print(f'\nPrato adicionado ao pedido!')
                    for pratos in lista_pratos:
                        print(f'- {pratos} - R${valor:.2f}')
                        print(f'Total de pratos: {len(lista_pratos)}')
                        input('Toque em uma tecla para continuar...')
                    cardapio_exibido = True
            else:
                print('Você ja exibiu o menu uma vez.')
                print('Para adicionar um novo prato, vá para a opção 3.')
                input('Toque em uma tecla para continuar...')
            
        case 2:
            print('\n=== PRATOS NO PEDIDO ATUAL ===')
            if len(lista_pratos) == 0:
                print('Não há pratos no pedido.')
                input('Toque para continuar...')
            else:
                for contador, (pratos, valores) in enumerate(zip(lista_pratos, lista_valores), start=1):
                    print(f'{contador} - {pratos} - R${valores:.2f}')
                print(f'Total de pratos: {len(lista_pratos)}')
                input('Toque em uma tecla para continuar...')
        case 3:
            print(f'\n=== ADICIONAR PRATO(S) AO PEDIDO ===')
            print('''
1 - Picanha - R$25.00
2 - Lasanha - R$20.00
3 - Strogonoff - R$18.00
4 - Bife Acebolado - R$15.00
5 - Pão com ovo - R$5.00''')
            while True:
                prato = int(input('Escolha o prato que deseja: '))
                if prato <= 0 or prato >= 6:
                    print(f'Prato "{prato}" não é valido, digite um codigo de prato valido')
                    input('Toque em uma tecla para continuar...')
                    continue
                else:
                    break
            while True:
                quantidade = int(input('Quantas unidades do prato você deseja?: '))
                if quantidade < 0:
                    print(f'A quantidade "{quantidade}" é inválida, selecione uma quantidade valida para continuar')
                    input('Toque em uma tecla para continuar...')
                    continue
                else:
                    break
            match prato:
                case 1 | 2 | 3 | 4 | 5:
                    comida = ['Picanha', 'Lasanha', 'Strogonoff', 'Bife Acebolado', 'Pão com ovo']
                    valor = [25.00, 20.00, 18.00, 15.00, 5.00]
                    comida = comida [prato - 1]
                    valor = valor [prato - 1]
                case _:
                    print('Prato inválido.')
            if prato <= 0 or prato >= 6:
                print(f'Prato "{prato}" não é valido, digite um codigo de prato valido')
            if quantidade > 0:
                for i in range(quantidade):
                    lista_pratos.append(comida)
                    lista_valores.append(valor)

                contador += quantidade
                valor_total += valor * quantidade
                if quantidade > 1:
                    print('Pratos adicionados ao pedido.')
                    input('Toque em uma tecla para continuar...')
                else:
                    print('Prato adicionado ao pedido.')
                    input('Toque em uma tecla para continuar...')
        case 4:
            print('\n=== REMOVER PRATO ===')
            if len(lista_pratos) == 0:
                print('Não há pratos para remover.')
                input('Toque em uma tecla para continuar...')
                continue
            for contador, (pratos, valores) in enumerate(zip(lista_pratos, lista_valores), start=1):
                print(f'{contador} - {pratos} - R${valores:.2f}')
            posicao = int(input('Digite o número do prato que deseja remover: '))
            if posicao < 1 or posicao > len(lista_pratos):
                print('Posição inválida.')
            else:
                indice = posicao - 1
                comida_removida = lista_pratos.pop(indice)
                valor_removido = lista_valores.pop(indice)
                contador -= 1
                valor_total -= valor_removido
                print(f'{comida_removida} removido do pedido.')
                print(f'Valor removido: R${valor_removido:.2f}')
                input('Toque em uma tecla para continuar...')
        case 5:
            print('\n=== TOTAL DO PEDIDO ===')
            if len(lista_pratos) == 0:
                print('Não há pratos no pedido.')
            else:
                for contador, (pratos, valores) in enumerate(zip(lista_pratos, lista_valores), start=1):
                    print(f'{contador} - {pratos} - R${valores:.2f}')
                print(f'Quantidade de pratos: {contador}')
                print(f'Valor total a pagar: R${valor_total:.2f}')
                input('Toque em uma tecla para continuar...')