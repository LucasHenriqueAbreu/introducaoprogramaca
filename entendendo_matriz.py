
matriz = []
lista_filha = []
print('Registrando valores em uma matriz: ')
for i in range(0, 3):
    print('Regirstrando valores para a linha {}'.format(i))
    for j in range(0, 3):
        print('Regirstrando valores para a coluna {}'.format(j))
        lista_filha.append(input('Informe uma valor para a linha {} e coluna {}: '.format(i, j)))
    
    matriz.append(lista_filha[:])
    lista_filha.clear()

print(matriz)
