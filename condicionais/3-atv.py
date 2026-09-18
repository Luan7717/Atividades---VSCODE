import os
os.system('cls')

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))

match a == b:
    case True:
        c = a + b
    case False:
        c = a * b

print('C =',c)