# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

valores = (
    int(input('Informe um número: ')),
    int(input('Informe um número: ')),
    int(input('Informe um número: ')),
    int(input('Informe um número: ')),
    int(input('Informe um número: ')),
)

print('A quantidade de noves encontrados é: {}'.format(valores.count(9)))
if 3 in valores:
    print('O valor 3 foi encontrado na posição: {}'.format(valores.index(3)))
else:
    print('O valor 3 não foi encontrado na tupla. ')

for valor in valores:
    if valor % 2 == 0:
        print('Número par: {}'.format(valor))