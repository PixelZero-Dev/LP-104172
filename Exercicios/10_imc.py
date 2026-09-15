import os
os.system('cls')

peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))

imc = peso / (altura * altura)

if imc <= 18.5:
    print('Abaixo do peso. ')
elif imc <= 24.9:
    print('Peso Ideal (Parabéns!) ')
elif imc <= 29.9:
    print('Levemente acima do peso. ')
elif imc <= 34.9:
    print('Obesidade grau I' )
elif imc <= 39.9:
    print('Obesidade grau II (Severa)' )
else:
    imc > 40
    print("Obesidade III")

print(f'Altura: {altura}')
print(f'Peso: {peso}')