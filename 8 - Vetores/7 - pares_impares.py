import os
os.system('cls')

vetor_pares = [] # Criando um vetor vazio.
vetor_impares = [] # Criando um vetor vazio.
pares = 0
impares = 0

numeros = int(input('Quantos números deseja armazenar no vetor? ')) # Solicitando a quantidade de números que o usuário deseja armazenar no vetor.
os.system('cls')

print(' = INSERINDO NÚMEROS NO VETOR = ')
for i in range(numeros):
    numeros = float(input(f'Digite o {i + 1}° número: '))
    if numeros % 2 == 0:
        pares += 1
        vetor_pares.append(numeros)
    else:
        impares += 1
        vetor_impares.append(numeros)

print('\n = NÚMEROS ARMAZENADOS = ')
print('Pares:')
for i, numeros in enumerate(vetor_pares):
    print(f'{i + 1}° número: {numeros}')

print('\nÍmpares:')
for i, numeros in enumerate(vetor_impares):
    print(f'{i + 1}° número: {numeros}')

print('\n = EXIBINDO O MAIOR E MENOR NÚMERO = ')
print(f'Pares: {pares}')
print(f'Ímpares: {impares}')