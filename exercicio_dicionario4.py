# 4. Crie um programa que gerencie o aproveitamento de um jogador de futebol.
#  O programa vai ler o nome do jogador e quantas partidas ele jogou. 
#  Depois vai ler a quantidade de gols feitos em cada partida. 
#  No final, tudo isso será guardado em um dicionário,
#  incluindo o total de gols feitos durante o campeonato.

jogador = dict()

jogador['nome'] = input('Informe o nome do jogador: ')
jogador['qtd_partidas'] = int(input('Informe a quantidade de partidas que ele jogou: '))
gols = list()
for i in range(0, jogador.get('qtd_partidas')):
    gols.append(int(input(f'Informe a quantidade de gols para a {i + 1}º partida: ')))

jogador['gols'] = gols
jogador['total_gols'] = sum(gols)

print(jogador)