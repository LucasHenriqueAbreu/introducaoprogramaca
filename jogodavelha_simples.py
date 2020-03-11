pos1 = None
pos2 = None
pos3 = None
pos4 = None
pos5 = None
pos6 = None
pos7 = None
pos8 = None
pos9 = None

turno_incorreto = True
jogador_atual = None

print('''
        Para jogar, digite o número correspondente à posição no tabuleiro para fazer sua jogada nela.
        Por exemplo, digamos que você queira jogar no centro, então você digita 5.
            |     |     
            {0} |  {1}  | {2}  
        ____|_____|_____
            |     |     
            {3} |  {4}  | {5}  
        ____|_____|_____
            |     |     
            {6} |  {7}  | {8}  
            |     |     
            '''.format(pos1 or 1, pos2 or 2, pos3 or 3, pos4 or 4, pos5 or 5, pos6 or 6, pos7 or 7, pos8 or 8, pos9 or 9))

# Validação de turno (quem está jogando)
while(turno_incorreto):
    escolha = input('Quem vai começar jogando? ')
    if escolha == 'X' or escolha == 'x':
        turno_incorreto = False
        jogador_atual = 'X'
    elif escolha == 'O' or escolha == 'o':
        turno_incorreto = False
        jogador_atual = 'O'
    else:
        print('Apenas X ou O são opções válidas!')

# Fluxo do jogo, repetição até que alguém tenha ganhado
jogo_acabou = False
while not jogo_acabou:
    print('''
            A vez é do jogador {9}.
                |     |     
              {0} |  {1}  | {2}  
            ____|_____|_____
                |     |     
              {3} |  {4}  | {5}  
            ____|_____|_____
                |     |     
              {6} |  {7}  | {8}  
                |     |     
                '''.format(pos1 or 1, pos2 or 2, pos3 or 3, pos4 or 4, pos5 or 5, pos6 or 6, pos7 or 7, pos8 or 8, pos9 or 9, jogador_atual))
    opcao_incorreta = True
    # Laço de verifica opção de qual posição o jogador escolheu.
    while opcao_incorreta:
        # Verifica se é uma opição válida
        opcao = int(input('Informe a posição desejada: '))
        if opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4 or \
            opcao == 5 or opcao == 6 or opcao == 7 or opcao == 8 or opcao == 9:
            opcao_incorreta = False
        else:
            print('Opção incorreta ')
    # Atribui à variável correspondente à posição selecionada 
    if opcao == 1:
        pos1 = jogador_atual
    if opcao == 2:
        pos2 = jogador_atual
    if opcao == 3:
        pos3 = jogador_atual
    if opcao == 4:
        pos4 = jogador_atual
    if opcao == 5:
        pos5 = jogador_atual
    if opcao == 6:
        pos6 = jogador_atual
    if opcao == 7:
        pos7 = jogador_atual
    if opcao == 8:
        pos8 = jogador_atual
    if opcao == 9:
        pos9 = jogador_atual

    # Verifica se alguém ganhou o jogo
    # Validação para linhas
    if pos1 != None and pos1 == pos2 and pos1 == pos3:
        jogo_acabou = True
        #Mostrar o o tabuleiro
        print('Jogador {}, venceu!'.format(jogador_atual))
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
                '''.format(pos1 or 1, pos2 or 2, pos3 or 3, pos4 or 4, pos5 or 5, pos6 or 6, pos7 or 7, pos8 or 8, pos9 or 9))
    
    elif pos4 != None and pos4 == pos5 and pos3 == pos6:
        jogo_acabou = True
        #Mostrar o o tabuleiro
        print('Jogador {}, venceu!'.format(jogador_atual))
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
                '''.format(pos1 or 1, pos2 or 2, pos3 or 3, pos4 or 4, pos5 or 5, pos6 or 6, pos7 or 7, pos8 or 8, pos9 or 9))
    
    elif pos7 != None and pos7 == pos8 and pos7 == pos9:
        jogo_acabou = True
        #Mostrar o o tabuleiro
        print('Jogador {}, venceu!'.format(jogador_atual))
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
                '''.format(pos1 or 1, pos2 or 2, pos3 or 3, pos4 or 4, pos5 or 5, pos6 or 6, pos7 or 7, pos8 or 8, pos9 or 9))
    

    # Validação para colunas
    elif pos1 != None and pos1 == pos4 and pos1 == pos7:
        jogo_acabou = True
        #Mostrar o o tabuleiro
        print('Jogador {}, venceu!'.format(jogador_atual))
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
                '''.format(pos1 or 1, pos2 or 2, pos3 or 3, pos4 or 4, pos5 or 5, pos6 or 6, pos7 or 7, pos8 or 8, pos9 or 9))
    
    elif pos2 != None and pos2 == pos5 and pos2 == pos8:
        jogo_acabou = True
        #Mostrar o o tabuleiro
        print('Jogador {}, venceu!'.format(jogador_atual))
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
                '''.format(pos1 or 1, pos2 or 2, pos3 or 3, pos4 or 4, pos5 or 5, pos6 or 6, pos7 or 7, pos8 or 8, pos9 or 9))
    
    elif pos3 != None and pos3 == pos6 and pos3 == pos9:
        jogo_acabou = True
        #Mostrar o o tabuleiro
        print('Jogador {}, venceu!'.format(jogador_atual))
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
                '''.format(pos1 or 1, pos2 or 2, pos3 or 3, pos4 or 4, pos5 or 5, pos6 or 6, pos7 or 7, pos8 or 8, pos9 or 9))
    
    
    # Validação para diagonal
    elif pos5 != None and pos5 == pos3 and pos5 == pos7:
        jogo_acabou = True
        #Mostrar o o tabuleiro
        print('Jogador {}, venceu!'.format(jogador_atual))
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
                '''.format(pos1 or 1, pos2 or 2, pos3 or 3, pos4 or 4, pos5 or 5, pos6 or 6, pos7 or 7, pos8 or 8, pos9 or 9))
    
    elif pos5 != None and pos5 == pos1 and pos5 == pos9:
        jogo_acabou = True
        #Mostrar o o tabuleiro
        print('Jogador {}, venceu!'.format(jogador_atual))
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
                '''.format(pos1 or 1, pos2 or 2, pos3 or 3, pos4 or 4, pos5 or 5, pos6 or 6, pos7 or 7, pos8 or 8, pos9 or 9))
    
    # Troca o jogador
    if jogador_atual == 'X':
        jogador_atual = 'O'
    elif jogador_atual == 'O':
        jogador_atual = 'X'