import os
os.system('cls')

login_salvo = '@SENAI123'
senha_salva = '@AlunoSENAI'
tentativas = 1

while True:
    if tentativas <= 3:
        print(f'Tentativas: {tentativas}')
        login = input('Digite seu nome de usuario: ')
        senha = input('Digite sua senha: ')
        tentativas += 1
        if login == login_salvo and senha == senha_salva:
            print('Bem-Vindo!')
            break
        else:
            print('\n Login ou senha incorreto! Tente novamente.')
            input('Deseja tentar novamente?')
            os.system('cls')

    else:
        print('=FIM=')
        break