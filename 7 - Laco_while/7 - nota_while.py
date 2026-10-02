import os
os.system('cls')

soma = 0
QUANTIDADE_NOTAS = 2

for i in range(QUANTIDADE_NOTAS):
    while True:
        nota = float(input(f'Digite a {i+1}° nota do aluno entre 0 a 10: '))
        if nota < 0 or nota > 10:
            print('Nota invalida. \n Tente novamente! \n')
            input('Pressione uma tecla...')
            os.system('cls')
        else:
            print()
            soma += nota
            break

media = soma / QUANTIDADE_NOTAS
print(f'Media: {media}')