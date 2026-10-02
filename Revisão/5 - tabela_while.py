import os
os.system('cls')
# VAMOS LA, AQUI COMEÇAMOS COM WHILE SENDO ELE VERDADEIRO.
# DENTRO DELE É ONDE VAMOS JOGAR TODAS AS INFORMAÇÕES PEDIDA PELO USUARIO.
while True:
# AQUI USANDO 3 ASPAS (''') SERVE PARA DEIXAR COMO ESTA VENDO ABAIXO NA PARTE DO MENU.
    print('''
================ MENU ================
Opção       Produto         Preço
1           Aperol          R$: 7,00
2           Vodka           R$: 25,00
3           Whisky          R$: 35,00
4           Picanha         R$: 95,00
5           Frango Assado   R$: 50,00
======================================
''')

    tabela = input('Selecione o que deseja: ')
    # AQUI USAMOS O MATCH CASE PARA SUBSTITUIR O IF/ELSE E DEIXA O CODIGO MAIS ORGANIZADO.
    # O MATCH CASE E PRATICAMENTE UM "CONTAINER" ONDE ELE ARMAZENA AS COISAS QUE TEM DISPONIVEL.
    match tabela:
        # CASE '1' FUNCIONA COMO UM CODIGO DE COMANDO TIPO, VOÇÊ DIGITA O NUMERO 1 NO TERMINAL E PRONTO, SERA EXECUTADO O QUE ESTÁ COM ESSA VARIAVEL.
        case '1':
            resultado = 'Aperol'
            valor = 'R$: 7,00'
            break
        # CASE '2' MESMO FUNCIONAMENTO DO ANTERIOR.
        case '2':
            resultado = 'Vodka'
            valor = 'R$: 25,00'
            break
        # CASE '3' MESMO FUNCIONAMENTO DO ANTERIOR.
        case '3':
            resultado = 'Whisky'
            valor = 'R$: 35,00'
            break
        # CASE '4' MESMO FUNCIONAMENTO DO ANTERIOR.
        case '4':
            resultado = 'Picanha'
            valor = 'R$: 95,00'
            break
        # CASE '5' MESMO FUNCIONAMENTO DO ANTERIOR.
        case '5':
            resultado = 'Frango Assado'
            valor = 'R$: 50,00'
            break
    # E ENTAO ASSIM QUE TUDO ESTA FUNCIONANDO CORRETO E ORGANIZADO, POSSO ADICIONAR O BREAK ONDE EU QUERO QUE SE UMA DAS OPÇÕES ESCOLHIDAS FOREM CORRETAS.
    # ENTAO PARE O CODIGO E ME MOSTRE O RESULTADO.


print(f'tabela: {tabela}')
print(f'Valor: {valor}')

print(f'Resultado: {resultado}')