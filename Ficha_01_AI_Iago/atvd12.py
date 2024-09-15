def calcular_conceito():
    numero_aluno = input("Digite o número de identificação do aluno: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    media_exercicios = float(input("Digite a média dos exercícios: "))

    media_aproveitamento = (nota1 + nota2 * 2 + nota3 * 3 + media_exercicios) / 7

    if media_aproveitamento >= 90:
        conceito = 'A'
        status = 'Aprovado'
    elif media_aproveitamento >= 75:
        conceito = 'B'
        status = 'Aprovado'
    elif media_aproveitamento >= 60:
        conceito = 'C'
        status = 'Aprovado'
    elif media_aproveitamento >= 40:
        conceito = 'D'
        status = 'Reprovado'
    else:
        conceito = 'E'
        status = 'Reprovado'

    print(f"\nNúmero do Aluno: {numero_aluno}")
    print(f"Notas: {nota1}, {nota2}, {nota3}")
    print(f"Média dos Exercícios: {media_exercicios:.2f}")
    print(f"Média de Aproveitamento: {media_aproveitamento:.2f}")
    print(f"Conceito: {conceito}")
    print(f"Resultado: {status}")

calcular_conceito()
