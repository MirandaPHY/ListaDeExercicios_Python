# 8 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
# sabendo que a decisão é sempre pelo mais barato.

preco1 = float(input("Digite o primeiro preço do produto: "))
preco2 = float(input("Digite o segundo preço do produto: "))
preco3 = float(input("Digite o terceiro preço do produto"))

if preco1 < preco2 and preco1 < preco3:
    print("O produto mais barato é o primeiro e custa R$ {:.2f}".format(preco1))
elif preco2 < preco1 and preco2 < preco3:
    print("O produto mais barato é o segundo e custa R$ {:.2f}".format(preco2))
else:
    print("O produto mais barato é o terceiro e custa R$ {:.2f}".format(preco3))
