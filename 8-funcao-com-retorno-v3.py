import os
os.system('cls')

# Função com parâmetro e com retorno.
def calcular_notas(nota1, nota2):
    resultado = (nota1 + nota2) / 2
    return resultado

def verificar_resultado(media):
    if media >= 7:
        resultado = 'Aprovado'
    else:
        resultado = 'Reprovado'
    return resultado

print(f'= SOLICITANDO NOTAS =')

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

# Chamando a função com parâmetro e com retorno.
# Inserindo o retorno na variável "soma".
media = calcular_notas(nota1, nota2)
situacao = verificar_resultado(media)

print(f'= EXIBINDO NOTAS =')
print(f'Media: {media}')
print(f'Situação: {situacao}')

if media >= 7:
    print('Aprovado')
else:
    print('Reprovado')