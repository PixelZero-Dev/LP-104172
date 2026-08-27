import os

os.system('cls')

primeiro_numero = int(input('Digite um numero: '))
segundo_numero = int(input('Digite outro numero: '))

soma = primeiro_numero + segundo_numero
media = soma / 2
produto = primeiro_numero * segundo_numero
maior = max(primeiro_numero, segundo_numero)
menor = min(primeiro_numero, segundo_numero)

# if primeiro_numero > segundo_numero:
#     maior = primeiro_numero
#     menor = segundo_numero
# else:
#     maior = segundo_numero
#     menor = segundo_numero

print(f'\n Média {media}')
print(f'Soma: {media}')
print(f'Produto: {produto}')
print(f'Maior numero: {maior}')
print(f'Menor numero: {menor}')