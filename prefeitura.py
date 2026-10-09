import os
os.system('cls')

def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print('Digite um número inteiro válido.')


def ler_float(mensagem):
    while True:
        try:
            return float(input(mensagem).replace(',', '.'))
        except ValueError:
            print('Digite um valor numérico válido.')


dados = []

while True:
    os.system('cls')
    print('''   === MENU ===

Código  |  Descrição          |
1       |  Adicionar Pessoa   |
2       |  Exibir Resultado   |
3       |  Sair               |

''')

    codigo = input('Selecione uma opção: ').strip()

    if codigo == '1':
        os.system('cls')
        print('Insira os dados da pessoa.')
        nome = input('Digite o nome da pessoa: ').strip()
        idade = ler_inteiro('Digite sua idade: ')
        sexo = input('Digite seu sexo (F/M): ').strip().upper()
        salario = ler_float('Digite seu salário: ')

        dados.append({
            'nome': nome,
            'idade': idade,
            'sexo': sexo,
            'salario': salario,
        })

        print('\nDados cadastrados com sucesso!')
        input('Pressione ENTER para voltar ao menu...')

    elif codigo == '2':
        os.system('cls')
        print('=== RESULTADOS DA PESQUISA ===')
        if dados:
            soma_salarios = sum(pessoa['salario'] for pessoa in dados)
            media_salario = soma_salarios / len(dados)

            idades = [pessoa['idade'] for pessoa in dados]
            maior_idade = max(idades)
            menor_idade = min(idades)

            mulheres_5k = sum(
                1
                for pessoa in dados
                if pessoa['sexo'] == 'F' and pessoa['salario'] >= 5000.00
            )

            print(f'a) Média de salário do grupo: R$ {media_salario:.2f}')
            print(f'b) Maior idade: {maior_idade} | Menor idade: {menor_idade}')
            print(f'c) Mulheres com salário a partir de R$ 5.000,00: {mulheres_5k}')
        else:
            print('Nenhum dado registrado ainda.')

        input('\nPressione ENTER para voltar ao menu...')

    elif codigo == '3':
        os.system('cls')
        print('Encerrando o programa...')
        break

    else:
        print('Opção inválida! Tente novamente.')
        input('Pressione ENTER para voltar ao menu...')
