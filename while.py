
usuario_e_senha_invalidos = True

while(usuario_e_senha_invalidos):
    usuario = input('Informe um usuário: ')
    senha = input('Informe uma senha')
    if usuario != senha:
        usuario_e_senha_invalidos = False
    else:
        print('Usuário e senha não devem ser iguais, seu apedeuta!')

print('Usuário: {} \nSenha: {}'.format(usuario, senha))
