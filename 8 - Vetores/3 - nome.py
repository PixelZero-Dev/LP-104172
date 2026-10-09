import os
os.system('cls')

vetor_nomes = []

for i in range(3):
    nome = input(f'Digite o nome {i + 1}: ')
    vetor_nomes.append(nome) # Inserindo o nome no vetor de nomes.

for i in range(3):
    print(f'Nome {i + 1}: {vetor_nomes[i]}') # Acessando o nome no vetor de nomes.