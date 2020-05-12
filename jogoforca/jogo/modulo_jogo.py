from random import choice

def define_jogador_desafiado_desafiador(jogador1, jogador2):
    if not jogador1.get('desafiado') and not jogador2.get('desafiado'):
        escolhido = choice([jogador1, jogador2])
        escolhido['desafiado'] = True
    else:
        if jogador1.get('desafiado'):
            jogador1['desafiado'] = False
            jogador2['desafiado'] = True
        elif jogador2.get('desafiado'):
            jogador2['desafiado'] = False
            jogador1['desafiado'] = True


def obtem_jogador_desafiado(jogador1, jogador2):
    if jogador1.get('desafiado'):
        return jogador1
    elif jogador2.get('desafiado'):
        return jogador2

def obtem_jogador_desafiador(jogador1, jogador2):
    if not jogador1.get('desafiado'):
        return jogador1
    elif not jogador2.get('desafiado'):
        return jogador2
