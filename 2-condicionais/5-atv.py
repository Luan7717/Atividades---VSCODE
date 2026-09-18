import os
os.system('cls')

a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
operacao = input('Digite sua operação (+, -, * ou /): ')

match operacao:
    case '+':
        print(f'{a} + {b} é igual a {a+b}')
    case '-':
        print(f'{a} - {b} é igual a {a-b}')
    case '*':
        print(f'{a} * {b} é igual a {a*b}')
    case '/':
        print(f'{a} / {b} é igual a {a/b}')