import os
from datetime import date
os.system('cls')

# ENTRADA
matricula = input('Digite a matricula do empregado: ')
ano_de_nascimento = int(input('Digite o ano de nascimento do empregado: '))
tempo_trabalhado = float(input('Quanto tempo contribuindo para o Governo?: '))

idade = date.today().year - ano_de_nascimento
# PROCESSAMENTO
if ano_de_nascimento >= 65 or tempo_trabalhado >= 30:
    resultado = 'Requerer a aposentadoria!'
else:
    resultado = 'Não requerer a aposentadoria!'

# SAÍDA
print(f'Nome do Trabalhador: {matricula}')
print(f'Ano de Nascimento do Trabalhador {ano_de_nascimento}')
print(f'Idade do Trabalhador {idade}')
print(f'Tempo Trabalhado do Trabalhador: {tempo_trabalhado}')
print(f'Resultado da aposentadoria: {resultado}')
print(f'Data: {date.today()}')