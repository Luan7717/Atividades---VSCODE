import os
os.system('cls')

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
operador = input('Digite o operador (+, -, *, /): ')

match operador:
    case '+':
        resultado = n1 + n2
    case '-':
        resultado = n1 - n2
    case '*':
        resultado = n1 * n2
    case '/':
        resultado = n1 / n2
    case _:
        resultado = 'Operador inválido.'

print('\nNúmero 1: ', n1)
print('Numero 2: ', n2)
print('Operador: ', operador)
print('Resultado: ', resultado)