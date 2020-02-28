from random import randint
opcoes = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''
0 para PEDRA;
1 para PAPEL;
2 para TESOURA;
''')
jogador = int(input('Informe uma opção: '))
print('O computador escolheu a opção: {}'.format(opcoes[computador]))
print('O jogador escolheu a opção: {}'.format(opcoes[jogador]))

if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('VOCÊ GANHOU!')
    elif jogador == 2:
        print('VOCÊ PERDEU!')
    else:
        print('Opção incorreta! Seu Jamas!')
        
elif computador == 1:
    if jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('VOCÊ GANHOU!')
    elif jogador == 0:
        print('VOCÊ PERDEU!')
    else:
        print('Opção incorreta! Seu Jamas!')

elif computador == 2:
    if jogador == 2:
        print('EMPATE!')
    elif jogador == 0:
        print('VOCÊ GANHOU!')
    elif jogador == 1:
        print('VOCÊ PERDEU!')
    else:
        print('Opção incorreta! Seu Jamas!')