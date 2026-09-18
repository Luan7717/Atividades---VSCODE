import os
os.system('cls')

nome = input('Digite seu nome: ')
sexo = input('Informe seu sexo (M ou F): ').upper()
ec = input('Informe seu estado civil: ').lower()

match sexo:
    case 'F':
        match ec:
            case 'casada':
                anos = int(input('Quantos anos de casamento?: '))
        print(f'\nNome: {nome}')
        print(f'Sexo: {sexo}')
        print(f'Estado civil: {ec}')
match sexo:
     case 'F':
        match ec:
            case 'casada':
                print(f'Tempo de casada: {anos}')