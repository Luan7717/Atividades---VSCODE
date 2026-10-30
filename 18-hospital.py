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
            paciente_nome = input('\nDigite seu nome: ').strip()
            paciente_sobrenome = input('Digite seu sobrenome: ')
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
            print('=== ATUALIZAR PACIENTE ===')
            atualizar = input('Digite o nome do paciente que deseja atualizar: ')
            if atualizar in lista_pacientes:
                posicao = lista_pacientes.index(posicao)
                lista_pacientes[posicao] = atualizar
                print('Dados do paciente atualizados!')
            else:
                print('Paciente não encontrado!')
                input('Clique em uma tecla para continuar')