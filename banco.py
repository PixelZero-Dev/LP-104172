import os
os.system('cls')

saldo = [500]
extrato = []

while True:
    print("""
=== Banco Cofrinho ° Caixa ===

1 - Ver Saldo
2 - Depositar
3 - Sacar
4 - Ver Extrato
0 - Sair

    """)

    opcao = int(input('Escolha uma Opção: '))

    os.system('cls')
    match opcao:
        case 1:
            print = 'Saldo Disponivel.'
        case 2:
            deposito = int(input('Informe o valor do Deposito: '))
        case 3:
            sacar = int('Informe o valor que deseja sacar: ')
        case 4:
            extrato = 'Extrato de Movimentação.'
        case 5:
            print('Até mais, nosso banco agradece.')
            break
        case _:
            print('Opção invalida. \nTente novamente... \n')

    voltar = input('Deseja voltar ao menu novamente? \nResponda com S ou N: ').upper()
    if voltar == 'N':
        print('Até mais, nosso banco agradece.')
        break