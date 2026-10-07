import os
os.system('cls')

soma = 0
quantidade = 0

while True:
    nota = float(input('Digite uma nota: '))
    soma += nota
    quantidade += 1

    resposta = input('Deseja inserir mais uma nota?: ')

    if resposta == 'N':
        break

if quantidade > 0:
    media = soma /quantidade
    print(f'\nA média aritmética das {quantidade} notas informadas é: {media:.2f}')
else:
    print('\nNenhuma nota foi informada.')