import os
os.system('cls')

# Função com parâmetros e retorno.
def calcular_notas(nota1, nota2):
    resultado = nota1 + nota2
    return resultado

print('= SOLICITANDO NOTAS =')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

# Usando a função com parâmetros e com retorno.
# Inserindo o retorno da variavel soma.
soma = calcular_notas(nota1, nota2)

print('= EXIBINDO RESULTADOS =')
print(f'Soma: {soma}')