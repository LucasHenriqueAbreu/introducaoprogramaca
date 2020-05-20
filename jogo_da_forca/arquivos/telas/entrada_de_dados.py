
def pergunta_nome_jogadores():
    while True:
        jogador1=input('informe o nome do jogador 1: ')
        jogador2=input('informe o nome do jogador 2: ')
        return jogador1, jogador2

        if not jogador1.str() or not jogador2.str():
            print('tem que informar alguma coisa')

def pergunta_jogador_desafiador():
    while True:
        jogador_desafiador=input('quem e o desafiador?jogador1 ou jogador2 ')
        
        if jogador_desafiador=='jogador1' or jogador_desafiador=='1':
            return 1
        elif jogador_desafiador=='jogador2' or jogador_desafiador=='2':
            return 2
        else:
            print('aceitamos apenas os valores: jogador1 ou 1, jogador2 ou 2')
