import os
os.system('cls')

print('=== SOLICITANDO DADOS === ')

QUANTIDADE_NOTAS = 3
soma_notas = 0.0

for i in range(QUANTIDADE_NOTAS):
    soma_notas += float(input('Digite a nota: '))
    media = soma_notas / QUANTIDADE_NOTAS

if media >= 7:
    resultado = 'Aprovado!'
elif media >= 4:
    resultado = 'Recuperação'
else:
    resultado = 'Reprovado'

print('\n Mostrando resultado. ')

print(f'Média: {media}')
print(f'Resultado: {resultado}')