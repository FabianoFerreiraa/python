# 4. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros 
#quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros 
#quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário 
#a quantidades de latas de tinta a serem compradas e o preço tota.

area = float(input("qual o tamanho da area?"))          "o usuario deve digitar um valor para gravar na variavel area"
litros = area / 3.0                                     "a variavel litro vai receber o valor digitado em area e dividir por 3"
latas = int(litros / 18.0)                              "a variavel latas vai receber um numero inteiro digitado em litro dividindo po 18"
if litros % 18 != 0:                                    "se resto de litro for diferente ou igual a 0 vai somar o valor da lata mais 1 "
    latas += 1
print(f"Voce deverá comprar {latas}")                   "mostrara a quantidade de latas ha ser comprada"
print(f"O valor total é: R$:{latas * 80}")              "mostrara o valor em real a se pagar pelas latas"