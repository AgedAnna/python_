## Escreva um algoritmo que leia três valores inteiros e diferentes e mostre-os em ordem decrescente.

print("Digite três valores inteiros diferentes:")
valor1 = int(input("Primeiro valor: "))
valor2 = int(input("Segundo valor: "))
valor3 = int(input("Terceiro valor: "))

if valor1 == valor2 or valor1 == valor3 or valor2 == valor3:
    print("Os valores devem ser diferentes. Tente novamente.")
else:
    if valor1 >= valor2 and valor1 >= valor3:
        maior = valor1
        if valor2 >= valor3:
            meio = valor2
            menor = valor3
        else:
            meio = valor3
            menor = valor2
    elif valor2 >= valor1 and valor2 >= valor3:
        maior = valor2
        if valor1 >= valor3:
            meio = valor1
            menor = valor3
        else:
            meio = valor3
            menor = valor1
    else:
        maior = valor3
        if valor1 >= valor2:
            meio = valor1
            menor = valor2
        else:
            meio = valor2
            menor = valor1

    print("Valores em ordem decrescente:")
    print(maior)
    print(meio)
    print(menor)
