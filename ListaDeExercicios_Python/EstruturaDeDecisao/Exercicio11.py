# - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e 
# lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo
# o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario = float(input("Digite o Salario do Coloborador: "))

while salario <= 280.00:
    aumento = salario * 0.20 
    salario = salario + aumento
    print(f"Salario antes do reajuste: {salario - aumento}")
    print(f"Percentual de aumento aplicado: 20%")
    print(f"Valor do aumento: {aumento}")
    print(f"Novo salario: {salario}")
    break

while salario > 280.00 and salario <= 700.00:
    aumento = salario * 0.15
    salario = salario + aumento
    print(f"Salario antes do reajuste: {salario - aumento}")
    print(f"Percentual de aumento aplicado: 15%")
    print(f"Valor do aumento: {aumento}")
    print(f"Novo salario: {salario}")
    break

while salario > 700.00 and salario <= 1500.00:
    aumento = salario * 0.10
    salario = salario + aumento
    print(f"Salario antes do reajuste: {salario - aumento}")
    print(f"Percentual de aumento aplicado: 10%")
    print(f"Valor do aumento: {aumento}")
    print(f"Novo salario: {salario}")
    break

while salario > 1500.00:
    aumento = salario * 0.05
    salario = salario + aumento
    print(f"Salario antes do reajuste: {salario - aumento}")
    print(f"Percentual de aumento aplicado: 5%")
    print(f"Valor do aumento: {aumento}")
    print(f"Novo salario: {salario}")
    break