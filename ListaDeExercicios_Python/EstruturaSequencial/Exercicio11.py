## - 11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

n1 = int(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))
n3 = int(input("Digite um terceiro valor:"))

dobro = 2 * n1
metade_do_segundo = n2 / 2
soma_n1 = dobro + metade_do_segundo
triplo_primeiro = 3 * n1
soma_do_primeiro_com_terceiro = triplo_primeiro + n3
cubo = n3 ** 2

print("O Dobro do Primeiro {} com a metade do Segundo {} e {}".format(dobro, metade_do_segundo,soma_n1))
print("A Soma do Triplo de {} com o Terceiro {} e {}".format(triplo_primeiro, n3, soma_do_primeiro_com_terceiro))
print("o terceiro elevado ao cubo e {}".format(cubo))
