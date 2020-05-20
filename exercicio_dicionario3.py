# 3. Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar

from datetime import datetime

def mostrar_pessoa(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} {value}')

funcionario = {}

funcionario['nome'] = input('Informe o nome do funcionário: ')
funcionario['ano_nasc'] = int(input('Informe o ano de nascimento do funcionário: '))
funcionario['idade'] = datetime.now().year - funcionario.get('ano_nasc')
funcionario['ctps'] = input('Informe a CTPS do funcionário, ou 0 caso não tenha:')

if (funcionario.get('ctps') != '0'):
    funcionario['ano_cont'] = int(input('Informe o ano de contratação: '))
    funcionario['salario'] = float(input('Informe o salário do funcionário: R$ '))
    funcionario['ano_apon'] =  funcionario.get('ano_cont') + 30 

mostrar_pessoa(**funcionario)