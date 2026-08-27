import os
os.system('cls')

# SOLICITANDO DADOS.
primeiro_numero = float(input('Digite o primeiro numero: '))
segundo_numero = float(input('Digite o segundo numero: '))

# CALCULANDO.
media = (primeiro_numero + segundo_numero) / 2
soma = primeiro_numero + segundo_numero
produto = primeiro_numero * segundo_numero

# PROCESSAMENTO
if primeiro_numero > segundo_numero:
    maior = primeiro_numero
    menor = segundo_numero
else:
    maior = segundo_numero
    menor = primeiro_numero

# RESULTADO
print(f'\nMédia: {media}')
print(f'Soma: {soma}')
print(f'Produto: {produto}')
print(f'Maior número: {maior}')
print(f'Menor número: {menor}')