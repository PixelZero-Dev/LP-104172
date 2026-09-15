import os
os.system('cls')

prato = input('Digite o Codigo do Prato: ')

print('=== MENU ===')

match prato:
    case '1':
        resultado = 'Picanha'
        valor = 'R$25,00'
    case '2':
        resultado = 'Picanha'
        valor = 'R$20,00'
    case '3':
        resultado = 'Picanha'
        valor = 'R$18,00'
    case '4':
        resultado = 'Picanha'
        valor = 'R$15,00'
    case '5':
        resultado = 'Pão com Ovo'
        valor = 'R$5,00'


print(f'Prato: {prato}')
print(f'Valor: {valor}')

print(resultado)

