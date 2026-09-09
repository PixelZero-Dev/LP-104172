import os

os.system('cls')

nome = input('Digite o nome do aluno: ')
idade = int(input('Digite a idade do aluno: '))
primeira_nota = float(input('Digite a primeira nota do aluno: '))
segunda_nota = float(input('Digite a segunda nota do aluno: '))
terceira_nota = float(input('Digite a terceira nota do aluno: '))

print('Nome do aluno: ', nome)
print('Idade do aluno: ', idade)
print('Primeira nota do aluno: ', primeira_nota)
print('Segunda nota do aluno: ', segunda_nota)
print('Terceira nota do aluno: ', terceira_nota)

media = (primeira_nota + segunda_nota + terceira_nota) / 3

if media >= 7:
    resultado = ('O Aluno está Aprovado. ')
else:
    resultado = ('O Aluno está Reprovado ')

print(f'Média: {media}')
print(f'Resultado: {resultado}')