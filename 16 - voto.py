import os
os.system('cls')

idade = int(input('Digite sua idade: '))

if idade < 16:
    print('Não está apto a votar.')
elif idade <= 17:
    print('Seu voto é opcional.')
elif idade <= 65:
    print('Seu voto é obrigatório.')
else:
    print('Não é obrigado a votar.')