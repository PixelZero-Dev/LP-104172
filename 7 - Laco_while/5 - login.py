import os
os.system('cls')

for i in range(2):
    while True:

        senhaCadas = input('Digite uma nova senha para ter acesso ao sistema: ')
        senhaLogin = input('Digite a senha criada para ter acesso ao Banco de Dados: ')
        
        if senhaCadas == senhaLogin:
            print('Seja Bem-Vindo Funcionário 1! ')
            print('')
            print('Acesso Permitido! ')

        else:
            print('Senha Incorreta. ')
            print('')
            print('Digite a senha novamente! ')