import os
os.system('cls')

# Função com parâmetro e com retorno.
def calcular_notas(nota1, nota2):
    resultado = (nota1 + nota2) / 2
    return resultado

print(f'= SOLICITANDO NOTAS =')

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

# Chamando a função com parâmetro e com retorno.
# Inserindo o retorno na variável "soma".
media = calcular_notas(nota1, nota2)

print(f'= EXIBINDO NOTAS =')
print(f'Media: {media}')