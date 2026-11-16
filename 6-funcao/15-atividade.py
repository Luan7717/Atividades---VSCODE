import os
os.system('cls')

vetor_nota = []
def mostrar_media():
    for lugar, nota in enumerate (vetor_nota, start=1):
        print(f'{lugar}° Nota do aluno: {nota}')
        media_aluno(nota)
    print(f'\nMédia: {media:.2f}')

def media_aluno(nota):
    nota_media = sum(vetor_nota) / 3
    return nota_media

for i in range(3):
    nota = float(input(f'Digite a {i+1}º nota do aluno: '))
    vetor_nota.append(nota)

media = media_aluno(vetor_nota[-1])

print(f'')
mostrar_media()