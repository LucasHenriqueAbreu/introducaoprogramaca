from arquivos.telas import entrada_de_dados, saida_de_dados
saida_de_dados.msg_boas_vindas()

jogador1, jogador2 = entrada_de_dados.pergunta_nome_jogadores()
jogador_desafiador = entrada_de_dados.pergunta_jogador_desafiador()

print(jogador1, jogador2)
print(jogador_desafiador)