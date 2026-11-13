import os
os.system('cls')

def adicao_funcao(n1, n2):
    resultado = n1 + n2
    return resultado
def subtracao_funcao(n1, n2):
    resultado = n1 - n2
    return resultado
def multiplicacao_funcao(n1, n2):
    resultado = n1 * n2
    return resultado
def divisao_funcao(n1, n2):
    resultado = n1 / n2
    return resultado

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número número: '))

adicao = adicao_funcao(n1, n2)
subtracao = subtracao_funcao(n1, n2)
multiplicacao = multiplicacao_funcao(n1, n2)
divisao = divisao_funcao(n1, n2)

print('\n= EXIBINDO RESULTADO =')
print(f'{n1} + {n2} = {adicao}')
print(f'{n1} - {n2} = {subtracao}')
print(f'{n1} * {n2} = {multiplicacao}')
print(f'{n1} / {n2} = {divisao}')