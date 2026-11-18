import os
os.system('cls')

def calcular_peso_ideal():
    imc = peso / (altura * altura)
    print(f'IMC: {imc:.2f}')
    return imc
def imc_definido(imc):
    if imc < 18.5:
        print('Abaixo do peso.')
    elif imc <= 24.9:
        print('Peso ideal (parabéns).')
    elif imc <= 29.9:
        print('Levemente acima do peso.')
    elif imc <= 34.9:
        print('Obesidade grau I')
    elif imc <= 39.9:
        print('Obesidade grau II (severa)')
    else:
        print('Obesidade III (mórbida)')

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = calcular_peso_ideal()
imc_definido(imc)
