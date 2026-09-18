import os
os.system('cls')

numero_um = int(input('Digite um numero: '))
numero_dois = int(input('Digite outro numero: '))

soma = numero_um + numero_dois
media = soma / 2
produto = numero_um * numero_dois
max = numero_um, numero_dois
min = numero_um, numero_dois
menor = 0
maior = 0


if numero_um == numero_dois:
    print('SÃO IGUAIS')
    maior = numero_um
    menor = numero_dois
else:
    maior = numero_dois
    menor = numero_um

print(f'\n Média: {media}')
print(f'\n Soma: {soma}')
print(f'\n Produto: {produto}')
print(f'\n Maior valor: {numero_um}')
print(f'\n Menor valor: {numero_dois}')