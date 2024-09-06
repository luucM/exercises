#Cálculo de Imposto de Renda(IRPF)

salario = float(input("Digite o valor do seu salário: "))

if salario <= 2259.20:
    print("Sem desconto de IRPF")
elif salario >= 2259.21 and salario <= 2826.65:
    salario = (salario * 0.075)
    salario = (salario - 169.44)
    print(f"A sua retenção na fonte é de: {salario}")
elif salario >= 2826.66 and salario <= 3751.05:
    salario = (salario * 0.15)
    salario = (salario - 381.44)
    print(f"A sua retenção na fonte é de: {salario}")
elif salario >= 3751.06 and salario <= 4664.68:
    salario = (salario * 0.225)
    salario = (salario - 662.77)
    print(f"A sua retenção na fonte é de: {salario}")
elif salario >= 4664.69:
    salario = (salario * 0.275)
    salario = (salario - 896)
    print(f"A sua retenção na fonte é de: {salario}")

