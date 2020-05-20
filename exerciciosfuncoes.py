# 1. Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular 
# (largura e comprimento) e mostre a área do terreno.
def area(largura, comprimento):
    return largura * comprimento

assert area(2,2) == 4


# 2. Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
#  Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

def contador(inicio, fim, passo):
    for i in range(inicio, fim, passo):
        print(i)

# print('Contagem 1')
# contador(1, 11, 1)
# print('Contagem 2')
# contador(10, 0, -2)
# print('Contagem 3')
# contador(50, 100, 2)


# 3. Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
#  Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
def maior(*args):
    maior = 0
    for num in args:
        if num > maior:
            maior = num

    return maior

assert maior(1,2,3,4,5,6,7,8,9,10) == 10
numeros = (1,2,3,4,5,6,7,8,9,10)
assert maior(*numeros) == 10
numeros = (500,300,1200,999)
assert maior(*numeros) == 1200

# 4. Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a
#  soma entre todos os valores pares sorteados pela função anterior.
from random import randint

def sorteia():
    numeros = []
    for i in range(0, 5):
        numeros.append(randint(0, 100))
    return numeros

def soma(*args):
    total = 0
    for num in args:
        if num % 2 == 0:
            total += num

    return total

# Teste quantidade de números
numeros = sorteia()
assert len(numeros) == 5

# Teste soma
numeros = [2, 5, 4, 9, 10]
assert soma(*numeros) == 16 

# Teste soma
numeros = sorteia()
total = soma(*numeros)
assert total % 2 == 0 


# 5. Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, 
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

# 6. Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número 
# a calcular e outro chamado show,
#  que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def fatorial(num, show=False):
    ft = 1
    for i in range(num, 0, -1):
        if show:
            print(i, end='')
            if i > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
        ft *= i
    print(ft)
    return ft

assert fatorial(5, show=True) == 120

# 7. Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
#  o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do 
# jogador, mesmo que algum dado não tenha sido informado corretamente.

# 8. Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input()
#  do Python, só que fazendo a validação para aceitar apenas um valor numérico.

# 9. Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar 
# um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)