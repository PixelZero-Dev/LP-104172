import os
os.system('cls')
# Comecamos com o login real.
print('= TELA PARA CADASTRO = ')
login_cadastrado = input('Digite seu login: ')
senha_cadastrada = input('Digite sua senha: ')
# Colocamos o while True.
# E damos o comando que prescisamos para aparecer na tela.
# Como o limpador do terminal, print, login e senha para tentativas.
while True:
        os.system('cls')
        print('= TELA PRAR LOGIN =')
        login = input('Digite seu nome de usuario: ')
        senha = input('Digite sua senha: ')
# Adicionamos um If e Else.
# e junto a ele adicionamos o login que recebe o login verdadeiro.
        if login == login_cadastrado and senha == senha_cadastrada:
            print('Bem-Vindo!')
            break
        else:
            print('\n Login ou senha incorreto! Tente novamente.')
            input('Deseja tentar novamente? Press Enter...')
            os.system('cls')