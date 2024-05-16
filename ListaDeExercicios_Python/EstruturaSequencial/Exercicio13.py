# 13 - Tendo como dado de entrada a altura (h) de uma pessoa, 
# construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

altura = float(input("Digite a sua altura: ")) # 1.70
sexo = input("Digite o seu sexo (M/F): ") # M
if sexo.upper() == "M":
    peso_ideal = (72.7 * altura) - 58
    print(f"O seu peso ideal é: {peso_ideal:.2f}kg") # 65.90kg
elif sexo.upper() == "F":
    peso_ideal = (62.1 * altura) - 44.7
    print(f"O seu peso ideal é: {peso_ideal:.2f}kg") # 62.37kg
else: 
    print("Sexo inválido")
# Output: O seu peso ideal é: 65.90kg



