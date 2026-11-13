import os
os.system('cls')

# Função com parâmetros e retorno.
def calcular_notas(nota1, nota2):
    resultado = nota1 + nota2 / 2
    return resultado

def exibir_resultados(media):
    print('= EXIBINDO RESULTADOS =')
    print(f'Média: {media}')
    if media >= 6:
        resultado = 'Aluno aprovado!'
    else:
        resultado = 'Aluno reprovado!'
    return resultado

print('= SOLICITANDO NOTAS =')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

# Usando a função com parâmetros e com retorno.
# Inserindo o retorno da variavel soma.
media = calcular_notas(nota1, nota2)
resultado = exibir_resultados(media)

if media >= 6:
    print('= EXIBINDO RESULTADOS =')
    print(f'Média: {media}')
    print('Aluno aprovado!')
else:
    print('= EXIBINDO RESULTADOS =')
    print(f'Média: {media}')
    print('Aluno reprovado!')