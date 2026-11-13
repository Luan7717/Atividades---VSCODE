import os
os.system('cls')

def par_impar():
    if numero % 2 == 1:
        resultado = 'O número é impar'
    else:
        resultado = 'O número é par'
    return resultado

numero = int(input('Digite um número: '))

impar_par = par_impar()
print(f'{impar_par}')
