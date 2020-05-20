from moeda import aumentar, diminuir, dobro, metade

print('Nosso programa de gerenciamento de moeda')
valor = 10.0
print(aumentar(valor, 10, formata_valor=True))
print(diminuir(valor, 10))
print(dobro(valor))
print(metade(valor))