import os
os.system('cls')

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

match media:
    case x if media >= 6:
        print(f'Média: {media:.1f}')
        print(f'Parabéns! Aluno Aprovado.')
    case x if media >= 4:
        print(f'Média: {media:.1f}')
        print(f'Aluno em recuperação.')
    case _:
        print(f'Média: {media:.1f}')
        print(f'Aluno reprovado.')