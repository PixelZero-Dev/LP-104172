import os
os.system('cls')

def soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

def subtracao(numero1, numero2):
    resultado = numero1 - numero2
    return resultado

def multiplicacao(numero1, numero2):
    resultado = numero1 * numero2
    return resultado

def divisao(numero1, numero2):
    resultado = numero1 / numero2
    return resultado

print('= SOLICITANDO DADOS = ')
numero1 = int(input("Digite um numero inteiro: "))
numero2 = int(input("Digite outro numero inteiro: "))

print('= EXIBINDO RESULTADOS = ')

print(f'Soma: {soma(numero1, numero2)}')
print(f'Subtração: {subtracao(numero1, numero2)}')
print(f'Multiplicação: {multiplicacao(numero1, numero2)}')
print(f'Divisão: {divisao(numero1, numero2)}')