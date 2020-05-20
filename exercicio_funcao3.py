# 3. Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
#  Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(numeros):
    m = 0
    for i in numeros:
        if i > m:
            m = i
    
    return m

assert maior([11, 10, 8, 4, 3]) == 11

assert maior([110, 100, 78, 4, 33]) == 110

print('Testes OK!')