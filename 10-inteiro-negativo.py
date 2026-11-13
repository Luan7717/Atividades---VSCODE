import os
os.system('cls')

def positivo_negativo():
    if numero >= 1:
        resultado = 'positivo.'
    elif numero == 0:
        resultado = 'neutro'
    else:
        resultado = 'negativo'
    return resultado

numero = int(input('Digite um número: '))

resultado_final = positivo_negativo()
print(f'O número {numero} é {resultado_final}')