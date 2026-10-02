import os
os.system('cls')

soma = 0
QUANTIDADE_NOTAS = 3

print('=== SOLICITANDO DADOS ===')

for i in range(QUANTIDADE_NOTAS):
    while True:
            nota = float(input(f'Informe a {i+1}° nota de 0 a 10: '))
            if nota < 0 or nota > 10:
                print('Nota invalida. Tente novamente!')
                input('Pressione qualquer Tecla...')
                os.system('cls')
            else:
                soma += nota
                break

media = soma / QUANTIDADE_NOTAS

if media >= 7:
    resultado = ('Aprovado.')
elif media >= 5:
    resultado = ('Recuperação.')
else:
    resultado = ('Reprovado.')
    os.system('cls')

media = soma / QUANTIDADE_NOTAS
print(f'Media: {media}')
print(f'Resultado: {resultado}')