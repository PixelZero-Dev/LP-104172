import os
os.system('cls')

quantidade_pares = 0
quantidade_impares = 0
soma_pares = 0
soma_geral = 0
quantidade_geral = 0

while True:
    valor = int(input('Digite um numero inteiro positivo (ou 0 para sair): '))

    if valor == 0:
        break

    if valor % 2 == 0:
        quantidade_pares += 1
        soma_pares += valor
    else:
        quantidade_impares += 1

    soma_geral += valor
    quantidade_geral += 1

print(f'\n Quantidade de numeros pares: {quantidade_pares}')
print(f'Quantidade de numeros impares: {quantidade_impares}')

if quantidade_pares > 0:
    media_pares = soma_pares / quantidade_pares
    print(f'b. Media de valores pares: {quantidade_pares}')
else:
    print(f'b. Nenhum valor par foi informado.')
if quantidade_geral > 0:
    media_geral = soma_geral / quantidade_geral
    print(f'c. Media geral dos numeros lidos: {media_geral:.2f}')
else:
    print(f'c. Nenhum numero foi lido. ')