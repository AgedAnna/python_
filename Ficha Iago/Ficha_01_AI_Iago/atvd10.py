## O IMC – Indice de Massa Corporal é um critério da Organização Mundial de Saúde para dar uma indicação sobre a condição de peso de uma pessoa adulta. A fórmula é IMC = peso / ( altura )2 Elabore um algoritmo que leia o peso e a altura de um adulto e mostre sua condição de acordo com a tabela abaixo. IMC em adultos Condição Abaixo de 18,5 Abaixo do peso Entre 18,5 e 25 Peso normal Entre 25 e 30 Acima do peso Acima de 30 obeso


peso = float(input("Digite seu peso: "))
altura = float(input("Digite seu altura: "))


IMC = peso / ( altura ) ** 2

if IMC < 18.5:
    print(f"Abaixo do peso: {IMC}")

elif IMC > 18.5 and IMC <= 25:
    print(f"Peso normal: {IMC}")

elif IMC > 25 and IMC <= 30:
    print(f"Acime do peso: {IMC}")

else:
    print(f"Obeso: {IMC}")