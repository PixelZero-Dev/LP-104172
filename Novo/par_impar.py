import os
os.system('cls')

# função sem retorno e sem parâmetros.
def par_ou_impar():
    if numero % 2 == 0:
        print(f'{numero} é um número par.')
    else:
        print(f'{numero} é um número ímpar.')

print('= SOLICITANDO NÚMERO =')
numero = int(input("Digite um numero inteiro: "))

resultado = par_ou_impar()
