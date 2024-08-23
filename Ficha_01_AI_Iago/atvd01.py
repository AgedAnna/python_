##Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que C.

A = float(input("Digite n1: "))
B = float(input("Digite n2: "))
C = float(input("Digite n3: "))

soma = A + B

if soma > C:
    print(f"Soma de {A} + {B} é maior que {C}")
else:
    print(f"{C} é maior que a soma de {A} + {B}")
