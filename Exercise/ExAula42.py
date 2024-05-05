frase = 'o marco tulio é um dev bom pra crl, e muito lindo'

i = 0
qtdMaisVezes = 0
letraMaisVezes = 0

while i < len(frase):
    letraAtual = frase[i]

    if letraAtual == ' ':
        i += 1
        continue

    maisVezesAtual = frase.count(letraAtual)

    if qtdMaisVezes < maisVezesAtual:
        qtdMaisVezes = maisVezesAtual
        letraMaisVezes = letraAtual

    i += 1

print(f'A letra que apareceu mais vezes foi: "{letraMaisVezes}", que apareceu {qtdMaisVezes}x')
