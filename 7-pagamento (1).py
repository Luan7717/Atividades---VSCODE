import os
os.system('cls')

valor = float(input('Digite o valor do produto: R$'))
print('\n1 - Pagamento à vista.')
print('2 - Pagamento à prazo.')
pagamento = int(input('Digite o número da forma de pagamento: '))

valor_desconto = valor * 0.10
desconto = valor - valor_desconto

match pagamento:
    case 1:
        forma_pagamento = 'À vista'
        preço = desconto
        print(f'\nValor do produto: R${valor:.2f}')
        print(f'Forma de Pagamento: {forma_pagamento}')
        print(f'Valor do desconto: R${valor_desconto:.2f}')
        print(f'Total a pagar: R${preço:.2f}')
    case 2:
        forma_pagamento = 'À prazo'
        preço = valor
        parcela = int(input('Digite a quantidade de parcelas que deseja: '))
        if parcela > 6:
            print('Quantidade de parcelas inválida.')
            exit()
        print(f'\nValor do produto: R${valor:.2f}')
        print(f'Forma de Pagamento: {forma_pagamento}')
        print(f'Quantidade de parcelas: {parcela}')
        print(f'Valor das parcelas: R${preço / parcela:.2f}')
        print(f'Valor final: R${preço:.2f}')
    case _:
        print(f'\nForma de Pagamento: Inválido')