from componentes_tela.modulo_inputs import input_cria_usuario, input_definicao_palavra, input_letra
from componentes_tela.modulo_janelas import desenha_jogo
from jogo.modulo_jogo import define_jogador_desafiado_desafiador, obtem_jogador_desafiado, obtem_jogador_desafiador

print('Bem vindo ao jogo da forca!')

jogador1 = input_cria_usuario()
jogador2 = input_cria_usuario()

define_jogador_desafiado_desafiador(jogador1, jogador2)

jogador_desafiador = obtem_jogador_desafiador(jogador1, jogador2)
jogador_desafiado = obtem_jogador_desafiado(jogador1, jogador2)
palavra = input_definicao_palavra(jogador_desafiador)
desenha_jogo(0, len(palavra))
letra = input_letra(jogador_desafiado)
