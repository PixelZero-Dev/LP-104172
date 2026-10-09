import os
os.system('cls')

vetor_notas = []

for i in range(3):
    nota = float(input(f'Digite a nota {i + 1}: '))
    vetor_notas.append(nota) # Inserinedo a nota no vetor de notas.

    media = sum(vetor_notas) / len(vetor_notas) # Calculando a média das notas.

for i in range(3):
    print(f'Nota {i + 1}: {vetor_notas[i]}') # Acessando a nota no vetor de notas.
    print(f'Média das notas: {media:.2f}') # Exibindo a média das notas.