def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    return num1 / num2

def calculadora(num1, num2):
    som = soma(num1, num2)
    sub = subtracao(num1, num2)
    mul = multiplicacao(num1, num2)
    div = divisao(num1, num2)
    return som, sub, mul, div

def velociada_media(distancia, tempo):
    return divisao(distancia, tempo)

print(velociada_media(200, 10))