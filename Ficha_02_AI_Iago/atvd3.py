# Desenvolver um algoritmo que leia um número não determinado de valores e calcule e escreva a média aritmética dos valores lidos, a quantidade de valores positivos, a quantidade de valores negativos e o percentual de valores negativos e positivos.


def calcular_estatisticas():
    valores = []  
    positivos = 0 
    negativos = 0 
    
    while True:
        valor = input("Digite um valor (ou 'sair' para encerrar): ")
        
        if valor.lower() == 'sair': 
            break

        valor = float(valor)  
        valores.append(valor)
        
        if valor > 0:
            positivos += 1
        elif valor < 0:
            negativos += 1
    
    if len(valores) > 0:
        media = sum(valores) / len(valores)
        total_valores = len(valores)
        
        percentual_positivos = (positivos / total_valores) * 100
        percentual_negativos = (negativos / total_valores) * 100

        # Exibe os resultados
        print(f"\nMédia aritmética dos valores lidos: {media:.2f}")
        print(f"Quantidade de valores positivos: {positivos}")
        print(f"Quantidade de valores negativos: {negativos}")
        print(f"Percentual de valores positivos: {percentual_positivos:.2f}%")
        print(f"Percentual de valores negativos: {percentual_negativos:.2f}%")
    else:
        print("Nenhum valor foi inserido.")

calcular_estatisticas()
