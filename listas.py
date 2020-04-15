
tabuleiro = [
    ['X', 'X', 'X'],
    ['O', 'O', 'O'],
    ['X', 'X', 'X']
]

for index, linha in enumerate(tabuleiro):
    print(' {} | {} | {} '.format(linha[0] or ' ', linha[1] or ' ', linha[2] or ' '))
    if index != len(tabuleiro) -1:
        print('_'*11)
    print()