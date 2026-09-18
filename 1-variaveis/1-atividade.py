import os

# Limpa o terminal.
os.system('cls')

# ENTRADA.
print('= SOICITANDO DADOS =')
primeiro_numero = int(input('Digite o primeiro numero: '))
segundo_numero = int(input('Digite o segundo numero: '))

# PROCESSAMENTO.
soma = primeiro_numero + segundo_numero
subtracao = primeiro_numero - segundo_numero
multiplicacao = primeiro_numero * segundo_numero
divisao = primeiro_numero / segundo_numero

# SAIDA.
print('\n= EXIBINDO DADOS =')
print('Soma: ', soma)
print('Subtração: ', subtracao)
print('Multiplicação: ', multiplicacao)
print('Divisão: ', divisao)