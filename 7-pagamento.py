import os
os.system('cls')

valor = float(input('Digite o valor do produto: R$'))
print('\n1 - Pagamento à vista.')
print('2 - Pagamento à prazo.')
pagamento = int(input('Digite o número da forma de pagamento: '))

valor_desconto = valor * 10 / 100
desconto = valor - (valor * 10) / 100

match pagamento:
    case 1:
        forma_pagamento = 'À vista'
        preço = desconto
        print('Valor do produto: ',valor)
        print('Forma de Pagamento: ', forma_pagamento)
        print('Valor do desconto: ', valor_desconto)
        print('Valor final: ', preço)
    case 2:
        forma_pagamento = 'À prazo'
        preço = valor
        parcela = int(input('Digite a quantidade de parcelas que deseja: '))
        print('Valor do produto: ',valor)
        print('Forma de Pagamento: ', forma_pagamento)
        print('Quantidade de parcelas: ', parcela)
        print('Valor final: ', preço / parcela)
    case _:
        forma_pagamento = 'Inválido'
        preço = 0
