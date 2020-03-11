soma = 0
for i in range(0, 6):
    numero = int(input('Informe um número'))
    if numero % 2 == 0:
        soma += numero

print(soma)