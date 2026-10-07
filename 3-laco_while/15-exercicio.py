import os
os.system('cls')

total_familias = 0
soma_salarios = 0
soma_filhos = 0
maior_salario = 0
menor_salario = 0

while True:
    print("\n===== MENU =====")
    print("1 - Adicionar família")
    print("2 - Sair e exibir resultados")

    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        salario = float(input("Digite o salário da família: R$ "))
        filhos = int(input("Digite o número de filhos: "))

        # Primeira família
        if total_familias == 0:
            maior_salario = salario
            menor_salario = salario
        else:
            if salario > maior_salario:
                maior_salario = salario

            if salario < menor_salario:
                menor_salario = salario

        total_familias += 1
        soma_salarios += salario
        soma_filhos += filhos

    elif opcao == 2:
        print("\n===== RESULTADOS =====")

        if total_familias > 0:
            media_salario = soma_salarios / total_familias
            media_filhos = soma_filhos / total_familias

            print("a) Total de famílias:", total_familias)
            print(f"b) Média do salário: R$ {media_salario:.2f}")
            print(f"c) Média do número de filhos: {media_filhos:.2f}")
            print(f"d) Maior salário: R$ {maior_salario:.2f}")
            print(f"e) Menor salário: R$ {menor_salario:.2f}")
        else:
            print("Nenhuma família foi cadastrada.")

        break

    else:
        print("Opção inválida! Digite 1 ou 2.")