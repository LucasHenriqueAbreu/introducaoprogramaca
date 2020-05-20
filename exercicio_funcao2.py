# 2. Faça um programa que tenha uma função chamada contador(), 
# que receba três parâmetros: início, fim e passo. 
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada


def contador(inicio, fim, passo):
    resultado = []
    if inicio < fim:
        fim += 1
    else:
        if passo > 0:
            passo *= -1 
        fim -= 1
    for i in range(inicio, fim, passo):
        resultado.append(i)
    
    return resultado

# a) de 1 até 10, de 1 em 1
assert contador(1, 10, 1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b) de 10 até 0, de 2 em 2
assert contador(10, 0, 2) == [10, 8, 6, 4, 2, 0]
# c) uma contagem personalizada
assert contador(100, 50, 10) == [100, 90, 80, 70, 60, 50]
assert contador(5, 1, 1) == [5, 4, 3, 2, 1]
assert contador(5, 1, -1) == [5, 4, 3, 2, 1]



print('testes ok!')