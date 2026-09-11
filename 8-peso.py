import os
os.system('cls')

sexo = input('Digite seu sexo (M ou F): ').upper()
altura = float(input('Digite sua altura: '))

match sexo:
    case 'M':
        print(f'\nSexo: {sexo}')
        print(f'Altura: {altura:.2f}')
        print(f'Peso ideal: {(72.7 * altura) - 58:.3f}')
    case 'F':
        print(f'\nSexo: {sexo}')
        print(f'Altura: {altura:.2f}')
        print(f'Peso ideal: {(62.1 * altura) - 44.7:.3f}')
    case _:
        print('Sexo inválido.')