import os
os.system('cls')

primeiro_numero = int(input('Digite o primeiro numero: '))
segundo_numero = int(input('Digite o segundo numero: '))
terceiro_numero = int(input('Digite o terceiro numero: '))
maior = max (primeiro_numero, segundo_numero, terceiro_numero)
menor = min (primeiro_numero, segundo_numero, terceiro_numero)


print(f'\n Primeiro número {primeiro_numero}')
print(f'\n Segundo número: {segundo_numero}')
print(f'\n Terceiro número {terceiro_numero}')
print(f'\n Maior {maior}')
print(f'\n Menor {menor}')