lista_de_livros = []
continhar_registrando_livros = True

while continhar_registrando_livros:
    dicionario_livro = {}
    dicionario_livro['autor'] = input('Informe o autor do livro: ')
    dicionario_livro['titulo'] = input('Informe o título do livro: ')
    dicionario_livro['editora'] = input('Informe a editora do livro: ')

    lista_de_livros.append(dicionario_livro)

    decisao_usuario = input('Deseja continuar registrando livros? S/N')
    if decisao_usuario in 'Nn':
        continhar_registrando_livros = False

print('-='*20) # apenas mostra uma linha no terminal 
print('      LIVROS REGISTRADOS     ')
print('-='*20) # apenas mostra uma linha no terminal 

for livro in lista_de_livros:
    print('Autor: {}, Título: {}, Editora: {}'.format(livro['autor'], livro['titulo'], livro['editora']))