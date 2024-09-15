## Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: para homens: (72.7 * h) – 58; para mulheres: (62.1 * h) – 44.7

altura = float(input("Digite sua altura: "))
sexo = str(input("Digite seu sexo: "))

homem_calculo =  (72.7 * altura) - 58
mulhere_calculo = (62.1 * altura) - 44.7

if sexo == "F":
    print(mulhere_calculo)
else:
    print(homem_calculo)