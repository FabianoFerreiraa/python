#2. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o 
#rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o ....


peso = float(input("digite o Peso: "))                 "a variavel peso vai receber o numero digitado pelo usuario"
excesso = 0
multa = 0
if peso <= 50:                                         "se o valor da variavel peso for menor que 50, mostrarar o excesso de peso mais o valor da multa que sera igual a 0"
    print(f"O excesso de peso é: {excesso}K")
    print(f"A multa foi de R$: {multa}")
else:                                                  "se a variavel peso for diferente de menos a 0, então mostrara o excesso mais o valor da multa a se pagar"
    excesso = peso - 50
    multa = excesso * 4
    print(f"o excesso de peso é: {excesso}K")
    print(f"A multa foi de R$: {multa}")