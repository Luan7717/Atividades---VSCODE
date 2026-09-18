import os
os.system('cls')


# INICIO.
idade = int(input('Digite sua idade: '))

# PROCESSO.
if idade < 16:
    print('Não pode votar.')
elif idade < 18:
    print('Voto opcional.')
elif idade <= 65:
    print('Voto obrigatorio.')
else:
    print('Voto não obrigatorio')