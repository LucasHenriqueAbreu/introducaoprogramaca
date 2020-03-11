numero = int(input('Informe um número para ver sua tabuada: '))
for i in range(1, 11):
    print('{} X {} = {}'.format(i, numero, i * numero))