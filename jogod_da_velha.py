pos1 = None
pos2 = None
pos3 = None
pos4 = None
pos5 = None
pos6 = None
pos7 = None
pos8 = None
pos9 = None

def mostrar_tabuleiro():
    print('''
        |     |     
      {0} |  {1}  | {2}  
    ____|_____|_____
        |     |     
      {3} |  {4}  | {5}  
    ____|_____|_____
        |     |     
      {6} |  {7}  | {8}  
        |     |     
    '''.format(pos1 or 1,pos2 or 2,pos3 or 3, \
        pos4 or 4,pos5 or 5,pos6 or 6,pos7 or 7, \
            pos8 or 8,pos9 or 9,))

print('''
Para jogar, digite o número correspondente 
à posição no tabuleiro para fazer sua jogada nela.
Por exemplo, digamos que você queira jogar no centro, 
então você digita 5.
''')
mostrar_tabuleiro()

turno_incorreto = True
jogador_atual = None

while turno_incorreto:
    opcao = input('Quem vai começar jogando? ')

    if opcao == 'X' or opcao == 'x':
        turno_incorreto = False
        jogador_atual = 'X'
    elif opcao == 'O' or opcao == 'o':
        turno_incorreto = False
        jogador_atual = 'O'
    else:
        print('Opção incorreta, apenas X ou O são opções válidas!')

jogo_acabou = False

while not jogo_acabou:
    print('O jogador da vez é {}'.format(jogador_atual))
    mostrar_tabuleiro()
    
    opcao_incorreta = True
    posicao_ocupada = True
    opcao_tabuleiro = None
    while opcao_incorreta or posicao_ocupada:
        opcao_tabuleiro = int(input('Informe qual é a posição do tabuleiro '))

        if opcao_tabuleiro == 1 or \
            opcao_tabuleiro == 2 or \
            opcao_tabuleiro == 3 or \
            opcao_tabuleiro == 4 or \
            opcao_tabuleiro ==  5 or \
            opcao_tabuleiro == 6 or \
            opcao_tabuleiro ==  7 or \
            opcao_tabuleiro == 8 or \
            opcao_tabuleiro == 9:
            opcao_incorreta = False
        else:
            print('Informe uma opção correta, apenas número \
                entre 1 e 9 são corretos')
    
        if opcao_tabuleiro == 1:
            if pos1 == None:
                pos1 = jogador_atual
                posicao_ocupada = False
            else:
                print('Posição ocupada pelo jogador, tente outra, seu apedeuta!')
        elif opcao_tabuleiro == 2:
            if pos2 == None:
                pos2 = jogador_atual
                posicao_ocupada = False
            else:
                print('Posição ocupada, tente outra, seu apedeuta!')
        elif opcao_tabuleiro == 3:
            if pos3 == None:
                pos3 = jogador_atual
                posicao_ocupada = False
            else:
                print('Posição ocupada, tente outra, seu apedeuta!')
        elif opcao_tabuleiro == 4:
            if pos4 == None:
                pos4 = jogador_atual
                posicao_ocupada = False
            else:
                print('Posição ocupada, tente outra, seu apedeuta!')
        elif opcao_tabuleiro == 5:
            if pos5 == None:
                pos5 = jogador_atual
                posicao_ocupada = False
            else:
                print('Posição ocupada, tente outra, seu apedeuta!')
        elif opcao_tabuleiro == 6:
            if pos6 == None:
                pos6 = jogador_atual
                posicao_ocupada = False
            else:
                print('Posição ocupada, tente outra, seu apedeuta!')
        elif opcao_tabuleiro == 7:
            if pos7 == None:
                pos7 = jogador_atual
                posicao_ocupada = False
            else:
                print('Posição ocupada, tente outra, seu apedeuta!')
        elif opcao_tabuleiro == 8:
            if pos8 == None:
                pos8 = jogador_atual
                posicao_ocupada = False
            else:
                print('Posição ocupada, tente outra, seu apedeuta!')
        elif opcao_tabuleiro == 9:
            if pos9 == None:
                pos9 = jogador_atual
                posicao_ocupada = False
            else:
                print('Posição ocupada, tente outra, seu apedeuta!')

    # Validação para linhas
    if pos1 != None and pos1 == pos2 and pos1 == pos3:
        jogo_acabou = True
        print('O jogador vencedor é {}'.format(jogador_atual))
    elif pos4 != None and pos4 == pos5 and pos4 == pos6:
        jogo_acabou = True
        print('O jogador vencedor é {}'.format(jogador_atual))
    elif pos7 != None and pos7 == pos8 and pos7 == pos9:
        jogo_acabou = True
        print('O jogador vencedor é {}'.format(jogador_atual))

    # Validação para colunas
    elif pos1 != None and pos1 == pos4 and pos1 == pos7:
        jogo_acabou = True
        print('O jogador vencedor é {}'.format(jogador_atual))
    elif pos2 != None and pos2 == pos5 and pos2 == pos8:
        jogo_acabou = True
        print('O jogador vencedor é {}'.format(jogador_atual))
    elif pos3 != None and pos3 == pos6 and pos3 == pos9:
        jogo_acabou = True
        print('O jogador vencedor é {}'.format(jogador_atual))

    # Validação para diagonal
    elif pos1 != None and pos1 == pos5 and pos1 == pos9:
        jogo_acabou = True
        print('O jogador vencedor é {}'.format(jogador_atual))
    elif pos3 != None and pos3 == pos5 and pos3 == pos7:
        jogo_acabou = True
        print('O jogador vencedor é {}'.format(jogador_atual))

    elif pos1 != None and \
        pos2 != None and \
        pos3 != None and \
        pos4 != None and \
        pos5 != None and \
        pos6 != None and \
        pos7 != None and \
        pos8 != None and \
        pos9 != None:
        jogo_acabou = True
        print('Deu velha!!') 

    mostrar_tabuleiro()
    
    if jogador_atual == 'X':
        jogador_atual = 'O'
    elif jogador_atual == 'O':
        jogador_atual = 'X'
