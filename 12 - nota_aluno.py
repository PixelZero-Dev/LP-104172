import os

os.system('cls')

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
primeira_nota = float(input('Digite a primeira nota: '))
segunda_nota = float(input('Digite a segunda nota: '))
terceira_nota = float(input('Digite a terceira nota: '))

media = (primeira_nota) + (segunda_nota) + (terceira_nota) / 3

if media >= 7:
    print('Aprovado.')
else:
    print('Reprovado')


print('Nome: ', nome)
print('Idade: ', idade)
print('Primeira nota: ', primeira_nota)
print('Segunda nota: ', segunda_nota)
print('Terceira nota: ', terceira_nota)