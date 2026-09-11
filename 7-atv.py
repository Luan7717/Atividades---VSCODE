import os
os.system('cls')

nome = input('Digite o nome do produto: ')
quantidade = int(input('Calcule a quantidade adquirida: '))
preco = float(input('Digite o preço unitário: '))

total = quantidade * preco

match quantidade:
    case x if quantidade <= 5:
        desconto = total * 0.02
    case x if quantidade <= 10:
        desconto = total * 0.03
    case _:
        desconto = total * 0.05

total_pagar = total - desconto

print(f'Produto: {nome}')
print(f'Total: R${total:.2f}')
print(f'Desconto: R${desconto:.2f}')
print(f'Total a pagar: R${total_pagar:.2f}')