## 09 - Faça um Programa que peça a temperatura em graus Fahrenheit,
# transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).

fahrenheit = float(input("Digite um valor de Temperatuda em Graus Fahrenheit: "))
celsius = 5 * ((fahrenheit - 32) / 9)
print("A temperatura em Celsius é: {}".format(celsius))