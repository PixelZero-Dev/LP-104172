import os
os.system('cls')

tentativas = 1

login_salvo = 'Rafael'
senha_salva = 'Rafael123'

print(' === LOGIN === ')

while True:
    os.system('cls')
    if tentativas <= 3:
        login = input('Digite seu nome de Usuario: ')
        senha = input('Digite a senha de Usuario: ')
        tentativas += 1
        if login == login_salvo and senha == senha_salva:
            print('Acesso concedido!')
            break
        else:
            os.system('cls')
            print('Login ou Senha incorretos! Tente novamente.')
            input('Pressione qualquer tecla...')
    else:
        print('Acesso bloqueado! Reinicie o sistema e tente novamente.')
        break