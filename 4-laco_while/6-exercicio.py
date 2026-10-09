import os
import time
os.system('cls')

while True:
    print('     === MENU ===')
    print('\n1 - Macarrão = R$29,99')
    print('2 - Frango assado = R$19,99')
    print('3 - Strogonoff = R$24,99')
    print('4 - Picanha = R$39,99')
    print('5 - Rodizio = R$59,99')
    prato = int(input('\nDigite o número do prato que deseja: '))
    if prato == 1:
        comida = 'Macarrão'
        valor = 'R$29,99'
        break
    elif prato == 2:
        comida = 'Frango assado'
        valor = 'R$19,99'
        break
    elif prato == 3:
        comida = 'Strogonoff'
        valor = 'R$24,99'
        break
    elif prato == 4:
        comida = 'Picanha'
        valor = 'R$39,99'
        break
    elif prato == 5:
        comida = 'Rodizio'
        valor = 'R$59,99'
        break
    else:
        os.system('cls')
        print('O prato escolhido é inválido, tente novamente.')
        time.sleep(4)
        os.system('cls')

print(f'\nOpção escolhida: {comida}')
print(f'Total a pagar: {valor}')