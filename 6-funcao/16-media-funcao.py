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

def status_do_aluno(media):
    if media >= 7:
        resultado = 'Aprovado'
    else:
        resultado = 'Reprovado'
    return resultado

for i in range(3):
    while True:
        nota = float(input(f'Digite a {i+1}º nota do aluno: '))
        if nota >= 0 and nota <= 10:
            vetor_nota.append(nota)
            break
        else:
            print('Nota inválida, tente novamente!\n')

media = media_aluno(vetor_nota[-1])
situacao = status_do_aluno(media)
status_aluno = status_do_aluno(media)

print(f'')
mostrar_media()
print(f'Situação: {situacao}')