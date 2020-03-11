maior = 0
menor = 0
for pessoa in range(0, 6):
    peso = float(input('Informe o seu peso'))
    if pessoa == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peso é: {}'.format(maior))
print('O menor peso é: {}'.format(menor)) 