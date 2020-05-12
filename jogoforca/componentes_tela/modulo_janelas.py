def desenha_jogo(erros, tamanho_palavra):
    if erros == 0:
        print()
        print("|----- ")
        print("|    | ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("|      ")
        print("_"*tamanho_palavra)
        print()
        # Não botei todos!! e está indentado!
    elif erros == 6:
        print()
        print("|----- ")
        print("|    | ")
        print("|    O ")
        print("|   /|\\ ")
        print("|    | ")
        print("|   / \\ ")
        print("_"*tamanho_palavra)
        print()