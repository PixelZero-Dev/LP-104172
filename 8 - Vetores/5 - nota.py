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
menor_nota = min(vetor_notas) # Encontrando a menor nota no vetor.
maior_nota = max(vetor_notas) # Encontrando a maior nota no vetor.

resultado = (f'Média das notas: {media}') # Exibindo a média das notas.
resultado += (f'\nMenor nota: {menor_nota}') # Exibindo a menor nota.
resultado += (f'\nMaior nota: {maior_nota}') # Exibindo a maior nota.


print(' = EXIBINDO NOTAS DO VETOR = ')
for posicao, nota in enumerate(vetor_notas, start=1):
    print(f'{posicao}° nota: {nota}') # Acessando a nota no vetor de notas.

print(' = RESULTADO FINAL = ')
print(f'Média: {media}') # Exibindo a média das notas.
print(f'Resultado: {resultado}') # Exibindo o resultado final.

print('\n = EXIBINDO A MENOR E MAIOR NOTAS DO VETOR = ')
print(f'Menor nota: {menor_nota}')
print(f'Maior nota: {maior_nota}')