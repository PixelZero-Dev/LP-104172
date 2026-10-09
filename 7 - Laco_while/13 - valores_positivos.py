import os
os.system('cls')

soma = 0
quantidade = 0

while True:
    valor = int(input('Digite um valor inteiro positivo (ou um valor negativo para sair): '))

    if valor < 0:
        break

    soma += valor
    quantidade += 1

if quantidade > 0:
    media = soma / quantidade
    print(f'A média aritmética dos números informados é: {media}')
else:
    print('Nenhum valor positivo foi informado. ')