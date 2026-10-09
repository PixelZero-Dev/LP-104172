contador_familias = 0
quantidade_geral_filhos = 0
soma_salarios = 0
maior_salario = 0
menor_salario = 9999

while True:
    print('\n=== MENU ===')
    print('1. Adicionar família')
    print('2. Exibir resultados')
    print('3. Sair')

    opcao = input('Selecione uma opção: ')

    match opcao:
        case '1':
            contador_familias += 1
            print(f'\nCadastro da família {contador_familias}:')

            salario = float(input('Digite o salário do chefe da família: '))
            quantidade_filhos = int(input('Digite a quantidade de filhos: '))

            soma_salarios += salario
            quantidade_geral_filhos += quantidade_filhos

            if maior_salario is None or salario > maior_salario:
                maior_salario = salario

            if menor_salario is None or salario < menor_salario:
                menor_salario = salario

        case '2':
            if contador_familias > 0:
                media_salarios = soma_salarios / contador_familias
                media_filhos = quantidade_geral_filhos / contador_familias

                print('\n=== RESULTADOS ===')
                print(f'Média salarial das famílias: R$ {media_salarios:.2f}')
                print(f'Média de filhos por família: {media_filhos:.2f}')
                print(f'Maior salário registrado: R$ {maior_salario:.2f}')
                print(f'Menor salário registrado: R$ {menor_salario:.2f}')
            else:
                print('\nNenhuma família cadastrada ainda.')

        case '3':
            print('\nEncerrando o programa.')
            break

        case _:
            print('\nOpção inválida. Tente novamente.')