# 4. Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a 
# soma entre todos os valores pares sorteados pela função anterior./
from random import randint
def sorteia():
    numeros = []
    for count in range(0, 5):
        numeros.append(randint(0, 100))

    return numeros

def e_par(num):
    return num % 2 == 0

def soma_par(numeros):
    total = 0
    for numero in numeros:
        if e_par(numero):
            total+=numero
    return total

numeros = sorteia()

assert len(numeros) == 5
assert e_par(soma_par(numeros))
assert e_par(2)
assert e_par(4)
assert not e_par(5)

print('Teste OK!')