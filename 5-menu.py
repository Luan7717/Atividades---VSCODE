import os
os.system('cls')

print('===MENU===')
print('1 - Picanha - R$25.00')
print('2 - Lasanha - R$20.00')
print('3 - Strogonoff - R$18.00')
print('4 - Bife Acebolado - R$15.00')
print('5 - Pão com ovo - R$5.00')

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

print('\nPrato escolhido: ',nome)
print('Valor: R$',valor)