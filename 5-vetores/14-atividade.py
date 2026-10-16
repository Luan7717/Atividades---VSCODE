import os
import time
os.system('cls')

vetor_codigo = [0]
vetor_nome = []
valortotal = 0

print('===MENU===')
print('1 - Picanha - R$25.00')
print('2 - Lasanha - R$20.00')
print('3 - Strogonoff - R$18.00')
print('4 - Bife Acebolado - R$15.00')
print('5 - Pão com ovo - R$5.00')

print()
while True:
    codigo = int(input('Digite o código do prato: '))
    match codigo:
        case 1:
            nome = 'Picanha'
            valor = 25.00
        case 2:
            nome = 'Lasanha'
            valor = 20.00
        case 3:
            nome = 'Strogonoff'
            valor = 18.00
        case 4:
            nome = 'Bife Acebolado'
            valor = 15.00
        case 5:
            nome = 'Pão com ovo'
            valor = 5.00
        case _:
            nome = 'Prato inválido'
            valor = 0
    vetor_codigo.append(codigo)
    vetor_nome.append(nome)
    print(f'Prato escolhido: {nome}!')
    print(f'Valor do prato: R${valor:.2f}')
    print(f'Valor total: R${valor:.2f}')
    valortotal += valor
    adicionar = input('\nDeseja adicionar mais um prato? (S ou N): ').upper()
    if adicionar == 'N':
        os.system('cls')
        break

print('\n=== PEDIDO FINAL ===')
print('\nPrato escolhido:')
print()
for nome in vetor_nome:
    print(nome)
print(f'\nValor total: {valortotal}')