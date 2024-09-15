#Escrever um algoritmo que gera e escreve os números ímpares entre 100 e 200.

def gerar_impares_100_200():
    print("Números ímpares entre 100 e 200:")
 
    for numero in range(101, 200, 2):
        print(numero)

gerar_impares_100_200()
