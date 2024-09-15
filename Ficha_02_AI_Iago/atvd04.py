#  Escrever um algoritmo que leia uma quantidade desconhecida de números e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deve terminar quando for lido um número negativo.


def contar_numeros_por_intervalo():
    intervalo_0_25 = 0
    intervalo_26_50 = 0
    intervalo_51_75 = 0
    intervalo_76_100 = 0

    while True:
        numero = float(input("Digite um número (ou um número negativo para encerrar): "))

        if numero < 0:
            break

        if 0 <= numero <= 25:
            intervalo_0_25 += 1
        elif 26 <= numero <= 50:
            intervalo_26_50 += 1
        elif 51 <= numero <= 75:
            intervalo_51_75 += 1
        elif 76 <= numero <= 100:
            intervalo_76_100 += 1

    print("\nResultados:")
    print(f"Números no intervalo [0-25]: {intervalo_0_25}")
    print(f"Números no intervalo [26-50]: {intervalo_26_50}")
    print(f"Números no intervalo [51-75]: {intervalo_51_75}")
    print(f"Números no intervalo [76-100]: {intervalo_76_100}")

contar_numeros_por_intervalo()
