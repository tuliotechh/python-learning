"""
Repetiçoes 
While (enquanto) -> Executa uma ação enquanto uma condição for verdadeira
Continue (continua) -> Pula um laço
Break -> Quebra/Para um laço
Lopp infinito -> Qaundo um codigo não tem fim
Operadores de atribuição -> = += -= *= /= //= **= %=
"""
#--------------------------------------------------------------------------------

condicao = True

while condicao:
    nome = input('Digite seu nome: ')
    print(f'Seu nome é: {nome}')

    if nome == 'sair':
        break

print('Acabou!')

#--------------------------------------------------------------------------------

cont = 0

while cont <= 10:
    print(cont)
    cont += 1
    
print('Acabou!')

#--------------------------------------------------------------------------------

qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print( f'{linha=} {coluna=}')
        coluna += 1
    linha += 1

print('Acabou!')