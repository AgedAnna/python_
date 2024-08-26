## Encontrar o dobro de um número caso ele seja positivo e o seu triplo caso seja negativo, imprimindo o resultado.

n = float(input("Digite um número: "))

if n % 2 == 0:
    print(n * 2)
else:
    print(n * 3)