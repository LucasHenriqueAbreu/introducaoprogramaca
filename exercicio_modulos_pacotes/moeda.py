def aumentar(valor, percent_para_aumentar, formata_valor=False):
    resultado = valor + (valor / 100 * percent_para_aumentar)
    if formata_valor:
        return moeda(resultado)
    return resultado

def diminuir(valor, percent_para_diminuir):
    return valor - (valor / 100 * percent_para_diminuir)

def dobro(valor):
    return valor * 2

def metade(valor):
    return valor / 2

def moeda(num):
    return f'R$ {float(num):.2f}'