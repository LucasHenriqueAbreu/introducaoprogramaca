# 5. Crie um programa que leia nome, sexo e idade de várias pessoas, 
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

pessoas = []
pessoa = {}
total_idade = 0

while True:
    pessoa['nome'] = input('Informe o nome da pessoa: ')
    pessoa['idade'] = int(input('Informe a idade da pessoa: '))
    pessoa['sexo'] = input('Informe o sexo da pessoa M/F/O: ')
    total_idade += pessoa.get('idade')
    pessoas.append(pessoa.copy())

    decisao = input('Deseja continuar cadastrando? S/N')
    if decisao in 'Nn':
        break

qtd_pessoas = len(pessoas)
media = total_idade / qtd_pessoas
mulheres = []
pessoas_idade_acima_media = []

for pessoa in pessoas:
    if pessoa.get('sexo') in 'Ff':
        mulheres.append(pessoa)
    if pessoa.get('idade') > media:
        pessoas_idade_acima_media.append(pessoa)


print(f'A quantidade de pessoas cadastradas é: {qtd_pessoas}')
print(f'A média de idade é: {media}')
print(f'A lista de mulheres cadastradas, foi de {len(mulheres)}, são as seguintes: ')
for mulher in mulheres:
    print(f'    Nome: {mulher.get("nome")}, idade: {mulher.get("idade")}')

print(f'A lista de pessoas cadastradas, com idade acima da média é de {len(pessoas_idade_acima_media)}, são as seguintes: ')
for pessoa in pessoas_idade_acima_media:
    print(f'    Nome: {pessoa.get("nome")}, idade: {pessoa.get("idade")}')


