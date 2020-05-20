# 1. Faça um programa que tenha uma função chamada area(), 
# que receba as dimensões de um terreno retangular 
# (largura e comprimento) e mostre a área do terreno.

def area(largura, comprimento):
    return largura * comprimento

assert area(2, 2) == 4, 'A função de área não está retornando o valor calculado corretamente'

print('Testes ok!')