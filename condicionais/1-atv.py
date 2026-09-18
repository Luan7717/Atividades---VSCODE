import os
os.system('cls')

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceriro número: '))

resultado = a + b

match resultado:
    case x if resultado < c:
        print('A + B é menor que C')
    case x if resultado > c:
        print('A + B é maior que C')
    case x if resultado == c:
        print('A + B é igual a C')