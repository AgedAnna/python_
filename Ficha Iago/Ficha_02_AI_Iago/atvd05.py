# Faça um algoritmo estruturado que leia uma quantidade não determinada de números positivos. Calcule a quantidade de números pares e ímpares, a média de valores pares e a média geral dos números lidos. O número que encerrará a leitura será zero.


def calcular_pares_impares_medias():
    total_numeros = 0  
    total_pares = 0 
    total_impares = 0
    soma_pares = 0
    soma_geral = 0

    while True:
        numero = int(input("Digite um número positivo (ou 0 para encerrar): "))

        if numero == 0:
            break

        soma_geral += numero
        total_numeros += 1

        if numero % 2 == 0:
            total_pares += 1
            soma_pares += numero
        else:
            total_impares += 1

    if total_pares > 0:
        media_pares = soma_pares / total_pares
    else:
        media_pares = 0

    if total_numeros > 0:
        media_geral = soma_geral / total_numeros
    else:
        media_geral = 0

    print("\nResultados:")
    print(f"Quantidade de números lidos: {total_numeros}")
    print(f"Quantidade de números pares: {total_pares}")
    print(f"Quantidade de números ímpares: {total_impares}")
    print(f"Média dos valores pares: {media_pares:.2f}")
    print(f"Média geral dos números lidos: {media_geral:.2f}")

calcular_pares_impares_medias()
