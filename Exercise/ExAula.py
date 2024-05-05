"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input('Digite um numero inteiro: ')

if numero.isdigit:
    numeroInt = int(numero)
    par_impar = numeroInt % 2 == 0
    par_texto = 'impar'

    if par_impar:
        par_texto = 'par'
        print(f'o numero {numeroInt} é {par_texto}')
    else:
        print('Isso não é um numero inteiro!')

"""
Faça um programa que exige a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação correspondente. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input('Que horas sao?: ')

try:
    hora = int(hora)

    if hora >= 0 and hora <= 11:
        print('Bom Dia!')
    elif hora >= 12 and hora <= 17:
        print('Boa Tarde!')
    elif hora >= 18 and hora <= 23:
        print('Boa Noite!')
    else:
       print('nao conheço essa hora...')
except:
    print('Por favor, digite epenas numeros inteiros!')

"""
Faça um programa que parte do primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
“Seu nome é normal”; maior que 6 escreva "Seu nome é muito grande".
"""

nome = input('Digite sue nome: ')
tamanhoNome = len(nome)

if tamanhoNome > 1:
    if tamanhoNome <= 4:
        print('Seu nome é curto!')
    elif tamanhoNome >= 5 and tamanhoNome <= 6:
        print('Seu nome é normal!') 
    elif tamanhoNome > 6:
        print('Seu nome é muito grande!')
else:
    print('Digite mais de uma letra!')