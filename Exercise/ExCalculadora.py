# Calculadora com While

while True:
    numero1 = input('Digite um numero: ')
    numero2 = input('Digite outro numero: ')
    operador = input('Digite o operador (+ - * /): ')
    validos = None
    
    num1F = 0
    num2F = 0    
    
    try: 
        num1F = float(numero1)
        num2F = float(numero2)   

        validos = True
    except:
        validos = None

    if validos is None:
        print('Algum numero invalido!')
        continue

    operadorV = '+ - * /'

    if operador not in operadorV:
        print('Algum operador invalido!')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador!')
        continue

    print('Confia o resultado abaixo:')

    if operador == '+':
        print(num1F + num2F)
    elif operador == '-':
        print(num1F - num2F)
    elif operador == '/':   
        print(num1F / num2F)     
    elif operador == '*':
        print(num1F * num2F)        
    else:        
        print('Não deveria ter chagdo aqui...')
    
    sair = input('Quer sair? [s]sim ').lower().startswith('s')

    if sair is True:
        break 