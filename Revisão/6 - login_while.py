import os
os.system('cls')

print('= TELA PARA CADASTRO = ')
login_cadastrado = input('Digite seu login: ')
senha_cadastrada = input('Digite sua senha: ')

while True:
        os.system('cls')
        print('= TELA PRAR LOGIN =')
        login = input('Digite seu nome de usuario: ')
        senha = input('Digite sua senha: ')

        if login == login_cadastrado and senha == senha_cadastrada:
            print('Bem-Vindo!')
            break
        else:
            print('\n Login ou senha incorreto! Tente novamente.')
            input('Deseja tentar novamente? Press Enter...')
            os.system('cls')