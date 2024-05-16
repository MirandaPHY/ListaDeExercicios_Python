# 12 - Faça um programa para o cálculo de uma folha de pagamento, 
# sabendo que os descontos são do Imposto de Renda, que depende 
# do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e 
# que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado 
# (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto 
# menos os descontos. O programa deverá pedir ao usuário o valor da sua hora 
# e a quantidade de horas trabalhadas no mês.
# Sindicato 3%
# FGTS 11%

# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% 
# Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.

#        Salário Bruto: (5 * 220)        : R$ 1100,00
#        (-) IR (5%)                     : R$   55,00  
#        (-) INSS ( 10%)                 : R$  110,00
#        FGTS (11%)                      : R$  121,00
#        Total de descontos              : R$  165,00
#        Salário Liquido                 : R$  935,00

valor_da_hora = float(input("Qual o valor da sua hora trabalhada: "))
quantidade_de_horas_trabalhadas = ("Quantidade de horas trabalhadas no dia: ")

salario = quantidade_de_horas_trabalhadas * valor_da_hora

while salario <= 900.00:
    print(f"Salario Bruto: {salario}")
    print(f"(-) IR (0%)")
    print(f"(-) INSS (10%): {salario * 0.10}")
    print(f"FGTS (11%): {salario * 0.11}")
    print(f"Total de descontos: {salario * 0.10}")
    print(f"Salario Liquido: {salario - (salario * 0.10)}")
    print(f"O valor da hora é {valor_da_hora} e a quantidade de horas Trabalhadas é {quantidade_de_horas_trabalhadas}.")
    break

while salario > 900.00 and salario <= 1500.00:
    print(f"Salario Bruto: {salario}")
    print(f"(-) IR (5%): {salario * 0.05}")
    print(f"(-) INSS (10%): {salario * 0.10}")
    print(f"FGTS (11%): {salario * 0.11}")
    print(f"Total de descontos: {salario * 0.15}")
    print(f"Salario Liquido: {salario - (salario * 0.15)}")
    print(f"O valor da hora é {valor_da_hora} e a quantidade de horas Trabalhadas é {quantidade_de_horas_trabalhadas}.")
    break
  
while salario > 1500.00 and salario <= 2500.00:
    print(f"Salario Bruto: {salario}")
    print(f"(-) IR (10%): {salario * 0.10}")
    print(f"(-) INSS (10%): {salario * 0.10}")
    print(f"FGTS (11%): {salario * 0.11}")
    print(f"Total de descontos: {salario * 0.21}")
    print(f"Salario Liquido: {salario - (salario * 0.21)}")
    print(f"O valor da hora é {valor_da_hora} e a quantidade de horas Trabalhadas é {quantidade_de_horas_trabalhadas}.")
    break

while salario > 2500.00:
    print(f"Salario Bruto: {salario}")
    print(f"(-) IR (20%): {salario * 0.20}")
    print(f"(-) INSS (10%): {salario * 0.10}")
    print(f"FGTS (11%): {salario * 0.11}")
    print(f"Total de descontos: {salario * 0.31}")
    print(f"Salario Liquido: {salario - (salario * 0.31)}")
    print(f"O valor da hora é {valor_da_hora} e a quantidade de horas Trabalhadas é {quantidade_de_horas_trabalhadas}.")
    break

