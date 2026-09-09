import os
os.system('cls')

dia = int(input('Digite o número do dia da semana: '))

match dia:
    case 1:
        print('Hoje é final de semana')
    case 2:
        print('Hoje é dia útil')
    case 3:
        print('Hoje é dia útil')
    case 4:
        print('Hoje é dia útil')
    case 5:
        print('Hoje é dia útil')
    case 6:
        print('Hoje é dia útil')
    case 7:
        print('Hoje é fim de semana.')
    case _:
        print('Dia inválido')