
def input_float(msg):
    while True:
        valor = input(msg)
        if valor.isnumeric() or valor.isalnum():
            return float(valor)
        else:
            print('O valor informado não é um número')

