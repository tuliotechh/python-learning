"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
palavra = 'Marco'
letraCerta = ''
tentativas = 0

while True: # loop infinito 
    letraDigitada = input('Digite uma letra: ')
    tentativas += 1

    if len(letraDigitada) > 1: # se a letraDigitada for maior que 1
        print('Digite apenas uma letra!')
        continue

    if letraDigitada in palavra: # se a letraDigitada estiver na palavra vai salvar a letra na variavel letraCerta
        letraCerta += letraDigitada

    palavraFormada = ''
    for letraSecreta in palavra: # se a letraSecreta estiver na palvra...
        if letraSecreta in letraCerta: # e se a letraSecreca estiver nas letrasCertas
            palavraFormada += letraSecreta # vai salvar a letra na variavel
        else: 
            palavraFormada += '*' # se não, vai exibir *
    
    print(f'Palavra formada: {palavraFormada}')

    if palavraFormada == palavra: 
        print('VOCE GANHOU!!')
        print(f'a palavra era: {palavra}')
        print(f'Voce tentou {tentativas} vezes')



