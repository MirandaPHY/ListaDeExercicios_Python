#  9 - Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num1 > num2 and num1 > num3:
    if num2 > num3:
        print(f"{num1}, {num2}, {num3}")
    else:
        print(f"{num1}, {num3}, {num2}")
        
if num1 < num2 and num1 < num3:
    if num2 > num3:
        print(f"{num2}, {num3}, {num1}")
    else:
        print(f"{num3}, {num2}, {num1}")
  