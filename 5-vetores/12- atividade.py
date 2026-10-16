import os
os.system('cls')

vetor_numero = []
negativos = 0

print('\n= INSERINDO NÚMEROS =')
for i in range(5):
    numero = int(input(f'Digite o {i+1}º numero: '))
    vetor_numero.append(numero)
    if numero < 0:
        negativos += 1
    soma = sum(numero for numero in vetor_numero if numero > 0)

print(f'\nQuantidade de números negativos: {negativos}')
print(f'Soma dos números positivos: {soma}')
