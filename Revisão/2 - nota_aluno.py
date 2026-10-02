import os
os.system('cls')

nome = input('Digite o nome do aluno: ')
idade = int(input('Digite a idade de aluno: '))
nota_um = int(input('Digite a primeira nota do aluno: '))
nota_dois = int(input('Digite a segunda nota do aluno: '))

media = nota_um + nota_dois / 2

if media >= 7:
    resultado = 'Aprovado'
elif media >= 5:
    resultado = 'Recuperação'
else:
    resultado = 'Reprovado'

print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Primera nota: {nota_um}')
print(f'Segunda nota: {nota_dois}')
print(f'Média: {media}')
print(f'Resultado: {resultado}')