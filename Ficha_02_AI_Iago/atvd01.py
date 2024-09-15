# Desenvolver um algoritmo que efetue a soma de todos os números ímpares que são múltiplos de três e que se encontram no conjunto dos números de 1 até 500

def soma_impares_multiplos_tres():
    soma = 0  

    for numero in range(1, 501):
        if numero % 2 != 0 and numero % 3 == 0:
            soma += numero  

    print(f"A soma de todos os números ímpares múltiplos de 3 entre 1 e 500 é: {soma}")

soma_impares_multiplos_tres()
