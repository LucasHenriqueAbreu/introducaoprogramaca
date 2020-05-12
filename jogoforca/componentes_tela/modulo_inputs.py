def input_cria_usuario():
    usuario = dict()
    usuario['nome'] = input('Informe o seu nome: ')
    usuario['pontos'] = 0
    usuario['desafiado'] = False
    return usuario

def input_definicao_palavra(jogador):
    print(f"{jogador.get('nome')}, "
          f"informe a palava que deseja desafiar o seu adversário. "
          f"Tome cuidado para que ele não veja!")
    while True:
        palavra = input('Qual palavra deseja usar? (Ex.: Abelha, Cachorro...)')
        if palavra:
            break

    return palavra

def input_letra(jogador):
    while True:
        letra = input(f'{jogador.get("nome")}, informe uma letra: ')
        if len(letra) > 1:
            print('É apenas uma letra, seu apedeuta!')
        elif len(letra) < 1:
            print('Por favor, informe uma letra!')
        elif letra.isnumeric():
            print('Por favor, informe uma letra e não um número, seu apedeuta!')
        else:
            break

    return letra