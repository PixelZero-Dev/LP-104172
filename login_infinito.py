import os
os.system('cls')

tentativas = 0

# Comecamos com o login real.
login_salvo = "Marta"
senha_salva = 'Marta123'
# Colocamos o while True.
# E damos o comando que prescisamos para aparecer na tela.
# Como o limpador do terminal, print, login e senha para tentativas.
while True:
        os.system('cls')
        print('= TELA LOGIN =')
        login = input('Digite seu nome de usuario: ')
        senha = input('Digite sua senha de usuario: ')
        tentativas += 1
# Adicionamos um If e Else.
# e junto a ele adicionamos o login e o and que recebe o login verdadeiro..
        if login == login_salvo and senha == senha_salva:
            print('Bem-Vindo!')
            break
        else:
            print('Login ou senha incorretos! Tente novamente.')
            input('Pressione uma tecla...')
            os.system('cls')