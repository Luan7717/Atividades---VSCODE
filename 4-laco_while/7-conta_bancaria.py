import os
os.system('cls')

saldo = 1000

while True:
    print('\n1 - Consultar saldo')
    print('2 - Depositar')
    print('3 - Sacar')
    print('4 - Sair')

    opcao = int(input('Escolha a opção desejada: '))
    if opcao == 1:
        print(f'\nSeu saldo é R${saldo:.2f}')
    elif opcao == 2:
        valor = float(input('Digite o valor do depósito: '))
        if valor > 0:
            saldo += valor
            print('\nDepósito realizado!')
        else:
            print('Valor inválido!')
    elif opcao == 3:
        valor = float(input('Digite o valor do saque: '))
        if valor > 0:
            if valor <= saldo:
                saldo -= valor
                print('\nSaque realizado!')
            else:
                print('\nSaldo insuficiente!')
        else:
            print('\nValor inválido!')
    elif opcao == 4:
        print('\nPrograma encerrado!')
        break
    else:
        print('\nOpção inválida!')