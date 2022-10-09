#. Faça um Programa que peça um número e informe se o número é inteiro ou decimal

numero = float(input("Digite um número: "))      "a variavel numero vai receber um valor digitado pelo usuario"
if numero % 1 == 0:                              "se o resto desse valor for igual a 0, ele mostrara que é um numero inteiro"
    print("Inteiro")
else:                                            "se o resto da variavel numero for diferente de 0, ele motrara que é um numero decimal"
    print("Decimal")