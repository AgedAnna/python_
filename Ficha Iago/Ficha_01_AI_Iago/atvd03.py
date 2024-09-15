## Faça um algoritmo para receber um número qualquer e informar na tela se é par ou ímpar.

n = float(input("Digite um número: "))

if n % 2 == 0:
    print(f"{n} é par")
else:
    print(f"{n} é ímpar")
