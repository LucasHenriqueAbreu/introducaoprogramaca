total = 0
for contador in range(0, 5):
    valor_informado_icorreto = True
    nota = 0
    while valor_informado_icorreto:
        valor_do_teclado = input('Informe a {}ª nota: '.format(contador + 1))
        if valor_do_teclado.isnumeric():
            valor_informado_icorreto = False
            nota = float(valor_do_teclado)
        else:
            print('Só aceitamos números para o campo nota')
    
    total = total + nota

media = total / 5

print('A média do aluno é :{:.2f}'.format(media))

if media >= 7:
    #sim
    print('Aluno aprovado!')
    if media <= 7.5:
        print('Passou, mas passou raspando!') 
else:
    #não
    print('O apedeuta reprovou!')