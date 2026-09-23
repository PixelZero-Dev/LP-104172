import os
os.system('cls')

soma = 0
for i in range(1,6):
    numero = int(input(f'Digite o {i}° número: '))
    soma += numero

print(f'Soma: {soma}')

