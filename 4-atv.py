import os
os.system('cls')

morangos = float(input('Digite a quantidade de morangos (Kg): '))
macas = float(input('Digite a quantidade de maçãs (Kg): '))

match morangos <= 5:
    case True:
        valor_morangos = morangos * 2.50
    case False:
        valor_morangos = morangos * 2.20

match macas <= 5:
    case True:
        valor_macas = macas * 1.80
    case False:
        valor_macas = macas * 1.50

total_kg = morangos + macas
valor_total = valor_morangos + valor_macas

match total_kg >= 10 and valor_total > 15:
    case True:
        valor_total = valor_total * 0.90

print(f'Valor a pagar: R${valor_total:.2f}')