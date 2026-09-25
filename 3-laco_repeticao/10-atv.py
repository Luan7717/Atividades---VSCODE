import os
os.system('cls')

media = 0

for i in range(3):
    nota = float(input('Digite sua nota: '))
    media = media + nota
    total = media / 3
    if  total >= 7:
        resultado = 'Aprovado'
    elif total >= 4:
        resultado = 'Recuperação'
    else:
        resultado = 'Reprovado'

print(f'Sua média é: {total}')
print(f'{resultado}')