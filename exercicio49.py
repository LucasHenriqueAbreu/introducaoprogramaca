# Crie um programa que vai gerar cinco números aleatórios e 
# colocar em uma tupla. Depois disso, mostre a listagem de números
# gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

numeros_aleatorios = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100),)
print(numeros_aleatorios)
maior = 0
menor = 0

for index, num in enumerate(numeros_aleatorios):
    if index == 0:
        maior = num
        menor = num
    else:
        if maior < num:
            maior = num
        if menor > num:
            menor = num

print('Maior valor: {}'.format(maior))
print('Menor valor: {}'.format(menor))
