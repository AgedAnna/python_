## Faça um algoritmo que leia uma variável e some 5 caso seja par ou some 8 caso seja ímpar, imprimir o resultado desta operação.

n = float(input("Digite um número: "))

if n % 2 == 0:
    print(n + 5)
else:
    print(n + 8)