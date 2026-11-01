import os
import time

lista_pacientes = []
contador = 0

while True:
    os.system('cls')
    print('''
=== CADASTRO DE PACIENTES ===
1 - Cadastrar paciente
2 - Listar pacientes
3 - Atualizar paciente
4 - Excluir paciente
0 - Sair''')

    opcao = int(input('Digite uma opção: '))

    match opcao:
        case 1:
            contador += 1
            paciente_nome = input('\nDigite seu nome: ').strip().lower()
            paciente_sobrenome = input('Digite seu sobrenome: ').strip().lower()
            if paciente_nome == '' or paciente_sobrenome == '':
                print('Nome ou sobrenome não pode ser vazio!')
                input('Clique em uma tecla para continuar')
            else:
                lista_pacientes.append((paciente_nome, paciente_sobrenome))
                print(f'\nNome: {paciente_nome}')
                print(f'Sobrenome: {paciente_sobrenome}')
                print('Paciente cadastrado com sucesso!')
                input('Clique em uma tecla para continuar')
        case 2:
            print('\n=== PACIENTES CADASTRADOS ===')
            if len(lista_pacientes) == 0:
                print('Não há pacientes cadastrados.')
                input('Clique em uma tecla para continuar')
            else:
                for contador, (nome, sobrenome) in enumerate (lista_pacientes, start=1):
                    print(f'{contador} - {nome} {sobrenome}')
                print(f'Quantidade de pacientes cadastrados: {len(lista_pacientes)}')
                input('Clique em uma tecla para continuar')
        case 3:
            print('\n=== ATUALIZAR PACIENTE ===')
            atualizar = input('Digite o nome do paciente que deseja atualizar: ').strip().lower()
            posicao = -1
            for i, (nome, sobrenome) in enumerate (lista_pacientes):
                nome_completo = f'{nome} {sobrenome}'.lower()
                if nome_completo == atualizar:
                    posicao = i
                    break
            if posicao != -1:
                novo_nome = input('Novo nome: ')
                novo_sobrenome = input('Novo sobrenome: ')
                lista_pacientes[posicao] = (novo_nome, novo_sobrenome)
                print('Dados do paciente atualizados!')
            else:
                print('Paciente não encontrado!')
            input('Clique em uma tecla para continuar')
        case 4:
            print('\n=== REMOVER PACIENTE ===')
            nome_completo = input('Qual paciente deseja remover?: ')
            for i, (nome, sobrenome) in enumerate(lista_pacientes):
                if f'{nome} {sobrenome}'.strip().lower() == nome_completo:
                    lista_pacientes.pop(i)
                    print('Paciente removido com sucesso!')
                    input('Clique em uma tecla para continuar')
                    break
            else:
                print('Paciente não encontrado!')
                input('Clique em uma tecla para continuar')