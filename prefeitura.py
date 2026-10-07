import os
os.system('cls')

dados = []

print('''   === MENU ===

Código  |  Descrição          |
1       |  Adicionar Pessoa   |
2       |  Exibir Resultado   |
3       |  Sair               |

''')

codigo = int(input('Selecione uma opção: '))

while True:

    match codigo:
        case 1:
            os.system('cls')
            print('Insira dos dados da pessoa.')
            nome = input('Digite o nome da pessoa: ')
            idade = int(input('Digite sua Idade: '))
            sexo = input('Digite seu Sexo: ')
            salario = float(input('Digite seu salario: '))

            # Adicionando os dados na lista.
            dados.append({
                'Idade:': idade,
                'Sexo:': sexo,
                'Salario': salario,
            })
            
            print('\nDados cadastrados com sucesso!')
            input('Pressione ENTER para voltar ao menu...')

            os.system('cls') # Limpa o terminal após adicionar, conforme pedido no enuciado.

        case 2:
            os.system('cls')
            print('=== RESULTADOS DA PESQUISA ===')
            if len(dados) > 0:
                soma_salarios = sum(p['salario'] for p in dados)
                media_salario = soma_salarios / len(dados)

                idades = [p['idade'] for p in dados]
                maior_idade = max(idades)
                menor_idade = min(idades)

                mulheres_5k = sum(1 for p in dados if p['sexo'] == 'F' and p['salario'] >= 5000.00)

                print(f'a) Média de salário do grupo: R$ {media_salario:.2f}')
                print(f'b) Maior idade: {maior_idade} | Menor idade: {menor_idade}')
                print(f'c) Mulheres com salário a partir de R$ 5.000,00: {mulheres_5k}')
            else:
                print('Nenhum dado registrado ainda.')

                # Esta linha faz o programa pausar para você conseguir ler o resultado
                input('\nPressione ENTER para voltar ao menu...')
                os.system('cls')

            print() # Espaçamento.

        case 3:
            os.system('cls')
            print('Encerrando o programa...')
            break # O break aqui encerra o while True e fecha o programa.

        case _:
            os.system('cls')
            print('Opção invalida! Tente novamente.')
            input('Pressione ENTER para tentar novamente...')