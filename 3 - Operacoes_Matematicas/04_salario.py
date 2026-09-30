import os
os.system('cls')

print('= SOLICITANDO DADOS =')

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
salario_empregado = float(input('Digite seu salario: '))
salario_minimo = 1621
salario_minimo = salario_empregado / salario_minimo

print('= EXIBINDO DADOS =')

print('Nome do empregado: ', nome)
print('Idade do empregado ', idade)
print('Salario do empregado: ', salario_empregado)
print('Quantidade total de salario minimos: ', salario_minimo)