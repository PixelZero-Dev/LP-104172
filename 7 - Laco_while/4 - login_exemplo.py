import os
os.system('cls')

login_salvo = 'Marta'
senha_salva = '@123'

while True:
    login = input('Digite o login: ')
    senha = input('Digite a senha: ')

    if login == login_salvo and senha == senha_salva:
        print('Bem-vindo! ')
        break
    else:
        print('\n Login ou senha invalido!')
        print('Tente novamente! \n')
        input('Pressione uma tecla para continuar...')
        os.system('cls')