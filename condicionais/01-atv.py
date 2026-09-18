import os
os.system('cls')

quantidade = int(input('Digite a quantidade de maçãs: '))

# PROCESSO.
if quantidade < 12:
    total = quantidade * 1.30
else:
    total = quantidade * 1.00

# SAIDA.
print(f'Valor total da compra: R${total:.2f}')