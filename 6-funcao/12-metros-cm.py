import os
os.system('cls')

def metros_cm():
    resultado = metros * 100
    return resultado

metros = float(input('Digite a quantidade de metros que quer converter: '))

centimetros = metros_cm()

print(f'\n= EXIBINDO RESULTADOS =')
print(f'{metros} metros são {centimetros} centímetros.')