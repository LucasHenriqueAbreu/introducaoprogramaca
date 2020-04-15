produtos = (
    'Item 1 ', 1.75,
    'Item 2 ', 2.50,
)

for posicao in range(0, len(produtos)):
    if posicao % 2 == 0:
        print('{:.<30}'.format(produtos[posicao]), end='')
    else:
        print('R$ {:>5.2f}'.format(produtos[posicao]))