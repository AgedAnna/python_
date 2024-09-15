##Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa. Caso sexo seja “F” e estado civil seja “CASADA”, solicitar o tempo de casada (anos).

nome = str(input("Digite seu nome: "))
sexo = str(input("Digite seu sexo: "))
estado_civil = str(input("Digite seu estado civil: "))

tempo_casada = float

if sexo == "F" or sexo == "feminino" or sexo == "FEMININO" and estado_civil == "CASADA":
    tempo_casada = (input("Digite quanto tempo de casada em meses: "))
    print(f"Ola {nome}, vc tem {tempo_casada} meses de casada")

else:
    print("ok")