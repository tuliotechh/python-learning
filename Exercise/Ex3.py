nota1 = float(input('Informe a nota um: '))
nota2 = float(input('Informe a nota dois: '))
nota3 = float(input('Informe a nota tres: '))

media = (nota1 + nota2 + nota3) / 3

mediaFormatada = '{:.2f}'.format(media) # media formatada

print(f'A media das notas a cima é de: {mediaFormatada}')

