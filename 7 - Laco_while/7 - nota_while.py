import os
os.system('cls')

soma = 0
QUANTIDADE_NOTAS = 2

for i in range(QUANTIDADE_NOTAS):
    while True:
        nota = float(input(f'Digite a {i+1}° nota do aluno entre 0 a 10: '))
        if nota >= 0 and nota <= 10:
            soma = soma + nota
            break
        else:
            print()
            print('Nota invalida, tente novamente!')

media = soma / QUANTIDADE_NOTAS

print(f'Media: {media}')
print('=Fim=')
