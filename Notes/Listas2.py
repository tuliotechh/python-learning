"""
Métodos úteis: append, insert, pop, del, clear, extend, (+/-) Concatena
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40] #Create
lista[2] = 300 #Update
del lista[2] #Delete
print(lista)
lista.append(90)
lista.append(90) #Adiciona ao final da lista
lista.append(895)
print('Append: ', lista)
lista.pop() #Remove o ultimo intem da lista
print('Pop: ', lista)
lista.insert(0, 5) #Adiciona um item no indice escolhido (0 = indice e 5 = item/valor)
print('Insert: ', lista)

print('---------------------------')

listaA = [1, 2, 3]
listaB = [4, 5, 6]
listaC = listaA + listaB 
print('Concatena: ', listaC)
listaA.extend(listaB)
print('Extend: ', listaA)

print('---------------------------')

"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy() 

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)