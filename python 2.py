#1. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu 
#peso ideal, utilizando as seguintes fórmulas:
#a. Para homens: (72.7*h) - 58
#b. Para mulheres: (62.1*h) - 44.7

sexo = input("Digite seu sexo? masculino (M) ou feminino (F)? ")       "pedindo para o usuario escolher variavel "sexo" entre (M) ou (F)"
altura = (input("digite sua altura"))                                  "o usuario deve colocar a altura" 
peso_m = (72.7*float(altura)) - 58                                     "a variavel peso_m vai receber a altura digitada pelo o usuario masculino 'x' a altura ideal masculina e dividir por 58"
peso_f = (62.1*float(altura)) - 44.7                                   "a varriavel peso_f faz o mesmo, caso o usuario digite (F) na variavel sexo"
if sexo == "M":                                                        "caso o usuario digite (M), o calculo da variavel peso_m aparecera na linha de baixo"                                          
    print(F"seu peso idea é {peso_m:.1f}K")                            "aparecerar o valor da variavel peso_m"
elif sexo == "F":                                                      "caso o usuario digite (F), o calculo da variavel peso_f aparecera na linha de baixo"         
    print(F"seu peso ideal é {peso_f:.1f}K")                           "aparecerar o valor da variavel peso_f"
else:                                                                  
    print("desculpa ocorreu um erro!!!")                               "caso o usuario digite qual coisa diferente de (M) ou (F)"