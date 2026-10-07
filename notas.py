import os
os.system('cls')

tentativas = 0
login_salvo = 'Marta'
senha_salva = 'Marta@123'

print('=== LOGIN ===')

while True:
    os.system('cls')
    login = input('Digite seu Login: ')
    senha = input('Digite sua Senha: ')
    if login == login_salvo and senha == senha_salva:
        print('Acesso Liberado!')
        break
    else:
        os.system('cls')
        print('Login/Senha incorretos, Tente novamente.')
        input('Pressione Enter...')