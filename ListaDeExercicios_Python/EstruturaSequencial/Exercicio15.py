# 15 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, 
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS
# e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R

salario_por_hora = float(input("Quanto voce recebe por hora trabalhada : "))
horas_trabalhadas = float(input("Quantas horas voce trabalha no dia:"))

horas_trabalhadas_no_mes = horas_trabalhadas * 30

salario_bruto = salario_por_hora * horas_trabalhadas_no_mes

desconto = salario_bruto * 11 / 100

inss = salario_bruto * 8 / 100

sindicato = salario_bruto * 5 / 100

salario_liquido = salario_bruto - desconto - inss - sindicato

print("Salario Bruto e R${}".format(salario_bruto))
print("IR (11%) : R${}".format(desconto))
print("INSS (8%) : R${}".format(inss))
print("indicato ( 5%) : R${}".format(sindicato))
print("Salário Liquido : R${}".format(salario_liquido))
