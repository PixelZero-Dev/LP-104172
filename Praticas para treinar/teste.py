import os
os.system('cls')

tentativas = 1
login_salvo = 'Marta123'
senha_salva = 'Marta@123'

while True:
    os.system('cls')
    if tentativas <= 3:
        login = input('Digite seu login: ')
        senha = input('Digite sua senha')
        tentativas += 1
        if login == login_salvo and senha == senha_salva:
            print('Acesso Concedido!')
            break
        else:
            os.system('cls')
            print('Login ou senha incorretos! tente novamente.')
            input('Pressione qualquer tecla...')
    else:
        print('Acesso Bloqueado, Reinicie o Sistema.')
        break