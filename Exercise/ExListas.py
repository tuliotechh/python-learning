import os #limpar o terminal
lista = []

while True: 

    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls') #comando para limpar o terminal 
        valor = input('Qual valor deseja inserir: ')
        lista.append(valor)

    elif opcao == 'l':
        os.system('cls')
        
        if len(lista) == 0: #se o tamanho da lista for igual a 0
            print('Não ha nada para listar!')
        
        for i, valor in enumerate(lista): #para cara indice e valor enumerar lista
            print(i, valor)

    elif opcao == 'a': 
        apagarStr = input('Qual indice deseja apagar: ')
        try:
            apagar = int(apagarStr) #tranformando em numero inteiro
            del lista[apagar]
        except ValueError: #tratar um erro!!
            print('Digite um numero inteiro!')
        except IndexError: 
            print('Não existe na lista!')

    else:
        print('Não existe essa opção')







