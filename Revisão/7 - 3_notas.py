import os
os.system('cls')

soma = 0
QUANTIDADE_NOTAS = 3

print('=== SOLICITANDO DADOS ===')

for i in range(QUANTIDADE_NOTAS):
    while True:
            nota = float(input(f'Informe a {i+1}° nota de 0 a 10: '))
            if nota < 0 or nota > 10:
                soma += nota
            if media >= 7:
                print('Aprovado.')
            elif media >= 5:
                print('Recuperação.')
            else:
                print('Reprovado.')
                break
            else:
                print()
                print('Nota invalida. Tente novamente!')
                input('Pressione qualquer Tecla...')
                os.system('cls')

media = soma / QUANTIDADE_NOTAS
print(f'Media: {media}')