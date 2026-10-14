import os
os.system('cls')

vetor = [] # Criando um vetor vazio.

numeros = int(input('Quantos números deseja armazenar no vetor? ')) # Solicitando a quantidade de números que o usuário deseja armazenar no vetor.
os.system('cls')

print(' = INSERINDO NÚMEROS NO VETOR = ')
for i in range(numeros):
    numeros = float(input(f'Digite o {i + 1}° número: '))
    vetor.append(numeros) # Inserindo o número no vetor de números.
    menor_numero = min(vetor) # Encontrando o menor numero no vetor.
    maior_numero = max(vetor) # Encontrando o maior numero no vetor.

print('\n = NÚMEROS ARMAZENADOS = ')
for i, numeros in enumerate(vetor):
    print(f'{i + 1}° número: {numeros}')

print('\n = EXIBINDO O MAIOR E MENOR NÚMERO = ')
print(f'Pares: {menor_numero}')
print(f'Ímpares: {maior_numero}')