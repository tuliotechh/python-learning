# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras.

entrada = input('[E]ntrar [S]air: ')
senhaDigitada = input('Digite a senha: ')

senhaPermitida = '1234'

if entrada == 'E' and senhaDigitada == senhaPermitida:
    print('Entrar')
else: 
    print('Sair')

# -----------------------------------------------------------

# Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor
# São considerados falsy == 0 / 0.0 / '' / False
# Também existe o tipo None que é usado para representar um não valor

print(True and False and True)
print(bool(0))
print(True and 0 and True)

# -----------------------------------------------------------

# Avaliação de curso circuito

print(0 or False or 0 or 'abc' or True)

senha = input('Senha: ') or 'Sem senha'
print(senha)

# -----------------------------------------------------------

# Operador lógico 'not'
# Usado para inverter expressões 
# not True == False
# not False == True

print(not True)
print(not 0)

# -----------------------------------------------------------

# Operadores in (entre) e not in (não entre)
# Strings são iteráveis
# 0 1 2 3 4 5
# M a r c o
# -6-5-4-3-2-1

nome = 'Marco'
print(nome[3])
print(nome[-2])

print('a' in nome)
print('h' in nome)

nome  =  input ('Digite seu nome: ' )
encontrar  =  input ('Digite o que deseja encontrar: ')

if  encontrar  in  nome:
    print ( f'{encontrar} está em {nome}') 
else:
    print (f'{encontrar} não está em {nome}')


