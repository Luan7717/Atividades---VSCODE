import os
os.system('cls')

soma_salarios = 0
quantidade = 0
maior_idade = 0
menor_idade = 999
mulheres_5000 = 0

while True:
    print('\n===== MENU =====')
    print('1 - Adicionar pessoa')
    print('2 - Exibir resultado')
    print('3 - Sair')

    opcao = int(input('\nDigite uma opção: '))
    match opcao:
        case 1:
            idade = int(input('Digite a idade: '))
            sexo = input('Digite o sexo (M/F): ').upper()
            salario = float(input('Digite o salário: R$'))
            os.system('cls')
            soma_salarios += salario
            quantidade += 1
            if idade > maior_idade:
                maior_idade = idade
            if idade < menor_idade:
                menor_idade = idade
            if sexo == 'F' and salario >= 5000:
                mulheres_5000 += 1
            os.system('cls')
        case 2:
            os.system('cls')
            if quantidade > 0:
                media = soma_salarios / quantidade
                print('\n===== RESULTADOS =====')
                print(f'Média salarial: R$ {media:.2f}')
                print(f'Maior idade: {maior_idade}')
                print(f'Menor idade: {menor_idade}')
                print(f'Mulheres com salário a partir de R$5000: {mulheres_5000}')
                input('Clique qualquer tecla para continuar...')
                os.system('cls')
            else:
                os.system('cls')
                print('\n===== RESULTADOS =====')
                print('\nNenhuma pessoa foi cadastrada.')
                break
        case 3:
            print('Programa encerrado!')
            break
        case _:
            print('Opção inválida!')