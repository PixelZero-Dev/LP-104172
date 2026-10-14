import os
os.system('cls')

print(' = INSERINDO NOTAS NO VETOR = ')
vetor_notas = []
QUANTIDADE_NOTAS = 2

for i in range (QUANTIDADE_NOTAS):
    nota = float(input(f'Digite a {i + 1}° nota: '))
    vetor_notas.append(nota) # Inserindo a nota no vetor de notas.

# Sum - Simar tudo que esta no vetor.
media = sum(vetor_notas) / len(vetor_notas) # Calculando a média das notas.

print(f'Média das notas: {media}') # Exibindo a média das notas.
for posicao, nota in enumerate(vetor_notas, start=1):
    print(f'{posicao}° nota: {nota}') # Acessando a nota no vetor de notas.

print(f'Média: {media}') # Exibindo a média das notas.

print(' = RESULTADO FINAL = ')