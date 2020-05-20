import matematica_utils
import view_utils

print('=== Calculadora ===')

num1 = view_utils.input_float('Informe o primeiro número: ')
num2 = view_utils.input_float('Informe o segundo número: ')

print(f'soma {matematica_utils.soma(num1, num2)}')
print(f'subtracao {matematica_utils.subtracao(num1, num2)}')
print(f'multiplicacao {matematica_utils.multiplicacao(num1, num2)}')
print(f'divisao {matematica_utils.divisao(num1, num2)}')