import os
os.system('cls')

print('=== SOLICITANDO NOTAS DO ALUNO === ')

QUANTIDADE_NOTAS = 4
soma_notas = 0.0

for i in range(QUANTIDADE_NOTAS):
    soma_notas += float(input('Digite uma nota: '))

media = soma_notas / QUANTIDADE_NOTAS

print(f'A média das notas é: {media}')
