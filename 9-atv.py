import os
os.system('cls')

# SOLICITANDO DADOS.
primeiro_numero = int(input('Digite o primeiro numero: '))
segundo_numero = int(input('Digite o segundo numero: '))

# CALCULANDO.
media = (primeiro_numero + segundo_numero) / 2
soma = primeiro_numero + segundo_numero
produto = primeiro_numero * segundo_numero

# PROCESSAMENTO.
if primeiro_numero > segundo_numero:
    maior = primeiro_numero
    menor = segundo_numero
    iguais = "Não"
elif segundo_numero > primeiro_numero:
    maior = segundo_numero
    menor = primeiro_numero
    iguais = "Não"
else:
    maior = primeiro_numero
    menor = segundo_numero
    iguais = "Sim"

# SAÍDA.
print(f'\nMédia: {media}')
print(f'Soma: {soma}')
print(f'Produto: {produto}')
print(f'Maior número: {maior}')
print(f'Menor número: {menor}')
print(f'Os números são iguais?: {iguais}')