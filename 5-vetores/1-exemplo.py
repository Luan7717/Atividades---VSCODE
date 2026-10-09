import os
os.system('cls')

vetor_notas = []
quantidade = 3
nota = 0
for i in range(quantidade):
    nota += float(input('Digite uma nota: '))
    vetor_notas.append(nota) # Inserindo a nota no vetor de notas

for i in range(3):
    print(f'Nota: {vetor_notas[i]}')

print(f'Média {vetor_notas[i] / quantidade}')