# ELABORE UM ALGORITMO PARA RESOLVER A SEGUINTE QUESTÃO:
# ESCREVA UM PROGRAMA QUE SOLICITE AO USUÁRIO A QUANTODADE DE MAÇAS DESEJADAS.
# AS MAÇAS CUSTARÃO R$ 1,30 CADA, SE FOREM COMPRADAS MENOS DE UMA DÚZIA, E CUSTARÃO R$ 1,00 CADA, SE FOREM COMPRADAS PELO MENOS 12.
# CALCULE E MOSTRE O VALOR TOTAL DA COMPRA.

import os
os.system('cls')

maca = int(input('Informe a quantidade de maçãs que será compradas: '))


if maca >= 12:
    preco = 1.00
else:
     preco = 1.30

print(f"Quantidade de maças: {maca}")
print(f"Valor total da compra: {preco}")

valor = preco * maca

print(f'O valor das compras deram {valor:.2f}: ')
