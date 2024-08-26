def ler_booleano(mensagem):
    while True:
        entrada = input(mensagem).strip().lower()
        if entrada in ['true', '1', 'sim', 's']:
            return True
        elif entrada in ['false', '0', 'não', 'n']:
            return False
        else:
            print("Entrada inválida. Por favor, digite 'true', 'false', 'sim', 'não', '1' ou '0'.")

# Ler dois valores booleanos
valor1 = ler_booleano("Digite o primeiro valor booleano (true/false, 1/0, sim/não): ")
valor2 = ler_booleano("Digite o segundo valor booleano (true/false, 1/0, sim/não): ")

# Verificar se ambos os valores são verdadeiros ou falsos
if valor1 and valor2:
    print("Ambos os valores são VERDADEIROS.")
elif not valor1 and not valor2:
    print("Ambos os valores são FALSOS.")
else:
    print("Os valores são diferentes: um é VERDADEIRO e o outro é FALSO.")
