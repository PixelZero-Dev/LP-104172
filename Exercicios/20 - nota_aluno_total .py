import os
os.system('cls')

nome = input('Informe o nome do aluno: ')
nota_um = float(input('Informe a primeira nota do aluno: '))
nota_dois = float(input('Informe a segunda nota do aluno: '))
media = max
media = min

media = nota_um + nota_dois / 2

if media >= 9:
    print('-------------------------------------------------------')
    print('Nota: A')
    print('-------------------------------------------------------')

elif media >= 7.5:
    print('-------------------------------------------------------')
    print('Nota: B')
    print('-------------------------------------------------------')

elif media >= 6:
    print('-------------------------------------------------------')
    print('Nota: C')
    print('-------------------------------------------------------')

elif media >= 4:
    print('-------------------------------------------------------')
    print('Nota: D')
    print('-------------------------------------------------------')

else:
    print('-------------------------------------------------------')
    print('Nota: E')
    print('-------------------------------------------------------')

if media >= 6:
    print('Aprovado. ')
else:
    print('Reprovado. ')

print(f'Nome: {nome}')
print(f'Total: {media}')