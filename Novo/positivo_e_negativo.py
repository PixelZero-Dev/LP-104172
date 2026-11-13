import os
os.system('cls')

def positivo_ou_negativo(numero):
    if numero < 0:
        print(f'{numero} é um numero negativo.')
    elif numero == 0:
        print(f'{numero} é um numero neutro.')
    else:
        print(f'{numero} é um numero positivo.')
    return numero

numero = int(input("Digite um número inteiro: "))

resultado = positivo_ou_negativo(numero)
