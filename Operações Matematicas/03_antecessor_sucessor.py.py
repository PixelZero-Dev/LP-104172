import os

# Limpa o terminal

os.system('cls')

print('= PEDINDO INFORMAÇÃO =')

numero = int(input('Digite um número: '))

antecessor = numero - 1
sucessor = numero + 1


print('\n = EXIBINDO DADOS =')
print('Antecessoor', antecessor)
print('Sucessor', sucessor)