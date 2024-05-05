'''
enumerate -> enumera iteraveis (indices)
'''

lista = ['Marco', 'Tulio', 'Santiago']
lista.append('Joao')

listaEnumerada = enumerate(lista)
print(next(listaEnumerada))

for indice, nome in enumerate(lista):
    print(indice, nome)