import os
os.system('cls')

def exibir_tabuada():
    for i in range(1, 11):
        print(f'{numero} x {i} = {numero * i}')

numero = int(input('Digite um número para realizar a tabuada: '))

print('\n= RESULTADOS =')
exibir_tabuada()