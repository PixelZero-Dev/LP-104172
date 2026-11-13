import os
os.system('cls')

#Função sem retorno e sem parâmetros
def logo_senai():
    print("==========")
    print("   SENAI   ")
    print("==========")

# Função sem retorno e com parâmetros
def mostrar_dados(nome, idade):
    print(f'{nome} tem {idade} anos.')

# Função sem retorno e sem parâmetros
logo_senai()
print('\n= SOLICITANDO DADOS =')
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

logo_senai()
print('\n= EXIBINDO DADOS =')
# Função sem retorno e com parâmetros
mostrar_dados(nome, idade)