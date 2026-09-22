import os
os.system('cls')

print('=== TABUADA ===')
numero = int(input('Digite um numero: '))

# ADIÇÃO
for i in range(1, 11):
    print(f'{numero} + {i} = {numero + i}')

# SUBTRAÇÃO
print('\n=== TABUADA ===')
numero = int(input('Digite um numero: '))
for i in range(1, 11):
    print(f'{numero} - {i} = {numero - i}')

# MULTIPLICAÇÃO
print('\n=== TABUADA ===')
numero = int(input('Digite um numero: '))
for i in range(1, 11):
    print(f'{numero} * {i} = {numero * i}')

# DIVISÃO
print('\n=== TABUADA ===')
numero = int(input('Digite um numero: '))
for i in range(1, 11):
    print(f'{numero} / {i} = {numero / i}')