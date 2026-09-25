import os
os.system('cls')

media = 0

for i in range(4):
    nota = float(input('Digite sua nota: '))
    media = media + nota

print(f'Sua média é: {media / 4}')