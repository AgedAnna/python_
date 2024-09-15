# Escreva um algoritmo que leia um valor inicial A e imprima a seqüência de valores do cálculo de A! e o seu resultado. Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120

def calcular_fatorial():
    # Leitura do valor inicial A
    A = int(input("Digite um valor positivo inteiro (A): "))

    if A < 0:
        print("O valor deve ser um inteiro positivo.")
        return

    fatorial = 1
    sequencia = []

    for i in range(A, 0, -1):
        fatorial *= i
        sequencia.append(str(i))

    sequencia_str = " X ".join(sequencia)
    resultado_str = f"{A}! = {sequencia_str} = {fatorial}"

    print(resultado_str)

calcular_fatorial()
