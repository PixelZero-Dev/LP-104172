import os
from datetime import date
os.system('cls')

mes = input('Digite qual mês é hoje: ')

match mes:
    case '1':
        resultado = 'Janeiro / 2026'
    case '2':
        resultado = 'Fevereiro / 2026'
    case '3':
        resultado = 'Março / 2026'
    case '4':
        resultado = 'Abril / 2026'
    case '5':
        resultado = 'Maio / 2026'
    case '6':
        resultado = 'Junho / 2026'
    case '7':
        resultado = 'Julho / 2026'
    case '8':
        resultado = 'Agosto / 2026'
    case '9':
        resultado = 'Setembro / 2026'
    case '10':
        resultado = 'Outubro / 2026'
    case '11':
        resultado = 'Novembro / 2026'
    case '12':
        resultado = 'Dezembro / 2026'


print(f'Mês: {mes}')
print(resultado)