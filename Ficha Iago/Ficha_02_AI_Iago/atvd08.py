# Escreva um algoritmo que leia um valor inicial A e uma razão R e imprima uma seqüência em P.A. contendo 10 valores.

def gerar_sequencia_pa():

    A = int(input("Digite o valor inicial (A): "))
    R = int(input("Digite a razão (R): "))
    
    print("\nSequência de P.A.:")
    
    for i in range(10):
        termo = A + i * R 
        print(termo)

gerar_sequencia_pa()
