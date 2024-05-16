## 07 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = float(input("Digite o lado do quadrado: "))
area = lado ** 2
dobro_area = area * 2
print("A área do quadrado é: {} e o dobro desta área é: {}".format(area, dobro_area))