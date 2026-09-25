import os
os.system('cls')

print('ACUMULANDO VALORES EM UMA VARIÁVEL.')
soma = 0

print(f'Valor Inicial da variavel soma: {soma}')

for i in range(3):
    numero = int(input('Digite um número para somar: '))
    soma = soma + numero
    print(f'Valor temporario da variavel soma: {soma}')

print(f'\nValor final da variavel soma: {soma}')