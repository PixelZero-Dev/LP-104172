import os
os.system('cls')

soma = 0
quantidade_notas = 0

while True:
    print("""
    === MENU ===
S   |  Adicionar nota   |
N   |  Calcular media aritmética   |
    """)

    resposta = input('Deseja inserir uma nota?: ').lower()

    match resposta:
        case 's':
            nota = float(input('Digite a nota: '))
            soma += nota
            quantidade_notas += 1
        case 'n':
            break
        case _:
            print('Opção inválida! \n')
            input('Pressione ENTER para voltar ao menu...')

if quantidade_notas == 0:
    print('Nenhuma nota foi inserida.')
else:
    media = soma / quantidade_notas
    print(f'A média aritmética das notas inseridas é: {media:.2f}')