# 6 - Faça um Programa que leia três números e mostre o maior deles.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o Terceiro número: "))

if num1 > num2 and num1 > num3:
  print("O maior número e o Primeiro {}".format(num1))
elif num2 > num1 and num2 > num3:
  print("O maior número e o Segundo {} ".format(num2))
else:
  print("O maior número e o Terceiro {}".format(num3))