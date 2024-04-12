'''

Desenvolva um programa que leia as duas notas de um aluno e retorne sua média.

'''

n1 = int(input('Digite a nota do primeiro bimestre um aluno: '))
n2 = int(input('Digite a nota do segundo bimestre: '))
n3 = int(input('Digite a nota do terceiro bimestre: '))
n4 = int(input('Agora digite a nota do quarto bimestre para podemos ter retornar a média do ano: '))

media = (n1 + n2 + n3 + n4)/4  # para fazer a média
print(f'A média do aluno foi = {media}')

# print('A média do aluno foi {}'.format((n1 + n2 + n3 + n4 )/4))
