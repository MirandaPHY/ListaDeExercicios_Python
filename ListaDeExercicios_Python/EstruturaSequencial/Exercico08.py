## 08 - Faça um Programa que pergunte quanto você ganha por hora e 
# o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

salario_po_horas = float(input("Quanto voce ganha por hora: "))
horas_trabalhadas = float(input("Quantas horas voce trabalha no dia: "))

salario = salario_po_horas * horas_trabalhadas * 30
dolar = salario * 5

print("Seu salario no mes é: R$ {}".format(salario))
print("Meu Salario em reais e {}".format(dolar))

