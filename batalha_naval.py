# posicionar 3 navios no campo batalha
# 1 vez de cada tentar acertar a posição do advesário.
# acaba quando um jogador destroi todos os navios do adversário.
# import emoji
from random import randint
from time import sleep
import sys

def mostrar_tabuleiro():
    print('\033[34m=-'*20)
    print('\033[31m Máquina')
    print('\033[32m Você')
    print('\033[34m=-'*20)
    print('    \033[34m0    1    2    3    4    5    6    7\033[m')
    for i, linha in enumerate(tabuleiro):
        print(f'\033[34m{i}', end=' \033[m')

        for j, coluna in enumerate(linha):
            if i <= 3:
                valor_coluna = 'X'
                print('\033[31m| {} |'.format(valor_coluna), end='\033[m')
            if i > 3:
                valor_coluna = coluna or 'X'
                print('\033[32m| {} |'.format(valor_coluna), end='\033[m')
        print()

def carregando():
    for i in range(100):
        sleep(0.01)
        sys.stdout.write("\r%d%%" % i)
        sys.stdout.flush()
    print()

tabuleiro = []

for x in range(0, 8):
    linha = []
    for j in range(0, 8):
        linha.append(None)
    
    tabuleiro.append(linha)

mostrar_tabuleiro()

print('\033[34m=-'*20)
print('1º rodada, posicionamento.')
print('Informe a linha e coluna de onde quer adicionar seu barco, lembre-se que sua área é a verde.')
print('\033[34m=-'*20, end='\033[m')
print()

# Perdir 3 x para o usuário informar onde ele quer por o barco
for i in range(0, 3):
    linha = 0
    coluna = 0
    while True:
        linha = input('Informe a linha que deseja adcionar seu {}º barco: '.format(i + 1))
        coluna = input('Informe a coluna que deseja adcionar seu {}º barco: '.format(i + 1))

        if not linha.isnumeric() or not coluna.isnumeric():
            print('\033[31mÔOooo, apedeuta! Linhas e colunas só podem ser números.\033[m')
        elif int(linha) <= 3:
            print('\033[31mÔooo, apedeuta! Eu não te falei que a sua área era a verde? Esconha uma linha maior que 3\033[m')
        elif int(linha) > 7 or int(coluna) > 7:
            print('\033[31mÔOooo, apedeuta! Informe um índice que exista no tabuleiro.\033[m')
        elif tabuleiro[int(linha)][int(coluna)] is not None:
            print('\033[31mÔooo, apedeuta! Você já adicionou um barco nessa posição!\033[m')
        else:
            break
    
    tabuleiro[int(linha)][int(coluna)] = '\033[33m╧\033[m'


print('\033[34m=-'*20)
print('1º rodada, posicionamento.')
print('A maquina está adicionando seus barcos...')
print('\033[34m=-'*20, end='\033[m')
print()
carregando()

for x in range(0, 3):
    while True:
        coluna = randint(0, 7)
        linha = randint(0, 3)

        if tabuleiro[linha][coluna] != '\033[33m╧\033[m':
            tabuleiro[linha][coluna] = '\033[33m╧\033[m'
            break

mostrar_tabuleiro()

print('\033[34m=-'*20)
print('2º rodada, BATALHA!.')
print('\033[34m=-'*20, end='\033[m')
print()

jogo_acabou = False
vez = 'usuario'
pontos_usuario = 0
pontos_computador = 0

while not jogo_acabou:
    if vez == 'usuario':
        #perdir para o usuário onde ele quer mandar o míssil
        while True:
            linha_coluna = input('Informe linha e coluna na ordem respectiva: ')
            if len(linha_coluna) == 2:
                linha = int(linha_coluna[0])
                coluna = int(linha_coluna[1])
                if linha < 4:
                    if coluna > 7:
                        print('Você está jogando o míssil muito longe, vai para fora do tabuleiro. hehhehh')
                        print('Tente novamente')
                    else:
                        if tabuleiro[linha][coluna] == '\033[33m╧\033[m':
                            pontos_usuario += 1
                            tabuleiro[linha][coluna] = '\033[37m☠\033[m'
                            print('Vocế destruiu um barco do inimigo')
                            break
                        else:
                            print('Infelizmente você errou!')
                else:
                    print('Você está tentando jogar um míssil no seu campo de batalha')
                    print('Tente novamente')
            else:
                print('Você precisa informar linha e coluna, respectivamente')
                print('Tente novamente')
    else:
        # sortear um posição para mandar o míssil