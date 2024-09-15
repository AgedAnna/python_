# Escreva um algoritmo que leia um valor inicial A e uma razão R e imprima uma seqüência em P.G. contendo 10 valores.

def gerar_sequencia_pg():
   
    A = int(input("Digite o valor inicial (A): "))
    R = int(input("Digite a razão (R): "))
    
    print("\nSequência de P.G.:")
    
    for i in range(10):
        termo = A * (R ** i)
        print(termo)

gerar_sequencia_pg()
