import os
os.system('cls')

lista_produto = []
lista_valores = []

def taxa_produto(valor):
    if valor < 100:
        resultado = valor * 1.10
    else:
        resultado = valor * 1.20
    return resultado

def menu_estoque():
    print('''
===== ESTOQUE =====
1 - Caixa de ferramentas - R$90.99
2 - Parafuzadeira - R$139.90
3 - Cimento - R$80.90
4 - Monitor - R$499.90
5 - Gabinete - R$389.59
''')


while True:
    menu_estoque()
    opcao = int(input('\nDigite a opção que deseja comprar: '))
    match opcao:
        case 1 | 2 | 3 | 4 | 5:
            produto = ['Caixa de ferramentas', 'Parafuzadeira', 'Cimento', 'Monitor', 'Gabinete']
            valor = [90.99, 139.90, 80.90, 499.90, 389.59]
            lista_produto.append(produto[opcao - 1])
            lista_valores.append(valor[opcao - 1])
            print('\nPedido feito com sucesso!')
            input('Toque em uma tecla para continuar...')
            break
        case _:
            print('\nProduto não encontrado\nTente novamente')
            input('Toque em uma tecla para continuar...')
            os.system('cls')

taxa = taxa_produto(lista_valores[-1])

print(f'\nProduto: {lista_produto[-1]}')
print(f'Valor: {lista_valores[-1]}')
print(f'Valor inflacionado: {taxa:.2f}')