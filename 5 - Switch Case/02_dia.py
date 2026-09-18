
dia = input('Digite dia da semana: ')

match dia:
    case 'segunda':
        print('hoje é segunda feira.')
    case 'terça':
        print('hoje é terça feira.')
    case 'quarta':
        print('hoje é quarta feira.')
    case 'quinta':
        print('hoje é quinta feira.')
    case 'sexta':
        print('hoje é sexta feira.')
    case 'sabádo' | 'domingo':
        print('hoje é final de semana.')
    case _:
        print('Dia invalido.')

print(dia)
print('=== FIM ===')