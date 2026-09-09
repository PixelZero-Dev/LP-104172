import os
os.system('cls')

# ENTRADA
idade = int(input('Informe sua Idade: '))
sexo = input('Informe seu sexo (M ou F): ')

# PROCESSAMENTO
if idade >= 18 and sexo == 'M':
    resultado = 'Deve apresentar-se ao serviço militar.'
else:
    resultado = 'Não deve apresentar-se ao serviço militar.'

# SAÍDA
print(f'Resultado: {resultado}')