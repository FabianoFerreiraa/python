#2. Faça um Programa que peça um número inteiro e determine se ele é par ou ímpar

numero = int(input("Digite um número: "))       "a variavel numero vai receber um numero inteiro digitada pelo usuario"
im_pa = numero % 2                              "a variavel im_pa vai receber o resto da divisão da variavel numero "
if im_pa == 0:                                  "se o resultado for igual a 0 então mostrara que o resultado é par"
    print(f"O número: {numero} é par")
else:                                           "se for diverente de 0 então o printara o resultado impar"
    print(f"O Número: {numero} é impar")
