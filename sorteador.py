from random import randint
pessoas = [
    'João',
    'Pedro',
    'Maria'
]

while True:
    if len(pessoas) == 0:
        print('Acabou as pessoas!')
        break
    
    sorteado = randint(0, len(pessoas) -1)
    print('Sorteado foi:', pessoas[sorteado])
    pessoas.pop(sorteado)
    decisao = input('Deseja continular sorteando? S/N ')
    if decisao in 'Nn':
        break