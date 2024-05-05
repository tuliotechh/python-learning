import random
import sys

# print(random.randint(0, 9)) #um numero aleatoria interio entre 0 e 9
noveDig = ''

for i in range(9):
    noveDig += str(random.randint(0, 9))

# cpf = '150.442.126-44'.replace('.', '').replace('-', '') #.replace serve para subistituir algo por outro
# noveDig = cpf[:9]
contRegress = 10
resultado = 0

for dig in noveDig: #contador decressente digito 1
    resultado += int(dig) * contRegress
    contRegress -= 1

dig = (resultado * 10) % 11 
dig = dig if dig <= 9 else 0 #dig so vai ser verdadeiro se for menor ou igual a nove, se noa vai ser 

dezDig = noveDig + str(dig)
cont2 = 11
result2 = 0

for dig2 in dezDig: #contador decressente digito 2
    result2 += int(dig2) * cont2
    cont2 -= 1

dig2 = (result2 * 10) % 11
dig2 = dig2 if dig2 >= 9 else 0

cpfGerado = f'{noveDig}{dig}{dig2}'

# if cpfGerado == cpf:
#     print(f'{cpfGerado} é valido')
# else:
#     print('CPF invalido')

print(noveDig)

