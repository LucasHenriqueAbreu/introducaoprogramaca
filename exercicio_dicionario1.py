# 1. Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
# No final, mostre o conteúdo da estrutura na tela.

aluno = {}
aluno['nome'] = input('Informe o nome do aluno: ')
aluno['media'] = float(input('Informe a média do aluno: '))

if aluno.get('media') >= 7:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'

print(aluno)
