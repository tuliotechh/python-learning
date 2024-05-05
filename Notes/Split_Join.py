"""
split e join com list e str

"""
frase = '   Olha só que   , coisa interessante          '
lista_frases_cruas = frase.split(',') #split - divide uma string (list)

lista_frases = []

for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip()) #strip - corta os espaços do começo e do fim

frases_unidas = ', '.join(lista_frases) #join - une uma string
print(frases_unidas)