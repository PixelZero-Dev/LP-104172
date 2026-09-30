import os
os.system('cls')

while True:
    nota = int(input("Informe a nota do aluno: "))
    if nota < 0 or nota > 10:
        print()
        print('Erro, informe novamente!')
    else:
        print()
        print('A nota esta entre 0 a 10.')
        print(f'Nota: {nota}')
        break

print('= FIM =')