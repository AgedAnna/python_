nome = "Anna"
altura = 1.57
peso = 57
imc = peso / (altura * altura)

linha_1 = f'{nome} tem {altura:.2f} de altura'

print(nome, "tem", altura, "de altura", end=(",\n"))
print("pesa", peso, "quilos e seu IMC é")
print(f"{imc:.2f}")

print(linha_1)