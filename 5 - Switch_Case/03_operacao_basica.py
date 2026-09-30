import os
os.system('cls')

primeiro_numero = int(input('Digite o primeiro numero: '))
operador = input('Digite um operador: ')
segundo_numero = int(input('Digite o segundo numero: '))



match operador:
    case '+':
        resultado = primeiro_numero + segundo_numero
    case '-':
        resultado = primeiro_numero - segundo_numero
    case '*':
        resultado = primeiro_numero * segundo_numero
    case '/':
        resultado = primeiro_numero / segundo_numero
    case _:
        resultado = ('Operador incorreto!')

print(f'Primeiro Número: {primeiro_numero}')
print(f'Segundo Número: {segundo_numero}')

print(resultado)